print("                              Login System                     ")
print()
print()
print()
count = 0
while  count <3 :
     user_input = "xyz"
     user_password ="887972"
     username = input("User Name : ")
     password = input("Password: ")
    
     if username == user_input and user_password == password :
                     print("Access Granted")
                     break
     else :
                     print("Try Again ")
                     count += 1
 
if count == 2 :
     print("Number of attempts exhausted")
     break
     

          
