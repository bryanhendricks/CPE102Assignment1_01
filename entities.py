import point

class Background:
   def __init__(self, name, imgs):
      self.name = name
      self.imgs = imgs
      self.current_img = 0

   def set_position(self, point):
      self.position = point
   def get_position(self):
      return self.position
   def get_images(self):
      return self.imgs
   def get_image(self):
      return self.imgs[self.current_img]
   def get_rate(self):
      return self.rate
   def set_resource_count(self, n):
      self.resource_count = n
   def get_resource_count(self):
      return self.resource_count
   def get_resource_limit(self):
      return self.resource_limit
   def get_resource_distance(self):
      return self.resource_distance
   def get_name(self):
      return self.name
   def get_animation_rate(self):
      return self.animation_rate
   def remove_pending_action(self, action):
      if hasattr(self, "pending_actions"):
         self.pending_actions.remove(action)
   def add_pending_action(self, action):
      if hasattr(self, "pending_actions"):
         self.pending_actions.append(action)
   def get_pending_actions(self):
      if hasattr(self, "pending_actions"):
         return self.pending_actions
      else:
         return []
   def clear_pending_actions(self):
      if hasattr(self, "pending_actions"):
         self.pending_actions = []
   def next_image(self):
      self.current_img = (self.current_img + 1) % len(self.imgs)


class MinerNotFull:
   def __init__(self, name, resource_limit, position, rate, imgs,
      animation_rate):
      self.name = name
      self.position = position
      self.rate = rate
      self.imgs = imgs
      self.current_img = 0
      self.resource_limit = resource_limit
      self.resource_count = 0
      self.animation_rate = animation_rate
      self.pending_actions = []

   def set_position(self, point):
      self.position = point
   def get_position(self):
      return self.position
   def get_images(self):
      return self.imgs
   def get_image(self):
      return self.imgs[self.current_img]
   def get_rate(self):
      return self.rate
   def set_resource_count(self, n):
      self.resource_count = n
   def get_resource_count(self):
      return self.resource_count
   def get_resource_limit(self):
      return self.resource_limit
   def get_resource_distance(self):
      return self.resource_distance
   def get_name(self):
      return self.name
   def get_animation_rate(self):
      return self.animation_rate
   def remove_pending_action(self, action):
      if hasattr(self, "pending_actions"):
         self.pending_actions.remove(action)
   def add_pending_action(self, action):
      if hasattr(self, "pending_actions"):
         self.pending_actions.append(action)
   def get_pending_actions(self):
      if hasattr(self, "pending_actions"):
         return self.pending_actions
      else:
         return []
   def clear_pending_actions(self):
      if hasattr(self, "pending_actions"):
         self.pending_actions = []
   def next_image(self):
      self.current_img = (self.current_img + 1) % len(self.imgs)
   def entity_string(self):
      return ' '.join(['miner', self.name, str(self.position.x),
         str(self.position.y), str(self.resource_limit),
         str(self.rate), str(self.animation_rate)])

class MinerFull:
   def __init__(self, name, resource_limit, position, rate, imgs,
      animation_rate):
      self.name = name
      self.position = position
      self.rate = rate
      self.imgs = imgs
      self.current_img = 0
      self.resource_limit = resource_limit
      self.resource_count = resource_limit
      self.animation_rate = animation_rate
      self.pending_actions = []

   def set_position(self, point):
      self.position = point
   def get_position(self):
      return self.position
   def get_images(self):
      return self.imgs
   def get_image(self):
      return self.imgs[self.current_img]
   def get_rate(self):
      return self.rate
   def set_resource_count(self, n):
      self.resource_count = n
   def get_resource_count(self):
      return self.resource_count
   def get_resource_limit(self):
      return self.resource_limit
   def get_resource_distance(self):
      return self.resource_distance
   def get_name(self):
      return self.name
   def get_animation_rate(self):
      return self.animation_rate
   def remove_pending_action(self, action):
      if hasattr(self, "pending_actions"):
         self.pending_actions.remove(action)
   def add_pending_action(self, action):
      if hasattr(self, "pending_actions"):
         self.pending_actions.append(action)
   def get_pending_actions(self):
      if hasattr(self, "pending_actions"):
         return self.pending_actions
      else:
         return []
   def clear_pending_actions(self):
      if hasattr(self, "pending_actions"):
         self.pending_actions = []
   def next_image(self):
      self.current_img = (self.current_img + 1) % len(self.imgs)

