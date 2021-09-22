import taichi as ti

ti.init()

res = (512, 512)
pixels = ti.Vector.field(3, dtype=float, shape=res)


@ti.kernel
def paint(time: int):
    for i, j in pixels:
        u = i / res[0]
        v = j / res[1]
        pixels[i, j] = [u, v, sin(time)]


gui = ti.GUI('UV', res)
i = 0
while not gui.get_event(ti.GUI.ESCAPE):
    paint(i)
    gui.set_image(pixels)
    gui.show()
    i += 1
