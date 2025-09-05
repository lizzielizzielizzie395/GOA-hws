#1)მომხმარებელს შემოატანინეთ ორი რიცხვი,შეამოწმეთ თუ პირველი 
# რიცხვი მეტია მეორე რიცხვზე დაპრინტე რომ ‘first is more than second’,ასევე შეამოწმე თუ 
# პირველი რიცხვი ნაკლებია მეორე რიცხვზე დაპრინტე რომ ‘first is less than second’ და სხვა 
# დანარჩენ შემთხვევაში დაპტინტე რომ ‘first number equal to second number’

num = int(input("Enter your first number: "))
num_1 = int(input("Enter your second number: "))
if num > num_1:
    print('first is more than second')
elif num <num_1:
    print('first is more than second')
else:
    print('first number is equal to second number')

# 2)მომხმარებელს შემოატანინე რაიმე სტრინგი,ასევე შექმენი ცვლადი სადაც 
# შეინახავთ თქვენს სახელს,შემდეგ შეამოწმე თუ მომხმარებლის შემოყვანილი სტრინგი უდრის შენა 
# სახელს დაუპრინტე რომ ‘სეხნიები ვართ’ სხვა შემთხვევაში დაუპრინტეთ რომ ‘სხვადასხვა სახელები გავქვს’

name = 'lizi'
name_1=input('enter your name: ')
if name == name_1:
    print('We have the same names yay')
else:
    print('we have different names lmao')


# 3)შექმენი ორი ცვლადი სადაც შეინახავთ ინტეჯერ ტიპოს მონაცემებს,თქვენი დავალებაა შეამოწმოთ 
# თუ პირველი რიცხვი მეტია 0 ზე და და მეორე რიცხვიც მეტია 0 ზე დაუპრინტე რომ ‘ორივე რიცხვი დადებითია,
#  ასევე შეამოწმე თუ პირველი რიცხვი ნაკლებია 0 ზე და მეორე რიცხვიც ნაკლებია 0 ზე დაპურინტე რომ  
# ‘ორივე რიცხვი არის უარყოფით’,სხვა დანარჩენ შემთხვევაში დაუპრინტე რომ ‘ეს რა ჯანდაბაა’.

num_2 = str(input('enter your first number: '))
num_3 = str(input('enter your second number: '))
if num_2>0 and num_3>0:
    print('both numbers are positive.')
elif num_2<0 and num_3<0:
    print('both numbers are negative.')
else:
    print('get out dawg')


# 4)დაატრიალეთ ფორ ლუპი 50 დან 100 მდე 2 ის გამოტივებით 
for i in range (50,100,2):
    print(i)


# 5)ვაილ ლუპის გამოყენებით 20 დან 40 მდე გამოიტანეთ ყველა რიცხვი
temp_outside = 20
while temp_outside<40:
    print(temp_outside)
    temp_outside += 1