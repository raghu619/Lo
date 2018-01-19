import logging
# create and configure logger
LOG_FORMAT="%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="/home/raghvendra/Desktop/LumberJack.Log",level=logging.DEBUG,format=LOG_FORMAT,filemode='w')
logger=logging.getLogger()
#Test the logger

'''logger.debug("This is a harmless debug message")
logger.info("Just some useful info")
logger.warning("im sorry,but i can't do that ,Dave")
logger.error("Did you just try to divide by zero?")
logger.critical("There is no internet connection")
print(logger.level)'''
import math
def quadratic_formula(a,b,c):
    """Return the solution to the equation ax^2+bx+c=0."""
    logger.info("quadratic_formula({0},{1},{2})".format(a,b,c))

    #Compute the discriminant
    logger.debug("Compute the discriminant")
    disc=b**2-4*a*c
    #compute the two roots
    logger.debug("compute the two roots")
    root1=(-b+math.sqrt(disc))/(2*a)
    root2= (-b-math.sqrt(disc))/(2*a)

    #Return the roots
    logger.debug('Return the roots')
    return (root1,root2)


roots=quadratic_formula(1,3,1)
print(roots)