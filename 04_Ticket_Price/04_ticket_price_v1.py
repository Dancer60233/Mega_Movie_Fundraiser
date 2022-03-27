#28/3/22
#Kate barber
# MMF Ticket Price - V1

profit = 0

name = ""

while name != "xxx":

  name= input("Name: ") #replace with function

  # end the loop if the exit code is entered
  if name == "xxx":
    break
    
   #Get age (Between 12 and 130)
  age = int(input("Age:")) #replace with function

  #Calculate Ticket Price
  if age < 16:
   ticket_price = 7.5
  elif age >= 65:
   ticket_price = 6.5
  else:
   ticket_price = 10.5

  #Calculate Profit
  profit_made = ticket_price - 5
  profit += profit_made
  
  print("{} : ${:.2f}".format(name, ticket_price))

print("Profit from Ticket Prices is ${:.2f}".format(profit))