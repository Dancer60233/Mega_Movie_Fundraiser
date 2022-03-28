#29/3/22
#Kate barber
# MMF Yes or No - V1

#Functions

def yes_no(question):

  error = "Please enter yes/no"

  valid = False

  while not valid:

    response = input(question).lower()

    if response == "y" or response == "yes":
     return "yes"

    elif response == "n" or response == "no":
     return "no"

    else:
      print(error)

#Main Routine

for item in range (0,6):
  want_snacks = yes_no("Do you want snacks? ")
  print("Answer OK, you said: {} \n".format(want_snacks))
