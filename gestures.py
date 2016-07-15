import random, sys
 
class Player:#two methods in comun between user player and computer player
    score = 0
 
    def update_score(self):
        self.score += 1
 
    def get_score(self):
        return self.score
        
        # return score
 
 
class Computerp(Player): # The computer player class, it has in addition to the two Player method, it's own choose method.
 
    def choose(self):
        choice = random.choice('rps')
        return choice
        # use random library in order to determine computer choice   
 
 
class Userp(Player): # Same as computer player class
 
    def choose(self):
        choice = input('Please enter your choice(r, p, s)')
        print(choice)
        if (choice == 'r' or 'p' or 's'):
            
            return str(choice)
        else:
            print('Please enter a valid choice')
        # get user choice from input. You need to check user input has a correct format.  
 
class Game: # This is a wrapper class for the "Game logic", it has: compare_choices method, play, and play_again methods.
 
    def compare_choices(self, computer_choice, user_choice):
        if (((computer_choice == 'r') and (user_choice == 's')) or
            ((computer_choice == 's') and (user_choice == 'p')) or
            ((computer_choice == 'p') and (user_choice == 'r'))):
            return 'computer'
        if (((user_choice == 'r') and (computer_choice == 's')) or
            ((user_choice == 's') and (computer_choice == 'p')) or
            ((user_choice == 'p') and (computer_choice == 'r'))):
            return 'user'
        if (((user_choice == 'r') and (computer_choice == 'r')) or
            ((user_choice == 's') and (computer_choice == 's')) or
            ((user_choice == 'p') and (computer_choice == 'p'))):
            return 'n'
        
        # You should compare computer choice and user choise and return 'computer' or 'user' or 'n'
 
    def play(self):
        user = Userp()
        computer = Computerp()
        i = 1
        while i <= 3:
            user_ch = user.choose()
            computer_ch = computer.choose()
            result = self.compare_choices(computer_ch, user_ch)
            if result == 'user':
                user.update_score()
                print (" Your choice was " + user_ch + ", the computer's choice was "+ computer_ch)
                print (" You WON ! \n")
            elif result == 'computer':
                computer.update_score()
                print (" Your choice was " + user_ch + ", the computer's choice was "+ computer_ch)
                print (" The computer won. \n")
            else:
                print (" Your choice was " + str(user_ch) + ", the computer's choice was "+ str(computer_ch))
                self.play_again()
            i = i + 1
        print ("Your score was: "+str(user.get_score())+", The Computer's score was: "+str(computer.get_score()))
        if user.get_score() > computer.get_score():
            print ("You are the WINNER, CONGRATULATIONS! \n\n")
        else:
            print ("The Computer is the WINNER. \n\n")
        self.play_again()
 
 
    def play_again(self):
        print ("Game Over")
        choice = input(" Would you like to play again? (Y/N) ")
        if choice == "y" or choice == "Y":
            self.play()
        elif choice == "n" or choice == "N":
            exit()
        else:
            print (" Wrong input, Please try again.\n")
            self.play_again()
 
 
######################################################################
 
print ("""
          +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
          +                          WECLOME TO ROCK, PAPER, SISSORS GAME.                         +
          +                                                                                                                                          +
          + To test you luck, please choose "r" for Rock, "s" Sissors and "p" for paper.+
          +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
         """)
 
game = Game()
 
game.play()
