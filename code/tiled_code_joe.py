import pygame, sys
from pytmx.util_pygame import load_pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)

TILED_CELL_WIDTH = 128
TILED_CELL_HEIGHT = 128
pygame.init()
screen = pygame.display.set_mode((1280,720))
# load tmx file
tmx_data = load_pygame('./data/tmx/basic.tmx')
sprite_group = pygame.sprite.Group()

# cycle through all layers and get tiles (not objects)
for layer in tmx_data.visible_layers:
    if hasattr(layer,'data'):   # This is the best way he knows of getting tiles only, but may be better way
        for x,y,surf in layer.tiles():
            pos = (x * TILED_CELL_WIDTH, y * TILED_CELL_HEIGHT)
            Tile(pos = pos, surf = surf, groups = sprite_group)


    # Get objects
    for obj in tmx_data.objects:
        pos = obj.x,obj.y
        if obj.type not in ('Shape','Text'): # This type is set in Tiled.
            Tile(pos = pos, surf = obj.image, groups = sprite_group)



        




# # Layers
# print(tmx_data.layers) # Get all layer names and types
# for layer in tmx_data.visible_layers: # Get only layers visilbe in tiled
#     print(layer)
# print(tmx_data.layernames) # Get a dictionary of all layer names
# print(tmx_data.get_layer_by_name('Floor')) # Get one layer by name)

# # Objects
# for obj_layer in tmx_data.objectgroups: # Get object layers
#     print(obj_layer)


### Get tiles
# layer = tmx_data.get_layer_by_name('Floor')
# print(dir(layer)) # See what you can get from a layer

# for tile in layer.tiles():
#     print(tile) # Returns the x, y, and Surface of each tile
    # Note that the x and y values are actually the cell grid location, so you'd need to multiply them by the tile sizes

# This is the main way you'll be working with this information:
# for x,y,surf in layer.tiles():
#     print(x * 128)
#     print(y * 128)
#     print(surf)

# print(layer.data) # Returns csv information (probably won't use)

### Get objects 
# If you just want objects from a specific layer: (You'll use this most often)
# object_layer = tmx_data.get_layer_by_name('Objects')
# for obj in object_layer:
    # print(obj.x)
    # print(obj.y)
    # print(obj.image)

# If you want all objects:
# for obj in tmx_data.objects:    
#     print(obj.x)
    # print(obj.y)
    # print(obj.image)

# If you want to get shapes
# for obj in object_layer:
#     if obj.type == 'Shape':
        # if obj.name == 'Marker':
        #     print(obj.x)
        #     print(obj.y)
        # if obj.name == 'Rectangle':
        #     print(obj.x)
        #     print(obj.y)
        #     print(obj.width)
        #     print(obj.height)
        #     print(obj.as_points) # Returns all four corners
        # if obj.name == 'Ellipse':
        #     print(dir(obj))
        # if obj.name == 'Polygon':
        #     print(obj.as_points) # Bounding box of the shape, not the actual points
        #     print(obj.points) # Returns the actual points of the polygon




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    sprite_group.draw(screen)

    for obj in tmx_data.objects:    # Doing this here because doesn't make sense to add these to the Tile class (Thgouh same for obj imho but whatever)
        if obj.type in ('Shape'): 
            if obj.name == 'Marker':
                pygame.draw.circle(screen,'red',(obj.x,obj.y),5)
            if obj.name == 'Rectangle':
                rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                pygame.draw.rect(screen,'yellow',rect)
            if obj.name == 'Ellipse':
                rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height)
                pygame.draw.ellipse(screen,'blue',rect)
            if obj.name == 'Polygon':
                points = [(point.x,point.y) for point in obj.points]
                pygame.draw.polygon(screen,'green',points)


    pygame.display.update()
