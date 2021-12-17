#Put these lines in a file called info
#1991 Eelta word
#1990 Alpha word
#1994 Cword word
#1993 Dword word
#1992 Fifth word

########################
#1st method using a list
list_1=[]
file_o=open("info", "r")
for items in file_o:
    list_1.append(items)

list_1.sort()
for items in list_1:
    print(items)

###############################
#2nd method u sing a while loop
with open("info", "r") as r:
    for line in sorted(r):
        print(line)

