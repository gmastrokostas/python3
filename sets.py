#Demonstrating a Union

print("Demonstrating a Union")
set_1={'Zero', 'One', 'Two', 'Three', 'Four'}
set_2={'Five', 'Six', 'Seven', 'Eight', 'Nine'}
print(set_1.union(set_2))

print()

#Demonstrating an Interserction
print("Demonstrating an Interserction")
set_3={'Zero', 'One', 'Two', 'Three', 'Four', 'Five'}
set_4={'Five', 'Six', 'Seven', 'Eight', 'Nine'}
print(set_3.intersection(set_4))

print()

#Demonstrating a Difference
print("Demonstrating a Difference")
set_5={'Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Cat'}
set_6={'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Dog'}
print(set_5.difference(set_6))
print(set_6.difference(set_5))

print()

#Demonstrating a Symmetric Difference
print("Demonstrating a Symmetric Difference")
set_7={'Zero', 'One', 'Two', 'Dog'}
set_8={'Zero', 'One', 'Two', 'Cat'}
print(set_7.symmetric_difference(set_8))


#Below is output examples
Demonstrating a Union
{'Four', 'Nine', 'Two', 'Zero', 'Five', 'Three', 'Eight', 'Seven', 'Six', 'One'}

Demonstrating an Interserction
{'Five'}

Demonstrating a Difference
{'Four', 'Cat', 'Zero', 'Two', 'Three', 'One'}
{'Nine', 'Dog', 'Seven', 'Eight', 'Six'}

Demonstrating a Symmetric Difference
{'Cat', 'Dog'}

#####################################################################
Various Set examples

Remove duplicates from a list using a set
list_1=['One', 'Two', 'One']
list_1=list(set(list_1))
print(list_1)


Remove and add value from a set
set_1={'One', 'Two', 'Three'}
set_1.discard('One')
set_1.add('One')

Sort the values in a set
set_1={'A', 'B', 'C', 'D', 'E', 'F', 'G'}
print(sorted(set_1))





