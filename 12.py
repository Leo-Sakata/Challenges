#1
class Apple:
  def __init__(self, s, w, c, p):
    self.size=s
    self.weight=w
    self.color=c
    self.place=p

apple=Apple(6.5, 450, 'Red', 'Aomori')
print(apple.size)
print(apple.weight)
print(apple.color)
print(apple.place)

#2
import math

class Circle:
  def __init__(self, r):
    self.area=r*r*math.pi

cir=Circle(7)
print(cir.area)

#3
class Triangle:
  def __init__(self, w, h):
    self.area=w*h/2

triangle=Triangle(4,8)
print(triangle.area)

#4
class Hexagon:
  def __init__(self, a, b, c, d, e, f):
    self.calculate_perimeter=a+b+c+d+e+f

hexagon=Hexagon(3,5,2,6,4,3)
print(hexagon.calculate_perimeter)
