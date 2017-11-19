#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week Eight - Pig Game with Computer"""

import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="Name of the Player",default=None)
args = parser.parse_args()

upper_limit = 100

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

class Game(object):
    def __init__(self, value1, value2):  # Assign method name
        self.player1 = value1
        self.player2 = value2

    def introducePlayers(self):
        player1 = PlayerData(self.player1)
        player2 = PlayerData(self.player2)

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
                    answer = raw_input("Roll(r) or Hold(h): ")
                    if answer == 'h':
                        player.score = temp_player_score
                        break
                    else:
                        continue
        return

def main():
    # Call the Game Class to begin Game
    print 'Welcome to Our Game'
    player_one = args.name if args.name else raw_input("Please enter name of first player: ")

    if player_one:
        player_two = args.name if args.name else raw_input("Please enter name of second player: ")

    if player_one and player_two:
        game = Game(player_one,player_two)

        player1,player2= game.introducePlayers()

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
