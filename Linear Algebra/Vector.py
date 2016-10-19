import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    
    def plus(self, vec2):
        returnVec = []
        i = 0
        for x in self.coordinates:
            
            returnVec.append(self.coordinates[i] + vec2.coordinates[i])
            i += 1
        return returnVec
    def minus(self, vec2):
        returnVec = []
        i = 0
        for x in self.coordinates:
            
            returnVec.append(self.coordinates[i] - vec2.coordinates[i])
            i += 1
        return returnVec
    def scalarMultiply(self, scale):
        returnVec = []
        i = 0
        for x in self.coordinates:
            returnVec.append(self.coordinates[i]*scale)
            i += 1
        return returnVec        
    def magnitude(self):
        squaredSubtotal = 0
        for x in self.coordinates:
            squaredSubtotal += (x * x)
        magnitude = math.sqrt(squaredSubtotal)
        return magnitude
    def normalize(self):
        magnitude = self.magnitude()
        scale = 1/magnitude
        return self.scalarMultiply(scale)
    
vec1 = Vector((-0.221,7.437))
vec2 = Vector((8.813, -1.331, -6.247))
vec3 = Vector((5.581, -2.136))
vec4 = Vector((1.996, 3.108, -4.554))
print(vec1.magnitude())
print(vec2.magnitude())
print(vec3.normalize())
print(vec4.normalize())
