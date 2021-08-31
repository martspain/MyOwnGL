from msmath import *
import random

def flat(render, **kwargs):
    A, B, C = kwargs['verts']
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)

        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    normal = cross(subtract3(B, A), subtract3(C, A))
    normal = normalize(normal)
    intensity = dot(normal, scalarVec(-1, render.directional_light))

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def gouraud(render, **kwargs):
    A, B, C = kwargs['verts']
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)

        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    intensityA = dot(nA, scalarVec(-1, render.directional_light))
    intensityB = dot(nB, scalarVec(-1, render.directional_light))
    intensityC = dot(nC, scalarVec(-1, render.directional_light))

    intensity = intensityA * u + intensityB * v + intensityC * w
    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def phong(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)

        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = V3(nX, nY, nZ)

    intensity = dot(normal, scalarVec(-1, render.directional_light))

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def unlit(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)

        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    return r, g, b

def toon(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)

        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = V3(nX, nY, nZ)

    intensity = dot(normal, scalarVec(-1, render.directional_light))

    if intensity > 0.7:
        intensity = 1
    elif intensity > 0.3:
        intensity = 0.5
    else:
        intensity = 0.05


    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def BWToon(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = V3(nX, nY, nZ)

    intensity = dot(normal, scalarVec(-1, render.directional_light))

    if intensity > 0.85:
        intensity = 1
    elif intensity > 0.6:
        intensity = 0.8
    elif intensity > 0.45:
        intensity = 0.55
    elif intensity > 0.3:
        intensity = 0.4
    elif intensity > 0.15:
        intensity = 0.25
    else:
        intensity = 0.1


    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return intensity, intensity, intensity
    else:
        return 0,0,0

def thermal(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)

        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = V3(nX, nY, nZ)

    intensity = dot(normal, scalarVec(-1, render.directional_light))

    if intensity > 1:
        intensity = 1
    elif intensity < 0:
        intensity = 0

    if intensity > 0.9:
        r = 1
        g = 1
        b = 0
    elif intensity > 0.8:
        r = 1
        g = 0.5
        b = 0
    elif intensity > 0.7:
        r = 1
        g = 0
        b = 0
    elif intensity > 0.6:
        r = 1
        g = 0.3
        b = 0.28
    elif intensity > 0.5:
        r = 0.8
        g = 0.2
        b = 0.3
    elif intensity > 0.4:
        r = 0.7
        g = 0.1
        b = 0.4
    elif intensity > 0.3:
        r = 0.5
        g = 0
        b = 0.5
    elif intensity > 0.2:
        r = 0.3
        g = 0
        b = 0.3
    elif intensity > 0.1:
        r = 0.1
        g = 0
        b = 0.1
    else:
        r = 0
        g = 0
        b = 0


    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0
    

def lines(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)

        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = V3(nX, nY, nZ)

    intensity = dot(normal, scalarVec(-1, render.directional_light))

    if intensity > 1:
        intensity = 1
    elif intensity < 0:
        intensity = 0

    r = random.random()
    g = random.random()
    b = random.random()

    edgeLim = 0.02

    if (u < edgeLim) and (v < edgeLim) and (w < edgeLim):
        return r * intensity, g * intensity, b * intensity
    elif (u < edgeLim) and (v < edgeLim):
        return r * intensity, g * intensity, b * intensity
    elif (u < edgeLim) and (w < edgeLim):
        return r * intensity, g * intensity, b * intensity
    elif (v < edgeLim) and (w < edgeLim):
        return r * intensity, g * intensity, b * intensity
    elif (u < edgeLim) or (v < edgeLim) or (w < edgeLim):
        return r * intensity, g * intensity, b * intensity
    else:
        return None, None, None

def negative(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)

        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = V3(nX, nY, nZ)

    intensity = dot(normal, scalarVec(-1, render.directional_light))

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return 1 - r, 1 - g, 1 - b
    else:
        return 1,1,1


def normalMap(render, **kwargs):
    A, B, C = kwargs['verts']
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)

        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = V3(nX, nY, nZ)

    if render.normal_map:
        texNormal = render.normal_map.getColor(tx, ty)
        texNormal = [texNormal[2] / 255 * 2 - 1, texNormal[1] / 255 * 2 - 1, texNormal[0] / 255 * 2 - 1]

        edgeOne = subtract3(B, A)
        edgeTwo = subtract3(C, A)
        #deltaUV1

    else:
        intensity = dot(normal, scalarVec(-1, render.directional_light))

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0
    
