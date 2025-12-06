print("             REGISTRATION FORM            ")
print()
print()


final_list = []

no_of_entries = int(input("Number of people allowed to register :  "))
print(f"Only {no_of_entries} people are allowed to register.")
print()
print()


for i in range(no_of_entries):
  print(f" Seats Left: {no_of_entries}.")
  print()
  
  user_name = input("Please Enter Your Name: "  )
  user_phone_number =int(input("Please Enter Your Number: "))
  
  input_collection = { user_name:user_phone_number }
  
  final_list.append (input_collection)
  
  no_of_entries -= 1
  print("Registered Successfully!")
  print(input_collection)
  print()

print("\n Guest List: \n")
print(f"{'Name':20} {'Phone':15}")
print("-" * 35)

for entry in final_list:
  for name,phone in entry.items():
    print(f"{name:20} {phone:15}")





