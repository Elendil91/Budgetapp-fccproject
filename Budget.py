class Category:

    def __init__(self, category):
        self.legder = []
        self.amount = 0
        self.caterogy = category

# A `deposit` method that accepts an amount and description.
#The method should append an object to the ledger list in the form of
#`{"amount": amount, "description": description}`.
    def deposit(self, amount, description=""):
        self.ledger.append({"amount":amount, "description":description})
        self.amount += amount
#* A `withdraw` method that is similar to the `deposit` method,
#but the amount passed in should be stored in the ledger as a negative number.
#If there are not enough funds, nothing should be added to the ledger.
#This method should return `True` if the withdrawal took place, and `False` otherwise.
    def withdraw(self, amount, description = ""):
       if self.check_funds(amount) == True:
           self.amount -= amount
           self.ledger.append({"amount":- amount, "description":description})
           return True
       else:
           return False

#A `get_balance` method that returns the current balance of the
#budget category based on the deposits and withdrawals that have occurred.
    def get_balance(self):
        return self.amount
#A `transfer` method that accepts an amount and another budget category as arguments.
#The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]".
#The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]".
#If there are not enough funds, nothing should be added to either ledgers.
#This method should return `True` if the transfer took place, and `False` otherwise.
    def transfer(self, category, amount):
        if self.check_funds(amount) == True:
            self.amount -= amount
            self.ledger.append({"amount":-amount,"description":"Transfer to " + Category.category})
            category.legder.append({"amount":amount, "description": "Transfer from" + self.Category})
            return True
        else:
            return False
#* A `check_funds` method that accepts an amount as an argument.
#It returns `False` if the amount is greater than the balance of the budget category and returns `True` otherwise.
#This method should be used by both the `withdraw` method and `transfer` method.
    def check_funds(self, amount):
        if self.amount < amount:
            return False
        else:
            return True

#When the budget object is printed it should display:
#* A title line of 30 characters where the name of the category is centered in a line of `*` characters.
#* A list of the items in the ledger. Each line should show the description and amount.
#The first 23 characters of the description should be displayed, then the amount.
#The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
#* A line displaying the category total.
    def __str__(self):
        result = ""
        result += "*************Food*************"+"\n"
        for transaction in self.ledger:
            amount = 0
            description = ""
            for key,value in transaction.items():
                if key == "amount":
                    amount = value
                elif key=="description":
                    description=value
            if len(description) > 23:
                description = description[:23]
            amount = str(format(float(amount),'.2f'))
            if len(amount) > 7:
                amount= amount[:7]
            result += description + str(amount).rjust(30-len(description))+"\n"
        result += "Total: "+str(format(float(self.amount),'.2f'))
        return result
#`create_spend_chart` that takes a list of categories as an argument. It should return a string that is a bar chart.

def create_spend_chart(categories):
    result1 = " Percentage spent by category\n"
    i = 100
    totals = getTotals(categories)
    while i >= 0:
        cat_space = " "
        for total in totals:
            if total * 100 >= i:
                cat_space += "o  "
            else:
                cat_space += "   "
        result1+= str(i).rjust(3) + "|" + cat_space + ("\n")
        i-= 10

    dashes = "-" + "---"*len(categories)
    names = []
    x_axis = ""
    for category in categories:
        names.append(category.name)

    maxi = max(names, key=len)

    for x in range(len(maxi)):
        namesStr= '    '
        for name in names:
            if x >= len(name):
                nameSrt += "   "
            else:
                nameSrt += name[x] + "  "


        if (x != len(maxi) -1):
            nameSrt += "\n"

        x_axis += nameSrt

    result1 += dashes.rjust(len(dashes) + 4) + "\n" + x_axis
    return result1