def toonvar(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)

        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = V3(nX, nY, nZ)

    magNor = magnitude(normal)
    magCam = magnitude(scalarVec(-1,render.directional_light))

    if round(dot(normal, render.directional_light)) == -round(magNor * magCam):
        intensity = dot(normal, scalarVec(-1, render.directional_light))
        
        if intensity < 0.3:
            b *= 0.3
            g *= 0.3
            r *= 0.3
        elif intensity < 0.6:
            b *= 0.6
            g *= 0.6
            r *= 0.6
        elif intensity < 0.9:
            b *= 0.9
            g *= 0.9
            r *= 0.9
        else:
            b *= 1
            g *= 1
            r *= 1
    else:
        intensity = 1
        b = 1 - render.curr_color[0]/255
        g = 1 - render.curr_color[1]/255
        r = 1 - render.curr_color[2]/255

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def glow(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)

        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = V3(nX, nY, nZ)

    intensity = dot(normal, scalarVec(-1, render.directional_light))

    b *= intensity
    g *= intensity
    r *= intensity

    camVec = V3(render.camMatrix[0][2],
              render.camMatrix[1][2],
              render.camMatrix[2][2])

    glowSum = 1 - dot(normal, camVec)
    glowAdd = [1,1,0]

    r += glowAdd[0] * 0.5 * glowSum
    g += glowAdd[1] * 0.5 * glowSum
    b += glowAdd[2] * 0.5 * glowSum

    if r > 1:
        r = 1
    elif r < 0:
        r = 0
    if g > 1:
        g = 1
    elif g < 0:
        g = 0
    if b > 1:
        b = 1
    elif b < 0:
        b = 0

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def static(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)

        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = V3(nX, nY, nZ)

    intensity = dot(normal, scalarVec(-1, render.directional_light))

    r = random.random()
    g = random.random()
    b = random.random()

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def zebra(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)

        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = V3(nX, nY, nZ)

    intensity = dot(normal, scalarVec(-1, render.directional_light))

    colVal = [0,0,0]

    if 0.9 < intensity <= 1:
        colVal = [0.2, 0.2, 0.2]
    elif 0.8 < intensity <= 0.9:
        colVal = [1,1,1]
    elif 0.7 < intensity <= 0.8:
        colVal = [0.2, 0.2, 0.2]
    elif 0.6 < intensity <= 0.7:
        colVal = [1,1,1]
    elif 0.5 < intensity <= 0.6:
        colVal = [0.2, 0.2, 0.2]
    elif 0.4 < intensity <= 0.5:
        colVal = [1,1,1]
    elif 0.3 < intensity <= 0.4:
        colVal = [0.2, 0.2, 0.2]
    elif 0.2 < intensity <= 0.3:
        colVal = [1,1,1]
    elif 0.1 < intensity <= 0.2:
        colVal = [0.2, 0.2, 0.2]
    elif 0 < intensity <= 0.1:
        colVal = [1,1,1]

    r = colVal[0]
    g = colVal[1]
    b = colVal[2]

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def rand(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)

        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = V3(nX, nY, nZ)

    intensity = dot(normal, scalarVec(-1, render.directional_light))

    random.seed((u + v + w) * 100)
    r = random.random() * intensity
    #random.seed((u + v + w) * 50)
    g = random.random() * intensity
    #random.seed((u + v + w) * 50)
    b = random.random() * intensity

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def sky(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)

        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = V3(nX, nY, nZ)

    intensity = dot(normal, scalarVec(-1, render.directional_light))

    definer = random.random()

    if 0 <= intensity < 0.33:
        if 0.999 <= definer < 1:
            r = 1
            g = 1
            b = 1
        else:
            r = 0.0549
            g = 0.0431
            b = 0.2471
    elif 0.33 <= intensity < 0.66:
        if 0.989 <= definer < 1:
            r = 1
            g = 1
            b = 1
        else:
            r = 0.0549
            g = 0.0431
            b = 0.2471

    elif 0.66 <= intensity <= 1:
        if 0.979 <= definer < 1:
            r = 1
            g = 1
            b = 1
        else:
            r = 0.0549
            g = 0.0431
            b = 0.2471

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def points(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)

        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = V3(nX, nY, nZ)

    intensity = dot(normal, scalarVec(-1, render.directional_light))

    definer = random.random()

    if 0 <= definer < 0.5:
        r = render.clear_color[0]/255
        g = render.clear_color[1]/255
        b = render.clear_color[2]/255

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def triangleColor(render, **kwargs):
    A, B, C = kwargs['verts']
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)

        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    normal = cross(subtract3(B, A), subtract3(C, A))
    normal = normalize(normal)
    intensity = dot(normal, scalarVec(-1, render.directional_light))

    random.seed(intensity * 100)

    r = random.random()
    g = random.random()
    b = random.random()

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0
