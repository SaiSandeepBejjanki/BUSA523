#!/usr/bin/env python
# coding: utf-8

# Question1: Write a program for flipping a coin 10,000 times and store the results in a list.
# After which, identify the number of streaks. (streak - a series of 5 or more
# heads or tails)

# In[12]:


import random

flip = {
    'heads': 0,
    'tails': 0,
}

dicToList = list(flip.keys())

listOfCoins = [random.choice(dicToList) for toss in range(10000)]
print(listOfCoins)

headStreak = 0
totalHS = 0

for i in listOfCoins:
    if i == 'heads':
        headStreak += 1
        if headStreak >= 5:
            totalHS += 1
    else:
        headStreak = 0
print('Total HS : ', totalHS)
tailStreak = 0
totalTS = 0
for j in listOfCoins:
    if j == 'tails':
        tailStreak += 1
        if tailStreak >= 5:
            totalTS += 1
    else:
        tailStreak = 0
print('Total TS : ', totalTS)


# Question2: Write a program to take user inputs (number of swords, diamonds, gold coins,
# ropes and potions) for a video game and store them in a dictionary. After
# which print the following output.
# Inventory:
# 5 swords
# 10 diamonds
# 6 gold coins
# 3 rope
# 2 potions

# In[2]:


n = 5
dict_items = dict()
for i in range(n):
    data = input('Enter key & value ')
    temp = data.split(':')
    dict_items[temp[0]] = int(temp[1])
rev_di = {value : key for (key, value) in dict_items.items()}
print("Inventory:")
for d in rev_di:
    print(d, rev_di[d])


# Question3: Repeat question 1 using arrays.

# In[3]:


import random
import itertools

import numpy as np

flip = {
    'heads': 0,
    'tails': 0,
}

dicToList = list(flip.keys())

listOfCoins = [random.choice(dicToList) for toss in range(10000)]
print(listOfCoins)

arrayOfCoins = np.asarray(listOfCoins)

headStreak = 0
totalHS = 0

for i in arrayOfCoins:
    if i == 'heads':
        headStreak += 1
        if headStreak >= 5:
            totalHS += 1
    else:
        headStreak = 0
print('Total HS : ', totalHS)
tailStreak = 0
totalTS = 0
for j in arrayOfCoins:
    if j == 'tails':
        tailStreak += 1
        if tailStreak >= 5:
            totalTS += 1
    else:
        tailStreak = 0
print('Total TS : ', totalTS)


# Question4: Create a game with the following instructions: 
# a. There are 3 players and 10 iterations.
# b. In each iteration, every player rolls a die.
# c. The winner of the game is the one who has the highest score when rolls
# from all the iterations are added.

# In[11]:


import random


def roll():
    return random.choice([1, 2, 3, 4, 5, 6])


class player(object):
    def __init__(self, name):
        self.name = name

    def score(self, score):
        self.score = score

    def getscore(self):
        return self.score

    def __str__(self):
        return 'NAME: ' + self.name + '\nSCORE: ' + str(self.score)


class game(object):
    def __init__(self, playr, trails):
        self.trails = trails
        self.playr = playr

    def gaming(self):
        throw = 0
        score = 0
        for i in range(self.trails):
            throw = roll()
            if throw >= 6:
                throw = throw + roll()
            score = throw + score
        return score

    def __str__(self):
        return self.playr.getname() + str(self.score)


tri = 10

p1Name = player('player1')
p2Name = player('player2')
p3Name = player('player3')

print("-----------LETS PLAY THIS GAME--------------\n")

player_1 = game(p1Name, tri)
player_2 = game(p2Name, tri)
player_3 = game(p3Name, tri)

scr = []
scr.append(player_1.gaming())
scr.append(player_2.gaming())
scr.append(player_3.gaming())


pL1 = scr[0]
print("Player1 score is: ", pL1)
pL2 = scr[1]
print("Player2 score is: ", pL2)
pL3 = scr[2]
print("Player3 score is: ", pL3)

if pL1 > pL2 and pL1 > pL3:
    print("Player1 wins and his score is:", pL1)
elif pL2 > pL1 and pL2 > pL3:
    print("Player2 wins and his score is:", pL2)
elif pL3 > pL1 and pL3 > pL2:
    print("Player3 wins and his score is:", pL3)
elif pL1 == pL2 == pL3:
    print("Draw")
elif pL1 == pL2:
    print("P1,P2 wins")
elif pL2 == pL3:
    print("P2,P3 wins")
else:
    print("P1,P3 wins")


# In[ ]:




