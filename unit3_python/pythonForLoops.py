#While while something is true keep running
# 
# for loops is a type of loop that iterates over 
# a list. 
#for loops shouldnt repeat for ever
#loops thourgh the length of the list
#numbers=[1,2,3,4]
#for x  in numbers:
#    print(x)
#    print('loop is repeating...')
#    if x==4:
#      print('loop stoped')

#shoppingList=['apple','ornge','milk','apple' ]
#for item in shoppingList:
 #   if item== 'apple':
 #       continue
#    print(item)

grades=[100,50,70,80,80,90,70,50]
    
for grade in grades:
        if grade < 70:
            grade +=5
        print(grade)