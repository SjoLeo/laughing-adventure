import random as rand

class Player():
    def __init__(self, lifes):
      self.lifes = lifes
      self.score = 0
      self.hit_him = False
      self.got_hit = False

    def inc_score(self):
        self.score += 1

    def red_lifes(self):
        self.lifes -= 1

    def fire(self):
        #träffar
        if rand.randint(1,3) == 1:
            self.hit_him = True
            self.inc_score()
        else:
            self.hit_him = False
        #blir träffad
        if rand.randint(1,4) == 2:
            self.got_hit = True
            self.red_lifes()
            
        else:
            self.got_hit = False
        
    
a_player = Player(3)

while True:
    input('Tryck Enter för att skjuta\n')
    a_player.fire()
    if a_player.hit_him:
       print('Du träffade han!\n')
       print(f'ditt score: {a_player.score}\n')
    else:
       print('Du missade han \n')

    if a_player.got_hit:
        print('AAAAAAAAAAAAAAh \n')
        print(f'du har {a_player.lifes} liv kvar \n')
        if a_player.lifes == 0:
            print(f'ditt score blev: {a_player.score} \n')
            break
        
    else:
        print('du klarade dig denna gång\n')
        

    
