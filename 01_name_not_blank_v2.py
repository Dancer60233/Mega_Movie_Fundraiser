#18/3/22
#Kate barber
# MMF V1- Name not blank


#Functions   
def not_blank(question, error_message):
  valid = False

  while not valid:
    response = input(question)

    if response != "":
      return response

    else:
      print(error_message)

#Main Routine

name= not_blank("Name: ", 
                "Sorry- this can't be blank, "
                "please enter your name")
  
     