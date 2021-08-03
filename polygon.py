# Representa un poligono

class Polygon(object):
    def __init__(self, verts):
        self.vertices = []

        for x in verts:
            self.vertices.append(x)

    def triangulate(self):
        if len(self.vertices) == 0:
            print("No hay vertices")
            return False
        elif len(self.vertices) < 3:
            print("No hay suficientes vertices")
            return False
        elif len(self.vertices) > 1024:
            print("Se excedió el límite")
            return False
    
    def isSimplePoly(self):
        pass