#challenge 2.2
#define the base class player 
class player:
  def play(self):
    print("The player is playing cricket.")
    
#define the derived class batsman
class batsman(player):
  def play(self):
    print("The batsman is batting.")

#define the derived class bowler
class bowler(player):
  def play(self):
    print("The bowler is bowling.")
    
#create objects of batsman and bowler classes
batsman=batsman()
bowler=bowler()