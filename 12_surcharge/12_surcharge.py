

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
  sub_total = input("Sub Total:")
  pay_choice = input("What payment method are you using? ").lower()
  check_pay = string_check(pay_choice, pay_method)

  #Calculate sur charge  
  if check_pay == "Credit":
    total = sub_total * SURCHARGE
  elif check_pay == "Cash":
    total = sub_total
  print (total)

