print("\nWELCOME TO PYTHON!\n")
print("Create a new account")
Acc_User_Name = input("Input new user name:\n")
Acc_Pass = input("Input new secure password:\n")

attempt_count = 0
attempt_limit = 3
User_Name_Guess = ""
Pass_Guess = ""
out_of_attempts = False 

while not(out_of_attempts):
    while User_Name_Guess != Acc_User_Name and Pass_Guess != Acc_Pass:
        if attempt_count < attempt_limit:
            print("\nAccount log in\n")
            Acc_Guess = input("Enter User Name:\n")
            Pass_Guess = input("Enter The Password:\n")
            attempt_count += 1
        else:
            out_of_attempts = True
            break
    break

if out_of_attempts:
    print("ACCESS DENIED!")
else:
    print("ACCESS GRANTED!")
    



