# 1) მომხმარებელს შემოაყვანიეთ რაიმე რიცხვი(მთელი/ათწილადი); შეამოწმეთ ეს რიცხვი - 
# --> თუ დადებითია დაპრინტეთ 'ეს რიცხვი დადებითი რიცხვია'
# --> თუ უარყოფითია დაპრინტეთ 'ეს რიცხვი უარყოფითი რიცხვია'
# --> თუ ნულია დაპრინტეთ 'ეს რიცხვი ნულია'

num = float(input("Enter a number: "))
if num > 0:
    print("This is a positive number")
elif num < 0:
    print("This is a negative number")
else:
    print("This number is zero.")

# 2)მომხმარებელს შემოაყვანიეთ თავისი ასაკი:
# 0–12 წლის ასაკი --> დაპრინტეთ 'ბავშვი ხარ'
# 13-19 წლის ასაკი --> დაპრინტეთ 'მოზარდი/თინეიჯერი ხარ'
# 20-64 წლის ასაკი --> დაპრინტეთ 'ზრდასრული ხართ'
# 65-120 წლის ასაკი --> დაპრინტეთ 'ხანში შესული ხართ'
# 120 და ზემოთ --> დაპრინტეთ 'გურუ ან ჯადოქარი'
# თუ შემოყვანილი ასაკი უარყოფითია --> დაპრინტეთ 'არასწორი ინფო'

num_1 = int(input("How old are you?: "))
if 0<num_1<12:
    print("You are a child")
elif 13<num_1<19:
    print("You are a teenager.")
elif 20<num_1<64:
    print("You are an adult.")
elif 65<num_1<120:
    print("You are old lmao.")
elif num_1<0:
    print("Incorrect info.")
else:
    print("You are a witch or a guru lmao.")

#3)დაწერეთ "password guesser" პროგრამა, შექმენით რაიმე ცვლადი და მასში შეინახეთ ის პაროლი რომელსაც ყველგან იყენებთ ;)
# მომხმარებელს მოთხოვეთ გამოიცნოს თქვენი პაროლი
# აღნიშნეთ ცდების რაოდენობა
# გამოიყენეთ while loop, მანამ ატრიალეთ სანამ მომხმარებელი პაროლს არ გამოიცნობს ან დაწერს --> 'nah strong password'
# ბოლოს აჩვენეთ(დაუპრინტეთ) რამდენი ცდა დაჭირდა პაროლის გამოსაცნობად

password = input("guess my password:")
pass_1 = "liziko98"
guess = 0

while password != pass_1 or password != "nah strong password":
    guess = guess+ 1

    if password == pass_1 or password=="nah strong password":
        print("Correct! You took", guess," guesses in total.")
        break
    else:
        password = input("guess my password:")



#4) მომხმარებელს შემოატანიეთ სამი რიცხვი(მთელი/ათწილადი) და ამ სამი რიცხვთაგან დაბეჭდეთ უდიდესი

Num = float(input("Enter your first number: "))
Num_1 = float(input("Enter your second number: "))
Num_2 = float(input("Enter your third number: "))

if Num<Num_1<Num_2:
    print("The biggest number is ", Num_2)
elif Num<Num_2<Num_1:
    print("The biggest number is ", Num_1)
elif Num_1<Num_2<Num:
    print("The biggest number is ", Num)
else:
    print("Please try again.")

# 5) შემოატანიეთ მომხმარებელს რიცხვი 1-დან 7-ჩათვლით
# თუ 1 --> დაპრინტეთ 'ორშაბათი'
# თუ 2 --> დაპრინტეთ 'სამშაბათი'
# თუ 3 --> დაპრინტეთ 'ოთხშაბათი'
# თუ 4 --> დაპრინტეთ 'ხუთშაბათი'
# თუ 5 --> დაპრინტეთ 'პარასკევი' 
# თუ 6 --> დაპრინტეთ 'შაბათი'
# თუ 7 --> დაპრინტეთ 'კვირა' 
# სხვა დანარჩენი --> 'არ ვიცი ეგ რა დღეა

day_1 = int(input("Enter your first number(1-7): "))
day_2 = int(input("Enter your second number(1-7): "))
day_3 = int(input("Enter your third number(1-7): "))
day_4 = int(input("Enter your fourth number(1-7): "))
day_5 = int(input("Enter your fifth number(1-7): "))
day_6 = int(input("Enter your sixth number(1-7): "))
day_7 = int(input("Enter your seventh number(1-7): "))

if day_1 == 1:
    print("Its monday.")
elif day_2 == 2:
    print("Its tuesday.")
elif day_3 == 3:
    print("Its wednesday.")
elif day_4 == 4:
    print("Its thursday.")
elif day_5 == 5:
    print("Its friday.")
elif day_6 == 6:
    print("Its saturday.")
elif day_7 == 7:
    print("Its sunday.")
else:
    print("Idk whats that day dawg.")




