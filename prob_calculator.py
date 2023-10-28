import copy
import random
# Consider using the modules imported above.

class Hat:


  def __init__(self, **kwargs):
    self.contents = []
    self.contents = dict_to_list(kwargs)

  def draw(self, balls_to_draw):
    drawn_balls = []
    if balls_to_draw > len(self.contents):
      return self.contents
    else:
      #drawn_balls = random.sample(self.contents, balls_to_draw)
      for i in range(balls_to_draw):
        ball_choice = random.choice(self.contents)
        drawn_balls.append(ball_choice)
        self.contents.remove(ball_choice)
      return drawn_balls
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  successful_experiments_M = 0
  
  for i in range(num_experiments):
    hat1 = copy.deepcopy(hat)
    draw_list = hat1.draw(num_balls_drawn)
    temp_expected_balls = dict_to_list(expected_balls)
    
    for ball in draw_list:
      if ball in temp_expected_balls:
        temp_expected_balls.remove(ball)
      else:
        continue
      if len(temp_expected_balls) == 0:
        successful_experiments_M += 1
        break

  return successful_experiments_M/num_experiments


def dict_to_list(dict):
  mylist = []
  for color, number in dict.items():
    i = 1
    while(i <= int(number)):
      mylist.append(color)
      i += 1
  return mylist