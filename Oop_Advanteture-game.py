import time
import random

#------------------------- collect_pointts ---------------------------

points=[]

#----------------- Parent class_fundamentals ------------------


class Fundamentals:
    

    def __init__(self):
        pass

    #------------------------- points ---------------------------


    def point(self,x):
        points.append(x)
        return sum(points)

    #------------------------- print_pause ---------------------------


    def print_pause(self,x):
        """Print a message and pause for 1 second."""
        print(x)
        time.sleep(1)

    #------------------------- tools ---------------------------


    def random_tool(self):
        """Choose a random magical tool and update player's points."""
        tools = [
            {"Name": "Wand of ice", "Points": 4, "Accuracy": "High"},
            {"Name": "Amulet of fire resistance", "Points": 3, "Accuracy": "Mid"},
            {"Name": "Potion of speed", "Points": 2, "Accuracy": "Low"}
        ]
        self.print_pause("Magic tools:")
        self.print_pause("")
        for tool in tools:
            self.print_pause(f"Tool: `{tool['Name']}` points: `{tool['Points']}` and "
                        f"accuracy: `{tool['Accuracy']}`")
        use_tool = random.choice(tools)
        tool_name = use_tool["Name"]
        tool_points = use_tool["Points"]
        print("")
        self.print_pause(f"You have ` {tool_name} ` tool with {tool_points} bonus .")
        bonus = tool_points
        points.append(bonus)
        total_points = sum(points)
        print(f"Total points {total_points}")

    #------------------------- option ---------------------------


    def option(self):
        """Make player choose between (cave or bridge)."""
        option = input("In which way will you go? (1 or 2): ")
        while option:
            if option == "1":
                x=Game()
                x.Visit_cave()
                break
            elif option == "2":
                x= Game()
                x.bridge()
                break
            else:
                print("Please choose (1 or 2).")
                option = input("In which way will you go? (1 or 2): ")

    #------------------------- go ---------------------------


    def go(self):
        """Choose (go to bridge or fight the super dragon)."""
        self.print_pause("To fight super dragon must have 10 points")
        go_action = input("Go to bridge or fight the SUPER dragon.(g or f): ")
        while go_action:
            if go_action == "g":
                print("Going to the bridge...")
                x=Game()
                x.bridge()
                break
            elif go_action == "f":
                if sum(points) >= 10:
                    self.print_pause("You fight the dragon!")
                    print("After a huge fight, you win!")
                    self.end_game()     #-----
                    break
                else:
                    self.print_pause("You decide to fight the SUPER dragon...")
                    self.print_pause("You fail..!")
                    self.print_pause(f"because you have {sum(points)} points.")
                    self.print_pause("The SUPER dragon kills you.")
                    self.print_pause("Game over")
                    points.clear()
                    points.append(0)
                    self.print_pause("You lose your points.")
                    self.print_pause(F"You have `{sum(points)}` points")
                    self.play_again()    #----
                    break
            else:
                print("Please choose a valid option (g/f).")
                go_action = input("Please use (g `go` or f `fight`): ")

    #------------------------- return to cave ---------------------------


    def return_to_cave(self):
        """Show message if player has points when returning to cave."""
        if sum(points) == 0:
            return
        self.print_pause("The dragon gives you his treasure")
        self.print_pause(f"You have:{sum(points)} points")
        self.print_pause("You find there's nothing else to do.")
        self.go()    #---

    #------------------------- end_game ---------------------------


    def end_game(self):
        """Conclude the game with a victory message."""
        points.append(5)
        total_points = sum(points)
        self.print_pause("You kill the dragon and...")
        self.print_pause("You see a light and run towards it.")
        self.print_pause("When you catch this light.")
        self.print_pause("you find a sea and a small boat to escape from this land.") 
        self.print_pause(f"You have {total_points} points.")
        self.print_pause("You end the game successfully.")
        self.print_pause("Thanks for playing.")
        self.play_again()   #---
    
    #------------------------- play_again ---------------------------


    def play_again(self):
        """Ask the player if they want to start a new game."""
        play_again = input("Do you want to play again? (yes or no): ")
        while play_again:
            if play_again == "yes":
                self.print_pause("Thanks for playing!")
                self.print_pause("Starting a new game...")
                self.reset_points()  #---
                x=Game()
                x.land()
                break
            elif play_again == "no":
                self.print_pause("Thanks for playing!")
                exit()
            else:
                print("Please choose a valid option.")
                play_again = input("Do you want to play again? (yes or no): ")

    #------------------------- reset_points ---------------------------


    def reset_points(self):
        """Reset player's points to 0."""
        points.clear()
        points.append(0)


