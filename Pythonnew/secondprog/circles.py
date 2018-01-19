from  math import pi
def circle_area(r):
    if(type(r) not in [int,float]):
        raise TypeError
    return pi*(r**2)
#Test Functicircle with r={} is {}"


