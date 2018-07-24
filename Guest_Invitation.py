#guest invitation
#python basic list operations, while loop, user input, functions


#function to print the guest list
def print_guests(guest_list):
	print("\n\nYour guest list:")

	cnt = 0
	for guest in guest_list:
		cnt = cnt + 1
		print(str(cnt) +": " + guest.title())
		
	print("\nNumber of guests: "+ str(len(guest_list)) + "\n")
		
#-------------------------------------------------------------------------	
#get the user input to create the guest list

guest_list = [] 
while True:
	guest_name = input("Enter guest name(or Enter to quit): ")
	if not guest_name:
		break
	else:
		guest_list.append(guest_name.title())	
		
print_guests(guest_list)
	

#-------------------------------------------------------------------------
#Changing guest list

#get input if some guests can't make it
while True:
	guest_not_coming = input("\nEnter the name of the guests who can not make it(or Enter to quit):")
	if not guest_not_coming:
		break
	else:
		if guest_not_coming.title() in guest_list:
			guest_list.remove(guest_not_coming.title())
		else:
			print("Guest not in the list")
		

#get input of new guests
while True:
	new_guest = input("\nEnter the name of the new guests you want to add(or Enter to quit):")
	if not new_guest:
		break
	else:
		guest_list.append(new_guest.title())
		
print_guests(guest_list)

#-------------------------------------------------------------------------
#Sorting the guest list with sort() method

while True:
	order = input("\nDo you want to sort in alphabetical order or reverse alphabetical order? Enter 1 for alphabetical order and 2 for reverse alphabetical order: ")
	if str(order) not in ('1','2'):
		print("\nWrong input")
		continue
	else:
		break
		
if str(order) == '1':
	print("\nsorting alphabetical order:")
	guest_list.sort()
	print_guests(guest_list)
else:
	print("\nsorting reverse alphabetical order:")
	guest_list.sort(reverse = True)
	print_guests(guest_list)
	

#-------------------------------------------------------------------------
#Shrinking guest list for some constraints

final_decision = input("Do you want to reduce guests list? (Type 'Y' to reduce or Enter to finalize)" )
if not final_decision:
	print("\nGuests list finalized")
	print_guests(guest_list)
else:
	print("\nlooks like you want to reduce the guests list for some reason")
	print("\nCurrently you have "+str(len(guest_list)) +" people")

	number_of_guests = int(input("\nEnter the number of people you would like to remove"))

	print("\nWe will remove "+ str(number_of_guests) +" people from the back of the list and print it")

	for i in range(0,number_of_guests):
		removed_guest = guest_list.pop()
		print("Removed guest :" + removed_guest)
		
	print("\nGuests list finalized")	
	print_guests(guest_list)

#-------------------------------------------------------------------------






	

