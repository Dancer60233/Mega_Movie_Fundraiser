#4/4/22
#Kate barber
# MMF String Checker - V3


#lists
valid_snacks =[
  ["popcorn", "p", "corn", "a"],
  ["M&M's", "m&m's", "mms", "m", "b"],
  ["pita chips", "chips", "pc", "pita", "c"],
  ["water", "w", "aqua", "d"]
]

#functions

def string_check(question):

  valid = False

  while not valid:

    response = input(question).lower()
    

    for var_list in valid_snacks:
   #if snack is in one of the lists, return the full name
      if response in var_list:
  #Get full name of snack and put it in titles case so it looks nice when outputted
       return var_list[0].title()
       snack_ok = "yes"
       
       
    

  #if the chosen snack is not valid, set snack_ok to 
      else:
       snack_ok = "no"

    if snack_ok == "no":
      print("Invalid choice!")

    
     

   
     
     

    
    

#Intialise variables


#*********** Main routine **********
for item in range (0,3):
 snack = string_check("Snack:")
 print("Snack Choice: ",snack)
 