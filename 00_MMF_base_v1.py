#import statements


#*********functions go here*************

#Check that ticket name isn't blank
def not_blank(question):
  valid = False

  while not valid:
    response = input(question)
    
    #If name is not blank program continues
    if response != "":
      return response
   #If name is blank, show error (& repeat loop)
    else:
      print("Sorry - this can't be blank, "
            "please enter your name")

#checks for an integer between two values
def int_check(question):
 error = "Please enter a whole number that is more than 0"
 
 valid = False
 while not valid:

   #ask user for number and check it is valid
  try:
    response = int(input(question))

    #Checks if number is in range
    if response <= 0:
     print(error)     
    else:
      return response
      
    
  #if an interger us not entered, display an error message   
  except ValueError:
    print(error)

#main routine
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
 #Tellsusers how many seats are left
  if count < 4:
    print("You have {} seats left".format(MAX_TICKETS-count))
    
  #Warns user that there is only one seat left
  else:
    print("*** There is ONE seat left!! ***")

 #Get details....
    
  #Get name (Can't be blank)
  name= not_blank("Name: ") 

  # end the loop if the exit code is entered
  if name == "xxx":
    break
    
  

  #Get age (Between 12 and 130)
  age = int_check("Age:") 

  #check that age is valid

  if age < 12:
    print("Sorry you are too young for this movie")
    continue
  elif age > 130:
    print("That is very old - it looks like a mistake")
    continue 

  count += 1
    


if count == MAX_TICKETS:
  print("You have sold all available tickets!")
   
else:
   print("You have sold {} tickets. \nThere are {} places still available".format(count,MAX_TICKETS-count))
   
  



 #Calculate ticket price

 #Loop to ask for snacks

 #Calculate snack price

 #ask for payment method (and apply surcharge if nesecracy)

#Calculate total Sales and profit

#Output data to text file