# 1)შექმენი სია 7 რიცხვით.
# დაბეჭდე პირველი და ბოლო ელემენტების ნამრავლი ისე, რომ ორივეჯერ უარყოფითი ინდექსი გამოიყენო.

Nums=[1,4,6,7,8,5,4]
print(Nums[0]*Nums[6])
print(Nums[-7]*Nums[-1])

# დაბეჭდე მესამე ელემენტი მარცხნიდან და მესამე ელემენტი მარჯვნიდან (უარყოფითიინდექსის გამოყენებით).
print(Nums[-5])

# 2)შექმენი სია "apple", "banana", "cherry", "grape", "kiwi", "orange".
fruits=["apple", "banana", "cherry", "grape", "kiwi", "orange"]

# დაბეჭდე შუა 2 ელემენტი (ორივე(დადებითი და უარყოფითი)) ინდექსით.
print(fruits[2]," and ", fruits[3])
print(fruits[-4]," and ", fruits[-3])

# 3)
# შექმენი [3,4,5,6,7,1,2,9,8,11]
Nums1=[3,4,5,6,7,1,2,9,8,11]

# მომხმარებელს შემოატანინე ერთი ინდექსი(რიცხვი) 0 დან 10 მდე.   თუ მომხმარებლის ინდექსი დადებითია → დაბეჭდე ის ელემენტი.   თუ უარყოფით რიცხვი ან  10 ზე მეტი მაღალირიცხვი შემოიყვანა დაბეჭდეთ --> "you entered negative or more than 10  number"

user_num= int(input("Enter a number (0-10): "))
if 0<user_num<10:
    print("Your number is", user_num)
else:
    print("you entered negative or number more than 10.")

# 4)შექმენით სია ["dog" ," most" ,"is" ,"angry" ,"running"  , "forest", "fast", "in" , "cat" ,"human", "very"]

list = ["dog" ," most" ,"is" ,"angry" ,"running"  , "forest", "fast", "in" , "cat" ,"human", "very"]

# --- მინუს ინდექსების გამოყენებით შეადგინეთ შემდეგი წინადადება და დაბეჭდეთ --> "dog is running in forest very fast"

print(list[-11],"",list[-9],"",list[-7],"",list[-4],"",list[-6],"",list[-1],"",list[-5])

# --- აასწყვეთ ზემოთ მოცემული წინადადება ოღონდ დადებითი ინდექსებით

print(list[0],"",list[2],"",list[4],"",list[7],"",list[5],"",list[10],"",list[6])

# --- დადებით ინდექსების გამოყენებით ააწყვეთ შემდეგი წინადადება ---> "cat is very angry"

print(list[8],"",list[2],"",list[10],"",list[3])

# 5)
# შექმენი სია ცხოველებით: ["dog", "cat", "horse", "cow", "sheep", "goat"].
# მომხმარებელს შემოიტანინე ინდექსი(რიცხვი).   თუ მომხმარებლის მიერ შემოყვანილ ინდექსზე მდგომი ელემენტი არის  "cat", დაბეჭდე 
# "შენ აირჩიე კატა".  თუ არის "goat", დაბეჭდე "შენ აირჩიე თხა".    სხვა შემთხვევაში დაბეჭდე "სხვა ცხოველი აირჩიე".

animals=["dog", "cat", "horse", "cow", "sheep", "goat"]

user_num1=int(input("Enter a number (0-5): "))
if user_num1==1:
    print("You chose", animals[user_num1])
elif user_num1==5:
    print("You chose", animals[user_num1])
else:
    print("You chose a different animal bruh")



# 6)
# შექმენი სია 6 ქალაქით.
# მომხმარებელი შემოიტანს ორ ინდექსს(რიცხვს). 
# თუ პირველი ინდექსი ნაკლებია მეორეზე → დაბეჭდე ამ ინდექსებზე მდგომი ორივე ელემენტი.
# თუ მეორე ნაკლებია პირველზე → დაბეჭდე "შეცვალე ინდექსები ადგილებით"--->ზემოთ თუ დაპრინტე a და b ამ შემთხვევაში დაპრინტე b და a.
# თუ ინდექსები ერთნაირია → დაბეჭდე "ორივე ერთია" და გამოიტანე ამ ინდექსზე მდგომი ელემენტი. ვთქვათ თუ შემოიყვანა 
# მომხმარებელმა 5 და 5 დაუბეჭდე მე 5 ინდექსზე მდგომი ელემენტი.


cities=["Berlin", "Vienna", "Tbilisi", "Budapest", "Prague", "Athens"]

user_num2=int(input("Enter the first number (0-5): "))
user_num3=int(input("Enter the second number (0-5): "))

if user_num2<user_num3:
    print(cities[user_num3],"and",cities[user_num2])
elif user_num2>user_num3:
    print("switched city indexes -->", cities[user_num2],"and",cities[user_num3])
else:
    print("Your city is",cities[user_num2])


# 7)მომხმარებელი შემოიტანს სიტყვას.
# თუ პირველი ასო "a"-ა → დაბეჭდე "სიტყვა იწყება a-თი".
# თუ ბოლო ასო "z"-ია → დაბეჭდე "სიტყვა მთავრდება z-ით".
# სხვაგვარად → დაბეჭდე "სიტყვა არც a-თი იწყება და არც z-ით მთავრდება".

user_word=input("Type a random word: ")
if user_word[0]=="a":
    print("Your word starts with the letter a.")
elif user_word[-1]=="z":
    print("Your word ends with the letter z.")
else:
    print("Your word doesnt start with either a or z.")

# 8)დავალება 4
# მომხმარებელი შემოიტანს სიტყვას.
# თუ პირველი და ბოლო ასო ერთმანეთს ემთხვევა → დაბეჭდე "პირველი და ბოლო ერთნაირია".
# თუ განსხვავდება → "პირველი და ბოლო განსხვავებულია".

user_word1=input("Type a random word: ")
if user_word1[0]==user_word1[-1]:
    print("The first and last letters are the same")
# else:
#     print("The first and last letters are different")

# 9)შექმენი ცვლადი სადაც შეინახავთ შემდეგ ასოებს ---> "agivorsbgitr" 
# ----ამ სიიდან შეადგინე სიტყვა "goga, 
# ----ამ სიტყვიდან შეადგინე სიტყვა "saba"
# ----ამ სიტყვიდან შეადგინე სიტყვა "bativar"

word="agivorsbgitr"
print(word[1]+word[4]+word[1]+word[0])
print(word[6]+word[0]+word[7]+word[0])
print(word[-5]+word[0]+word[-2]+word[2]+word[3]+word[0]+word[-1])


# 10)შექმენი შემდეგი სტრინგი --> 'giorgi'
# შენი დავალებააა რომ for დდა while loop ის დახმარებით გამოიტანო ამ სტრინგის თითეული ასო ცალ ცალკე

word1="giorgi"

for i in range(0,5):
    print(word1[i])

print("---------------------")

num=0
while num<6:
    print(word1[num])
    num+=1
