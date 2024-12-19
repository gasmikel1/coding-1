# A function definition provides instructions
# to the computer on what to do with data.
# data = just data types
# () curly brackets are called parameters.
# This is where we pass in data in the function
# definition. 
# parameter = placeholder (for data).
def customizeMyName(name):
    print('Your new custom name is the cool guy '+ name)
# arguement is the data passed inside of the function
# call. 
# arguement = evidence or real facts and data.
# customizeMyName('Ian')
# Lesson on Conditional Statements
# Conditional statements are built using 
# the 'IF' and 'ELSE' keywords. They allow us
# to make decisions based on the data we receive. 
# a conditional function for if someone is old enough
# to buy GTA VI
def ageVerification(age):
    if age > 10:
        print('Congrats!pay $5 ')
    else: 
        print('Sorry you must have an adult to get this game.')
#ageVerification(19)

def playerHealth(hp):
    if hp > 0 and hp < 99: 
        print('You are still alive!')
    elif hp > 100:
        print('Congrats! you have leveled up!') 
    else: 
        print('Game over your hp is zero')
playerHealth(101)