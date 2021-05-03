import math

def checkIfNegative(vars):
    for i in vars:
        if i <= 0:
            return True
    return False

def AreaOfTriangle(vars):
    a = b = c = AngleA = AngleB = AngleC = AHeight = BHeight = CHeight = None
    for i in vars:
        if i and i <= 0:
            i = None
    a, b, c, AngleA, AngleB, AngleC, AHeight, BHeight, CHeight = vars

    # If there are vars for heron method
    if a and b and c:
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    # If there are vars for base and height method
    elif a and AHeight:
        return a * AHeight / 2

    elif b and BHeight:
        return b * BHeight / 2

    elif c and CHeight:
        return c * CHeight / 2

    # If there are vars for sin method
    elif AngleA and b and c:
        return b * c * math.sin(math.radians(AngleA)) / 2

    elif AngleB and a and c:
        return a * c * math.sin(math.radians(AngleB)) / 2

    elif AngleC and b and a:
        return b * a * math.sin(math.radians(AngleC)) / 2

    # Else return message
    else:
        return "Please Enter the needed fields"


def PerimeterOfTriangle(vars):
    if checkIfNegative(vars):
        return "Please Enter the needed fields"
    a, b, c = vars
    return a + b + c


def VolumeOfTriangularPrism(vars):
    if checkIfNegative(vars):
        return "Please Enter the needed fields"
    a, b, c, h = vars
    return (1/4) * h * math.sqrt(-1 * a ** 2 + 2 * (a * b) ** 2 + 2 * (a * c) ** 2 - b ** 4 + 2 * (b * c) ** 2 - c ** 4)


def AreaOfSquare(vars):
    if checkIfNegative(vars):
        return "Please Enter the needed fields"
    a = vars[0]
    return a ** 2


def PerimeterOfSquare(vars):
    if checkIfNegative(vars):
        return "Please Enter the needed fields"
    a = vars[0]
    return 4 * a


def VolumeOfCube(vars):
    if checkIfNegative(vars):
        return "Please Enter the needed fields"
    a = vars[0]
    return a ** 3


def AreaOfRect(vars):
    if checkIfNegative(vars):
        return "Please Enter the needed fields"
    a, b = vars
    return a * b


def PerimeterOfRect(vars):
    if checkIfNegative(vars):
        return "Please Enter the needed fields"
    a, b = vars
    return 2 * (a + b)


def VolumeOfRectCube(vars):
    if checkIfNegative(vars):
        return "Please Enter the needed fields"
    a, b, c = vars
    return a * b * c


def AreaOfCircle(vars):
    if checkIfNegative(vars):
        return "Please Enter the needed fields"
    r = vars[0]
    return math.pi * r ** 2


def CircumferenceOfCircle(vars):
    if checkIfNegative(vars):
        return "Please Enter the needed fields"
    r = vars[0]
    return 2 * math.pi * r


def VolumeOfSphere(vars):
    if checkIfNegative(vars):
        return "Please Enter the needed fields"
    r = vars[0]
    return (4 / 3) * math.pi * r ** 3