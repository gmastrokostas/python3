#Define an empty  list
list_1=[]

#Define a list with elements
list_1=['One', 'Two', 'Three']

#Print all elements of a list
print(list_1)

#Loop through all elements of a list
#And perform a conditional statement
for loop in list_1:
    print(loop)
    if "One" in loop:
        print("we have a match")
        break;

#Compare two lists. Remember you have to sort them out
list_1=['Beta', 'Alpha', 'Gama']
list_2=['Gama', 'Beta', 'Alpha']

list_1.sort()
list_2.sort()
print(list_1)
print(list_2)

if list_1 == list_2:
    print("Lists are equal")
elif list_1 != list_2:
    print("Lists not equal")

#Eliminate duplicates from a list
#Method A) By using a loop
list_2=[]
for loop in list_1:
    if loop not in list_2:
        list_2.append(loop)
print(list_2)
#Method B) By using a set
list_1=list(set(list_1))
print(list_1)

#Add element in a list to a specific position within the list
list_2.insert(0, "Pizza")

#Append
list_2.append("Burger")

#Delete an element from a list
list_2.remove("Burger")

#Delete a specific index from a list
list_2.pop(0)
#or
del list_2[0]

#Change an element of a list
list_2[1]="HotDog"

#Print a list in reverese
list_2.sort(reverse=True)

