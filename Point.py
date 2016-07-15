class Point:
## Krutarth Rao
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.cords = (x,y)
        
    def show(self):
        print(self.cords)
        
    def move(self, x_inc, y_inc):
        new_x = self.cords[0] + x_inc
        new_y = self.cords[1] + y_inc
        new_cords = (new_x, new_y)
        self.cords = new_cords
        
    def distance(self, Point):
        a = Point.x - self.x
        b = Point.y - self.y
        sum_ab = (a**2) + (b**2)
        distance = sum_ab**0.5
        print("%.1f" % distance)

    def halfway(self, Point):
        sumx = self.x + Point.x
        sumy = self.y + Point.y
        mid_x = sumx / 2.0
        mid_y = sumy / 2.0
        half_point = (mid_x, mid_y)
        return half_point

def main():
    p1 =Point(-1,2)
    p2 = Point (3,-6)
    
    p1.distance(p2)
    
    mm = p1.halfway(p2)
    
    mid_p = Point(mm[0],mm[1])
    mid_p.show()

main()





        
