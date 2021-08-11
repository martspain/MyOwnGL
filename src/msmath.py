# Math Library
# Author: Martín España

from collections import namedtuple
from math import sin, cos

V2 = namedtuple('Point2', ['x', 'y'])
V3 = namedtuple('Point3', ['x', 'y', 'z'])

pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067

# Adds all values in array
def add(array):
    total = 0
    for elem in array:
        total += elem
    return total

# Adds points on 2 dimensional space
def add2(A, B):
    return V2(A.x + B.x, A.y + B.y)

# Adds points in array on 2 dimensional space
def add2(array):
    result = V2(0,0)
    for point in array:
        result = V2(result.x + point.x, result.y + point.y)
    return result

# Adds points on 3 dimensional space
def add3(A, B):
    return V3(A.x + B.x, A.y + B.y, A.z + B.z)

# Adds points in array on 3 dimensional space
def add3(array):
    result = V3(0,0,0)
    for point in array:
        result = V3(result.x + point.x, result.y + point.y, result.z + point.z)
    return result

def subtract2(A, B):
    return V2(A.x - B.x, A.y - B.y)

def subtract3(A, B):
    return V3(A.x - B.x, A.y - B.y, A.z - B.z)

def dot(A, B):
    return A.x * B.x + A.y * B.y + A.z * B.z

def cross(A, B):
    i = ((A.y * B.z) - (A.z * B.y))
    j = -((A.x * B.z) - (A.z * B.x))
    k = ((A.x * B.y) - (A.y * B.x))
    product = V3(i, j, k)
    return product

def sqroot(dividend, maxPrecision = None):
    
    if maxPrecision:
        maxPreci = maxPrecision
    else:
        maxPreci = 8

    isImaginarian = False

    def decimalCount(num):
        if str(num).find(".") >= 0:
            decimals = str(num).split(".")
            return len(decimals[1])
        elif str(num).find(".") < 0:
            return 0

    if dividend < 0:
        dividend = abs(dividend)
        isImaginarian = True

    if dividend == 0:
        return 0
    elif 0 < abs(dividend) < 10:
        divisor = 1.1
    elif 10 <= abs(dividend) < 10000:
        divisor = 10
    elif 10000 <= abs(dividend) < 1000000:
        divisor = 100
    else:
        divisor = 1000
    
    done = False

    while not done:
        quotient = dividend / divisor
        precision = min(decimalCount(quotient), decimalCount(divisor))
        if precision > maxPreci:
            precision = maxPreci
        
        if round(quotient, precision) < round(divisor, precision):
            divisor -= ((divisor - quotient) / 2)
        elif round(quotient, precision) > round(divisor, precision):
            divisor += ((quotient - divisor) / 2)
        elif round(quotient, precision) == round(divisor, precision):
            done = True
            if isImaginarian:
                return str(round(quotient, precision)) + " i"
            elif not isImaginarian:
                return round(quotient, precision)

def power(base, exp):
    # TODO 
    # This is functional but can do better
    result = 1
    while exp > 0:
        result = result * base
        exp -= 1
    return result

def normalize(vector):
    if len(vector) == 2:
        mag = sqroot(vector.x * vector.x + vector.y * vector.y)
        if mag != 0:
            unitVec = V2(vector.x / mag, vector.y / mag)
        else:
            unitVec = V2(0,0)
        return unitVec
    elif len(vector) == 3:
        mag = sqroot(vector.x * vector.x + vector.y * vector.y + vector.z * vector.z)
        if mag != 0:
            unitVec = V3(vector.x / mag, vector.y / mag, vector.z / mag)
        else:
            unitVec = V3(0,0,0)
        return unitVec

def sine(degrees):
    return sin(radians(degrees))

def cosine(degrees):
    return cos(radians(degrees))

def degrees(radians):
    return (radians * 180) / pi

def radians(degrees):
    return (degrees * pi) / 180

def identityMatrix(dimension):
    mat = []

    if dimension > 0:
        for n in range(dimension):
            mat.append([])
            for m in range(dimension):
                if n == m:
                    mat[n].append(1)
                else:
                    mat[n].append(0)
    
    return mat