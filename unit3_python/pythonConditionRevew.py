# functions are instructions that tell the cp what to do.
#def welcomeMsg():
#    print('hello and welcome to class!') 
#welcomeMsg()

#conditioanal 'if' 'else' to run mainy outcomes
def eatTime(time):
 
    if time == 'before noon':
        print('dont eat yet')
    elif time == 'after noon':
        print('do not eat')
    elif time == 'noon':
        print('lunch time')
    else:
        print('I dont know what you mean')
eatTime('before noon')