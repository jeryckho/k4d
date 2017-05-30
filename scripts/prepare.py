# "C:\Program Files\Blender Foundation\Blender\blender.exe" --python Doudou.py

import bpy
import sys
import time
start = time.time()

argv = sys.argv
try:
    index = argv.index("--") + 1
except ValueError:
    index = len(argv)

argv = argv[index:]

bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
if len(argv) > 0:
    bpy.context.scene.render.resolution_percentage = int(argv[0])

if (len(argv) > 1) and (int(argv[1]) > 0):
    bpy.ops.render.render(animation=True)

end = time.time()
elapsed = end - start
print(time.strftime("%A %d %B %Y %H:%M:%S",time.localtime(start)))
print(time.strftime("%A %d %B %Y %H:%M:%S",time.localtime(end)))
print(elapsed)