class Vein:
   def __init__(self, name, rate, position, imgs, resource_distance=1):
      self.name = name
      self.position = position
      self.rate = rate
      self.imgs = imgs
      self.current_img = 0
      self.resource_distance = resource_distance
      self.pending_actions = []

   def set_position(self, point):
      self.position = point
   def get_position(self):
      return self.position
   def get_images(self):
      return self.imgs
   def get_image(self):
      return self.imgs[self.current_img]
   def get_rate(self):
      return self.rate
   def set_resource_count(self, n):
      self.resource_count = n
   def get_resource_count(self):
      return self.resource_count
   def get_resource_limit(self):
      return self.resource_limit
   def get_resource_distance(self):
      return self.resource_distance
   def get_name(self):
      return self.name
   def get_animation_rate(self):
      return self.animation_rate
   def remove_pending_action(self, action):
      if hasattr(self, "pending_actions"):
         self.pending_actions.remove(action)
   def add_pending_action(self, action):
      if hasattr(self, "pending_actions"):
         self.pending_actions.append(action)
   def get_pending_actions(self):
      if hasattr(self, "pending_actions"):
         return self.pending_actions
      else:
         return []
   def clear_pending_actions(self):
      if hasattr(self, "pending_actions"):
         self.pending_actions = []
   def next_image(self):
      self.current_img = (self.current_img + 1) % len(self.imgs)
   def entity_string(self):
      return ' '.join(['vein', self.name, str(self.position.x),
         str(self.position.y), str(self.rate),
         str(self.resource_distance)])

class Ore:
   def __init__(self, name, position, imgs, rate=5000):
      self.name = name
      self.position = position
      self.imgs = imgs
      self.current_img = 0
      self.rate = rate
      self.pending_actions = []

   def set_position(self, point):
      self.position = point
   def get_position(self):
      return self.position
   def get_images(self):
      return self.imgs
   def get_image(self):
      return self.imgs[self.current_img]
   def get_rate(self):
      return self.rate
   def set_resource_count(self, n):
      self.resource_count = n
   def get_resource_count(self):
      return self.resource_count
   def get_resource_limit(self):
      return self.resource_limit
   def get_resource_distance(self):
      return self.resource_distance
   def get_name(self):
      return self.name
   def get_animation_rate(self):
      return self.animation_rate
   def remove_pending_action(self, action):
      if hasattr(self, "pending_actions"):
         self.pending_actions.remove(action)
   def add_pending_action(self, action):
      if hasattr(self, "pending_actions"):
         self.pending_actions.append(action)
   def get_pending_actions(self):
      if hasattr(self, "pending_actions"):
         return self.pending_actions
      else:
         return []
   def clear_pending_actions(self):
      if hasattr(self, "pending_actions"):
         self.pending_actions = []
   def next_image(self):
      self.current_img = (self.current_img + 1) % len(self.imgs)
   def entity_string(self):
      return ' '.join(['ore', self.name, str(self.position.x),
         str(self.position.y), str(self.rate)])

class Blacksmith:
   def __init__(self, name, position, imgs, resource_limit, rate,
      resource_distance=1):
      self.name = name
      self.position = position
      self.imgs = imgs
      self.current_img = 0
      self.resource_limit = resource_limit
      self.resource_count = 0
      self.rate = rate
      self.resource_distance = resource_distance
      self.pending_actions = []

   def set_position(self, point):
      self.position = point
   def get_position(self):
      return self.position
   def get_images(self):
      return self.imgs
   def get_image(self):
      return self.imgs[self.current_img]
   def get_rate(self):
      return self.rate
   def set_resource_count(self, n):
      self.resource_count = n
   def get_resource_count(self):
      return self.resource_count
   def get_resource_limit(self):
      return self.resource_limit
   def get_resource_distance(self):
      return self.resource_distance
   def get_name(self):
      return self.name
   def get_animation_rate(self):
      return self.animation_rate
   def remove_pending_action(self, action):
      if hasattr(self, "pending_actions"):
         self.pending_actions.remove(action)
   def add_pending_action(self, action):
      if hasattr(self, "pending_actions"):
         self.pending_actions.append(action)
   def get_pending_actions(self):
      if hasattr(self, "pending_actions"):
         return self.pending_actions
      else:
         return []
   def clear_pending_actions(self):
      if hasattr(self, "pending_actions"):
         self.pending_actions = []
   def next_image(self):
      self.current_img = (self.current_img + 1) % len(self.imgs)
   def entity_string(self):
      return ' '.join(['blacksmith', self.name, str(self.position.x),
         str(self.position.y), str(self.resource_limit),
         str(self.rate), str(self.resource_distance)])

