# program asking for a name and age and type of food:

#__________________________________________________________
#DEFINE!

def whenNumbers():
    print("we both know those are not words.\nTry again:")      
def col():
    print("what about colombian food, huh?\n Yes or No?")
    while True:
        cbia = input(">")
        try:
            bia = float(cbia)
            whenNumbers()
            print("yes or no mate")
        except:
            break
   
    if cbia == "yes":
        print("like what?")
        jd()
    elif cbia == "no":
        print("well, you should try it bye!")

#__________________________________________________________


print("hello, what is your name?")
while True:
    myName = input("Name:")
    try: 
        n = float(myName)
        whenNumbers()
    except:
        print("nice to meet you!",myName)
        break
    
print("How old are you?")
while True:
    theAge = input("Age:")
    try:
        a = int(theAge)
    except:
        print("please put a real number my friend!\ntry again:!")
        continue      
    if a == 25:
        print("Wow we are the same age brother!")
    elif a > 100:
        print("are you a vampire or what?")
    elif a > 25:
        print ("You are", a - 25, "older than me")
    elif a < 0:
        print("you haven't borned. Good luck! it is a tough world!")
    elif a == 24:
        print ("you are 1 year older than me?")
    else:
        print("you are", a,"years younger than me")
    break
print("What type of food do you like\nmexican - thai - colombian - other:?")
while True:
    food = input("Type of food: ")
    try:
        if food is not float(food):
            whenNumbers()
    except:
        break

def jd():
    while True:
        example = input(">")
        try:
            c = float(example)
            whenNumbers()
        except:
            break
    if example == "empanadas":
        print("Delicious! the beef are my favorites")
    elif example == "bandeja paisa":
        print("wow! thats a big feast!")
    elif example == "chicharron":
        print("I love crispy pork belly")
    else:
        print("it sounds sabroso!")
    
    
#__________________________________________________________

if food == "mexican":
    print("mm delicious! tacos de carne asada con cilantro OMG!")
    col()
elif food == "thai":
    print("that crispy pad thai right? yummy!")
    col()
elif food == "colombian":
    print("can you provide an example of colombian food please?")
    while True:
        jd()
        try:
            e = float(example)
            whenNumbers()
        except:
            break
else:
    print("like what?")    
    while True:
        food2 = input(">")
        try:
            g = float(food2)
            whenNumbers()
        except:
            break
               
    if food2 == "asian":
            print("WOW! I love mongolian beef man!")
    elif food2 == "italian":
            print("WOW! I love pasta, only with white sauce, tho!")
    else:
        print("I would need to try it to give you an answer")
print("thanks for taking the survey, enjoy your day!".upper())
quit()
#fin of the program!