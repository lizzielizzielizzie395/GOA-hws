# 1)კომენტარის სახით ახსენით თუ რა არის index და რაში ვიყენებთ მას

#index is the location of an element in a certain list. we use them to determine the location of the element and take out, change its value , put it in an another list and etc.



# 2)შექმენით ცვლადი სადაც შეინახავთ ამ სიას [4,6,1,5,9,8,4] ,თქვენი დავალებაა რომ მიწვდეთ ამ სიაში ელემენტებს ინდექსინგის გამოყენებით ,შეკრიბეთ ორი რიცხვი რომ მიიღთ შემდეგი რიცხვები --> 10 , 2 , 14 , 20 , 4 , 7 , 27 , გამოიყენეთ მათემატიკური ოპერატოები

num=[4,6,1,5,9,8,4]
print(num[0]+num[1])
print(num[2]*2)
print(num[3]+num[4])
print(num[3]*num[0])
print(num[5]-num[0])
print(num[1]+num[2])
print(num[3]*num[0]+num[1]+num[2])

# 3)შექმენით სია სადაც შეიყვანთ ადამიანის სახელებს,უნდა გქონდეთ სულ 10 სახელი,თქვენი დავალებაა რომ გამოიტანოტ ,მე 5 , მე 9 ,მე 3 ,მე 7 და პირველ ინდექსზე მდგომი ელემენტები ცალ ცალკე,გამოიყენეთ ინდექსინგი

names = ["Anna", "David", "Liza", "Mark", "Sophia", 
         "James", "Maria", "Leo", "Nina", "Daniel"]
print(names[1])
print(names[3])
print(names[5])
print(names[7])
print(names[9])


# 4)შექმენით სია სადაც მოათავსებთ სტრინგ ტიპის მონაცემებს,თქვენი დავალებაა გომ for loop და while loop (ორივე) ს დახმარებით გამოიტანოთ თთოეული ელემენტი ცალ ცალკე

fruits = ["Apple", "Banana", "Orange", "Grapes", "Mango"]
i=0

while i<5:
    print(fruits[i])
    i+=1

for i in range(0,5):
    print(fruits[i])


# 5)შექმენით სია სადაც შეინახავთ 7 ცალ ელემენტს(მონაცემის ტიპს არ აქვს მნიშვნელობა),თქვენი დავალებაა რომ ამ სიაში შეცვალოთ მე 3 ინდექსზე დმგომი ელემენტი და ჩაანაცვლო "vashli" ით, ასევე შეცვალე მე 6 ინდექსზე მდგომი ელემენტი და ჩაანაცვლე 'msxali' ით ,ასევე შეცვალე მე 4 ინდექსზე მდგომი ელემენტი და ჩაანაცვლე ის 'atami" ით,გამოიტანე საბოლოო სია ტერმინალში,სადაც ეს სალი ელემენტი იქნება განახლებული

fruits1 = ["Pineapple", "Strawberry", "Watermelon", "Kiwi", "Peach", "Cherry", "Papaya"]

fruits1[3]="vashli"
fruits1[4]="atami"
fruits1[6]="msxali"
print(fruits1)

# 6)იპოვეთ საბოლოო პასუხი--> True and False or False and True or false and false or true ---> true
#                                  false      or     false    or       false      or true


# 7)შექმენით სია სადაც მოთავსებული გექნებათ ცხოველების სახელები, თქვენი დავალებაა რომ -->  თუ ამ სიაში მოთავსებული მე 3 ინდექსზე მდგომი ელემენტი არის ლომი მაშნ დაპრინტე --> "there is lion on index 3" სხვა შემთხვევაში დაუპრინტე რომ --> "there is no lion on index 3"

animals = [
    "Dolphin",
    "Chimpanzee",
    "Elephant",
    "Crow",
]

if animals[3]=="lion":
    print("there is lion on index 3")
else:
    print("there is no lion on index 3")

# 8)
basket = ["ვაშლი", "ბანანი", "საზამთრო", "ატამი", "ყურძენი"]

# დაბეჭდეთ კალათის პირველი ხილი.
print(basket[0])

# დაბეჭდეთ კალათის მესამე ხილი.
print(basket[2])

# შეცვალეთ მეორე ხილი "ბანანი" სხვა ხილით (თქვენი არჩევანით).
basket[1]= "მარწყვი"

# დაბეჭდეთ თავიდან ბოლომდე ყველა ხილი ცალ–ცალკე, ინდექსების გამოყენებით (არა for-ით).
print(basket[0])
print(basket[1])
print(basket[2])
print(basket[3])
print(basket[4])

# 9)
letters = ["ა", "ბ", "გ", "ო", "ლ", "ა", "მ", "ა", "ტ", "ე"]

# დაბეჭდეთ მესამე ასო.
print(letters[2])

# დაბეჭდეთ მე–5 და მე–6 ასო.
print(letters[4])
print(letters[5])

# დაბეჭდეთ ბოლო ასო.
print(letters[9])

# ააწყეთ სიტყვა "მამა" ინდექსებით (ყველა ასო ინდექსით უნდა აიღონ და შეაერთონ).
print(letters[6]+letters[0]+letters[6]+letters[0])

# ააწყეთ სიტყვა "გოლა".
print(letters[2]+letters[3]+letters[4]+letters[5])

# ააწყვეთ სიტყვა "გოგა"
print(letters[2]+letters[3]+letters[2]+letters[0])


# 10)
letters = ["ა", "ბ", "გ", "ო", "ლ", "ა", "მ", "ა", "ტ", "ე"]

# აიღეთ მე–4 ინდექსზე არსებული ასო და შეინახე ცვლადში
letter= letters[4]

if letter=="ლ":      # თუ ეს ასო არის "ლ", დაბეჭდეთ: "სწორია! ასო ლ ა"
    print("სწორია! ასო ლ-ა.")
else:
    print("არასწორია, სცადე თავიდან")   # სხვა შემთხვევაში დაბეჭდეთ: "არასწორია, სცადე თავიდან"

# =========================
# აიღეთ ბოლო ასო და შეინახე ცვლადში

last_letter=letters[9]

if last_letter=="ე":              # თუ ეს "ე"–ა, დაბეჭდეთ "საიდუმლო სიტყვა იწყება სწორად".
    print("საიდუმლო სიტყვა იწყება სწორად")  
else:
    print("საიდუმლო სიტყვა არასწორია")   # სხვა შემთხვევაში – "საიდუმლო სიტყვა არასწორია".

# ==========================

# ააწყვეთ სიტყვა "გელა" და შეინახე ცვლადში 
Name= letters[2]+letters[9]+letters[4]+letters[5]
user_name=input("რა გქვია?(არ დაწერო გელა): ")

if user_name==Name:           # თუ ცვლადში შენახული სიტყვა "გელა"–ს ტოლია, დაბეჭდეთ "გაარტყი სახელი!"
    print("გაარტყი სახელი! რატო დაწერე გელა")
else:
    print("შტერი ხარ!დ")         # სხვა შემთხვევაში – "შტერი ხარ!დ".


# 11)შექმენი სია რომელიც იქნება სტრინგებით სავსე,შენი დავალებაა რომ მომხმარებელს შემოატანინო რაიმე რიცხვი,შენი დავალებაა რომ ამ სიიდან გამოიტანო მომხმარებლის მიერ შემოტანილ რიცხვზე(ინდექსზე) მდგომი ელემენტი

vegetables = ["Carrot", "Broccoli", "Spinach", "Tomato", "Cucumber", "Bell Pepper", "Cauliflower"]

Num = int(input("choose a number(0-6): "))
print(vegetables[Num])