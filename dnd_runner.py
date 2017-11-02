#!/bin/env python
　
import random
import itertools
from collections import OrderedDict
　
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
    return (self.total_score() <= 73 or
            self.best_score()  <= 14 or
            self.worst_score() <= 5  or
            self.scores()[2]   <= 9
           )
    
  def is_overpowered(self):
    return (self.total_score() >= 78 or
            self.worst_score() >  11 or
            self.best_score()  == 18 or
            self.scores()[3]   >= 15
           )
    
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
　
　
def regular_characters(num_chars=3):
  #num_chars = 3
  my_abs = ["int", "con", "dex", "wis", "cha", "str"]
  ok_chars = random_average_characters(num_chars, my_abs)
  if(num_chars >=2):
    while some_char_is_strictly_better_than_another(ok_chars):
      ok_chars = random_average_characters(num_chars, my_abs)
　
  return ok_chars
　
def stats_of_some_sample_chars(ok_chars):
  stats_scores = [0]*len(ok_chars[0].scores())
　
　
  for i, _ in enumerate(ok_chars[0].scores()):
    stats_scores[i] = {}#OrderedDict({3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0})
    for c in ok_chars:
      try:
        stats_scores[i][c.scores()[i]] += 1
      except (KeyError):
        stats_scores[i][c.scores()[i]] = 1
　
  for i, ith_worst in enumerate(stats_scores):
    print(str(6-i) + ":")
    thing = OrderedDict(sorted(ith_worst.items(), key=lambda t: t[0]))
    for k in thing.keys():
      print(str(k)+": " + str(thing[k]))
    print()
    print()
　
def print_regular_chars(ok_chars):
  for i, c in enumerate(ok_chars):
    print("Character ", i+1)
    print("Total score: ", c.total_score())
    print("Underpowered? ", c.is_underpowered())
    print("Overpowered? ", c.is_overpowered())
    c.print_abilities()
    print()
　
if __name__ == "__main__":
  #chars = regular_characters(1)
  stats_of_some_sample_chars(random_average_characters(1000))
  #stats_of_some_sample_chars(regular_characters(10))
  #stats_of_some_sample_chars(1000)
