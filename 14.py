#1, 2
class Square:

  square_list = []

  def __init__(self, s):
    self.s = s
    self.square_list.append(self.s)

  def __repr__(self):
    return '{} by {} by {} by {}'.format(self.s, self.s, self.s, self.s)

s1 = Square(4)
s2 = Square(8)

print(Square.square_list)
print(s1)

#3
class Player:

  def __init__(self):
    self.name = 'Garrincha'
    
gari = Player()
same_gari = gari
print(gari is same_gari)

another_gari = Player()
print(gari is another_gari)
