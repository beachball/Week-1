import math
class Polygon:

        def __init__(self):
            self.listofpoints = []
            self.get_distance = []
            self.distances = []
            self.areapoints = []

        def addPoint(self, x, y):
            self.listofpoints.append([x,y])


        def distancecalc(self, x, y):
            i = 0
            distances = []
            perimeter = 0
            for i in range(len(self.listofpoints)-1):
                point = self.listofpoints[i]
                next_point = self.listofpoints[i+1]
                x0 = point[0]
                y0 = point[1]
                x1 = next_point[1]
                y1 = next_point[1]

                point_distancex = math.sqrt((x1 - x0)**2)
                point_distancey = math.sqrt((y1 - y0)**2)
                point_distance = point_distancex + point_distancey
                distances.append(point_distance)
            for distance in distances:
                perimeter = perimeter + distance
            perimeter = str(perimeter)
            print("")
            print("")
            print("The perimeter is! " + perimeter)


        def area(self, x, y):
            i = 0
            for i in range(len(self.listofpoints)-1):
                pointa = self.listofpoints[i]
                next_pointa = self.listofpoints[i+1]
                x0 = pointa[0]
                y0 = pointa[1]
                x1 = next_pointa[0]
                y1 = next_pointa[1]

                bridge = (x0 * y1 - y0 * x1)
                area = bridge/2
                area = str(abs(area))
                print("")
                print("")
                print("The area is! " + area)

polygon = Polygon()

polygon.addPoint(1,1)
print(polygon.listofpoints)

polygon.addPoint(2,3)
print(polygon.listofpoints)

polygon.addPoint(3,4)
print(polygon.listofpoints)

polygon.distancecalc(0,0)

polygon.area(0,0)
