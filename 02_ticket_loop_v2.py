#21/3/22
#Kate barber
# MMF Ticket loop- V1

# start of loop

name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

 #Get details....
 name = input("Name: ")
 if name != "xxx":
  count += 1
  if count < MAX_TICKETS:
   print("You have {} seats left".format(MAX_TICKETS-count))
  else:
    print("You have sold all available tickets!")
 else:
   print("You have sold {} tickets. There are {} places still available".format(count,MAX_TICKETS-count))
   
  