#------------------------- Game ---------------------------


class Game(Fundamentals):

    #------------------------- Land ---------------------------


    def land(self):
        """Start the game by choosing between the cave or the bridge."""
        super().__init__()
        self.print_pause(" ")
        self.print_pause("You are in a land full of dragons.")
        self.print_pause("In front of you, you see a cave and a bridge.")
        self.print_pause("You need to collect 5 points at least to win.")
        self.print_pause("1.In the cave there is a friendly dragon and...")
        self.print_pause("Will share his treasure with you.")
        self.print_pause("2.On the bridge there is a dragon that is maybe..")
        self.print_pause("Hungry, and will eat you.")
        self.print_pause("")
        self.print_pause(f"Your points --> {self.point(0)}")
        self.option()

    #------------------------- Cave ---------------------------


    def Visit_cave(self):
        """Handle the cave scenario with the friendly dragon."""
        super().__init__()
        self.print_pause(" ")
        self.return_to_cave()
        self.print_pause("### The Cave ###")
        self.print_pause("You approach the cave...")
        self.print_pause("It is dark and spooky...")
        self.print_pause("A large dragon jumps out in front of you!")
        action = input("Run or talk? (run/talk): ")
        while action:
            if action == "talk":
                points.append(3)
                total_points = sum(points)
                self.print_pause("He opens his jaws and...")
                self.print_pause("Gives you his treasure!")
                self.print_pause("You are rich now!")
                self.print_pause(f"You have --> {total_points} points")
                self.print_pause(" ")
                self.random_tool()
                self.print_pause(" ")
                back = input("Leave the cave (y/n): ")
                while back:
                    if back == "y":
                        self.print_pause(" ")
                        self.print_pause("You leave the cave and return to the land.")
                        self.go()
                        break
                    elif back == "n":
                        self.print_pause(" ")
                        self.print_pause("You find there's nothing else to do.")
                        self.print_pause("You run back to the land.")
                        self.land()
                        break
                    else:
                        self.print_pause("Please choose a valid option (y/n).")
                        back = input("Leave the cave (y/n): ")
                break
            elif action == "run":
                self.print_pause("You run back to the land.")
                self.land()
                break
            else:
                self.print_pause("Please choose a valid option (run/talk).")
                action = input("Run or talk? (run/talk): ")

    #------------------------- Bridge ---------------------------


    def bridge(self):
        """Handle the bridge encounter with the dragon."""
        super().__init__()
        self.print_pause(" ")
        self.print_pause("### The Bridge ###")
        self.print_pause("You approach the bridge...")
        self.print_pause("Unfortunately..!")
        self.print_pause("A large dragon jumps out in front of you!")
        self.print_pause(f"But you have {sum(points)} points.")
        action = input(f"Run or fight?(Must have at least 5 points): ")
        while action:
            if action == "fight":
                if sum(points) >= 5:
                    self.print_pause("You fight the dragon on the bridge!")
                    self.print_pause("After a huge fight, you win!")
                    self.end_game()
                    break
                else:
                    self.print_pause("He opens his jaws and...")
                    self.print_pause("Gobbles you down in one bite!")
                    self.print_pause("You are dead!")
                    self.print_pause("Game over!")
                    points.clear()
                    points.append(0)
                    self.print_pause("You lose all your points.")
                    self.print_pause(f"You have `{sum(points)}` points")
                    self.play_again()
                    break
            elif action == "run":
                self.print_pause("You run back to the land.")
                self.land()
                break
            else:
                self.print_pause("Please choose a valid option (run/fight).")
                action = input("Run or fight? (run/fight): ")

#------------------------- start_game ---------------------------

start = Game()
start.land()