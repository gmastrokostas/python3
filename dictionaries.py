#What is the difference between an update method and a just replacing a value from a dictionary.

#What is the difference between removing a dictionary item like this:   dictionary.pop("item_1")  vs del.dictionary["item_1"]



dictionary = {
        "item_1"  : "ferrari",
        "facts"  : True,
        "list_1" : ["one", "two", "three"],
        "set_1"  : {"set1", "set2", "set3"}
        }
#Add a new item in a dictionary
dictionary["item_2"]="ford"
print(dictionary)

#Change an existing value of an item
dictionary["item_1"]="new_value"

#Print an element of a list within a dictionary
print(dictionary["list_1"][0:2])
