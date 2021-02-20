""" In this program, we are going to create a python command
 line program to play rock,paper, scissors with the users 
 input. If the user wins, the user can give a fun task 
 to computer based on the list of tasks available
 if the computer wins a random tasks from the list will
 will be given to the user. Funzzz expected ! 
 Also note : This program is coded and executed from 
 a mobile phone. """

import random

def rps():
  ans = input (" Cmon lets play ! Rock, paper, Scissors, U can enter either 'r' or 'p' or 's': ") 
  if ans.lower() == 'r':
    return 'Rock'
  elif ans.lower() == 'p':
    return 'Paper'
  else:
    return 'Scissors'
 
 
def comp_rps():
  lst = ['Rock', 'Paper', 'Scissors']
  return random.choice(lst)
  
  
def fun_rps(task_usr, task_comp, comp, usr):
    if comp == usr:
        return 'The game ties'
    elif (comp == 'Rock' and usr == 'Paper'):
        task = random.choice(task_comp)
        return ('User wins and the task for computer is ', task)
    elif (comp == 'Rock' and usr == 'Scissors'):
        task = random.choice(task_usr)
        return ('Computer wins and the task for you is ', task)
    elif (comp == 'Paper' and usr == 'Scissors'):
        task = random.choice(task_comp)
        return ('User wins and the task for computer is ', task)
    elif (comp == 'Paper' and usr == 'Rock'):
        task = random.choice(task_usr)
        return ('Computer wins and the task for you is ', task)
    elif (comp == 'Scissors' and usr == 'Rock'):
        task = random.choice(task_comp)
        return ('User wins and the task for computer is ', task)
    elif (comp == 'Scissors' and usr == 'Paper'):
        task = random.choice(task_usr)
        return ('Computer wins and the task for you is ', task)