class Obstacle:
   def __init__(self, name, position, imgs):
      self.name = name
      self.position = position
      self.imgs = imgs
      self.current_img = 0

   def set_position(self, point):
      self.position = point
   def get_position(self):
      return self.position
   def get_images(self):
      return self.imgs
   def get_image(self):
      return self.imgs[self.current_img]
   def get_rate(self):
      return self.rate
   def set_resource_count(self, n):
      self.resource_count = n
   def get_resource_count(self):
      return self.resource_count
   def get_resource_limit(self):
      return self.resource_limit
   def get_resource_distance(self):
      return self.resource_distance
   def get_name(self):
      return self.name
   def get_animation_rate(self):
      return self.animation_rate
   def remove_pending_action(self, action):
      if hasattr(self, "pending_actions"):
         self.pending_actions.remove(action)
   def add_pending_action(self, action):
      if hasattr(self, "pending_actions"):
         self.pending_actions.append(action)
   def get_pending_actions(self):
      if hasattr(self, "pending_actions"):
         return self.pending_actions
      else:
         return []
   def clear_pending_actions(self):
      if hasattr(self, "pending_actions"):
         self.pending_actions = []
   def next_image(self):
      self.current_img = (self.current_img + 1) % len(self.imgs)
   def entity_string(self):
      return ' '.join(['obstacle', self.name, str(self.position.x),
         str(self.position.y)])

class OreBlob:
   def __init__(self, name, position, rate, imgs, animation_rate):
      self.name = name
      self.position = position
      self.rate = rate
      self.imgs = imgs
      self.current_img = 0
      self.animation_rate = animation_rate
      self.pending_actions = []

   def set_position(self, point):
      self.position = point
   def get_position(self):
      return self.position
   def get_images(self):
      return self.imgs
   def get_image(self):
      return self.imgs[self.current_img]
   def get_rate(self):
      return self.rate
   def set_resource_count(self, n):
      self.resource_count = n
   def get_resource_count(self):
      return self.resource_count
   def get_resource_limit(self):
      return self.resource_limit
   def get_resource_distance(self):
      return self.resource_distance
   def get_name(self):
      return self.name
   def get_animation_rate(self):
      return self.animation_rate
   def remove_pending_action(self, action):
      if hasattr(self, "pending_actions"):
         self.pending_actions.remove(action)
   def add_pending_action(self, action):
      if hasattr(self, "pending_actions"):
         self.pending_actions.append(action)
   def get_pending_actions(self):
      if hasattr(self, "pending_actions"):
         return self.pending_actions
      else:
         return []
   def clear_pending_actions(self):
      if hasattr(self, "pending_actions"):
         self.pending_actions = []
   def next_image(self):
      self.current_img = (self.current_img + 1) % len(self.imgs)

class Quake:
   def __init__(self, name, position, imgs, animation_rate):
      self.name = name
      self.position = position
      self.imgs = imgs
      self.current_img = 0
      self.animation_rate = animation_rate
      self.pending_actions = []

   def set_position(self, point):
      self.position = point
   def get_position(self):
      return self.position
   def get_images(self):
      return self.imgs
   def get_image(self):
      return self.imgs[self.current_img]
   def get_rate(self):
      return self.rate
   def set_resource_count(self, n):
      self.resource_count = n
   def get_resource_count(self):
      return self.resource_count
   def get_resource_limit(self):
      return self.resource_limit
   def get_resource_distance(self):
      return self.resource_distance
   def get_name(self):
      return self.name
   def get_animation_rate(self):
      return self.animation_rate
   def remove_pending_action(self, action):
      if hasattr(self, "pending_actions"):
         self.pending_actions.remove(action)
   def add_pending_action(self, action):
      if hasattr(self, "pending_actions"):
         self.pending_actions.append(action)
   def get_pending_actions(self):
      if hasattr(self, "pending_actions"):
         return self.pending_actions
      else:
         return []
   def clear_pending_actions(self):
      if hasattr(self, "pending_actions"):
         self.pending_actions = []
   def next_image(self):
      self.current_img = (self.current_img + 1) % len(self.imgs)
   


##def set_position(entity, point):
##   entity.position = point
##def set_position(self, point):
##   self.position = point

##def get_position(entity):
##   return entity.position
##def get_position(self):
##   return self.position


##def get_images(entity):
##   return entity.imgs
##def get_images(self):
##   return self.imgs

