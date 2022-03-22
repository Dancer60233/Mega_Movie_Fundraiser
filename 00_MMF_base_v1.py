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



#************* Main Routine ****************

#Set up dictionaries / lists needed to hold data

#Ask user if they have used the program before and show instructions if nessecary

#Loop to get ticket details
#23/3/22
#Kate barber
# MMF Ticket loop- V3

# start of loop

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
  if name != "xxx":
   count += 1


if count == MAX_TICKETS:
  print("You have sold all available tickets!")
   
else:
   print("You have sold {} tickets. \nThere are {} places still available".format(count,MAX_TICKETS-count))
   
  


 #Get age (Between 12 and 130)

 #Calculate ticket price

 #Loop to ask for snacks

 #Calculate snack price

 #ask for payment method (and apply surcharge if nesecracy)

#Calculate total Sales and profit

#Output data to text file