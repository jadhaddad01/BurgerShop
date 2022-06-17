# Imports
import datetime
import random
import string
import os
import pickle

from flask import appcontext_popped

# Wifi Password PRECODE
y = datetime.datetime.now()

# CREATE RANDOM WI-FI PASSWORD


def passs():
    length = int(10)
    letter = string.ascii_letters
    num = string.digits
    all = letter + num
    temp = random.sample(all, length)
    password = "".join(temp)
    return password


wifiPass = [y.strftime("%d%m%y"), passs()]
# Open wifi password file
try:
    with open(os.path.join("utils", "wifiPass.txt"), "rb") as fp:			# Load Pickle
        wifiPass = pickle.load(fp)

# If Not Found, Create a new python password file
except Exception as e:
    print("Saved Values File wifiPass.txt Not Found. Initializing to:")
    print("	- Date:", wifiPass[0])
    print("	- Password:", wifiPass[1])

    with open(os.path.join("utils", "wifiPass.txt"), "wb") as fp:			# Save Pickle
        pickle.dump(wifiPass, fp)

# new date new pass
if not (y.strftime("%d%m%y") == wifiPass[0]):
    wifiPass[0] = y.strftime("%d%m%y")
    wifiPass[1] = passs()
    with open(os.path.join("utils", "wifiPass.txt"), "wb") as fp:			# Save Pickle
        pickle.dump(wifiPass, fp)


# Variables
# ---------

# how many orders
people = 0

# the list of order objects
orderList = []
# ORDER OBJECT -> [Main], [Side], etc etc
# ORDER LIST (people ordering) -> [ORDER1, ORDER2, ORDER3]


# Classes
# -------

class MainDish():
    main = [
        {"name": "Burger", "price": 0},
        {"name": "General Tao", "price": 10},
        {"name": "Seafood", "price": 0}
    ]

    burger = [
        {"name": "Original Wagyu", "price": 8},
        {"name": "Maya's Double Patty Kobe", "price": 12}
    ]

    seafood = [
        {"name": "Tuna Sushi", "price": 6},
        {"name": "Salmon Roses", "price": 8},
        {"name": "Jad's Octopus Roll", "price": 10}
    ]

    toppings_list = [
        {"name": "Pickles", "price": 0.5},
        {"name": "Japanese Mayo", "price": 0.5},
        {"name": "Soya Sauce", "price": 0.5},
        {"name": "Wasabi", "price": 0.5}
    ]

    # constructive method
    def __init__(self, main1, burger_type, seafood_type, extras):
        self.main1 = main1
        self.burger_type = burger_type
        self.seafood_type = seafood_type
        self.extras = extras
        # this create a list

    # def getNamePrice(self):
    #     tmp = []
    #     price = 0
    #     for i in self.extras:
    #         tmp.append(self.toppings_list[i])
    #         price += self.toppings_list[i]["price"]

    #     if (int(self.main1) == 1):
    #         return [[self.main[1]], self.main[1]["price"]]
    #     elif (int(self.main1) == 0):
    #         return [[self.main[0], self.burger[self.burger_type], tmp], (self.burger[self.burger_type]["price"]+price)]
    #     else:
    #         return [[self.main[2], self.seafood[self.seafood_type], tmp], (self.seafood[self.seafood_type]["price"]+price)]

    def getName(self):
        if (int(self.main1) == 1):
            return self.main[1]["name"]
        elif (int(self.main1) == 0):
            return self.burger[self.burger_type]["name"]
        else:
            return self.seafood[self.seafood_type]["name"]

    def getPrice(self):
        tmp = []
        price = 0
        for i in self.extras:
            tmp.append(self.toppings_list[i])
            price += self.toppings_list[i]["price"]

        if (int(self.main1) == 1):
            return self.main[1]["price"]
        elif (int(self.main1) == 0):
            return self.burger[self.burger_type]["price"]+price
        else:
            return self.seafood[self.seafood_type]["price"]+price

    def getType(self):
        return "Main"


