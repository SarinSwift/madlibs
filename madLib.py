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

def user_input(nothing):
    user = input(nothing)
    return user

print("This is a madlibs game, where your inputs will be filled in the blank spaces.")
print("The ____ was invented by ____ who worked very ____ and ____ to create it. The masterpiece was used across ____ people!")

noun = input("Input a noun: ")
person = input("Input a persons name: ")
adj_1 = input("Input an adjective: ")
adj_2 = input("Input a second adjective: ")
num = input("Input a number: ")

print ("The {} was invented by {} who worked very {} and {} to create it. The masterpiece was used by {} people!".format(noun,person,adj_1,adj_2,num))
