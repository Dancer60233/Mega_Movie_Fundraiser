#import statements

import re
import pandas

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




      

#Checks for integer more than 0


  

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


    

def check_tickets(tickets_sold, ticket_limit):
   #Tells users how many seats are left
  if tickets_sold < ticket_limit -1:
    print("You have {} seats left ".format(ticket_limit - tickets_sold))
    
  #Warns user that there is only one seat left
  else:
    print("*** There is ONE seat left!! ***")

  return ""





#Gets Ticket Price based on age
def get_ticket_price():
  #get  age (between 12 and 130)
  age = int_check("Age: ") 

  #check that age is valid
  if age < 12:
    print("Sorry you are too young for this movie")
    return "invalid ticket price"
  elif age > 130:
    print("That is very old - it looks like a mistake")
    return "invalid ticket price"


  #Calculate ticket price
  if age < 16:
   ticket_price = 7.5
  elif age >= 65:
   ticket_price = 6.5
  else:
   ticket_price = 10.5

  return ticket_price

  






def string_check(choice, options):

 for var_list in options:
   #if snack is in one of the lists, return the full name
      if choice in var_list:
  #Get full name of snack and put it in titles case so it looks nice when outputted
       return var_list[0].title()
       is_valid = "yes"
       break

      else:
        is_valid = "no"

 if is_valid == "yes":
    return chosen

 else:
    return "invalid choice"






#lists

#Valid snacks holds list of all snacks
#Each item in valid snacks is a list with valid optuons for each snack
#<full name, letter code(a - e), and possible abbreviations etc


#Gets List of snacks


#Gets list of snacks
def get_snack():
   #regular expression to find if item starts with a number
   number_regex = "^[1-9]"


#Valid snacks holds list of all snacks
#Each item in valid snacks is a list with valid optuons for each snack
#<full name, letter code(a - e), and possible abbreviations etc
   valid_snacks = [
  ["popcorn", "p", "corn", "a"],
  ["M&M's", "m&m's", "mms", "m", "b"],
  ["pita chips", "chips", "pc", "pita", "c"],
  ["water", "w", "aqua", "d"],
  ["orange juice", "oj", "juice", "o", "e",] ,
]
   #holds snack order for single user
   snack_order = []

   desired_snack = ""
   while desired_snack != "xxx":

    snack_row = []
   
  #ask user for desired snack and put it in lowercase
    desired_snack = input("Snack: ").lower()

    if desired_snack == "xxx":
     return snack_order

    #if item has a number, seperate it into two (number and letters)
    if re.match(number_regex, desired_snack):
     amount = int(desired_snack[0])
     desired_snack = desired_snack[1:]

# if item does not have number in front set number to 1
    else:
     amount = 1
     desired_snack = desired_snack

  #Remove white space around snack
    desired_snack = desired_snack.strip()
  
   
   #check if snack is valid  
    snack_choice = string_check(desired_snack, valid_snacks)

    if snack_choice == "invalid choice":
     print("Please enter a valid option")
     
     
     #check amount is valid
     
    elif amount >= 5:
     print("Sorry - we have a four snack maximum")
     snack_choice = "invalid choice"

    #add snack AND amount to 
     
    snack_row.append(amount)
    snack_row.append(snack_choice)

  # check that snack is not the exit code or invalid choice before adding
    if snack_choice != "xxx" and snack_choice != "invalid choice":
     snack_order.append(snack_row)
     return snack_order

   


      






#***************Main Routine****************

#Set up dictionaries / lists needed to hold data

# list for valid yes / no responses



yes_no = [
  ["yes", "y"],
  ["no", "n"],
]

#List for valid pay methods
pay_method = [
  ["cash", "ca"],
  ["credit", "cr"],
]
#Initilise loop
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales= 0

#Intialise lists ( to mae data-frame in due course)
all_names = []
all_tickets = []
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

#Data Frame Dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice
    }

#cost of each snack
price_dict = {
  'Popcorn': 2.5,
  'Water': 2,
  'Pita Chips': 4.5,
  'M&Ms': 3,
  'Orange Juice': 3.25,
}


#Ask user if they have used the program before and show instructions


#Loop to get Ticket details
while name != "xxx" and ticket_count < MAX_TICKETS:


 #checks numbers of ticket limit has not been exceeded
  check_tickets(ticket_count, MAX_TICKETS)

 #---Get details....---
    
  #Get name (Can't be blank)
  name= not_blank("Name: ") 

  # end the loop if the exit code is entered
  if name == "xxx":
    break
    
  # Get ticket price based on age
  ticket_price = get_ticket_price()

  if ticket_price == "invalid ticket price":
    continue 


  
  ticket_count += 1
  ticket_sales += ticket_price

  #add name and ticket price to lists
  all_names.append(name)
  all_tickets.append(ticket_price)

  #Get snacks
  check_snack = "invalid choice"
  while check_snack == "invalid choice":
   want_snack = input("Do you want to order snacks? ").lower()
   check_snack = string_check(want_snack, yes_no)
  
#If they say yes, ask wha snacks they want and add to our snack list
   if check_snack == "Yes":
    get_order = get_snack()

   else:
    get_order=[]

    
   
#show snack orders

  if len(get_order) == 0:
   print("\nSnacks Ordered: None")

  else:
   print("\nSnacks Ordered:")
   print(* get_order, sep = "\n")

    # Assume no snacks have been bought...
  for item in snack_lists:
    item.append(0)

    # print(snack_lists)
    count = 0
    # get order (hard coded for easy testing)...
    count += 1

    for item in get_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount


#Get Payment method (ie: work out if surcharge is needed)
  how_pay = "invalid choice"
  while how_pay == "invalid choice":
   how_pay = input("Please choose a payment method (cash or credit) ").lower()
   how_pay = string_check(how_pay, pay_method)
   if how_pay == "invalid choice":
     print("Please enter a valid choice")

  if how_pay == "Credit":
    surcharge_multiplier = 0.05
  else: 
    surcharge_multiplier = 0
  

#End of Tickets / snacks / payment Loop
  
#print details...
print()

#Create dataframe and set index to name column
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

#create column called 'Sub Total'
# fill in price for snacks and tickets

movie_frame["Sub Total"] = \
  movie_frame['Ticket'] + \
  movie_frame['Popcorn']*price_dict['Popcorn'] + \
  movie_frame['Water']*price_dict['Water'] + \
  movie_frame['Pita Chips']*price_dict['Pita Chips'] + \
  movie_frame['M&Ms']*price_dict['M&Ms'] + \
  movie_frame['Orange Juice']*price_dict['Orange Juice']

#Shorten Column names
#movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ',
#                                        'Pita Chips': 'Chips'})
print(movie_frame)

#calculate ticket profit
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))


#tells user if they have unsold tickets...
if ticket_count == MAX_TICKETS:
  print("You have sold all available tickets!")
   
else:
   print("You have sold {} tickets. \nThere are {} places still available".format(ticket_count,MAX_TICKETS-ticket_count))
   
  


#Calculate total Sales and profit

#Output data to text file