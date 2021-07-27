import struct
from collections import namedtuple
from obj import Obj

V2 = namedtuple('Point2', ['x', 'y'])

def char(c):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    # 2 bytes
    return struct.pack('=h', w)

def dword(d):
    # 4 bytes
    return struct.pack('=l', d)

def color(r, g, b):
    # Accepts values between 0 and 1
    return bytes([int(b * 255), int(g * 255), int(r * 255)])

# Default colors
Black = color(0,0,0)
White = color(1,1,1)

class Renderer(object):
    # Init
    def __init__(self, width, height):
        self.curr_color = Black
        self.clear_color = White
        self.glCreateWindow(width, height)

    # Creates the window
    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()
        self.glViewport(0,0, width, height)

    # Creates the Viewport
    def glViewport(self, x, y, width, height):
        self.vpX = x
        self.vpY = y
        self.vpWidth = width
        self.vpHeight = height

    # Resets the window
    def glClear(self):
        self.pixels = [[ self.clear_color for y in range(self.height)] for x in range(self.width)]

    # Changes writing color
    def glColor(self, r, g, b):
        self.curr_color = color(r,g,b)

    # Changes background color
    def glClearColor(self, r, g, b):
        self.clear_color = color(r, g, b)

    # Changes the color of 1 pixel of the window
    def glPoint(self, x, y, color = None):
        if x < self.vpX or x >= self.vpX + self.vpWidth or y < self.vpY or y >= self.vpY + self.vpHeight:
            return

        if (0 <= x < self.width) and (0 <= y < self.height):
            self.pixels[int(x)][int(y)] = color or self.curr_color

    # Changes the color of 1 pixel of the viewport
    def glVertex(self, x, y, color = None):
        # Check coordinates to be between -1 and 1
        if x < -1 or x > 1:
            return
        if y < -1 or y > 1:
            return

        pixelX = (x+1) * (self.vpWidth/2) + self.vpX
        pixelY = (y+1) * (self.vpHeight/2) + self.vpY

        if (-1 <= x <= 1) and (-1 <= y <= 1):
            self.pixels[int(pixelX)][int(pixelY)] = color or self.curr_color

    # Creates a line from vertex 1 to vertex 2
    def glLine(self, v0, v1, color = None):
        x0 = v0.x
        x1 = v1.x
        y0 = v0.y
        y1 = v1.y

        # Avoids drawing a line from one position to itself
        if x0 == x1 and y0 == y1:
            self.glPoint(x0, y1)
            return

        # Gets the differentials in absolute value so that the slope is always positive
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        # If slope is too steep then the axis are switched
        steep = dy > dx

        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        # Bresenham's Algorithm
        offset = 0
        limit = 0.5
        m = dy/dx
        y = y0

        for x in range(x0, x1 + 1):
            if steep:
                self.glPoint(y, x, color)
            else:
                self.glPoint(x, y, color)

            offset += m
            if offset >= limit:
                y += 1 if y0 < y1 else -1
                limit += 1

    # Loades an .obj model on screen
    def glLoadModel(self, filename, translate = V2(0.0,0.0),scale = V2(1.0,1.0), prev = False):
        model = Obj(filename)

        for face in model.faces:
            vertCount = len(face)

            for v in range(vertCount):
                index0 = face[v][0] - 1 # Minus 1 because of .obj format
                index1 = face[(v + 1) % vertCount][0] - 1

                vert0 = model.vertices[index0]
                vert1 = model.vertices[index1]

                x0 = int(vert0[0] * scale.x + translate.x)
                y0 = int(vert0[2] * scale.y + translate.y)
                x1 = int(vert1[0] * scale.x + translate.x)
                y1 = int(vert1[2] * scale.y + translate.y)

                if prev:
                    self.glPoint(x0, y0)
                else:
                    self.glLine(V2(x0, y0), V2(x1, y1))
                # self.glPoint(x0, y0)

    def glFinish(self, filename):
        with open(filename, "wb") as file:
            # # # # # # #
            # HEADER
            # # # # # # #
            # Signature
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            # File size
            file.write(dword(14 + 40 + (self.width * self.height * 3)))
            # Reserved
            file.write(dword(0))
            # Data Offset
            file.write(dword(14 + 40))

            # # # # # # # 
            # INFO HEADER
            # # # # # # # 
            # Size
            file.write(dword(40))
            # Width
            file.write(dword(self.width))
            # Height
            file.write(dword(self.height))
            # Planes
            file.write(word(1))
            # Bits per pixel
            file.write(word(24))
            # Compression
            file.write(dword(0))
            # Image Size
            file.write(dword(self.width * self.height * 3))
            # Horizontal resolution pixels/meter
            file.write(dword(0))
            # Vertical resolution pixels/meter
            file.write(dword(0))
            # Colors used
            file.write(dword(0))
            # Number of important colors (0 = all)
            file.write(dword(0))

            # # # # # # # 
            # COLOR TABLE
            # # # # # # #
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])