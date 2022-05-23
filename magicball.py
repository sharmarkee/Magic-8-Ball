import random
variable_name = "Shark"
question = "Will  I Be Rich"
answer = ""
random_number = random.randint(1,10)
print(random_number)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "Only time will tell."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
    answer = "Unclear, try again!"
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
   answer = "Best I not tell you now."
elif random_number == 7:
   answer = "My sources say no."
elif random_number == 8:
   answer = "Chances are low."
elif random_number == 9:
    answer = "Very Doubtful."
elif random_number == 10:
   answer = "Keep on dreaming."  
else:
  answer = "Error"

  print( Shark + "asks:" + "Will I be Rich")

  print ("Magic 8-Ball's answer: " + answer)