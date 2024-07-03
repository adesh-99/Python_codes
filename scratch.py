# Creating List
my_list = ["January","February","March","April","May","June","July","August","September","October","November","December"]

# print list
for i in my_list:
    print(i)

'''print("###################")
my_upper = [x.upper() for x in my_list]
print(my_upper)'''

# Print month string greater than length 5
big_m = [month for month in my_list if len(month)>5]
print(big_m)


# Creating Dictionary
my_dic = {
    "Adesh": "Jadhav",
    "Suraj": "Chothe",
    "Prashant": "Hinge",
    "Sumit": "Dhivar"
}

# Accessing Dictionary
print(my_dic["Adesh"])

# Add Element
my_dic["Kaushal"] = "Gawali"


# Modify Element
my_dic["Hello"] = "World"
print(my_dic)


'''from collections import namedtuple

dob = namedtuple("FirstName","LastName","Dob")
print(dob)'''
