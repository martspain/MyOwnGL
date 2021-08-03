import struct
from collections import namedtuple
from obj import Obj
from math import acos, degrees, sqrt

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

    # Changes the color of 1 pixel of the viewport (normalized)
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

    # Gets the points used for the line
    def glLinePoints(self, v0, v1):
        x0 = v0.x
        x1 = v1.x
        y0 = v0.y
        y1 = v1.y

        # Avoids drawing a line from one position to itself
        if x0 == x1 and y0 == y1:
            return [V2(x0,y0)]

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

        preanswer = []
        answer = []
        ycount = []

        for x in range(x0, x1 + 1):
            if steep:
                preanswer.append(V2(y, x))
            else:
                preanswer.append(V2(x, y))

            offset += m
            if offset >= limit:
                y += 1 if y0 < y1 else -1
                limit += 1
        
        for ind in range(len(preanswer)):
            if preanswer[ind].y not in ycount:
                ycount.append(preanswer[ind].y)
                answer.append(preanswer[ind])
            
        return answer

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

    # Draws the lines of a polygon
    def glPoly(self, poly, color = None):
        for p in range(len(poly)):
            nextIndex = p + 1
            if nextIndex < len(poly):
                x0 = poly[p].x
                y0 = poly[p].y
                x1 = poly[nextIndex].x
                y1 = poly[nextIndex].y

                self.glLine(V2(x0, y0), V2(x1, y1), color)
            
            else:
                x0 = poly[p].x
                y0 = poly[p].y
                initx = poly[0].x
                inity = poly[0].y
                self.glLine(V2(x0, y0), V2(initx, inity), color)

    # Draws a filled polygon
    def glSolidPoly(self, poly, color = None):
        #Verifies there is at least 3 vertexes
        if len(poly) < 3:
            if len(poly) == 1:
                self.glPoint(int(poly[0].x), int(poly[0].y), color)
            elif len(poly) == 2:
                self.glLine(V2(poly[0].x, poly[0].y), V2(poly[1].x, poly[1].y), color)
            else:
                return
        
        xverts = []
        yverts = []

        linesdata = []

        xmin = 0
        xmax = 0
        ymin = 0
        ymax = 0

        for v in range(len(poly)):
            # Se guardan las coordenadas de x y y por separado
            xverts.append(poly[v].x)
            yverts.append(poly[v].y)

            # Se dibuja el contorno del poligono
            nextIndex = v + 1
            if nextIndex < len(poly):
                x0 = poly[v].x
                y0 = poly[v].y
                x1 = poly[nextIndex].x
                y1 = poly[nextIndex].y

                self.glLine(V2(x0, y0), V2(x1, y1), color)

                linesdata.append(self.glLinePoints(V2(x0, y0), V2(x1, y1)))
            
            else:
                x0 = poly[v].x
                y0 = poly[v].y
                initx = poly[0].x
                inity = poly[0].y
                self.glLine(V2(x0, y0), V2(initx, inity), color)
                linesdata.append(self.glLinePoints(V2(x0, y0), V2(initx, inity)))

        # Se encuentra el minimo y maximo de x y y
        xmin = min(xverts)
        xmax = max(xverts)
        ymin = min(yverts)
        ymax = max(yverts)
        
        ycount = ymin
        xcount = xmin
        intercount = []

        while ycount < ymax:
            while xcount < xmax:
                for line in linesdata:
                    for point in line:
                        if point.x == xcount and point.y == ycount:
                            intercount.append(V2(xcount, ycount))
                # if len(intercount) > 0:
                #     if (len(intercount)%2) != 0:
                #         self.glPoint(xcount, ycount, color)
                #         xcount += 1
                #     else:
                #         xcount += 1
                # elif len(intercount) == 0:
                xcount += 1
            
            if len(intercount) > 0:
                if len(intercount) == 1:
                    self.glPoint(intercount[0].x, intercount[0].y, color)
                elif len(intercount) == 2:
                    self.glLine(intercount[0], intercount[1], color)
                elif len(intercount) == 3:
                    self.glLine(intercount[0], intercount[1], color)
                    self.glLine(intercount[1], intercount[2], color)
                elif len(intercount) == 4:
                    self.glLine(intercount[0], intercount[1], color)
                    self.glLine(intercount[2], intercount[3], color)



            ycount += 1
            xcount = xmin
            intercount = []

    # Draws a filled polygon through triangulation
    def glPolyTest(self, poly, color = None):
        
        triList = []
        vertIndex = 1
        
        while len(poly) >= 3:
            # Find the angle for each vert
            # Let b be the current vertex, and a, and c be the vertexes together
            # angle = arcos((xa * xb + ya * yb)/(sqr(xa^2 + ya^2) * sqr(xb^2 + yb^2))
            # angle = arcos( ((c.x - b.x) * (a.x - b.x) + (c.y - b.y) * (a.y - b.y)) / (sqrt() * sqrt())
            
            def cross(p1, p2, p3, p4):
                xcomp1 = p2.x - p1.x
                xcomp2 = p4.x - p3.x
                ycomp1 = p2.y - p1.y
                ycomp2 = p4.y - p3.y

                return xcomp1 * ycomp2 - ycomp1 * xcomp2
            
            def getItem(array, index):
                if index >= len(array):
                    return array[index % len(array)]
                elif index < 0:
                    return array[index % len(array) + len(array)]
                else:
                    return array[index]




            xa = None
            ya = None

            if (vertIndex + 1) < len(poly):
                xa = poly[vertIndex + 1].x - poly[vertIndex].x
                ya = poly[vertIndex + 1].y - poly[vertIndex].y
            else:
                xa = poly[0].x - poly[vertIndex].x
                ya = poly[0].y - poly[vertIndex].y

            xb = poly[vertIndex - 1].x - poly[vertIndex].x
            yb = poly[vertIndex - 1].y - poly[vertIndex].y

            # Angle in degrees from a certain vertex
            angle = degrees(acos((xa * xb + ya * yb)/(sqrt(xa * xa + ya * ya) * sqrt(xb * xb + yb * yb))))
            
            if angle < 180:
                print("Convex: ", angle)
            elif angle > 180:
                print("Reflex: ", angle)
            elif angle == 180:
                print("Straight: ", angle)

            poly.pop(vertIndex)
            if (vertIndex + 1) < len(poly):
                vertIndex += 1
            else:
                vertIndex = 1
            



    # Draws a filled triangle
    def glTriangle(self, A, B, C, color = None):
        
        self.glLine(A, B, color)
        self.glLine(B, C, color)
        self.glLine(C, A, color)

        if A.y < B.y:
            A, B = B, A
        
        if A.y < C.y:
            A, C = C, A
        
        if B.y < C.y:
            B, C = C, B
        
        def flatBottomTriangle(v1, v2, v3):
            slope_2_1 = (v2.x - v1.x) / (v2.y - v1.y)
            slope_3_1 = (v3.x - v1.x) / (v3.y - v1.y)

            x1 = v2.x
            x2 = v3.x

            for y in range(v2.y, v1.y + 1):
                self.glLine(V2(int(x1), int(y)), V2(int(x2), int(y)), color)
                x1 += slope_2_1
                x2 += slope_3_1

        def flatTopTriangle(v1, v2, v3):
            slope_3_1 = (v3.x - v1.x) / (v3.y - v1.y)
            slope_3_2 = (v3.x - v2.x) / (v3.y - v2.y)

            x1 = v3.x
            x2 = v3.x

            for y in range(v2.y, v1.y + 1):
                self.glLine(V2(int(x1), int(y)), V2(int(x2), int(y)), color)
                x1 += slope_3_1
                x2 += slope_3_2

        if B.y == C.y:
            # Triangle with bottom side straight
            flatBottomTriangle(A, B, C)
        elif A.y == B.y:
            # Triangle with upper side straight
            flatTopTriangle(A, B, C)
        else:
            # Divide triangle in 2, and draw both
            # Intercept Theorem
            # ((A.x + (B.y - A.y)) / (C.y - A.y)) * (C.x - A.x)
            D = V2(A.x + ((B.y - A.y) / (C.y - A.y)) * (C.x - A.x), B.y)

            flatBottomTriangle(A, B, D)
            flatTopTriangle(B, D, C)

    def glGetColor(self, pixel):
        print(self.pixels[int(pixel.x)][int(pixel.y)])

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