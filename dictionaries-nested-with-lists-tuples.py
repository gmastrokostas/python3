#######################################################
#Manipulating Nested Dictionaries.
#Following is a dictionary that contains
#as its first value a dictionary
#as its second value a list
#and the list is tuple
import netifaces
gateways=netifaces.gateways()
#{'default': {2: ('192.168.1.1', 'bridge0')}, 2: [('192.168.1.1', 'bridge0', True)]}
#Example-1
#To print the first key called "default"
print(gateways['default']
#{2: ('192.168.1.1', 'bridge0')}

#To print the first key of the nested dictionary
print(gateways['default'][2])
#('192.168.1.1', 'bridge0')

#To print any of the values with in the tuple
print(gateways['default'][2][0])
#192.168.1.1
#Example-2
#To print the second key called "2" and to also drill down to the list and tuple
print(gateways[2][0][1])

