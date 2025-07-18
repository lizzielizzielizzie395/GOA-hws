#1 - sololearn lessons till "Data conversion"

#2 input - any info that goes into a computer. for ex: the click of a button, speaking with sb on a call, bar code reader and etc. 
#  output is a way for the computer to communicate with the outside world. for ex:a message displayed on the screen, the sound from a speaker, a document coming out from a printer and etc.

#3
Height = input("Whats your height?: ")
print(Height)
print(type(Height))

#4
Name = "Mari"  #class str.
num_1 = 20     #class int.
temperature = 36.6   #class float
num_2 = 43.5    #class float
age = 100       #class int.


#5
name = "Lizi"
acc_balance = 200.56
height = 166
print(type(name))
print(type(acc_balance))
print(type(height))

#6
first_name = input("Whats your first name?; ")
last_name = input("Whats your last name?; ")
full_name = first_name + " " + last_name
print(full_name)

#7
Age = int(input("Whats your age?: "))
Height_1 = int(input("Whats your height?: "))
num_1 = int(input("Whats your favorite number?: "))
Date = int(input("What year were you born?: "))
num_2 = int(input("How much money do you have?: "))
sum = Age + Height_1 + num_1 + Date + num_2 
print(sum / 5)

#8
name_1 = input("Whats your first name?: ")
name_2 = input("Whats your last name?: ")
age_1 = input("Whats your age?: ")
height_2 = input("Whats your height?: ")
weight = input("Whats your weight?: ") 
full_name = name_1 + " " + name_2 
print("Your full name is " + full_name + ", " + "your age is " + age_1 + ", " + "your height and weight is "+ height_2 + "cm and " + weight + "kg.")