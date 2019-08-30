import cv2
import numpy as np
from math import fabs;
import math
img= cv2.imread('h3.jpeg')
img = cv2.resize(img, (500, 224))
cv2.imwrite('resized.jpg', img)
cv2.imshow("objects Found", img)
cv2.waitKey(0)
canny_img = cv2.Canny(img, 60, 100)

height, width = canny_img.shape[:4]

#print(height,width)
edges = []

for j in range(width):
    for i in range(height):
        if canny_img[i][j] == 255:
            edges.append((j,i))
            a1=i
            b1=j
            break
    if len(edges) > 0:
        break

for j in range(width-1,-1,-1):
    for i in range(height):
        if canny_img[i][j] == 255:
            edges.append((j,i))
            a2=i
            b2=j
            break
    if len(edges) >1:
            break
#print(height,width)
for k in range(height):
    for l in range(width):
        if canny_img[k][l] == 255:
            edges.append((l,k))
            a3=k
            b3=l
            print(k,l)
            break
    if len(edges) > 2:
        break
for k in range(height-1,-1,-1):
    for l in range(width):
        if canny_img[k][l] == 255:
            edges.append((l,k))
            a4=k
            b4=l
            break
    if len(edges) >3:
            break


minHeight = 9999
minHeightPoints = []

for j in range(width):
    gotStating = False
    start = ()
    end = ()
    for i in range(height):
        if not gotStating and canny_img[i][j] == 255 and i < height/2:
            start = (j, i)
            gotStating = True
        elif gotStating and canny_img[i][j] == 255 and i > height / 2 :
                end = (j,i)
    if(gotStating and len(end) is 2 and len(start) is 2):
        if end[-1] - start[-1] <  minHeight and j > width /2:
            minHeightPoints = [start, end]
            minHeight = end[-1] - start[-1]
        #print(start, end, "Height: ", end[-1] - start[-1])


cv2.circle(canny_img, minHeightPoints[0], 2, 100, thickness=2)
cv2.circle(canny_img, minHeightPoints[-1], 2, 100, thickness=2)

print(minHeightPoints[0], minHeightPoints[-1])
print('Before Tail height:')
g=(minHeightPoints[-1][1]-minHeightPoints[0][1])
print(g)
#print("lenght of Btail" ,((minHeightPoints[-1][0])-(minHeightPoints[0][-1]))*0.5)


areaOfTail = 0
for j in range(width):
    for i in range(height - 1, 0, -1):
        if j > minHeightPoints[0][0] and canny_img[i][j] == 255:
            areaOfTail += 1

print("Area of Tail = ", areaOfTail , "px")

#print(edges)
cv2.circle(canny_img,edges[0],2,100,thickness=10)
cv2.circle(canny_img,edges[1],2,100,thickness=10)
cv2.circle(canny_img,edges[2],2,100,thickness=10)
cv2.circle(canny_img,edges[3],2,100,thickness=10)


'''print("lenght of fish" ,edges[1][0] - edges[0][0])
print("lenght of fish sqrt: " ,(edges[1][0] - edges[0][0])**.5)'''
'print("Width of fish" ,edges[3][2] - edges[0][0])'
'dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)'
m=(((a2-a1)**2+(b2-b1)**2)**.5)
l=(((a4-a3)**2+(b4-b3)**2)**.5)
print("Length of fish: ",m)
print("Width of fish: ",l)
rt=(m/l)
print("Ratio of Hight and Width are: ",rt)
cv2.imshow("corners",canny_img)



#Data Store

a=float(format(m, '.3f'))
b=float(format(l, '.3f'))
c=float(format(rt, '.3f'))
d=float(format(g, '.3f'))
e=float(format(areaOfTail, '.3f'))

#mimg=[areaOfTail,m,l,rt]
#mimg = [1887,495.524,230.106,2.153]
mimg=[a,b,c,d,e]
print(mimg)
b1=[482.813, 186.968, 2.582, 4.0, 2.0]
b2=[492.26, 185.13, 2.659, 57.0, 50.0]
b3=[483.414, 212.009, 2.28, 30.0, 22.0]
h1=[474.081, 205.429, 2.308, 50.0, 2390.0]
h2=[495.525, 230.106, 2.153, 45.0, 1887.0]
h3=[499.985, 214.009, 2.336, 42.0, 2328.0]
h4=[425.978, 156.013, 2.73, 32.0, 1166.0]
h5=[464.389, 204.846, 2.267, 46.0, 1477.0]
k1=[492.915, 178.474, 2.762, 58.0, 738.0]
k2=[494.972, 179.234, 2.762, 69.0, 1037.0]
k3=[438.858, 160.854, 2.728, 67.0, 1456.0]
k4=[435.362, 164.685, 2.644, 69.0, 1445.0]
p1=[477.074, 205.448, 2.322, 27.0, 691.0]
p2=[417.634, 201.435, 2.073, 30.0, 952.0]
p3=[418.466, 197.041, 2.124, 30.0, 1420.0]
p4=[409.708, 188.282, 2.176, 34.0, 815.0]
r1=[469.54, 203.354, 2.309, 49.0, 2192.0]
r2=[467.547, 153.688, 3.042, 53.0, 2007.0]
r3=[491.015, 170.988, 2.872, 53.0, 3149.0]
#img=[50,492.260,185.129,2.659]
if mimg==b1 or mimg==b2 or mimg==b3:
    print("bhetki-barramundi")
elif mimg==h1 or mimg==h2 or mimg==h3 or mimg==h4 or mimg==h5:
    print("Hilsa – Ilish Shad")
elif mimg==k1 or mimg==k2 or mimg==k3 or mimg==k4:
    print("Catla – Indian Carp")
elif mimg==p1 or mimg==p2 or mimg==p3 or mimg==p4:
    print("Pomfret - Bramidae")
elif mimg==r1 or mimg==r2 or mimg==r3:
    print("Rohu – Labeo Rohita")
else:
    print("unknown")

cv2.waitKey(0)
cv2.destroyAllWindows()


