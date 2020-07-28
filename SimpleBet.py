# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:19:03 2020

@author: Farzaneh
Imagine that you want to bet! Here you can play with this code to know if you
will lose or win
"""

from statistics import mean 
import random
def Roll_Dice():
    """choose a random number between 0 and 100
    if 100 > number >= 50 you win 
    the function returns True for the win and 
    False for the loss"""
    Dice = random.randint(0,100)#a random number between 0,100
    if Dice == 100 or Dice < 50:#if Dice is 100 or less than 50 you lost
        return False
    elif Dice >= 50:#if dice is greater than 50 you won (not 100)
        return True

def WinLose(Bank, win, lose,Games_number ):
    """Based on the money(Bank), number of loss and win (lose, win are 
    the amount you will lose or win each time and number of games
    this function returns the total money at the end"""
    Whole_money = Bank
    Game_number = Games_number
    #the game finishes if there is no money
    while Game_number > 0 and Whole_money > 0:
        #the game finishes if there is no money o
        if Roll_Dice():
            Whole_money += win
        else:
            Whole_money -= lose
        Game_number -= 1
    return Whole_money

people = 1000
list = []
for i in range (0,people):#What if 100 people play the same game
    list.append(WinLose(1000, 20, 20,500 ))
#print(list)   
print(mean(list))