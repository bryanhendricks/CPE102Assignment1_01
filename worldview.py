import pygame
import worldmodel
import entities
import point

MOUSE_HOVER_ALPHA = 120
MOUSE_HOVER_EMPTY_COLOR = (0, 255, 0)
MOUSE_HOVER_OCC_COLOR = (255, 0, 0)

class WorldView:
   def __init__(self, view_cols, view_rows, screen, world, tile_width,
      tile_height, mouse_img=None):
      self.viewport = pygame.Rect(0, 0, view_cols, view_rows)
      self.screen = screen
      self.mouse_pt = point.Point(0, 0)
      self.world = world
      self.tile_width = tile_width
      self.tile_height = tile_height
      self.num_rows = world.num_rows
      self.num_cols = world.num_cols
      self.mouse_img = mouse_img

##   def viewport_to_world(self, pt):
##      return point.Point(pt.x + self.left, pt.y + self.top)

##   def world_to_viewport(self, pt):
##      return point.Point(pt.x - self.left, pt.y - self.top)

##   def create_shifted_viewport(self, delta, num_rows, num_cols):
##      new_x = clamp(self.left + delta[0], 0, num_cols - self.width)
##      new_y = clamp(self.top + delta[1], 0, num_rows - self.height)
##      return pygame.Rect(new_x, new_y, self.width, self.height)

   def draw_background(self):
      for y in range(0, self.viewport.height):
         for x in range(0, self.viewport.width):
            w_pt = viewport_to_world(self.viewport, point.Point(x, y))
            img = self.world.get_background_image(w_pt)
            self.screen.blit(img, (x * self.tile_width, y * self.tile_height))

   def draw_entities(self):
      for entity in self.world.entities:
         if self.viewport.collidepoint(entity.position.x, entity.position.y):
            v_pt = world_to_viewport(self.viewport, entity.position)
            self.screen.blit(entity.get_image(),
               (v_pt.x * self.tile_width, v_pt.y * self.tile_height))

   def draw_viewport(self):
      self.draw_background()
      self.draw_entities()

   def update_view(self, view_delta=(0,0), mouse_img=None):
      self.viewport = create_shifted_viewport(self.viewport, view_delta,
         self.num_rows, self.num_cols)
      self.mouse_img = mouse_img
      self.draw_viewport()
      pygame.display.update()
      self.mouse_move(self.mouse_pt)

   def update_view_tiles(self, tiles):
      rects = []
      for tile in tiles:
         if self.viewport.collidepoint(tile.x, tile.y):
            v_pt = world_to_viewport(self.viewport, tile)
            img = self.get_tile_image(v_pt)
            rects.append(self.update_tile(v_pt, img))
            if self.mouse_pt.x == v_pt.x and self.mouse_pt.y == v_pt.y:
               rects.append(update_mouse_cursor(self))
      pygame.display.update(rects)

   def update_tile(self, view_tile_pt, surface):
      abs_x = view_tile_pt.x * self.tile_width
      abs_y = view_tile_pt.y * self.tile_height
      self.screen.blit(surface, (abs_x, abs_y))
      return pygame.Rect(abs_x, abs_y, self.tile_width, self.tile_height)

   def get_tile_image(self, view_tile_pt):
      pt = viewport_to_world(self.viewport, view_tile_pt)
      bgnd = self.world.get_background_image(pt)
      occupant = self.world.get_tile_occupant(pt)
      if occupant:
         img = pygame.Surface((self.tile_width, self.tile_height))
         img.blit(bgnd, (0, 0))
         img.blit(occupant.get_image(), (0,0))
         return img
      else:
         return bgnd

   def create_mouse_surface(self, occupied):
      surface = pygame.Surface((self.tile_width, self.tile_height))
      surface.set_alpha(MOUSE_HOVER_ALPHA)
      color = MOUSE_HOVER_EMPTY_COLOR
      if occupied:
         color = MOUSE_HOVER_OCC_COLOR
      surface.fill(color)
      if self.mouse_img:
         surface.blit(self.mouse_img, (0, 0))
      return surface

   def update_mouse_cursor(self):
      return self.update_tile(self.mouse_pt,
         self.create_mouse_surface(self.world.is_occupied(viewport_to_world(self.viewport, self.mouse_pt))))

   def mouse_move(self, new_mouse_pt):
      rects = []
      rects.append(self.update_tile(self.mouse_pt,
         self.get_tile_image(self.mouse_pt)))
      if self.viewport.collidepoint(new_mouse_pt.x + self.viewport.left,
         new_mouse_pt.y + self.viewport.top):
         self.mouse_pt = new_mouse_pt
      rects.append(self.update_mouse_cursor())
      pygame.display.update(rects)




