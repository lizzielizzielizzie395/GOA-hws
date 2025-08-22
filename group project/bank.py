#ბანკში შესვლა
while True:
    print("Welcome to GoaCash!💚")
    users_choice = input("Have you used our bank before? (yes/no): ")
    if users_choice == 'yes':
        Pin = 1234

    else:
        Pin = int(input("Create your pin code(4 digits. only use numbers): "))
        print("Your pin code has been created successfully.")

    tries = 3
    while tries > 0:
        Pin1= int(input("Enter your PIN: "))
        if Pin1 == Pin:
            break
        else:
            tries = tries - 1
            print("Pin code incorrect. "+ str(tries) + " " + "tries left.")
        print( "Access denied. Please try again later.")
        print("--------------------------------------")
    print("")
    break


#account
print("----------✨Your account✨----------")
print("1- login")
print("2- registration")
choice_1=int(input("Choose: "))
print("--------------------------------------")
password="GOA"
password_2 = ""
default_password=""

if choice_1==1:
    user_name_1=input("Enter your username: ")
    while True:
        default_password="GOA"
        default_password_1=input("Enter your password: ")
        if default_password_1==default_password:
            print("Welcome!")
            print("")
            break
        else:
            print("password is incorrect")
            print("")

elif choice_1==2:
    input("Press Enter to start registration:")
    print("")
    print("--------🧾Registration Form🧾------")

#მომხმარებლის მონაცემების შეყვანა
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    user_id = input("Enter your ID: ")
    user_name=input("enter your username: ")
    #პაროლის შემოწმება while ციკლით
    while True:
        password = input("create your password: ")
        confirm_password = input("Repeat password: ")

    #თუ პაროლები ემთხვევა ციკლი შეწყდება
        if password == confirm_password:
            print("Password saved successfully!")
            break  
        else:
            print("Passwords do not match, try again.")

    while True:
        print("")
        print("--------🔑Login🔑--------")
        print("")
        user_name_2=input("enter your username: ")
        password_2=input("enter your password: ")
        if user_name_2=="" or password_2=="":
            print("input fields should not be empty")
        elif user_name_2!=user_name or password_2!=password:
            print("try again")
        else:
            #სტატუსის არჩევა
            print("Choose your status:")
            print("1 - Pupil")
            print("2 - Student")
            choice = int(input("Enter number: "))
            #სტატუსის შენახვა
            if choice == 1:
                status = "Pupil"
            else:
                status = "Student"
                break
            

            #რეგისტრაციის შედეგების ჩვენება
            print(" Registration completed!")
            print("---------------------------")
            print("First Name:", first_name)
            print("Last Name:", last_name)
            print("ID:", user_id)
            print("Status:", status)
            print("---------------------------")

            #პროგრამის დასასრული
            print(first_name ,"Thank you for using GOA Bank!")
            print("")

# ბალანსის შევსება:
print("--------------------------------------")
print("Would you like to fill your balance?")
print("Choose: yes/no ")
choice_6=input("enter your answer: ")

if choice_6=="yes":
    balance = float(input("enter your balance (₾): " )) #ბალანსი ლარებში
    print("you have succesfully updated your balance.")
else:
    balance = 0
    print("your balance has not been updated.")

print("--------------------------------------")
print("would you like to fill your Aura balance?") #ბალანსი აურებში/მასწავლებლის ველი
print("choose: yes/no")
choice_7=input("enter your answer: ")

if choice_7=="yes":
    A_balance=int(input("enter your Aura balance: "))
    print("Your aura balance has been updated: ", A_balance)
else:
    A_balance = 0
    print("Your aura balance has not been updated.")
print("")

