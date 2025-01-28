#Magic8Ball.py
#Name:Cooper Kinnan
#Date:1/28/2025
#Assignment:Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
question = input("What is your question?")
thing1 = input("As I see it, yes")
thing2 = input("Ask again later")
thing3 = input("Can't say yet")
thing4 = input("Cannot predict now")
thing5 = input("Try hearder asking")
thing6 = input("Don't count on it")
thing6 = input("For sure")
thing7 = input("It is decidedly so")
thing8 = input("Most likely")
thing9 = input("My reply is no")
thing10 = input("My sources say no")
thing11 = input("Outlook not so good")
thing12 = input("Outlook good")
thing13 = input("Repy hazy, try again")
thing14 = input("Signs say yes")
thing15 = input("Very doubtful")
thing16 = input("Without a doubt")
thing17 = input("Yes.")
thing18 = input("Oh yea for sure")
thing19 = input("You may rely on it")
thing20= input("Thats a stupid question")
answers = ["thing1", "thing2", "thing3", "thing4", "thing5", "thing6", "thing7", "thing8", "thing9", "thing10", "thing11", "thing12", "thing13", "thing14", "thing 15", "thing16", "thing17", "thing18", "thing19", "thing20"]
  #Answer question randomly with one of the options from your earlier list.
respone = random.choice(answers)

if __name__ == '__main__':
  main()
