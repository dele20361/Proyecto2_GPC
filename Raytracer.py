from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *

width = 412
height = 312

# Materiales
stone = Material(diffuse = (0.4, 0.4, 0.4), spec = 8)
brick = Material(diffuse = (0.8, 0.3, 0.3), spec = 16)
grass = Material(diffuse = (0.3, 1.0, 0.3), spec = 64)
mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)
glassFloor = Material(diffuse = (0.8, 0.8, 0.8), texture = Texture("chess.bmp"), spec = 64, ior = 1.5, matType = TRANSPARENT)
glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.5, matType = TRANSPARENT)
glass1 = Material(diffuse = (0.8, 0.8, 0.8), spec = 64, ior = 1.5, matType = REFLECTIVE)
glass2 = Material(diffuse = (0.8, 0.9, 0.9), spec = 64, ior = 2.417, matType = TRANSPARENT)
glass3 = Material(diffuse = (0.9, 0.8, 0.9), spec = 64, ior = 1.5, matType = TRANSPARENT)
glass4 = Material(diffuse = (0.9, 0.9, 0.8), spec = 64, ior = 2.417, matType = TRANSPARENT)
glass5 = Material(diffuse = (0.9, 0.7, 0.8), spec = 64, ior = 2.417, matType = TRANSPARENT)

rtx = Raytracer(width, height)

# Enviroment Map
rtx.envMap = Texture("sky4.bmp")

# Lightning
rtx.lights.append( AmbientLight(intensity = 0.13 ))
rtx.lights.append( PointLight(point = (-1,-1,1) ))
rtx.lights.append( DirectionalLight(direction=(0, 10, -20), intensity=0.5))

# Planes for room
rtx.scene.append( Plane(position = (0,-10,0), normal = (0,1,0), material = glassFloor )) # Floor

# Figures
# Spheres
rtx.scene.append( Sphere(V3(-9,-1,-17), 2.5, glass1)  ) # Derecha
rtx.scene.append( Sphere(V3(-0.5,-1,-20), 2, glass2)  ) # Centro
rtx.scene.append( Sphere(V3(3.3,1.5,-10), 1, glass3)  ) # Arriba caja
rtx.scene.append( Sphere(V3(-6,-1,-10), 0.2, glass3)  ) # Chiquis
rtx.scene.append( Sphere(V3(6,-1,-12), 0.5, glass2)  ) # Chiquis
# Squares
rtx.scene.append( AABB(position = (3,-0.5,-10), size = (2,2,2), material = glass4))
rtx.scene.append( AABB(position = (-1.5,-1.1,-5), size = (1,1,1), material = glass5))
# Donut
rtx.scene.append( Donut(center=(-1,0.5,-5), externalRadius = 0.85, internalRadius = 0.5, material = glass ))
rtx.scene.append( Donut(center=(-1,0.5,-5), externalRadius = 0.85, internalRadius = 0.5, material = glass ))
rtx.scene.append( Donut(center=(2.5,2,-4), externalRadius = 0.85, internalRadius = 0.5, material = glass ))

# Disk
rtx.scene.append( Disk(position = (2,-2,-7), radius = 1.5, normal = (0,1,0), material = mirror ))


rtx.glRender()
rtx.glFinish("output.bmp")