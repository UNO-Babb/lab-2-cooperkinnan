#Magic8Ball.py
#Name:Cooper Kinnan
#Date:1/28/2025
#Assignment:Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
 print("Magic 8 Ball")
thing1 = ("As I see it, yes")
thing2 = ("Ask again later")
thing3 = ("Can't say yet")
thing4 = ("Cannot predict now")
thing5 = ("Try hearder asking")
thing6 = ("Don't count on it")
thing6 = ("For sure")
thing7 = ("It is decidedly so")
thing8 = ("Most likely")
thing9 = ("My reply is no")
thing10 = ("My sources say no")
thing11 = ("Outlook not so good")
thing12 = ("Outlook good")
thing13 = ("Repy hazy, try again")
thing14 = ("Signs say yes")
thing15 = ("Very doubtful")
thing16 = ("Without a doubt")
thing17 = ("Yes.")
thing18 = ("Oh yea for sure")
thing19 = ("You may rely on it")
thing20 = ("Thats a stupid question")
  #Prompt the user for their question.
question = input("What is your question?")
answers = [thing1, thing2, thing3, thing4, thing5, thing6, thing7, thing8, thing9, thing10, thing11, thing12, thing13, thing14, thing15, thing16, thing17, thing18, thing19, thing20]
  #Answer question randomly with one of the options from your earlier list.
response = random.choice(answers)
print(response)
if __name__ == '__main__':
  main()