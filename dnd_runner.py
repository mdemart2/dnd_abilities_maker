import random
import itertools

def roll(x=1, d=6):
  return sum([random.randint(1,d) for _ in range(x)])

class Character:
  ATTRIBUTES = ['int', 'con', 'dex', 'wis', 'cha', 'str']
  #['str', 'dex', 'con', 'int', 'wis', 'dex']
  
  def __init__(self, abilities):
    self.abilities = abilities
    
  def is_strictly_better_than(self, other_char):
    for a, b in zip(self.scores(), other_char.scores()):
      if a < b:
        return False
        
    print("Found some strictly better chars!!")
    print(self.scores())
    print(other_char.scores())
    return True
    
  def print_abilities(self):
    for a in self.abilities:
      print("%s: %s" % (a.name, str(a.score)))
      
  def total_score(self):
    return sum([a.score for a in self.abilities])
    
  def scores(self):
    return sorted([a.score for a in self.abilities])
    
  def best_score(self):
    return max([a.score for a in self.abilities])
    
  def worst_score(self):
    return min([a.score for a in self.abilities])
    
  def is_underpowered(self):
    return (self.total_score() <= 71 or self.best_score() < 16 or self.worst_score() < 6 or self.scores()[2] <=9)
    
  def is_overpowered(self):
    return (self.total_score() >= 76 or self.worst_score() > 11 or self.best_score() == 18 or self.scores()[3] >=15)
    
  @classmethod
  def re_roll(cls, names=None):
    if names is None:
      names = cls.ATTRIBUTES
    rolls = []
    for r in range(6):
      rolls.append(Ability.random_score())
    rolls.sort(reverse=True)
    abilities = []
    for n, r in zip(names, rolls):
      abilities.append(Ability(n, r))
    return cls(abilities)
    
class Ability:
  
  def __init__(self, name=None, score=None):
    if name is None:
      raise Exception("You must specify a name!")
    self.name = name
    if score is None:
      self.score = Ability.random_score()
    else:
      self.score = score
      
  @staticmethod
  def random_score():
    temp_scores = []
    for _ in range(4):
      temp_scores.append(roll())
    return sum(temp_scores) - min(temp_scores)
    
def random_average_characters(num_chars=3, desired_abilities = None):
  if desired_abilities is None:
    desired_abilities = ["str", "dex", "con", "wis", "cha", "int"]
  ok_chars = []
  while(len(ok_chars) < num_chars):
    x = Character.re_roll(desired_abilities)
    if not (x.is_underpowered() or x.is_overpowered()):
      ok_chars.append(x)
  ok_chars.sort(key=lambda c: -c.total_score())
  return ok_chars
  
def some_char_is_strictly_better_than_another(chars):
  for a, b in itertools.combinations(chars, 2):
    if a.is_strictly_better_than(b) or b.is_strictly_better_than(a):
      return True
  return False


def main():
  num_chars = 3
  my_abs = ["str", "cha", "con", "dex", "wis", "int"]
  ok_chars = random_average_characters(num_chars, my_abs)
  while some_char_is_strictly_better_than_another(ok_chars):
    ok_chars = random_average_characters(num_chars, my_abs)

  for i, c in enumerate(ok_chars):
    print("Character ", i+1)
    print("Total score: ", c.total_score())
    print("Underpowered? ", c.is_underpowered())
    print("Overpowered? ", c.is_overpowered())
    c.print_abilities()
    print()

if __name__ == "__main__":
  main()
