#23/3/22
#Kate barber
# MMF Get Age - V1

#function
def get_age(question):
 valid = False
  
 while not valid:
  try:
    response = int(input(question))

    if response < 12 or response > 130 :
      print("Invalid Age! Please enter an age between 12 - 130" )
      

    else:
      return response
      
  except:
    print("Invalid age!")

#main routine
age = get_age("Age:")
#try:
  #age = int(input("Age:"))

#except:
  #print("Invalid age")