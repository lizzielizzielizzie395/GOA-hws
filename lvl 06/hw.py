#1 
age = int(input("How old are you?: "))
height = int(input("How tall are you?: "))
print(age>height)
print(age<height)
print(age==height)

#2
num_1 = int("10")
num_2 = int("20")
num_3 = int("30")
num_4 = 40
num_5 = 50
multiplication = num_1*num_2*num_3*num_4*num_5
print(multiplication)
print(multiplication/5)

#3
first_name = input("What's your first name?: ")
last_name = input("What's your last name?: ")
color = input("Whats your favorite color?: ")
Num = int(input("Whats the first number that comes to your mind?: "))
concatination = first_name + last_name + color
print(concatination*Num)

#4 --- ჩვენ ვისწავლეთ "and" და  "or" ლოგიკური ოპერატორები. "and" უპირატესობას ანიჭებს False-ს, თუ მოცემული პირობებიდან 
# ერთ-ერთი მაინც არ არის სწორი/შესრულებული. "or" კი უპირატესობას ანიჭებს True-ს, თუ მოცემული პირობებიდან ერთ-ერთი მაინც
# არის სწორი/შესრულებული

#5       (and)                             (or)
# True and True -- True      |   True or True -- True           
# True and False -- False    |   True or False -- True
# False and True -- False    |   False or True -- True
# False and False --False    |   False or False -- False 

#6
scenario_1 = True
scenario_2 = False
scenario_3 = True
scenario_4 = False 
print(scenario_1 or scenario_2)
print(scenario_3 and scenario_4)
print(scenario_2 or scenario_4)
print(scenario_1 and scenario_3)

#7
Name = "Lizi"
score = 100
temperature = 34.5
situation_1 = True 
print(type(Name))
print(type(score))
print(type(temperature))
print(type(situation_1))

#8
print(input("Whats your name?: "))
print(int(input("How many bottles of water have u drunk today?: ")))
print(float(input("What's the temperature outside?: ")))
