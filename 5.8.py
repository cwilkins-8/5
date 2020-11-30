#5.8 Hello Admin

#usernames = ['admin', 'manager', 'employee1', 'employe2', 'employe3']

#for username in usernames:
    #if username == 'admin':
        #print("Hello admin, would you like to see a status report?")
    #else:
       #print("Hello user, thank you for logging in again.")
usernames = []
if usernames:
    for username in usernames:
        print("Hello users" + username)
else:
        print("We need to find some users!")
        
current_users = ['admin', 'manager', 'employee1', 'employe2', 'employe3']

new_users = ['employe2', 'employe3' 'employe6', 'employe7' 'employe8']

for current_user in current_users:
    if current_user in new_users:
        print("Please enter a new username")
    else:
        print("This username is avaible")

#5.11 Ordinal numbers

numbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']
print(numbers)

number = [1.9]
print(number)