class Drink():
    drink = [
        {"name": "Adrian's Mother's Green Tea", "price": 4},
        {"name": "Sake", "price": 5},
        {"name": "Soft Drink", "price": 0},
    ]

    soft = [
        {"name": "Coke", "price": 2},
        {"name": "Japan Dry", "price": 2},
        {"name": "Miranda", "price": 2}
    ]

    def __init__(self, option1, softselect):
        self.option1 = option1
        self.softselect = softselect

    # def getNamePrice(self):
    #     if(int(self.option1) == 2):
    #         return [[self.drink[self.option1], self.soft[self.softselect]], self.soft[self.softselect]["price"]]
    #     else:
    #         return [[self.drink[self.option1]], self.drink[self.option1]["price"]]

    def getName(self):
        if(int(self.option1) == 2):
            return self.soft[self.softselect]["name"]
        else:
            return self.drink[self.option1]["name"]

    def getPrice(self):
        if(int(self.option1) == 2):
            return self.soft[self.softselect]["price"]
        else:
            return self.drink[self.option1]["price"]

    def getType(self):
        return "Drink"


class Side():
    side = [
        {"name": "Fried Rice", "price": 4},
        {"name": "Miso Soup", "price": 5},
        {"name": "Edamame", "price": 5},
        {"name": "Fried Tempura", "price": 4}
    ]

    def __init__(self, choice):
        self.choice = choice

    # def getNamePrice(self):
    #     return [[self.side[self.choice]], self.side[self.choice]["price"]]

    def getName(self):
        return self.side[self.choice]["name"]

    def getPrice(self):
        return self.side[self.choice]["price"]

    def getType(self):
        return "Side"


class Desert():
    desert = [
        {"name": "Abdel-Chocolate-Cream", "price": 4},
        {"name": "Fried Banana", "price": 5}
    ]

    def __init__(self, option):
        self.option = option

    # def getNamePrice(self):
    #     return [[self.desert[self.option]], self.desert[self.option]["price"]]

    def getName(self):
        return self.desert[self.option]["name"]

    def getPrice(self):
        return self.desert[self.option]["price"]

    def getType(self):
        return "Desert"


class Combo():
    def __init__(self, main, side, drink):
        self.main = main
        self.side = side
        self.drink = drink

    # def getNamePrice(self):
    #     return [
    #         [self.main.getName(),
    #          self.side.getName(),
    #          self.drink.getName()],
    #         (self.main.getPrice()
    #          + self.side.getPrice()
    #          + self.drink.getPrice())*0.9
    #     ]

    def getName(self):
        return [
            self.main.getName(),
            self.side.getName(),
            self.drink.getName()
        ]

    def getPrice(self):
        return (self.main.getPrice()
                + self.side.getPrice()
                + self.drink.getPrice())*0.9

    def getType(self):
        return "Combo"


# condiments
# temperature

class Order:
    loyaltyNum = 0
    price = 0
    food = []

    # constructor
    def __init__(self, loyaltyNum, price, food):
        self.loyaltyNum = loyaltyNum
        self.price = price
        self.food = food

    # getters and setters
    def getLoyaltyNum(self):
        return self.loyaltyNum

    def getPrice(self):
        return self.price

    def appendFood(self, foodObject):
        self.food.append(foodObject)
        self.price += foodObject.getPrice()

    def getFood(self):
        return self.food

    def removeFoodAtIndex(self, index):
        self.price -= self.food[index].getPrice()
        f = self.food.pop(index)
        return f

    def getNamePriceTypeFoodObjects(self):
        tmp = []
        tmp2 = []
        tmp3 = []
        for i in self.food:
            tmp.append(i.getName())
            tmp2.append(i.getPrice())
            tmp3.append(i.getType())

        return tmp, tmp2, tmp3


# Methods
# -------
def validNumAbove(num, str):
    while True:
        retVal = input(str)
        try:
            # check if integer
            retVal = int(retVal)
            # check if positive
            if(retVal > num):
                print('Please enter a valid number.')
                continue
            break
        except:
            print('Please enter a valid number.')

    return retVal


def validNumBelow(num, str):
    while True:
        retVal = input(str)
        try:
            # check if integer
            retVal = int(retVal)
            # check if positive
            if(retVal < num):
                print('Please enter a valid number.')
                continue
            break
        except:
            print('Please enter a valid number.')

    return retVal