def viewport_to_world(viewport, pt):
   return point.Point(pt.x + viewport.left, pt.y + viewport.top)


def world_to_viewport(viewport, pt):
   return point.Point(pt.x - viewport.left, pt.y - viewport.top)


#Not putting in class, doesn't deal with the view or viewport
def clamp(v, low, high):
   return min(high, max(v, low))


def create_shifted_viewport(viewport, delta, num_rows, num_cols):
   new_x = clamp(viewport.left + delta[0], 0, num_cols - viewport.width)
   new_y = clamp(viewport.top + delta[1], 0, num_rows - viewport.height)
   return pygame.Rect(new_x, new_y, viewport.width, viewport.height)
##
##
##def draw_background(view):
##   for y in range(0, view.viewport.height):
##      for x in range(0, view.viewport.width):
##         w_pt = viewport_to_world(view.viewport, point.Point(x, y))
##         img = view.world.get_background_image(w_pt)
##         view.screen.blit(img, (x * view.tile_width, y * view.tile_height))
##
##
##def draw_entities(view):
##   for entity in view.world.entities:
##      if view.viewport.collidepoint(entity.position.x, entity.position.y):
##         v_pt = world_to_viewport(view.viewport, entity.position)
##         view.screen.blit(entity.get_image(),
##            (v_pt.x * view.tile_width, v_pt.y * view.tile_height))
##
##
##def draw_viewport(view):
##   draw_background(view)
##   draw_entities(view)
##
##
##def update_view(view, view_delta=(0,0), mouse_img=None):
##   view.viewport = create_shifted_viewport(view.viewport, view_delta,
##      view.num_rows, view.num_cols)
##   view.mouse_img = mouse_img
##   draw_viewport(view)
##   pygame.display.update()
##   mouse_move(view, view.mouse_pt)
##
##
##def update_view_tiles(view, tiles):
##   rects = []
##   for tile in tiles:
##      if view.viewport.collidepoint(tile.x, tile.y):
##         v_pt = world_to_viewport(view.viewport, tile)
##         img = get_tile_image(view, v_pt)
##         rects.append(update_tile(view, v_pt, img))
##         if view.mouse_pt.x == v_pt.x and view.mouse_pt.y == v_pt.y:
##            rects.append(update_mouse_cursor(view))
##   pygame.display.update(rects)
##
##
##def update_tile(view, view_tile_pt, surface):
##   abs_x = view_tile_pt.x * view.tile_width
##   abs_y = view_tile_pt.y * view.tile_height
##   view.screen.blit(surface, (abs_x, abs_y))
##   return pygame.Rect(abs_x, abs_y, view.tile_width, view.tile_height)
##
##
##def get_tile_image(view, view_tile_pt):
##   pt = viewport_to_world(view.viewport, view_tile_pt)
##   bgnd = view.world.get_background_image(pt)
##   occupant = view.world.get_tile_occupant(pt)
##   if occupant:
##      img = pygame.Surface((view.tile_width, view.tile_height))
##      img.blit(bgnd, (0, 0))
##      img.blit(occupant.get_image(), (0,0))
##      return img
##   else:
##      return bgnd
##
##
##def create_mouse_surface(view, occupied):
##   surface = pygame.Surface((view.tile_width, view.tile_height))
##   surface.set_alpha(MOUSE_HOVER_ALPHA)
##   color = MOUSE_HOVER_EMPTY_COLOR
##   if occupied:
##      color = MOUSE_HOVER_OCC_COLOR
##   surface.fill(color)
##   if view.mouse_img:
##      surface.blit(view.mouse_img, (0, 0))
##   return surface
##
##
##def update_mouse_cursor(view):
##   return update_tile(view, view.mouse_pt,
##      create_mouse_surface(view,
##         view.world.is_occupied(viewport_to_world(view.viewport, view.mouse_pt))))
##
##
##def mouse_move(view, new_mouse_pt):
##   rects = []
##   rects.append(update_tile(view, view.mouse_pt,
##      get_tile_image(view, view.mouse_pt)))
##   if view.viewport.collidepoint(new_mouse_pt.x + view.viewport.left,
##      new_mouse_pt.y + view.viewport.top):
##      view.mouse_pt = new_mouse_pt
##   rects.append(update_mouse_cursor(view))
##   pygame.display.update(rects)

