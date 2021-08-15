
def truncate(n):
    multipler = 10
    return int(n*multipler)/multipler

def getTotals(categories):
    total = 0
    breakdown = []
    for caterogy in categories:
        total += category.get_withdrawls()
        breakdown.append(category.get_withdrawls())
    rounded = list(map(lambda x: truncate(x/total), breakdown))
    return rounded


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


class Category:

  def __init__(self, category):
        self.ledger =[]
        self.amount=0
        self.category = category


  def check_funds(self,amount):
    if self.amount< amount:
      return False
    else:
      return True


  def deposit(self,amount, description=""):
    self.ledger.append({"amount":amount,"description":description})
    self.amount += amount


  def withdraw(self,amount,description=""):
    if self.check_funds(amount) ==True:
      self.amount -=amount
      self.ledger.append({"amount":-amount,"description":description})
      return True
    else:
      return False

  # return balanace of budget
  def get_balance(self):
    return self.amount

  def __str__(self):
    result=""
    result+="*************Food*************"+"\n"
    for transaction in self.ledger:
      amount=0
      description=""
      for key,value in transaction.items():
          if key=="amount":
            amount = value
          elif key=="description":
            description=value
      if len(description)>23:
        description=description[:23]
      amount = str(format(float(amount),'.2f'))
      if len(amount)>7:
        amount= amount[:7]
      result+= description + str(amount).rjust(30-len(description))+"\n"
    result+="Total: "+str(format(float(self.amount),'.2f'))
    return result

  def transfer(self,amount,category):
    if self.check_funds(amount)==True:
      self.amount-=amount
      self.ledger.append({"amount": -amount,"description":"Transfer to "+category.category})
      category.ledger.append({"amount": amount,"description": "Transfer from "+self.category})
      return True
    else:
      return False

  def get_withdrawls(self):
      total = 0
      for item in self.legder:
          if item["amount"] < 0:
              total += item["amount"]
      return total
