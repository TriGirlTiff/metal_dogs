"""This is a game that will help you decide what kind of toy breed dog you should get based on your heavy metal choices"""
import random
dogs1= ["Pomeranian", 
    "Poodle", 
    "Papillion", 
    "Yorkshire Terrier", 
    "Pekingese"] 
dogs2 =["Chihuahua", 
    "Maltese", 
    "Havanese", 
    "Miniature Pinscer", 
    "Shih Tsu"] 
dogs3 =["Chinese Crested",
    "Japanese Chin",
    "Affenpinscer", 
    "Toy Fox Terrier",
    "King Charles Spaniel"]
dogs4 =["Brussels Griffon",
    "Italian Greyhound",
    "Pug",
    "Dachshund",
    "Norfolk Terrier"]


def greeting():
    print
    print
    print "Welcome! This is a Buzzfeed-style quiz will determine what toy breed of dog you should get based on your heavy metal preferences!"
    print
    print



def a_bands():
    while True:
        choice1 = raw_input("Choose an American heavy metal band: \n A. Metallica\n B. Megadeth\n C. Anthrax\n D. Pantera\n >> ")
        choice1 = choice1.upper()
        if choice1 not in ("A", "B", "C", "D"):
            print
            print "Please choose a letter from the options given."
            print
            continue
        return choice1


def b_bands():
    while True:
        choice2 = raw_input("Choose an English Heavy Metal band: \n A. Black Sabbath\n B. Iron Maiden\n C. Motorhead\n D. Judas Priest\n >> ")
        choice2 = choice2.upper()
        if choice2 not in ("A", "B", "C", "D"):
            print
            print "Please choose a letter from the options given."
            print
            continue
        return choice2

def h_bands():
    while True:
        choice3 = raw_input("Choose a hair band: \n A. Poison\n B. Bon Jovi\n C. Tesla\n D. Motley Crue\n >> ")
        choice3 = choice3.upper()
        if choice3 not in ("A", "B", "C", "D"):
            print
            print "Please choose a letter form the options given."
            print
            continue
        return choice3


def s_bands():
    while True:
        choice4 = raw_input("Choose a shock rock band: \n A. Alice Cooper\n B. Marilyn Manson\n C. Rob Zombie\n D. Gwar\n >> ")
        choice4 = choice4.upper()
        if choice4 not in ("A", "B", "C", "D"):
            print
            print "Please choose a letter from the options given."
            print
            continue
        return choice4

def assign_points(answer):
    total = 0
    if answer == "A":
        total =+ 1
    elif answer == "B":
        total =+2
    elif answer == "C":
        total =+3
    elif answer == "D":
        total =+ 4
    return total

def add_points(num1,num2, num3, num4):
    total_points = 0
    total_points = num1 + num2 + num3 + num4
    return total_points

def get_dog(points):
    if points in range (0,5):
        return random.choice(dogs1)
    elif points in range (5,10):
        return random.choice(dogs2)
    elif points in range (10,15):
        return random.choice(dogs3)
    elif points in range (15,21):
        return random.choice(dogs4)


def play_game():

    while play_game:
        choice1 = a_bands()
        total1 = assign_points(choice1)
        choice2 = b_bands()
        total2 = assign_points(choice2)
        choice3 = h_bands()
        total3 = assign_points(choice3)
        choice4 = s_bands()
        total4 = assign_points(choice4)
        total_points = add_points(total1, total2, total3, total4)
        what_dog = get_dog(total_points)
        print
        print "The dog you should get based on your Heavy Metal preferences is the: {}".format(what_dog)
        print
        print
        play_again = raw_input("Would you like to play again? Y/n: ")
        play_again.lower()
        if play_again == "Y":
            return True
        elif play_again == "n":
            print
            print "Thanks for playing!"
            return False
        


greeting()
play_game()


        
        









    





