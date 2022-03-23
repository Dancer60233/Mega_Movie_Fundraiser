#24/3/22
#Kate barber
# MMF Get Age - V2

#function
def int_check(question, low_num, high_num):
 error = "Please enter a whole number between {} and {}".format(low_num, high_num)
 
 valid = False
 while not valid:

   #ask user for number and check it is valid
  try:
    response = int(input(question))
    return response
    
  #if an interger us not enterd, display an error message   
  except ValueError:
    print(error)

#main routine
age = int_check("Age:", 12, 130)
