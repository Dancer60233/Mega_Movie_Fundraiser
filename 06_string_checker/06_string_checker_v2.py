#30/3/22
#Kate barber
# MMF String Checker - V2


#lists
valid_snacks =[
  ["popcorn", "p", "corn", "a"],
  ["M&M's", "m&m's", "mms", "m", "b"],
  ["pita chips", "chips", "pc", "pita", "c"],
  ["water", "w", "aqua", "d"]
]

#Intialise variables

snack_ok = ""
snack = ""

#loop three times to make testing quicker

for item in range (0,3):
   desired_snack = input("Snack:").lower()

   for var_list in valid_snacks:
   #if snack is in one of the lists, return the full name
    if desired_snack in var_list:
  #Get full name of snack and put it in titles case so it looks nice when outputted
     snack = var_list[0].title()
     snack_ok = "yes"
     break
    

  #if the chosen snack is not valid, set snack_ok to 
    else:
     snack_ok = "no"

    #if the snack is not OK - ask question again
   if snack_ok == "yes":
     print("Snack Choice: ",snack)

   else:
      print("Invalid choice")

    
 