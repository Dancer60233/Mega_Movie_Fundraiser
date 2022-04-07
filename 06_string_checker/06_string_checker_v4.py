#7/4/22
#Kate barber
# MMF String Checker - V4

import re

#lists
valid_snacks =[
  ["popcorn", "p", "corn", "a"],
  ["M&M's", "m&m's", "mms", "m", "b"],
  ["pita chips", "chips", "pc", "pita", "c"],
  ["water", "w", "aqua", "d"],
  ["orange juice", "oj", "juice", "o", "e",] ,
]

#functions

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



#Valid snacks holds list of all snacks
#Each item in valid snacks is a list with valid optuons for each snack
#<full name, letter code(a - e), and possible abbreviations etc
valid_snacks =[
  ["popcorn", "p", "corn", "a"],
  ["M&M's", "m&m's", "mms", "m", "b"],
  ["pita chips", "chips", "pc", "pita", "c"],
  ["water", "w", "aqua", "d"]
]

yes_no = [
  ["yes", "y"],
  ["no", "n"],
]

#holds snack order for single user
snacks_order = []
amount_snacks = []

#--------Variables----------
desired_snack = ""
snack_count = 0

 #regular expression to find if item starts with a number
number_regex = "^[1-9]"
    

#*********** Main routine **********

#ask user if they want a snack
check_snack = "invalid choice"
while check_snack == "invalid choice":
  want_snack = input("Do you want to order snacks? ").lower()
  check_snack = string_check(want_snack, yes_no)
  
#If they say yes, ask wha snacks they want and add to our snack list
if check_snack == "Yes":

  
 # loop six times to make testing quicker
 while desired_snack != "xxx":
  #ask user for desired snack and put it in lowercase
   desired_snack = input("Snack: ").lower()

   if desired_snack == "xxx":
     break

   #if item has a number, seperate it into two (number and letters)
   if re.match(number_regex, desired_snack):
    amount = int(desired_snack[0])
    snack_choice = desired_snack[1:].strip()

# if item does not have number in front set number to 1
   else:
    amount = 1
    snack_choice = desired_snack.strip()  

   #check if snack is valid  
   snack_choice = string_check(snack_choice, valid_snacks)
   
     

# remove white space around snack
   print("Snack Choice:" ,snack_choice)
   print("Amount:", amount)
   print("Length of snack:", len(desired_snack))

   #add snack to list...

   # check that snack is not the exit code or invalid choice before adding
   if snack_choice != "xxx" and snack_choice != "invalid choice":
    snacks_order.append(snack_choice)
    amount_snacks.append(amount)
    
  
   
#show snack orders

if len(snacks_order) == 0:
  print("\nSnacks Ordered: None")

else:
 print("\nSnacks Ordered:")
 print(* amount_snacks, * snacks_order, sep = "\n")
 