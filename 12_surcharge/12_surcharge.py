

#Function goes here
#WARNING: The response will be returned in title case

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


 





pay_method = [
  ["cash", "ca"],
  ["credit", "cr"],
]

name = ""
SURCHARGE = 2

#loop till exit code
while name != "xxx":
  name = input("Name: ")
  if name == "xxx":
    break

  #ask for payment method
  how_pay = "invalid choice"
  while how_pay == "invalid choice":
    
   how_pay = input("Please choose a payment method (cash or credit) ").lower()
   how_pay = string_check(how_pay, pay_method)
 
  #ask for a subtotal (for testing purposes)
  subtotal = float(input("Sub total? $"))
  if how_pay == "Credit":
    surcharge = 0.05 * subtotal
  else: 
    total = sub_total
  print (total)

