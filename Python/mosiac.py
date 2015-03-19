# import the necessary packages
import numpy as np
import argparse
import cv2
import random
import math
#import voronoi
import PIL
import scipy.spatial
import pygame

class Tile:
    points = np.array([])
    color = ()
    def __init__(self, points, color):
        self.points = points
        self.color = color
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

# load the image, clone it for output
image = cv2.imread(args["image"])
output = image.copy()

numCandidates = 10;
numPoints = 2000;
height = len(image)
width = len(image[0])
samples = []

def sample() :
	bestDistance = 0
	for i in range(0,numCandidates):
		c = [random.random() * width, random.random() * height]
		d = euclidDistance(findClosest(samples, c), c)
		if d > bestDistance:
			bestDistance = d;
			bestCandidate = c;
	return bestCandidate;
	
def findClosest(samples, point):
	distance = 100000000000
	returnPoint = [0,0]
	for i in range(0,len(samples)-1):
		tempDist = euclidDistance(point, samples[i])
		if tempDist < distance:
			distance = tempDist
			returnPoint = samples[i]
			
	return returnPoint	

def euclidDistance(a, b):
	dx = a[0] - b[0]
	dy = a[1] - b[1]
	return math.sqrt(dx * dx + dy * dy)
	
#draw = ImageDraw.Draw(output)
#draw.line((0, 0) + im.size, fill=128)
#draw.line((0, im.size[1], im.size[0], 0), fill=128)
#del draw

#output.save(sys.stdout, "PNG")
for i in range(0,numPoints):
	ret = sample()
	samples.append(ret)

for item in samples:
	cv2.circle(output, (int(item[0]),int(item[1])), 1, (255, 0, 0), 5)
	
vor = scipy.spatial.Voronoi(samples)

f = open('output.txt','w')
f.write(str(dir(vor)))
f.write('\n\n')
f.write(str(vor.regions))
f.write('\n\n')
f.write(str(vor.vertices))
f.write('\n\n')
f.write(str(vor.points))
f.write('\n\n')
f.write(str(vor.point_region))
f.close()

for item in vor.vertices:
	cv2.circle(output, (int(item[0]), int(item[1])), 1, (0,0,255),5)
	
allRegions = []
print(len(vor.regions))
print(len(vor.points))
print(len(image))
print(len(image[0]))
#firstPoints = np.append(firstPoints, vor.regions[2])
#for item in vor.regions:
#    if item[0] == 38:
#        np.append(firstPoints, [vor.vertices[item[1]], vor.vertices[item[0]]])
for indx, region in enumerate(vor.regions):
    print(indx)
    regionPoints = []
    interior = True
    if indx == numPoints:
        continue 
    for item in vor.regions[indx]:
        regionPoints.append(vor.vertices[item])
        if item == -1:
            interior = False
    if interior:
        x_pos = vor.points[indx][0]; y_pos = vor.points[indx][1]
        print(x_pos);print(y_pos)
        blue = int(image[y_pos, x_pos][0])
        green = int(image[y_pos, x_pos][1])
        red = int(image[y_pos, x_pos][2])
        allRegions.append((regionPoints, (blue,green,red)))

tiles = []
for points in allRegions:
    tiles.append(Tile(np.array(points[0]),points[1]))
    print("Added: "+str(points))


blue = int(image[vor.points[2][0], vor.points[2][1]][0])
green = int(image[vor.points[2][0], vor.points[2][1]][1])
red = int(image[vor.points[2][0], vor.points[2][1]][2])
print("blue: "+str(blue)+" -- green: "+str(green)+" -- red: "+str(red))
for tile in tiles:
    if tile.points.size <> 0:
        cv2.fillPoly(output, [tile.points.astype('int32')], tile.color)

cv2.imshow("output", output)##np.hstack([image, output]))
cv2.waitKey(0)