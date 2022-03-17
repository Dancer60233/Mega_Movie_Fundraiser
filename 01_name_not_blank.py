#16/3/22
#Kate barber
# MMF V1- Name not blank


#Functions   
def not_blank(question):
  valid = False

  while not valid:
    response = input(question)

    if response != "":
      return response

    else:
      print("Sorry - this can't be blank")

#Main Routine

name= not_blank("Name: ")
  
     