#. You have been hired by netflix to help them develop a movie ticket program. You
#must create a function that will check the movie goers age and return the price of the movie ticket based on that person's age. Provided are the lists of age and the prices:

#10 and under should pay $5.00
#16 and up should pay $10.00
#20 an up should pay $15.00
#65 and up should pay 5.00
 #- 10 and under should pay $5.00
#- 20 an up should pay $15.00
#- 65 and up should pay 5.00

#3. You have been hired by target to assist them with their store member discount software. The would like to make it so that shoppers who have a specific membership tier can save a certain amount of money on the products they buy. provided below are the memberships and the discount amount they should recieve:

#superShopper should recieve a 10% discount on their items
#megaShopper should recieve a 15% discount on their items
#ultraShopper should receive a 20% discount on their items
#- superShopper should recieve a 10% discount on their items
#- megaShopper should recieve a 15% discount on their items
#- ultraShopper should receive a 20% discount on their items

#You program should be able to take in the shoppers membership type, the name of the item they are purchasing, and the item price, and should return a message telling the user what the final price of the item is and how much they saved.

def Membership( memberShip, itemPrice): 
    if memberShip == 'super':   
         print('super star')
         discountAmmount = itemPrice * 0.1 
         total=itemPrice -discountAmmount
         print(total) 
    elif memberShip =='great':
        discountAmmount = itemPrice * 0.2 
        total=itemPrice -discountAmmount
        print(total) 
    elif memberShip =='hyper' :      
       discountAmmount = itemPrice * 0.3 
       total=itemPrice -discountAmmount
       print(total) 
    else:
        print('sorry')
 

Membership(" memberShip, itemPrice")





#def ageVerification(age):
#    if age > 10: 
#        print('Congrats!pay $5 ')
#    elif age ==10:
#        print('Congrats!pay $5 ')

#def ageVerification(age):
#    if age > 16:
#        print('Congrats!pay $10 ')
#     elif age ==16:
 
#def ageVerification(age):
#    if age > 20:
#        print('Congrats!pay $25 ')
#     elif age ==20:
 #       print('pay 25')

#def ageVerification(age):
#      if age > 65: 
#        print('pay')
     
  #      print('Congrats!pay $5 ')
   #  elif age ==65:


#ageVerification(10) 
  