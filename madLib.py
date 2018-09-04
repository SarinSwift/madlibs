# MadLibs
'''
Sentence = "The <noun> was invented by <person> who worked very <adj> and <adj> to create it. The masterpiece was used across <number> people!"

input: 1 noun
        1 person
        2 adjectives
        1 number

output: The complete sentence including the users inputs

process: noun()
        person()
        adj_1()
        adj_2()
        num()
'''

print("\nThis is a madlibs game, where your inputs will be filled in the blank spaces.")


def madlib_1():
    # print("\nStory 1:\nThe ____ was invented by ____ who worked very ____ and ____ to create it. The masterpiece was used across ____ people!")

    noun = input("Input an object: ")
    person = input("Input a persons name: ")
    adj_1 = input("Input an adjective: ")
    adj_2 = input("Input a second adjective: ")
    num = input("Input a number: ")

    print ("The {} was invented by {} who worked very {} and {} to create it. The masterpiece was used by {} people!".format(noun,person,adj_1,adj_2,num))

def madlib_2():
    # print("\nStory 2:\nIn a place called ____, there was a ____ prince named ____. His mansion was huge and he ____ all day.")

    place = input("Input a place: ")
    adj = input("Input an adjective: ")
    male = input("Input a male celebrity: ")
    verb = input("Input a '-s' verb: ")

    print("In a place called {}, there was a {} prince named {}. His mansion was huge and he {} all day.".format(place,adj,male,verb))

def select(choice):
    if choice == "1":
        madlib_1()
    elif choice == "2":
        madlib_2()
    elif choice == "Q" or "q":
        return False
    else:
        print("Input '1' or '2'")
    return True


# choice = input("Input '1' or '2' to randomize a story, or 'Q' to exit: ")

running = True
while running:
    selection = input("\nInput '1' or '2' to choose  a story, or 'Q' to exit: ")
    running = select(selection)
