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
        return r, g, b
    else:
        return 0,0,0

def BWToon(render, **kwargs):
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

    if intensity > 0.8:
        r = 1
        g = 1
        b = 0
    elif intensity > 0.4:
        r = 1
        g = 0.3
        b = 0.28
    else:
        r = 0.5
        g = 0
        b = 0.5


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
        return intensity, intensity, 0
    else:
        return r * intensity, g * intensity, b * intensity

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