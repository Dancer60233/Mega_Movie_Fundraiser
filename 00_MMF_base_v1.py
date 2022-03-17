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

 #Get name (Can't be blank)
 name= not_blank("Name: ")

 #Get age (Between 12 and 130)

 #Calculate ticket price

 #Loop to ask for snacks

 #Calculate snack price

 #ask for payment method (and apply surcharge if nesecracy)

#Calculate total Sales and profit

#Output data to text file