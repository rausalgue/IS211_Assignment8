#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week Eight - Pig Game with Computer"""

import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--player1", help="Player Type",default=None)
parser.add_argument("--player1Name", help="Name of the Player1",default=None)
parser.add_argument("--player2", help="Player Type",default=None)
parser.add_argument("--player2Name", help="Name of the Player2",default=None)
parser.add_argument("--timed", help="Boolean for Timed Game",default=None)
args = parser.parse_args()

upper_limit = 100

class Factory(object):
    def ConstructPlayer(self,type,name):
        if type == 'human':
            playerInstance = PlayerData(name)
        else:
            playerInstance = ComputerData(name)

        return playerInstance

class Dice(object):
    def __init__(self):
        self.value = None

    def roll(self):
        self.value = random.randint(1, 6)
        return self.value

class PlayerData(object):
    def __init__(self,name):
        self.name = name
        self.score = 0

    def makeDecision(self,score):
        answer = raw_input("Roll(r) or Hold(h): ")

        return answer

class ComputerData(PlayerData):
    def makeDecision(self,iteration_score):
        #print 'Computer Score',self.score
        #print 'Iteration Score',iteration_score

        if 100 - self.score > 25 and iteration_score < 25:
            answer = 'r'
        else:
            answer = 'h'

        return answer

class Game(object):
    def __init__(self, type1, name1, type2, name2):  # Assign method name
        self.player1_type = type1
        self.player1 = name1
        self.player2_type = type2
        self.player2 = name2

    def introducePlayers(self):
        factory = Factory()
        player1 = factory.ConstructPlayer(self.player1_type,self.player1)
        player2 = factory.ConstructPlayer(self.player2_type,self.player2)

        return player1,player2

    def rollDice(self,player):
        print '________',player.name,'________________ROLLING_______________________'
        print 'Player Data',player.name,'Current Score:',player.score

        gameDice = Dice()

        current_roll_value = 0
        temp_player_score = player.score

        while True:
            roll_value = gameDice.roll()
            current_roll_value = current_roll_value + roll_value

            if roll_value == 1:
                print 'Sorry',player.name,'you rolled a 1'
                temp_player_score = 0
                current_roll_value = 0
                player.score = player.score
                return
            else:
                temp_player_score = temp_player_score +  roll_value

                if temp_player_score >= upper_limit:
                    player.score = temp_player_score
                    print 'Congrats', player.name, 'you rolled:', roll_value
                    print 'Congrats', player.name, 'your score is', temp_player_score
                    break
                else:
                    print 'Congrats',player.name,'you rolled:',roll_value,'your temp score is',temp_player_score
                    print 'What would you like to do?'
                    answer = player.makeDecision(temp_player_score)
                    if answer == 'h':
                        player.score = temp_player_score
                        break
                    else:
                        continue
        return

def main():
    # Call the Game Class to begin Game
    print 'Welcome to Our Game'
    player_one_type = args.player1 if args.player1 else raw_input("Player Type (human/computer): ")

    player_one_name = args.player1Name if args.player1Name else raw_input("Player One Name: ")

    player_two_type = args.player2 if args.player2 else raw_input("Player Type (human/computer): ")

    player_two_name = args.player2Name if args.player2Name else raw_input("Player Two Name: ")

    timed = args.timed if args.timed else raw_input("Time the Game? (y/n)")

    if player_one_type and player_one_name and player_two_type and player_two_name:
        #print 'Game is set to begin.'
        #print player_one_type,'named',player_one_name,'vs',player_two_type,'named',player_two_name
        if timed == 'y':
            print 'Timed Game'
        else:
            game = Game(player_one_type,player_one_name,player_two_type,player_two_name)

        player1,player2= game.introducePlayers()

        print 'Welcome to the Game'
        print player_one_type,'named',player1.name,'vs',player_two_type,'named',player2.name

        while player1.score < upper_limit and player2.score < upper_limit:
            game.rollDice(player1)

            if player1.score >= upper_limit:
                print "Playes 1 Wins"
                break

            game.rollDice(player2)

            if player2.score >= upper_limit:
                print "Player 2 Wins"
                break

        print 'Final Results'
        print 'Player:',player1.name,'Score:',player1.score
        print 'Player:', player2.name, 'Score:', player2.score

    print 'Game has terminated...Play Again (y/n):...'

if __name__ == '__main__':
    main()
