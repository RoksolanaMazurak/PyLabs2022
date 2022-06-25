from Cone import Cone
from Cube import Cube
from Cylinder import Cylinder
from Ellipsoid import Ellipsoid
from Parallelepiped import Parallelepiped
from Sphere import Sphere


def main():

    parallelepiped1 = Parallelepiped("parallelepiped", 100, 5, 15, 12, "straight parallelepiped")
    cube1 = Cube("cube", 125, 5, 8.66, 12, "rectangular parallelpiped with equals sides", "cut cube")
    cone1 = Cone("cone", 256, 35, 10, 20, "1:10", "cut cone")
    cylinder1 = Cylinder("cylinder", 321, 9, 15, 30, "circles", "unknown")
    sphere1 = Sphere("sphere", 120, 7, 10, 20, "sphere", 25, "cut sphere")
    ellipsoid1 = Ellipsoid("ellipsoid", 240, 13, 3, 9, "triaxial")

    print(parallelepiped1)
    print(cube1)
    print(cone1)
    print(cylinder1)
    print(ellipsoid1)
    print(sphere1)

    print()

    print(parallelepiped1.draw_figure())
    print(cube1.draw_figure())
    print(cone1.draw_figure())
    print(cylinder1.draw_figure())
    print(ellipsoid1.draw_figure())
    print(sphere1.draw_figure())


if __name__ == "__main__":
    main()