def validNumBetween(min, max, str):
    while True:
        retVal = input(str)
        try:
            # check if integer
            retVal = int(retVal)
            # check if positive
            if(retVal < min) or (retVal > max):
                print('Please enter a valid number.')
                continue
            break
        except:
            print('Please enter a valid number.')

    return int(retVal)


def user_input_main():
    extras = []
    burger_type = 0
    seafood_type = 0
    # checking order details
    print("\nMain Menu:\n0: Burger\n1: General Tao Chicken\n2: Sea Food ")
    main1 = validNumBetween(0, 2, "Please choose your order: ")
    if main1 == 0:
        burger_type = validNumBetween(
            0, 1, "0: Original Wagyu or 1: Maya's Double Patty Kobe: ")
        topping_comfims = input("Would like an extra topping? y/n ")
        if topping_comfims == "y":
            extras_input = input(
                "0: Pickles 1: Japanese Mayo 2: Soya Sauce 3: Wasabi [Input many at once]: ")
            extras = [int(x) for x in extras_input.split(" ")]
    if main1 == 2:
        seafood_type = validNumBetween(
            0, 2, "0: Tuna Sushi 1: Salmon Roses 2: Jad's Octopus Roll ")
        topping_comfim2 = input("Would like an extra toppings? y/n ")
        if topping_comfim2 == "y":
            extras_input = input(
                "0: Pickles 1: Japanese Mayo 2: Soya Sauce 3: Wasabi [Input many at once]: ")
            extras = [int(x) for x in extras_input.split(" ")]
    maindish = MainDish(main1, burger_type, seafood_type, extras)
    return maindish


def user_input_sides():
    choice = validNumBetween(
        0, 3, "\nSides Menu:\n0: Fried Rice\n1: Miso Soup\n2: Edamame\n3: Fried Tempura \nPlease choose your order: ")
    s = Side(choice)
    return s


def user_input_drink():
    softselect = 0
    while True:
        option1 = validNumBetween(
            0, 2, "\nDrinking Menu:\n0: Adrian's Mother's Green Tea\n1: Sake\n2: Soft Drink \nPlease choose your order: ")
        if option1 == 1:
            option2 = validNumBelow(0, "What's your age? ")
            if option2 >= 18:
                break
            else:
                print("You are too young to drink, choose another ")
        else:
            break
    if option1 == 2:
        softselect = validNumBetween(
            0, 2, "Would you like:\n0: Coke\n1: Japan Dry\n2: Miranda \nPlease choose your order: ")
    d = Drink(option1, softselect)
    return d


def user_input_desert():
    option = validNumBetween(
        0, 1, "\nDesert menu:\n0: Abdel-Chocolate-Cream\n1: Fried Banana \nPlease choose your order: ")
    D = Desert(option)
    return D


def user_input_combo():
    main = user_input_main()
    side = user_input_sides()
    drink = user_input_drink()

    c = Combo(main, side, drink)
    return c


def listItem(o):
    name, _, _ = o.getNamePriceTypeFoodObjects()

    print("\nItems on Order:")
    for _, val in enumerate(name):
        print(val)


def removeItem(o):
    name, _, _ = o.getNamePriceTypeFoodObjects()

    print("\nItems to Delete:")
    for i, val in enumerate(name):
        print("{}: {}".format(i, val))

    rem = validNumBetween(
        0, len(name)-1, "Choose what to delete: ")

    o.removeFoodAtIndex(rem)


def checkCombo(orderList):
    for i in orderList:
        # get type of food
        _, _, typee = i.getNamePriceTypeFoodObjects()

        # get food object list
        food = i.getFood()

        # while combos are still available
        while ("Main" in typee and "Side" in typee and "Drink" in typee):
            index = typee.index("Main")
            typee.pop(index)
            mainFood = food[index]
            i.removeFoodAtIndex(index)

            index = typee.index("Side")
            typee.pop(index)
            mainSide = food[index]
            i.removeFoodAtIndex(index)

            index = typee.index("Drink")
            typee.pop(index)
            mainDrink = food[index]
            i.removeFoodAtIndex(index)

            # create combo after removing food from all lists
            c = Combo(mainFood, mainSide, mainDrink)
            # add combo to order
            i.appendFood(c)

