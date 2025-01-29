#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
  answers = ["Messi 8", "Ronaldo 1", "Cristiano Ronaldo 5", "Ronaldinhio 1", "KAka 1", "Benzema 1", "Modric 1",
              "Rodri 1", "Cannavaro 1", "Are you a soccr fanatic?", "Kane 0"]
  #Answer question randomly with one of the options from your earlier list.)

  num = random.random() #decimal 0-1
  num = num* 1000 #number 0-999 with decimals
  num = int(num) # no more decimals
  num = num % 10 #0 - 9
  question = input("ask me a question: ")
  print(answers[num])

if __name__ == '__main__':
  main()
