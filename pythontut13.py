# VIDEO 13 : Dictionaries

# While lists organize data based on sequential indexes Dictionaries instead use key / value pairs
# A key / value pair could be fName : "Derek" where fName is the key and "Derek" is the value
# Here is some code to help this make sense

# Create a Dictionary about me
swe_dict = {"f_name": "Swetha", "l_name": "Manikandan", "address": "123 Main St"}

# Get a value with the ke
print("May name :", swe_dict["f_name"])

# Change a value with the key
swe_dict["address"] = "215 North St"

# Dictionaries may not print out in the order created
# since they are unordered
print(swe_dict)

# Add a new key value
swe_dict['city'] = 'Pittsburgh'

# Check if a key exists
print("Is there a city :", "city" in swe_dict)

# Get the list of values
print(swe_dict.values())

# Get the list of keys
print(swe_dict.keys())

# Get the key and value with items()
for k, v in swe_dict.items():
    print(k, v)

# Get gets a value associated with a key or the default
print(swe_dict.get("m_name", "Not Here"))

# Delete a key value
del swe_dict["f_name"]

# Loop through the dictionary keys
for i in swe_dict:
    print(i)

# Delete all entries
swe_dict.clear()

# List for holding Dictionaries
employees = []

# Input employee data
f_name, l_name = input("Enter Employee Name : ").split()

employees.append({'f_name': f_name, 'l_name': l_name})

print(employees)

'''
Python Problem for you to Solve

Create an array of customer dictionaries and the output should look like this : 

Enter Customer (Yes/No) : y
Enter Customer Name : Derek Banas
Enter Customer (Yes/No) : y
Enter Customer Name : Sally Smith
Enter Customer (Yes/No) : n
Derek Banas
Sally Smith
'''

# Create customer array outside the for so it isn't local
# to the while loop
customers = []

while True:
    # Cut off the 1st letter to cover if the user
    # types a n or y
    create_entry = input("Enter Customer (Yes/No) : ")
    create_entry = create_entry[0].lower()

    if create_entry == "n":

        # Leave the while loop when n is entered
        break
    else:
        # Get the customer name by splitting at the space
        f_name, l_name = input("Enter Customer Name : ").split()

        # Add the dictionary to the array
        customers.append({'f_name': f_name, 'l_name': l_name})

# Print out customer list
for cust in customers:
    print(cust['f_name'], cust['l_name'])















