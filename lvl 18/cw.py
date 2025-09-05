# 1) შემოატანინეთ მომხმარებელს 3 რიცხვი, შეამოწმეთ:
# თუ 1 და 2 რიცხვი ტოლია -> დაწერეთ 1 და 2 ტოლია
# თუ 1 და 3 რიცხვი ტოლია -> დაწერეთ 1 და 3 ტოლია
# თუ 2და 3 რიცხვი ტოლია -> დაწერეთ 2და 3 ტოლია
# თუ სამივე ტოლია -> დაწერეთ სამივე ტოლია
# თუ არცერთი არ არის ტოლი -> დაწერეთ არცერთი არ არის ტოლია

num = str(input("Enter your first number: "))
num_1 = str(input("Enter your second number: "))
num_2 = str(input("Enter your third number: "))
if num == num_1:
    print(num, "is equal to ", num_1)
elif num == num_2:
    print(num, "is equal to ", num_2)
elif num_1 == num_2:
    print(num_1, "is equal to ", num_2)
elif num == num_1 == num_2:
    print( num, "" , num_1,"", "and ", num_2, "are all equal." )
else:
    print("None of them are equal.")


# 2) შემოატანინეთ მომხმარებელს რიცხვი 1-დან 12ჩათვლით:
# თუ ეს რიცხვი არის 12, 1, 2 -> დაპრინტეთ ზამთარი
# თუ ეს რიცხვი არის 3, 4, 5 -> დაპრინტეთ გაზაფხული
# თუ ეს რიცხვი არის 6, 7, 8 -> დაპრინტეთ ზაფხული
# თუ ეს რიხცვი არის 9, 10, 11 -> დაპრინტეთ

num_3 = str(input('Enter the current month(1-12): '))
if num_3 == 12 or 1 or 2:
    print("Its winter.")
elif num_3 == 3 or 4 or 5:
    print("Its spring.")
elif num_3 == 6 or 7 or 8:
    print("Its summer.")
else:
    print("Its autumn.")

# 3) შემოატანინეთ მომხმარებელს თავისი სახელი:
# თუ სახელი უდრის admin:
#    მოთხოვეთ შემოიყვანოს ადმინის პაროლი:
#       თუ პაროლი უდრის adminpassword123:
#         დაპრინტეთ სალამი ადმინ
#       სხვა შემთხვევაში:
#         დაპრინტეთ წვდომა არ გაქვს
# სხვა შემთხვევაში:
#   დაპრინტეთ სალამი მომხმარებელო

name = input("Enter your name: ")
if name == "admin":
    password = input("Enter your password: ")
    if password == "adminpassword123":
        print("Hello, admin!")
    else:
        print("password incorrect. please try again later.")
else:
    print("Hello, user!")