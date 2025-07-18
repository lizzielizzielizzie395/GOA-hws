#1 - We learned comparison operations.We use them to compare different data types and, in general,
# it makes machines evaluate different scenarios and make decisions. These are: > , < and ==.

#2 
previous_income = int(input("How much money did you use to make yearly before?: "))
yearly_income = int(input("How much money do you make yearly now?: "))
print(previous_income > yearly_income)
print(previous_income < yearly_income)
print(previous_income == yearly_income)

#3
Name_1 = input("Whats your first name? ")
Name_2 = input("Whats your last name?: ")
age = input("How old are you?: ")
height = input("How tall are you?: ")
color = input("What's your favorite color?: ")
print(Name_1 + " " + Name_2 + " " + age + " " + height + " " + color)

#4
num_1 = int(input("How many bottles of orange juice have you drunk this week?: "))
num_2 = int(input("How many cups of coffee have you drunk this week?: "))
num_3 = int(input("How many cups of tea have you drunk this week?: "))
num_4 = int(input("How many bottles of water have you drunk this week?: "))
sum = num_1 + num_2 + num_3 + num_4
print( sum / 4 )

#5
first_name = "Lizi" 
Num_1 = 100
temperature = 35.7
NikolaTesla_isCOOL = True 
print(type(first_name))
print(type(Num_1))
print(type(temperature))
print(type(NikolaTesla_isCOOL))

#6 
Fav_scientist = "Nikola Tesla"
Fav_mathematician = "Carl Gauss"
print(Fav_scientist == Fav_mathematician)

#7
Num_2 = int("40")
Num_3 = int("50")
Num_4 = int("60")
Num_5 = int("70")
sum = Num_2 + Num_3 + Num_4 + Num_5
print(sum)

#8
Num_6 = str(30)
Num_7 = str(40)
Num_8 = str(50)
Concatination = Num_6 + Num_7 + Num_8
print(Concatination)