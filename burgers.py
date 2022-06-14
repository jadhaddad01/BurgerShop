# Imports
import datetime
import random
import string

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
    pass


class Drink():
    pass


class Side():
    pass


class Desert():
    pass


class Combo():
    pass


# condiments
# temperature

class Order:
    loyaltyNum = 0
    price = 0

    # constructor
    def __init__(self, loyaltyNum, price):
        self.loyaltyNum = loyaltyNum
        self.price = price

    # getters and setters
    def getLoyaltyNum(self):
        return self.loyaltyNum

    def getPrice(self):
        return self.price


def user_input_burger():
    b = Burger()
    # ask user for input and store it in burger object
    return b


def user_input_drink():
    d = Drink()
    # ask user for input and store it in drink object
    return d


def user_input_side():
    s = Side()
    # ask user for input and store it in side object
    return s


def user_input_combo():
    c = Combo()
    # ask user for input and store it in combo object
    # a combo must include one burger, one side, and one drink
    return c

# print all receipts for multiple orders


def receipt_print(OrderList):
    # MAROUCHE HERE
    for i in OrderList:

        Subtotal = i.getPrice()

        # MAROUCHE ADDED THE FOLLOWING:

        company_name = 'BURGER SHOP '
        company_address = '155 BOUL ST-CATHERINE'
        company_city = 'MONTREAL'
        message1 = 'RECEIPT'
        message2 = 'ENJOY YOUR MEAL !'

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
        print('=' * 50)

        print('\t\t{}'.format(message1))
        print("")

        print('\t\t\tSubtotal'':', Subtotal, "$")

        Tax = Subtotal*0.13
        print('\t\t\tTax'':', Tax, "$")

        Total = Subtotal + Tax
        print('\t\t\tTotal before tip '':', Total, "$")

        Tip =(tipAmount/100)*Total
        while True:
            tipAmount = input("Tip: 0%, 10%, 15%, 20% or custom? :")
            try:
                # check if integer
                tipAmount = int(tipAmount)
                # check if positive
                if(tipAmount < 0):
                    print('Please enter a valid number for tip.')
                    continue
                break
            except:
                print('Please enter a valid number for tip.')

        if tipAmount == 0: 
            print ('You're not leaving a tip? You cheapskate.')
            Tip=0 
        else: 
            print ('Thank you for tip') 
            Tip =(tipAmount/100)*Total
      
        print('\t\t\tTip'':', Tip, "$")
        FinalTotal = Total + Tip

        print('*' * 50)
        print('\t\t\tFinal Total '':', FinalTotal, "$")

        # CREATE RANDOM WI-FI PASSWORD

        length = int(10)
        letter = string.ascii_letters
        num = string.digits
        all = letter + num
        temp = random.sample(all, length)
        password = "".join(temp)

        print('*' * 50)
        print("To connect to WI-FI use this password :", password)
        print("")
        print('\t\t{}\n'.format(message2))
        print('*' * 50)


# Welcome
#       NOT VEGAN FRIENDLY
print("Welcome to Abdel-Cream's World Famous Deli")
print("------------------------------------------\n")

print("This is NOT a vegan-friendly restaurant. (Irvens, please exit or cops will be called for trespassing)")

# valid number of people ordering
while True:
    people = input("How may people are ordering? ")
    try:
        # check if integer
        people = int(people)
        # check if positive
        if(people <= 0):
            print('Please enter a valid number of people that are ordering.')
            continue
        break
    except:
        print('Please enter a valid number of people that are ordering.')

# how many orders
for i in range(people):
    # loyalty number - registration or usage (choose not to use it) for point system
    #   age of client saved with the data

    # order taking
    #   system to check combos, discounts
    #   discounts are stackable
    #   insert, edit, delete of order.

    #   Main:
    #       Meat: Burger (Original, Maya's Double Patty), Lamb, Steak, Hot Dogs (Beef based)
    #       Chicken: Fried Chicken (Regular, Jad's Deep Fry), Grilled Chicken
    #       Seafood: Snapper, Hogfish

    #   Shawarma: Beef, Chicken or Mix.

    #   Any Sandwish: You can add any vegetable or sauce you want (50 cent extra per)
    #       Tomatoes, Lettuce, Onions, Pickles, Cucumber, Olives, Banana Peppers, Radish
    #       GARLIC, Tahini, Hummus, Ketchup, Mayo, Mustard, Relish, Chili Sauce

    #   Appetizers: Soup, Salad, Fries, Onion Rings

    #   Desert:
    #       Ice Cream: Vanilla, Chocolate, Abdel-Cream's Secret Original
    #       Brownies, Chocolate Cake.

    #   Drink:
    #       Coke, Sprite, Beer, Hot Chocolate, Tea (Green, English Breakfast), Coffee (French Vanilla, Espresso, Adrian's Mother's Secret Recipe)

    # payment - choose between different payments.

    # receipt (wifi generated daily) - split the tab or all together.

    order1 = Order(123456, 40)
    orderList.append(order1)
    receipt_print(orderList)
