#1, 2, 3

class Shape():

  def what_am_i(self):
    print('I am a shape')

class Rectangle(Shape):
  
  def __init__(self, w, l):
    self.width = w
    self.len = l

  def calculate_perimeter(self):
    return (self.width+self.len)*2

class Square(Shape):

  def __init__(self, s1):
    self.s1 = s1

  def calculate_perimeter(self):
    return self.s1*4

  def change_size(self, s2):
    self.s1 += s2


rectangle=Rectangle(5,6)
print(rectangle.calculate_perimeter())

square=Square(17)
print(square.calculate_perimeter())

square.change_size(-2)
print(square.calculate_perimeter())

square.what_am_i()


#4
class Player:

  def __init__(self, name, number, team):
    self.name = name
    self.number = number
    self.team = team

class Team:

  def __init__(self, name):
    self.name = name

bardral = Team('Bardral Urayasu')
marines = Team('Chiba Lotte Marines')

ryuma = Player('Ryuma Kato', 10, bardral)
takumi = Player('Takumi Nagasaka', 7, bardral)
shogo = Player('Shogo Nakamura', 8, marines)
fumio = Player('Fumio Nishimura', 11, 'Chiba Jets Funabashi')
koki = Player('Koki Yonekura', 11, 'JEF United Ichihara Chiba')

print(bardral.name)
print(ryuma.name)
print(takumi.team)
print(ryuma.number*takumi.number)
print(shogo.number)
print(shogo.team.name)
print(fumio.team)
print(koki.team.name)
