import sys
from math import sqrt

def calculateDistance(p1x, p2x, p1y, p2y):
	deltaX = p1x - p2x
	deltaY = p1y - p2y
	return sqrt((deltaX * deltaX) + (deltaY * deltaY))

def calculateForce(p1mass, p2mass, distance):
	return (p1mass * p2mass) / distance**2

particle1 = [float(x) for x in raw_input("Please enter the first particle's information (m,x,y): ").split(" ")]
particle2 = [float(x) for x in raw_input("Please enter the second particle's information (m,x,y): ").split(" ")]

distance = calculateDistance(particle1[1], particle2[1], particle1[2], particle2[2])

print "Repulsion-force: " + str(calculateForce(particle1[0],particle2[0],distance))
