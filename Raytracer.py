from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *

width = 612
height = 612

# Materiales
whiteWall = Material(diffuse = (1, 1, 1), spec = 64)
redWall = Material(diffuse = (1, 0.1, 0.1), spec = 64)
blueWall = Material(diffuse = (0, 0, 1), spec = 64)
stone = Material(diffuse = (0.4, 0.4, 0.4), spec = 8)
brick = Material(diffuse = (0.8, 0.3, 0.3), spec = 16)
grass = Material(diffuse = (0.3, 1.0, 0.3), spec = 64)
mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)
glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.5, matType = TRANSPARENT)

rtx = Raytracer(width, height)

# Enviroment Map
# rtx.envMap = Texture("parkingLot.bmp")

# Lightning
rtx.lights.append( AmbientLight(intensity = 0.13 ))
rtx.lights.append( PointLight(point = (-1,-1,1) ))
rtx.lights.append( DirectionalLight(direction=(0, 10, -20), intensity=0.5))
# rtx.scene.append( Disk(position = (0,0,-7), radius = 2, normal = (0,1,0), material = mirror ))

# Planes for room
rtx.scene.append( Plane(position = (0,-8,0), normal = (0,1,0), material = whiteWall )) # Floor
rtx.scene.append( Plane(position = (0,8,0), normal = (0,-1,0), material = whiteWall )) # Celing
rtx.scene.append( Plane(position = (-8,0,0), normal = (1,0,0), material = redWall )) # Side L
rtx.scene.append( Plane(position = (8,0,0), normal = (-1,0,0), material = blueWall )) # Side R
rtx.scene.append( Plane(position = (0,0,-30), normal = (0,0,1), material = whiteWall )) # Fondo

# Figures
# Spheres
rtx.scene.append( Sphere(V3(0,-7,-15), 1.5, glass)  )
rtx.scene.append( Donut(center=(0,-1,-10), externalRadius=1, internalRadius=0.5, material=stone ))


rtx.glRender()
rtx.glFinish("output.bmp")