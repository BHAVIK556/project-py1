import random
print("guess game")
number = random.randint(1,9)
chance = 0   



while chance < 5:

   guess = input("Guess a number(between 1,9)") 
   if guess == number:
      print("You Win")
      break

   else:
     print("wrong guess")
     
     
   chance = chance+1


if not chance<5:
   print("you lose!!!,the number",number) 
