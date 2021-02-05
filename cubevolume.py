def cubeVolume(sideLength):
    if(isinstance(sideLength, complex)):
        raise Exception("cubeVolume expected a non-complex number")
    if(not isinstance(sideLength, (int, float))):
        raise Exception("cubeVolume expected a number")
    if(float(sideLength) < 0):
        raise Exception("cubeVolume expected a positive input")
    return sideLength*sideLength*sideLength