# Carga un archivo tipo OBJ

from os import error


class Obj(object):
    def __init__(self, filename):
        
        with open(filename, "r") as file:
            self.lines = file.read().splitlines()

        self.vertices = []
        self.texcoords = []
        self.normals = []
        self.faces = []

        self.readFile()
    
    def readFile(self):
        for line in self.lines:
            if line and line[0] != '#':
                prefix, value = line.split(' ', 1)

                if prefix == 'v': # Vertex
                    self.vertices.append(list(map(float, value.split(' '))))
                elif prefix == 'vt': # Texture Coords
                    self.texcoords.append(list(map(float, value.split(' '))))
                elif prefix == 'vn': # Normal
                    self.normals.append(list(map(float, value.split(' '))))
                elif prefix == 'f': # Faces
                    self.faces.append([ list(map(int, vert.split('/'))) for vert in value.split(' ') if vert != ''])
                

                    
