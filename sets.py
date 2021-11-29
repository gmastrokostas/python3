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


