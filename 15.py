from random import shuffle 

class Card:

  suits = ['spades', 'hearts', 'diamonds', 'clubes']
  values = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

  def __init__(self, v, s):
    self.value = v
    self.suit = s

  def __lt__(self, c2):
    if self.value < c2.value:
      return True

    if self.value == c2.value:
      if self.suit < c2.suit:
        return True
      else:
        return False

    return False

  def __gt__(self, c2):
    if self.value > c2.value:
      return True

    if self.value == c2.value:
      if self.suit > c2.suit:
        return True
      else:
        return False

    return False

  def __repr__(self):
    v = self.values[self.value] +' of ' + self.suits[self.suit]
    return v

class Deck:
  def __init__(self):
    self.cards = []
    for s in range(2,15):
      for t in range(0,3):
        self.cards.append(Card(s,t))
    shuffle(self.cards)

  def rm_card(self):
    if len(self.cards) == 0:
      return
    return self.cards.pop()

class Player:
  def __init__(self, name):
    self.wins = 0
    self.card = None
    self.name = name

class Game:
  def __init__(self):
    name1 = input('プレイヤー1の名前：')
    name2 = input('プレイヤー2の名前：')
    self.deck = Deck()
    self.p1 = Player(name1)
    self.p2 = Player(name2)

  def wins(self, winner):
    w ='このラウンドは{}が勝ちました'.format(winner)
    print(w)

  def draw(self, p1n, p1c, p2n, p2c):
    d = "{}は{}、{}は{}を引きました".format(p1n, p1c, p2n, p2c)
    print(d)

  def winner(self, player1, player2):
    s = '{}の勝利！'
    if player1.wins > player2.wins:
      return s.format(player1.name)
    if player1.wins < player2.wins:
      return s.format(player2.name)
    return '引き分け！'

  def play_game(self):
    cards = self.deck.cards
    print('戦争を始めます！')
    
    while len(cards) >= 2 :

      response = input('任意のキーを入力(qで終了）')
      if response == 'q':
        break

      p1n = self.p1.name
      p1c = self.deck.rm_card()
      p2n = self.p2.name
      p2c = self.deck.rm_card()
      self.draw(p1n, p1c, p2n, p2c)
      
      if p1c > p2c:
        self.p1.wins += 1
        self.wins(self.p1.name)
      else:
        self.p2.wins +=1
        self.wins(self.p2.name)

    win = self.winner(self.p1, self.p2)
    print('ゲーム終了！{}'.format(win))

game = Game()
game.play_game()