#მთავარი menu
while True:
    print("----------💚Main Menu💚----------")
    print("0. view information")
    print("1. pay the tuition fee")
    print("2. send money to another student")
    print("3. view exchange menu")
    print("4. view balance")
    print("5. card ")
    print("6. settings")
    print("7. exit")

    choice = int(input("choose an action (0-7): "))

    #ინფორმაცია
    if choice == 0:
        print("")
        print("  ---------💚GoaCash💚--------")
        print("🏦GoaCash is the mobile app designed to put the power of banking at your fingertips."
        "Our app provides a secure and straightforward way to manage your cash and AURAS in one place.🤑")
        print("")
        print("---What are auras?---")
        print("Aura is a special GoaCash currency, which helps you to make money.💵")
        print("")
        print("---Why choose GoaCash?---")
        print("✅Instant account access: quick registration, check your balance and view transactions anywhere anytime!")
        print("")
        print("💵Quick transactions : easily convert AURA😎 to ₾")
        print("")
        print("💚Fast and easy transfers: Send money or AURAS to your fellow GOA academy friends, pupils and students!")
        print("")
        print("💰Get discounts and daily notifications about your finances!")
        print("")
        print("👾seamlessly and easily view your transaction history.")
        print("")
        print("---Why are GoaCash verification cards compulsory?---")
        print("At hackathons, participants are required to carry a special verification card that serves as proof of registration")
        print("and eligibility to enter the event.💻👩‍💻")
        print("These cards are typically issued after the participant has successfully checked in with their registration details.")
        print("")
        print("Generally, without discounts, when exchanging GEL to Aura,  you should know that: ")                                     
        print("if you exchange more than 1000 GEL, you get additional 200 Aura")                                                                     
        print("If you exchange more than 500 but less than 1000 GEL, you get additional 100 Aura")                                             
        print("if you exchange more than 200 but less than 500 GEL, you get bonus 50 Auras.")
        print("")
        print("--------💚💚💚--------")
        print("🗿Never forget! You are a GIGA CHAD, so use GoaCash to simplify your financial life and take control of your money")
        print("and AURAS like never before🧠.")
        print("")

    #გადასახადის გადახდა
    elif choice == 1:
        print("")
        print("  ---------💸Tuition fee payment💸--------")
        fee = float(input("enter the amount (₾): "))
        if fee <= balance:
            print("payment succesfull.")
            print("Enter to view transaction history")
            input("")
            balance -= fee
            print("You have paid tuition fee of "+ str(fee) +" and right now your balance is " + str(balance))
            print("")
        else:print("payment unsuccesful.")

    elif choice == 2: # ფულის გაგზავნა სხვა სტუდენტისთვის
        print("")
        print("  ---------💰Money transfer💰--------")
        sending = float(input("enter the amount: "))
        if sending <= balance:
            NAME = input("enter the user: ")
            print("Transfer succesful.")
            print("Enter to view transaction history")
            input("")
            print("You have sent money to "+ NAME)
            print("")
            balance -= sending
        else:
            print("Transfer unsuccessful.")
            print("")

    elif choice == 3: #ვალუტის შეცვლა და შეთავაზებების ნახვა
        import datetime
        disc = 0
        
        while True:
            print("") 
            print("------------✨Exchange Menu✨-----------")
            print("1. View special discounts ")
            print("2. Exchange Auras into Gel.")
            print("3. Exit.")
            Choice = int(input("Choose an action (1-3): "))

            #შეთავაზებები
            if Choice == 1:
                print("")
                print("----------💸Special   discounts💸----------")
                print("")
                print("1.THIS MONTH! Every Tuesday and Saturday, earn +15% extra AURAS on all exchanges.")
                print("--------------------------------")
                print("")
                print("2. NEW SALE ONLY IN SUMMER! Earn +20% more AURAS on Wednesday when you exchange.")
                print("--------------------------------")
                print("")
                print("3.On Saturdays and Sundays, most active users are granted priority processing for transactions, ensuring faster and")
                print("smoother service.")
                print("--------------------------------")
                print("")
                
                week = datetime.date.today().weekday() #შეთავაზებები დანიშნულ დროზე მუშაობს.

                choice1= int(input("Which one would you like to choose? (1-3): "))

                if choice1 == 1:
                    if week == 1 or week == 5 :  #სამშაბათი და შაბათი
                        disc = 0.15
                        print("")
                        print("Discount claimed successfully.💚")
                    else:
                        print("")
                        print("Discount currently unavailable, please try again later.")

                elif choice1 == 2: 
                    if week == 2:   #ოთხშაბათი
                        disc = 0.2
                        print("")
                        print("Discount claimed successfully💚")
                    else:
                        print("")
                        print("Discount currently unavailable, please try again later.")

                else:
                    print("")
                    print("Priority access claimed.💚")
                    print("")
                print("Thank you for using our services.")

            # აურებიდან ლარებში გადაცვლა
            elif Choice == 2:
                print("")
                print("Your balance is ",A_balance," Auras.")
                Auras= int(input("Enter how many Auras you want to exchange in GEL:"))
                Auras_1 = Auras * disc
                
                if A_balance >= Auras:
                    if Auras >= 1000:
                        exchanged = Auras / 10 + 20  
                    elif Auras >= 500:
                        exchanged = Auras / 10 + 10
                    elif Auras >= 200:
                        exchanged = Auras / 10 + 5
                    elif Auras >= 100 and Auras > 0:
                        exchanged = Auras / 10
                    else:
                        print('Not enough Aura balance.')

                    A_balance = A_balance - Auras + Auras_1
                    balance += exchanged 

                    
                    print("Balance after transaction: " + str(A_balance)+" Auras")
                    print("You received: " + str(exchanged) + " GEL")
                    print("")
                    print("The transaction is completed ")
                    print("Enter to view transaction history")
                    input("")
                    print("You succesfully exchanged "+ str(Auras) + " Auras into " + str(exchanged) +" GEL")
                else:
                    print("The transaction could not be completed ")
                print("")

            elif Choice ==3:
                print("Thank you for using our services.💚")
                print("")
                break
            else:
                print("Invalid choice. Please try again.")
                print("")

    #ბალანსის ნახვა
    elif choice == 4:
        print("")
        print("----------🏦Your balance🏦----------")
        print("your balance is " + str(balance)+" GEL")
        print("your Aura balance is " + str(A_balance) + " Auras")
        print("")
    #ბარათი
    elif choice==5:
        while True:
            print("")
            print("----------💳Your card💳----------")
            print("Choose: ")
            print("A. i want to make my card")
            print("B. i already have a card")
            print("C. i want to upgrade my card")
            print("D. Exit")
            sub_choice=(input("enter your choice: "))

            if sub_choice=="A":
                name_1=input("enter your name: ")
                surname_1=input("enter your surname: ")
                ID_1=int(input("enter your ID: "))
                age=int(input("enter your age: "))
                date=input("enter the creation date: ")
                while True:
                    passcode=int(input("enter 4 digit passcode: "))
                    repeat_passcode=int(input("repeat your passcode: "))   
                    if passcode==repeat_passcode:
                        robot=input("are you a robot? click enter to verify: ")
                        print("you have succesfuly created your card. claim the physical copy at principal's office.")
                        print("")
                        break
                    else:
                        print("try again")
            elif sub_choice=="B":
                while True:
                    default_passcode = 1234
                    passc= int(input("enter your 4 digit passcode: ")) 
                    if passc == default_passcode:
                        print("✔️")
                        user_issue = input("are you having any issues with your card? (yes/no): ")
                        if user_issue == 'yes':
                            input("tell us about the issue: ")
                            print("Thank you! You will receive feedback once we review your complaint.")
                        else:
                            print("Thank you for using our services.")
                            print("")
                        break
                    else:
                        print("try again.")
                
            elif sub_choice=="C":
                print("")
                print("upgrading started.")
                print("it may take a few days, you will get the digital version but if you want to")
                print("claim a physical copy, visit the principal's office.")

            elif sub_choice=="D":
                print("")
                print("Thank you for using our services.")
                break
            else:
                print("invalid choice. try again.")  

    # სეთინგები
    elif choice==6:
        while True:
            print("")
            print("----------🤍Settings🤍----------")
            print("Please choose: ")
            print("a. terms and conditions.")
            print("b. privacy")
            print("c. exit")

            sub_choice_1=input("enter your choice: ")
            if sub_choice_1=="a":
                print("")
                print("---------📜Terms & Conditions📜----------")
                print("1)By creating an account and using this application, you agree to comply with these Terms and Conditions. The app is intended solely for personal banking, payments, and related services.")
                print("")
                print("2)You are responsible for keeping your login credentials and PIN secure. The bank is not liable for losses arising from unauthorized access due to negligence in safeguarding your account.")
                print("")
                print("3)All payments and transfers made through the app are processed according to current banking policies. Once confirmed, transactions cannot be reversed")
                print("")
                print("4)service charges, discounts, or reward programs (including AURAS and cashback) may be subject to change.")
                print("")
                print("5)Your personal data will be collected and processed in accordance with the official Privacy Policy to ensure the security and efficiency of banking services.")
                print("---------------------------------------------------------------------")
                print("     Please review our Terms and Conditions before continuing.")
                print("By selecting “I agree”, you confirm that you have read, understood, and accepted the Terms and Conditions.")
                print("If you select “i disagree”, you will not be able to proceed with the use of this application.")
                print("")
                print("1. i agree.")
                print("2. i disagree.")
                choice2 = int(input("Please choose (1-2): "))
                if choice2== 1:
                    print("Thank you for accepting the Terms and Conditions. You may now proceed to use GoaCash.")
                else:
                    print("Access to GoaCash will be restricted until you agree to the terms.")
            elif sub_choice_1=="b":
                while True:
                    print("----------🔏Privacy🔏----------")
                    print("")
                    password_11= input("enter your password to access: ")
                    if password_11 == password_2 or password_11 == default_password or password_11 == password:
                        print("access granted!")
                        input("Press enter to proceed.")
                        print("--------------------------")
                        print("P. change my password")
                        print("C. change the card passcode")
                        print("B. change the bank passcode")
                        choice_0=input("what would you like to do?: ")
                        if choice_0=="P":
                            password=input("enter your new password: ")
                            password_2 = password   
                            default_password = password
                            print("you have succesfuly changed your password to:", password)
                        elif choice_0=="C":
                            new_passcode_card = ""
                            new_passcode_card=input("enter your new passcode: ")
                            print("you have succesfuly changed your passcode to:", new_passcode_card)
                        elif choice_0=="B":
                            new_passcode_bank=input("enter your new passcode: ")
                            print("")
                            print("you have succesfuly changed your passcode.")
                        break
            elif sub_choice_1=="c":
                print("")
                print("Thank you for using our services.")
                break                    
            else:
                print("Please try again later.")

    #გამოსვლა
    elif choice == 7:
        print("")
        print("---------⭐Rate Your Experience ⭐----------")
        print("We hope you’re enjoying 💚GoaCash💚!") 
        print("Your feedback helps us improve and provide you with the best possible service.")
        choice_8 = input("Would you like to review GoaCash?(yes/no): ")
        if choice_8 == "yes":
            print("")
            print("1. ⭐️⭐️⭐️⭐️⭐️")
            print("2. ⭐️⭐️⭐️⭐️")
            print("3. ⭐️⭐️⭐️")
            print("4. ⭐️⭐️")
            print("5. ⭐️")
            choice_9 = input("Choose your action (1-5): ")
            print("We appreciate your feedback!")
            print("Thank you for using 💚GoaCash💚. BYE BYE! 📌 ")
        else:
            print("Thank you for using 💚GoaCash💚. BYE BYE! 📌 ")
        break