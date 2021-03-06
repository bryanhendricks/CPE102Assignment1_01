import entities
import pygame
import ordered_list
import actions
import occ_grid
import point

class WorldModel:
   def __init__(self, num_rows, num_cols, background):
      self.background = occ_grid.Grid(num_cols, num_rows, background)
      self.num_rows = num_rows
      self.num_cols = num_cols
      self.occupancy = occ_grid.Grid(num_cols, num_rows, None)
      self.entities = []
      self.action_queue = ordered_list.OrderedList()
   def within_bounds(self, pt):
      return (pt.x >= 0 and pt.x < self.num_cols and
         pt.y >= 0 and pt.y < self.num_rows)
   def is_occupied(self, pt):
      return (self.within_bounds(pt) and
         occ_grid.get_cell(self.occupancy, pt) != None)
   def find_nearest(self, pt, type):
      oftype = [(e, distance_sq(pt, e.get_position()))
         for e in self.entities if isinstance(e, type)]
      return nearest_entity(oftype)
   def add_entity(self, entity):
      pt = entity.get_position()
      if self.within_bounds(pt):
         old_entity = occ_grid.get_cell(self.occupancy, pt)
         if old_entity != None:
            old_entity.clear_pending_actions()
         occ_grid.set_cell(self.occupancy, pt, entity)
         self.entities.append(entity)
   def move_entity(self, entity, pt):
      tiles = []
      if self.within_bounds(pt):
         old_pt = entity.get_position()
         occ_grid.set_cell(self.occupancy, old_pt, None)
         tiles.append(old_pt)
         occ_grid.set_cell(self.occupancy, pt, entity)
         tiles.append(pt)
         entity.set_position(pt)
      return tiles
   def remove_entity(self, entity):
      self.remove_entity_at(entity.get_position())
   def remove_entity_at(self, pt):
      if (self.within_bounds(pt) and
         occ_grid.get_cell(self.occupancy, pt) != None):
         entity = occ_grid.get_cell(self.occupancy, pt)
         entity.set_position(point.Point(-1, -1))
         self.entities.remove(entity)
         occ_grid.set_cell(self.occupancy, pt, None)
   def schedule_action(self, action, time):
      self.action_queue.insert(action, time)
   def unschedule_action(self, action):
      self.action_queue.remove(action)
   def update_on_time(self, ticks):
      tiles = []
      next = self.action_queue.head()
      while next and next.ord < ticks:
         self.action_queue.pop()
         tiles.extend(next.item(ticks))  # invoke action function
         next = self.action_queue.head()
      return tiles
   def get_background_image(self, pt):
      if self.within_bounds(pt):
         return occ_grid.get_cell(self.background, pt).get_image()
   def get_background(self, pt):
      if self.within_bounds(pt):
         return occ_grid.get_cell(self.background, pt)
   def set_background(self, pt, bgnd):
      if self.within_bounds(pt):
         occ_grid.set_cell(self.background, pt, bgnd)
   def get_tile_occupant(self, pt):
      if self.within_bounds(pt):
         return occ_grid.get_cell(self.occupancy, pt)
   def get_entities(self):
      return self.entities

##This function is being left out of WorldModel because it doesn't work
##when it's inside the class and I don't know why
##def within_bounds(world, pt):
##   return (pt.x >= 0 and pt.x < world.num_cols and
##      pt.y >= 0 and pt.y < world.num_rows)


##def is_occupied(world, pt):
##   return (within_bounds(world, pt) and
##      occ_grid.get_cell(world.occupancy, pt) != None)


#This function is being left out of WorldModel because is does not deal
#with the world itself, only entities in the world
def nearest_entity(entity_dists):
   if len(entity_dists) > 0:
      pair = entity_dists[0]
      for other in entity_dists:
         if other[1] < pair[1]:
            pair = other
      nearest = pair[0]
   else:
      nearest = None

   return nearest


#This function is being left out of WorldModel because is does not deal
#with the world itself, only points on the grid of the world
def distance_sq(p1, p2):
   return (p1.x - p2.x)**2 + (p1.y - p2.y)**2


##def find_nearest(world, pt, type):
##   oftype = [(e, distance_sq(pt, e.get_position()))
##      for e in world.entities if isinstance(e, type)]
##
##   return nearest_entity(oftype)
##
##
##def add_entity(world, entity):
##   pt = entity.get_position()
##   if within_bounds(world, pt):
##      old_entity = occ_grid.get_cell(world.occupancy, pt)
##      if old_entity != None:
##         old_entity.clear_pending_actions()
##      occ_grid.set_cell(world.occupancy, pt, entity)
##      world.entities.append(entity)
##
##
##def move_entity(world, entity, pt):
##   tiles = []
##   if within_bounds(world, pt):
##      old_pt = entity.get_position()
##      occ_grid.set_cell(world.occupancy, old_pt, None)
##      tiles.append(old_pt)
##      occ_grid.set_cell(world.occupancy, pt, entity)
##      tiles.append(pt)
##      entity.set_position(pt)
##
##   return tiles
##
##
##def remove_entity(world, entity):
##   remove_entity_at(world, entity.get_position())
##
##
##def remove_entity_at(world, pt):
##   if (within_bounds(world, pt) and
##      occ_grid.get_cell(world.occupancy, pt) != None):
##      entity = occ_grid.get_cell(world.occupancy, pt)
##      entity.set_position(point.Point(-1, -1))
##      world.entities.remove(entity)
##      occ_grid.set_cell(world.occupancy, pt, None)
##
##
##def schedule_action(world, action, time):
##   world.action_queue.insert(action, time)
##
##
##def unschedule_action(world, action):
##   world.action_queue.remove(action)
##
##
##def update_on_time(world, ticks):
##   tiles = []
##
##   next = world.action_queue.head()
##   while next and next.ord < ticks:
##      world.action_queue.pop()
##      tiles.extend(next.item(ticks))  # invoke action function
##      next = world.action_queue.head()
##
##   return tiles
##
##
##def get_background_image(world, pt):
##   if within_bounds(world, pt):
##      return occ_grid.get_cell(world.background, pt).get_image()
##
##
##def get_background(world, pt):
##   if within_bounds(world, pt):
##      return occ_grid.get_cell(world.background, pt)
##
##
##def set_background(world, pt, bgnd):
##   if within_bounds(world, pt):
##      occ_grid.set_cell(world.background, pt, bgnd)
##
##
##def get_tile_occupant(world, pt):
##   if within_bounds(world, pt):
##      return occ_grid.get_cell(world.occupancy, pt)
##
##
##def get_entities(world):
##   return world.entities
