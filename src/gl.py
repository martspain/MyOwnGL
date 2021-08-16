import struct
from msmath import V2, V3, V4, cross, dot, multMatrix, sine, cosine, tangent, sqroot, normalize, subtract3, invMatrix, scalarVec
from obj import Obj, Texture

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

def baryCoords(A, B, C, P):
    try:
        # PCB / ABC
        u = (((B.y - C.y) * (P.x - C.x) + (C.x - B.x) * (P.y - C.y)) / ((B.y - C.y) * (A.x - C.x) + (C.x - B.x) * (A.y - C.y)))

        # PCA / ABC
        v = (((C.y - A.y) * (P.x - C.x) + (A.x - C.x) * (P.y - C.y)) / ((B.y - C.y) * (A.x - C.x) + (C.x - B.x) * (A.y - C.y)))
        # 
        w = 1 - u - v

    except:
        return -1, -1, -1
    
    return u, v, w

# Default colors
Black = color(0,0,0)
White = color(1,1,1)

class Renderer(object):
    # Init
    def __init__(self, width, height):
        self.curr_color = Black
        self.clear_color = White
        self.glViewMatrix()
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

        self.viewportMatrix = [[width/2, 0, 0, x + width/2],
                               [0, height/2, 0, y + height/2],
                               [0, 0, 0.5, 0.5],
                               [0, 0, 0, 1]]
        
        self.glProjectionMatrix()

    # Resets the window
    def glClear(self):
        self.pixels = [[ self.clear_color for y in range(self.height)] for x in range(self.width)]

        self.zbuffer = [[float('inf') for y in range(self.height)] for x in range(self.width)]

    # Changes writing color
    def glColor(self, r, g, b):
        self.curr_color = color(r,g,b)

    # Gets the color of the specified pixel
    def glGetColor(self, pixel):
        print(self.pixels[int(pixel.x)][int(pixel.y)])

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
            
    # Draws a filled triangle using barycentric coordinates
    def glTriangle_bc(self, A, B, C, daColor = None,  intensity = 1, texture = None, texCoords = ()):
        
        #Bounding Box
        minx = round(min(A.x, B.x, C.x))
        miny = round(min(A.y, B.y, C.y))
        maxx = round(max(A.x, B.x, C.x))
        maxy = round(max(A.y, B.y, C.y))

        for x in range(minx, maxx + 1):
            for y in range(miny, maxy + 1):
                u, v, w = baryCoords(A, B, C, V2(x, y))

                if u >= 0 and v >= 0 and w >= 0:
                    
                    z = A.z * u + B.z * v + C.z * w

                    if texture:
                        tA, tB, tC = texCoords
                        xtex = tA[0] * u + tB[0] * v + tC[0] * w
                        ytex = tA[1] * u + tB[1] * v + tC[1] * w

                        daColor = texture.getColor(xtex, ytex)
                    else:
                        if not daColor:
                            daColor = self.curr_color

                    if 0 <= x < self.width and 0 <= y < self.height:
                        if z < self.zbuffer[x][y] and z <= 1 and z >= -1:

                            self.glPoint(x,y, color(daColor[2] * intensity / 255,
                                                    daColor[1] * intensity / 255,
                                                    daColor[0] * intensity / 255) )
                            self.zbuffer[x][y] = z

    # Draws a filled triangle
    def glTriangle_standard(self, A, B, C, color = None):
        
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

    # Transforms one vertex's magnitud
    def glTransform(self, vertex, vMatrix):
        augVertex = [[vertex[0]], 
                     [vertex[1]], 
                     [vertex[2]], 
                     [1]]
        
        # Multiplies model Matrix per augVertex
        transVertex = multMatrix(vMatrix, augVertex)
        
        # Converts it to a V4
        transVertex = V4(transVertex[0][0], transVertex[1][0], transVertex[2][0], transVertex[3][0])

        # Converts it to a V3
        if transVertex.w != 0:
            transVertex = V3(transVertex.x / transVertex.w,
                             transVertex.y / transVertex.w,
                             transVertex.z / transVertex.w)
        else:
            transVertex = V3(transVertex.x * 100000000,
                             transVertex.y * 100000000,
                             transVertex.z * 100000000)
        
        return transVertex

    def glCamTransform(self, vertex):
        augVertex = [[vertex[0]], 
                     [vertex[1]], 
                     [vertex[2]], 
                     [1]]
        
        transVertex = multMatrix(multMatrix(multMatrix(self.viewportMatrix, self.projectionMatrix), self.viewMatrix), augVertex)
        
        # Converts it to a V4
        transVertex = V4(transVertex[0][0], transVertex[1][0], transVertex[2][0], transVertex[3][0])

        # Converts it to a V3
        if transVertex.w != 0:
            transVertex = V3(transVertex.x / transVertex.w,
                             transVertex.y / transVertex.w,
                             transVertex.z / transVertex.w)
        else:
            transVertex = V3(transVertex.x * 100000000,
                             transVertex.y * 100000000,
                             transVertex.z * 100000000)

        return transVertex

    def glCreateRotationMatrix(self, rotate = V3(0,0,0)):

        rotationX = [
            [1, 0, 0, 0],
            [0, cosine(rotate.x), -sine(rotate.x), 0],
            [0, sine(rotate.x), cosine(rotate.x), 0],
            [0, 0, 0, 1]
        ]

        rotationY = [
            [cosine(rotate.y), 0, sine(rotate.y), 0],
            [0, 1, 0, 0],
            [-sine(rotate.y), 0, cosine(rotate.y), 0],
            [0, 0, 0, 1]
        ]

        rotationZ = [
            [cosine(rotate.z), -sine(rotate.z), 0, 0],
            [sine(rotate.z), cosine(rotate.z), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]

        return multMatrix(multMatrix(rotationX, rotationY), rotationZ)

    def glCreateObjectMatrix(self, translate = V3(0,0,0), scale = V3(1,1,1), rotate = V3(0,0,0)):

        translateMatrix = [ 
            [1, 0, 0, translate.x],
            [0, 1, 0, translate.y],
            [0, 0, 1, translate.z],
            [0, 0, 0, 1]
        ]
        
        scaleMatrix = [
            [scale.x, 0, 0, 0],
            [0, scale.y, 0, 0],
            [0, 0, scale.z, 0],
            [0, 0, 0, 1]
        ]

        rotationMatrix = self.glCreateRotationMatrix(rotate)

        return multMatrix(multMatrix(translateMatrix, rotationMatrix), scaleMatrix)

    def glViewMatrix(self, translate = V3(0,0,0), rotate = V3(0,0,0)):
        camMatrix = self.glCreateObjectMatrix(translate, V3(1,1,1), rotate)
        self.viewMatrix = invMatrix(camMatrix)

    def glProjectionMatrix(self, near = 0.1, far = 1000, fov = 60):
            aspectRatio = self.vpWidth / self.vpHeight

            t = tangent(fov/2) * near
            r = t * aspectRatio

            self.projectionMatrix = [[near/r, 0, 0, 0],
                                    [0, near/t, 0, 0],
                                    [0, 0, -(far+near)/(far-near), -2*far*near/(far-near)],
                                    [0, 0, -1, 0]]

    def glLookAt(self, eye, camPos = V3(0,0,0)):
        forward = subtract3(camPos, eye)
        forward = normalize(forward)

        right = cross(V3(0,1,0), forward)
        right = normalize(right)

        up = cross(forward, right)
        up = normalize(up)

        camMatrix = [
            [right.x, up.x, forward.x, camPos.x], 
            [right.y, up.y, forward.y, camPos.y], 
            [right.z, up.z, forward.z, camPos.z],
            [0, 0, 0, 1]
        ]

        self.viewMatrix = invMatrix(camMatrix)

    # Loades an .obj model on screen
    def glLoadModel(self, filename, texture=None, translate = V3(0,0,0), scale = V3(1,1,1), rotate = V3(0,0,0)):
        model = Obj(filename)

        modelMatrix = self.glCreateObjectMatrix(translate, scale, rotate)

        light = V3(0,0,-1)
        light = normalize(light)

        for face in model.faces:
            print(str(round((model.faces.index(face)/len(model.faces)) * 100, 2)) + " %")
            vertCount = len(face)

            vert0 = model.vertices[face[0][0] - 1]
            vert1 = model.vertices[face[1][0] - 1]
            vert2 = model.vertices[face[2][0] - 1]

            vt0 = model.texcoords[face[0][1] - 1]
            vt1 = model.texcoords[face[1][1] - 1]
            vt2 = model.texcoords[face[2][1] - 1]

            a = self.glTransform(vert0, modelMatrix)
            b = self.glTransform(vert1, modelMatrix)
            c = self.glTransform(vert2, modelMatrix)

            if vertCount == 4:
                vt3 = model.vertices[face[3][0] - 1]
                vt2 = model.texcoords[face[3][1] - 1]
                d = self.glTransform(vt3, modelMatrix)
            
            normal = cross(subtract3(V3(vert1[0],vert1[1],vert1[2]), V3(vert0[0],vert0[1],vert0[2])), subtract3(V3(vert2[0],vert2[1],vert2[2]), V3(vert0[0],vert0[1],vert0[2])))
            normal = normalize(normal)
            intensity = dot(normal, scalarVec(-1, light))

            if intensity > 1:
                intensity = 1
            elif intensity < 0:
                intensity = 0

            a = self.glCamTransform(a)
            b = self.glCamTransform(b)
            c = self.glCamTransform(c)

            if vertCount == 4:
                d = self.glCamTransform(d)

            # if round((model.faces.index(face)/len(model.faces)) * 100, 2) == 91.33:
            #     print("Paso 4")
            #     print("a = ", a , " b = ", b, " c = ", c)

            self.glTriangle_bc(a, b, c, daColor = None, texCoords = (vt0,vt1,vt2), texture = texture, intensity = intensity)

            if vertCount == 4:
                self.glTriangle_bc(a, c, d, daColor = None, texCoords = (vt0,vt2,vt3), texture = texture, intensity = intensity)

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