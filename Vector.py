import numpy
import  math
from decimal import Decimal,getcontext

getcontext().prec=3

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(map(lambda x:Decimal(x) , coordinates))
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
    def plus(self, other):
      new_coordinates=[x+y for x,y in zip(self.coordinates,other.coordinates)]
      return Vector(new_coordinates)
    def minus(self,v):
        new_coordinates=[x-y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self,c):
        new_coordinates=[c*x for x in self.coordinates]
        return  Vector(new_coordinates)

    def magnitude(self):
        values=[x**2 for x in self.coordinates]
        return math.sqrt(sum(values))

    def normalized(self):
        try:
            magnitude=self.magnitude()
            return self.times_scalar(Decimal(1.0/magnitude))
        except ZeroDivisionError:
            raise Exception("Cannot normalize the zero vector")
    def dot(self,other):
        value=[x*y for x,y in zip(self.coordinates,other.coordinates)]
        return sum(value)
    def angle_with(self,other,in_degrees=False):
        try:
          #dotproductvalue=self.dotproduct(other)
          #mag1=self.magnitude()
          #mag2=other.magnitude()
          #return math.acos(dotproductvalue/(mag1*mag2))
          u1=self.normalized()
          u2=other.normalized()
          angle_in_radians=math.acos(u1.dot(u2))
          if in_degrees:
              degrees_per_radian=180/math.pi
              return angle_in_radians*degrees_per_radian
          else :
              return angle_in_radians
        except Exception as e:
            if str(e)==self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')

            else:
                raise e


    def is_orthogonal_to(self,v,tolerance=1e-10):
        return abs(self.dot(v))<tolerance


    def is_parallel(self,other):
        return (self.is_zero() or other.is_zero()
                    or self.angle_with(other)==0 or self.angle_with(other)==math.pi)

    def is_zero(self,tolerance):
         return self.magnitude()<tolerance

    def projection_parallel_component(self,other):
        normalizedvector=other.normalized()
        parallelvec=normalizedvector.times_scalar(self.dot(normalizedvector))
        return parallelvec

    def projection_orthgonal_component(self,other):
        parallel_comp=self.projection_parallel_component(other)
        return self.minus(parallel_comp)
    def Cal_projection_compoenent_result(self,other):
        orthogonal_comp=self.projection_orthgonal_component(other)
        parallel_comp=self.projection_parallel_component(other)

        return orthogonal_comp.plus(parallel_comp)
my_vector=Vector([3.009,-6.172,3.692,-2.51])
print(my_vector)
my_vector1=Vector([6.404,-9.144,2.759,8.718])

print(my_vector==my_vector1)
print(Vector.plus(my_vector,my_vector1))
print(Vector.magnitude(my_vector))
print(my_vector.normalized())
print(abs(my_vector.dot(my_vector1)))

print("{0:.4f}".format(my_vector.angle_with(my_vector1)))

print(my_vector.projection_parallel_component(my_vector1))
print(my_vector.projection_orthgonal_component(my_vector1))
print(my_vector.Cal_projection_compoenent_result(my_vector1))