# print all receipts for multiple orders


def receipt_print(OrderList, people, birthDiscount):
    newOrderList = OrderList
    if not (people == 1):
        print("\n")
        pay = validNumBetween(
            0, 1, "Would you like to:\n0: Pay Seperately\n1: Pay as a Single Order \nPlease choose your choice: ")

        # If pay as single order
        if pay == 1:
            newOrderList = [Order(loy[1], 0, [])]
            for i in OrderList:
                # get food object list
                food = i.getFood()

                for j in food:
                    newOrderList[0].appendFood(j)

    # MAROUCHE HERE
    for i in newOrderList:
        print("\n")

        Subtotal = round(i.getPrice(), 2)

        # MAROUCHE ADDED THE FOLLOWING:

        company_name = 'BURGER SHOP '
        company_address = '155 BOUL ST-CATHERINE'
        company_city = 'MONTREAL'
        message1 = 'RECEIPT'
        message2 = 'ENJOY YOUR MEAL !'
        message3 = 'YOU ORDERED:'
        print('*' * 50)

        # print company information first using format
        print('\t\t{}'.format(company_name.title()))
        print('\t\t{}'.format(company_address.title()))
        print('\t\t{}'.format(company_city.title()))

        print('=' * 50)

        e = datetime.datetime.now()
        print("Order's date: " + e.strftime("%Y-%m-%d %H:%M:%S"))
        # Loyalty number
        print("Loyalty Num:", i.getLoyaltyNum())
        print("Loyalty points:", loy[2])
        print('=' * 50)
        print('\t\t\t{}'.format(message1))
        print('=' * 50)
        print(message3)
        print("")

        # MAROUCH RECEIPT PUT BELOW RECEIPT HERRRRRRRREEEEEEEEEEE
        nameO, priceO, typeO = i.getNamePriceTypeFoodObjects()
        for j in range(len(nameO)):
            # if it is combo
            if (typeO[j] == "Combo"):
                for k, val in enumerate(nameO[j]):
                    # each item in combo
                    print(val)
                # price of total combo
                print('** Price of the combo .........:',
                      round((priceO[j]), 2), '$')
            # if not combo
            else:
                # print name and price of each item
                print(nameO[j], ':..................', priceO[j], '$')
        print('')
        print('-' * 50)
        print('\t\t\tSubtotal'':         ', Subtotal, "$")

        if birthDiscount:
            sub = round(Subtotal*0.2, 2)
            Subtotal = round(Subtotal*0.8, 2)
            print('\t\t\tBirthday Discount: -{}$'.format(sub))
            print('\t\t\tNew Subtotal:     ', Subtotal, "$")

        p = int(loy[2]//100)
        if(p > 0):
            sub = round(p*5, 2)
            Subtotal = round(Subtotal-sub, 2)
            print("Loyalty points discount ({} points used): -{}$".format(p*100, sub))
            print('\t\t\tNew Subtotal:     ', Subtotal, "$")

        Tax = round(Subtotal*0.13, 2)
        print('\t\t\tTax'':              ', Tax, "$")

        Total = round(Subtotal + Tax, 2)
        print('\t\t\tTotal before tip '':', Total, "$")

        tipAmount = validNumBelow(0, "Tip: 0%, 10%, 15%, 20% or custom: ")

        if tipAmount == 0:
            print("You're not leaving a tip? You cheapskate.")
            Tip = 0
        else:
            print('Thank you for tip')
            Tip = round(((tipAmount/100)*Total), 2)

        print('\t\t\tTip'':              ', Tip, "$")
        FinalTotal = round(Total + Tip, 2)

        print('-' * 50)
        print('\t\t\tFinal Total '':     ', FinalTotal, "$")
        print("")

        # WIFI PASS
        print('*' * 50)
        print("Points received: {}".format(FinalTotal))
        print("Points used: {}".format(p*100))
        print("Your points after the order: {}".format(
            loy[2]+FinalTotal-(p*100)))

        # save new points
        loy[2] = loy[2]+FinalTotal-(p*100)
        loyalty[ind][2] = loy[2]
        with open(os.path.join("utils", "loyalty.txt"), "wb") as fp:			# Save Pickle
            pickle.dump(loyalty, fp)

        print("To connect to WI-FI use this password :", wifiPass[1])
        print("")
        print('\t\t{}\n'.format(message2))
        print('*' * 50)


# Welcome
#       NOT VEGAN FRIENDLY
print("Welcome to Abdel-Cream's World Famous Deli")
print("------------------------------------------\n")

print("This is NOT a vegan-friendly restaurant. (Irvens, please exit or cops will be called for trespassing)")

# valid number of people ordering
people = validNumBelow(1, "How may people are ordering? ")

# how many orders
for i in range(people):
    # loyalty number - registration or usage (choose not to use it) for point system
    #   age of client saved with the data
    print("\nPerson #{}, welcome:".format(i+1))

    # Loyalty Number
    loyalty = []
    # Open loyalty file
    try:
        with open(os.path.join("utils", "loyalty.txt"), "rb") as fp:			# Load Pickle
            loyalty = pickle.load(fp)

    # If Not Found, Create a new python loyalty file
    except Exception as e:
        print("Saved Values File loyalty.txt Not Found. Initializing")
        with open(os.path.join("utils", "loyalty.txt"), "wb") as fp:			# Save Pickle
            pickle.dump(loyalty, fp)

    # each loyalty membership has: birthday, loyalty number, loyalty points
    loyaltyChoice = validNumBetween(0, 1, "\nAbdel-Loyalty Program (Every 100 points gets you 5$ off):\n"
                                    "0: Create New Membership\n1: Enter Membership Number\nPlease choose your option: ")

    loy = []
    # if new membership index is last element
    ind = -1
    if loyaltyChoice == 0:
        birth = None
        while True:
            birthyear = validNumAbove(
                2022, "Please input your birth year: ")
            birthmonth = validNumAbove(
                12, "Please input your birth month: ")
            birthday = validNumAbove(31, "Please input your birth day: ")
            try:
                birth = datetime.datetime(birthyear, birthmonth, birthday)
                break
            except:
                print("Please input a valid date.")

        if loyalty == []:
            loy.append(birth.strftime("%d%m%y"))
            loy.append(1000)
            loy.append(100)
        else:
            loy.append(birth.strftime("%d%m%y"))
            loy.append(loyalty[-1][1]+1)
            loy.append(100)

        loyalty.append(loy)
        with open(os.path.join("utils", "loyalty.txt"), "wb") as fp:			# Save Pickle
            pickle.dump(loyalty, fp)

        print("You have been given 100 points as a sign-up bonus!")

    elif loyaltyChoice == 1:
        flag = True
        while flag:
            memNum = validNumBelow(1000, "Please enter your loyalty number: ")
            for i, val in enumerate(loyalty):
                if memNum == val[1]:
                    flag = False
                    loy = val
                    ind = i
                    print(
                        "\nWelcome, you have {} points in your membership. Your number is {}".format(loy[2], loy[1]))
            if flag:
                print("Membership not valid.")

    birthDiscount = False
    if (y.strftime("%d%m%y") == loy[0]):
        print("Happy Birthday!! You will receive 20% off today!")
        birthDiscount = True

    o = Order(loy[1], 0, [])
    while True:
        menuchoice = validNumBetween(0, 7, "\nWhich menu you would like to order from?\n"
                                     "0: Main Menu\n1: Drink Menu\n2: Side Menu\n3: Desert Menu\n4: 10% Discounted Combination (Main, Side, Drink) \n5: List Items \n6: Delete Item\n7: Finish\nPlease choose your option: ")
        if menuchoice == 0:
            o.appendFood(user_input_main())
        elif menuchoice == 1:
            o.appendFood(user_input_drink())
        elif menuchoice == 2:
            o.appendFood(user_input_sides())
        elif menuchoice == 3:
            o.appendFood(user_input_desert())
        elif menuchoice == 4:
            o.appendFood(user_input_combo())
        elif menuchoice == 5:
            listItem(o)
        elif menuchoice == 6:
            removeItem(o)
        else:
            break

    orderList.append(o)

# check for combos and make them
checkCombo(orderList)

receipt_print(orderList, people, birthDiscount)
