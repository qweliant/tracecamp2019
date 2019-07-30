import datetime
today = datetime.date.today()
import random
import math
import requests 




horoscope_is_joke = [
    "Love is a good thing for you, feeling good seek it, not hug someone =)",
    "You should drink more water today or you will be struck with poverty =(",
    "Do not go into light, for a devil that loves light rest upon your torso"
]


month = int(input(r"Please enter your birthday month(e.g. 1, 2, 3, etc): "))
print (month)
day = int(input(r"Please enter your birthday day(e.g. 1, 16, etc): "))
print (day)

if month ==1:
    if day <=20:
        h = "Capricorn"
    else:
        h = "Aquarius"

elif month ==2:
    if day <= 19:
        h = "Aquarius"
    else:
        h = "Pisces"

elif month ==3:
    if day <= 20:
        h = "Pisces"
    else:
        h = "Aries"

elif month ==4:
    if day <= 20:    
        h = "Aries"
    else:
        h = "Taurus"

elif month ==5:
    if day <= 21:    
        h = "Taurus"
    else:
        h = "Gemini"

elif month ==6:
    if day <= 20:    
        h = "Gemini"
    else:
        h = "Cancer"

elif month ==7:
    if day <= 22:    
        h = "Cancer"
    else:
        h = "Leo"

elif month ==8:
    if day <= 22:    
        h = "Leo"
    else:
        h = "Virgo"

elif month ==9:
    if day <= 23:    
        h = "Virgo"
    else:
        h = "Libra"

elif month ==10:
    if day <= 23:    
        h = "Libra"
    else:
        h = "Scorpio"

elif month ==11:
    if day <= 22:    
        h = "Scorpio"
    else:
        h = "Sagittarius"

elif month ==12:
    if day <= 21:    
        h = "Sagittarius"
    else:
        h = "Capricorn"
 

def print_horoscope(str):
    print(h +", " + "your horoscope for the day," + today.strftime(' %d, %b %Y') + " is: " + random.choice(horoscope_is_joke) )

print_horoscope(h)

val = input("Do you want to edit the sages' wisdom? Enter yes/no: ")
print()

if val == "yes":
    for i,v in enumerate(horoscope_is_joke):
        print(i, v + "\n")
    edit = input("Write delete to delete phrase or add to add a phrase?: ")
    if edit == "delete":
        index = input("Enter index value to remove, 0-2: ")
        try :
            horoscope_is_joke.pop(index)
        except IndexError:
            print("Index Out of Range") 
    elif edit == "add":
        phrase = input("What is your new sage advice? Be spiritual... ")
        horoscope_is_joke.append(phrase)
        for i,v in enumerate(horoscope_is_joke):
            print(i, v + "\n")





num_list =[x for x in range(1,11)]
print("list comp number list 1-10:",num_list)

num_list_for = [x for x in range(1,11)]

for x, y in enumerate(num_list_for):
    num_list_for[x] = y + 2
print("add 2 to every value in list with for loop:",num_list_for)

num_list_add = [x + 2 for x in num_list]
print("add 2 to every value in list with list comp:",num_list_add)

nums_cubed = [x**3 for x in range(1,11)]
print("cube every value in list:",nums_cubed)

nums_add_3_if_mod_3 = [x+3 for x in range(1,11) if x%3 == False]
print("numbers 1-10 that are divisible by 3, + 3:",nums_add_3_if_mod_3)

even_odd = ['even' if x%2 == False else 'odd' for x in range(1,11)]
print("even odd values:",even_odd)


