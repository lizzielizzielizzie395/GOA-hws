#1
print(20>30 and 30 == 30)
print(40>50 or 60>90)
print(50==60 and 40>30)
print(40>70 and 70>80)
print(30==30 and 50>60)

print(40==40 and 50>40)
print(80<90 or 50==60)
print(50==50 or 60==67)
print(34>36 or 50==50)
print(45>40 and 51>50)

#2 - sequencing - the computer runs your code in order, from top to bottom. 
#    iteration - executing an instruction repeatedly.
#    selection - specifies when to follow each path,when the computer selects
    
#3 - the step-by-step instructions in a cooking recipe is an example of sequencing

#4 - A for loop is used to execute the same instruction over and over again, a specific number of times.

#5 range() gets a certain amount of numbers in the parenthesis and
# after indentation, which is followed by print(), terminal will show us 
# the data type printed the exact amount of times that range() function has.

#6
for car in range(10):
    print("Lexus GX 460")

#7
for i in range(100):
    print("Gugunishvili")

#8
for i in range(46):
    print("pink")

#9
for i in range(32):
    print("L")

#10
first_name = input("Whats your first name?: ")
last_name = input("Whats your last name?: ")
color = input("Whats your favorite color?: ")
age = int(input("How old are you?: "))
concatenation = first_name+last_name+color+str(age) 
print(concatenation)

#11
name = "Lizi Gugunishvili"
average_score = 89
temperature = 36.7
Its_sunny = True 
print(type(name))
print(type(average_score))
print(type(temperature))
print(type(Its_sunny))

#12
Age = int(input("How old are you?: "))
water = int(input("How many bottles of water have you drunk today?: "))
coffee = int(input("How many cups of coffee have you drunk this week?: "))
tea = int(input("How many cups of tea have you drunk this week?: "))
sum = Age + water + coffee + tea
print(sum)