##def get_image(entity):
##   return entity.imgs[entity.current_img]
##def get_image(self):
##   return self.imgs[self.current_img]


##def get_rate(entity):
##   return entity.rate
##def get_rate(self):
##   return self.rate


##def set_resource_count(entity, n):
##   entity.resource_count = n
##def set_resource_count(self, n):
##   self.resource_count = n

##def get_resource_count(entity):
##   return entity.resource_count
##def get_resource_count(self):
##   return self.resource_count


##def get_resource_limit(entity):
##   return entity.resource_limit
##def get_resource_limit(self):
##   return self.resource_limit


##def get_resource_distance(entity):
##   return entity.resource_distance
##def get_resource_distance(self):
##   return self.resource_distance


##def get_name(entity):
##   return entity.name
##def get_name(self):
##   return self.name


##def get_animation_rate(entity):
##   return entity.animation_rate
##def get_animation_rate(self):
##   return self.animation_rate


##def remove_pending_action(entity, action):
##   if hasattr(entity, "pending_actions"):
##      entity.pending_actions.remove(action)
##def remove_pending_action(self, action):
##   if hasattr(self, "pending_actions"):
##      self.pending_actions.remove(action)

##def add_pending_action(entity, action):
##   if hasattr(entity, "pending_actions"):
##      entity.pending_actions.append(action)
##def add_pending_action(self, action):
##   if hasattr(self, "pending_actions"):
##      self.pending_actions.append(action)


##def get_pending_actions(entity):
##   if hasattr(entity, "pending_actions"):
##      return entity.pending_actions
##   else:
##      return []
##def get_pending_actions(self):
##   if hasattr(self, "pending_actions"):
##      return self.pending_actions
##   else:
##      return []

##def clear_pending_actions(entity):
##   if hasattr(entity, "pending_actions"):
##      entity.pending_actions = []
##def clear_pending_actions(self):
##   if hasattr(self, "pending_actions"):
##      self.pending_actions = []


##def next_image(entity):
##   entity.current_img = (entity.current_img + 1) % len(entity.imgs)
##def next_image(self):
##   self.current_img = (self.current_img + 1) % len(self.imgs)


# This is a less than pleasant file format, but structured based on
# material covered in course.  Something like JSON would be a
# significant improvement.
##def entity_string(entity):
##   if isinstance(entity, MinerNotFull):
##      return ' '.join(['miner', entity.name, str(entity.position.x),
##         str(entity.position.y), str(entity.resource_limit),
##         str(entity.rate), str(entity.animation_rate)])
##   elif isinstance(entity, Vein):
##      return ' '.join(['vein', entity.name, str(entity.position.x),
##         str(entity.position.y), str(entity.rate),
##         str(entity.resource_distance)])
##   elif isinstance(entity, Ore):
##      return ' '.join(['ore', entity.name, str(entity.position.x),
##         str(entity.position.y), str(entity.rate)])
##   elif isinstance(entity, Blacksmith):
##      return ' '.join(['blacksmith', entity.name, str(entity.position.x),
##         str(entity.position.y), str(entity.resource_limit),
##         str(entity.rate), str(entity.resource_distance)])
##   elif isinstance(entity, Obstacle):
##      return ' '.join(['obstacle', entity.name, str(entity.position.x),
##         str(entity.position.y)])
##   else:
##      return 'unknown'


###if isinstance(entity, MinerNotFull):
##def entity_string(self):
##   return ' '.join(['miner', entity.name, str(entity.position.x),
##      str(entity.position.y), str(entity.resource_limit),
##      str(entity.rate), str(entity.animation_rate)])

###elif isinstance(entity, Vein):
##def entity_string(self):
##   return ' '.join(['vein', entity.name, str(entity.position.x),
##      str(entity.position.y), str(entity.rate),
##      str(entity.resource_distance)])

###elif isinstance(entity, Ore):
##def entity_string(self):
##   return ' '.join(['ore', entity.name, str(entity.position.x),
##      str(entity.position.y), str(entity.rate)])

###elif isinstance(entity, Blacksmith):
##def entity_string(self):
##   return ' '.join(['blacksmith', entity.name, str(entity.position.x),
##      str(entity.position.y), str(entity.resource_limit),
##      str(entity.rate), str(entity.resource_distance)])

###elif isinstance(entity, Obstacle):
##def entity_string(self):
##   return ' '.join(['obstacle', self.name, str(self.position.x),
##      str(self.position.y)])
###else:
##   return 'unknown'
