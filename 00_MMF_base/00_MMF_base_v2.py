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

#******************main routine***********

   


  #Calculate ticket price
  if age < 16:
   ticket_price = 7.5
   return ticket_price
  elif age >= 65:
   ticket_price = 6.5
   return ticket_price
  else:
   ticket_price = 10.5
   return ticket_price


#****************************** Main Routine ****************

#Set up dictionaries / lists needed to hold data

#Ask user if they have used the program before and show instructions


#Loop to get Ticket details
#start of loop

#initialise loop so that it runs at least once
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales= 0

while name != "xxx" and ticket_count < MAX_TICKETS:

  if ticket_count < MAX_TICKETS -1:
    print("You have {} seats left".format(MAX_TICKETS-ticket_count))
    
  #Warns user that there is only one seat left
  else:
    print("*** There is ONE seat left!! ***")


 #Get details....
    
  #Get name (Can't be blank)
  name= not_blank("Name: ") 

  # end the loop if the exit code is entered
  if name == "xxx":
    break
    
  #Tells users how many seats are left
  

  age = int_check("Age:") 

  #check that age is valid

  if age < 12:
    print("Sorry you are too young for this movie")
    continue
  elif age > 130:
    print("That is very old - it looks like a mistake")
    continue 

  #Get age (Between 12 and 130)
  
  ticket_count += 1
  ticket_sales += ticket_price

  #End of Ticket Loop
  
#Calculate Ticket Profit
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticketprofit: ${:.2f}".format(ticket_profit))

if ticket_count == MAX_TICKETS:
  print("You have sold all available tickets!")
   
else:
   print("You have sold {} tickets. \nThere are {} places still available".format(ticket_count,MAX_TICKETS-ticket_count))
   
  

 #Loop to ask for snacks

 #Calculate snack price

 #ask for payment method (and apply surcharge if nesecracy)

#Calculate total Sales and profit

#Output data to text file