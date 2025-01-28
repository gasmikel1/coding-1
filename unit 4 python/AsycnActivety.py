numberList= [1,23,56,3,56,3,20,200]

#numberList.reverse()
#print(numberList)

def numberRevers():
    Listcount = 7    
    while Listcount >=0:
        print(numberList[Listcount])
        Listcount-=1

#numberRevers()

 # make a two-factor system
# 1 value needs to be a string the other a float, if fisrt right 
#go to the second one< if non kick back
#both right entire.


# we need a function
#if /else condetional statemant
# we need input
#we need to accept string for the first password
# we need to accept integer for the seconde 
# and a while
#while the progam is running check the password is right

def password(): 
    stringpassword='lots'
    floatpassword=3.99
    userString=''
    userintger=0 
    while stringpassword!=userString:
        print('enter a string password:')
        userString = input("please typ string")
        if stringpassword== userString:
                while floatpassword!= userintger:
                    print("please type the second password")
                    userintger=float(input("please put float here"))
                    if floatpassword==userintger:
                        print('your in')
                    else:
                        print("sorry")
        else:
            print("try again")                
password()