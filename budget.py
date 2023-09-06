class Category:
  def __init__(self,category):
    self.category = category
    self.ledger = list()

  def check_funds(self, amount):
    return amount <= self.get_balance()
  
  def deposit(self, amount, description = ""):
     self.ledger.append({"amount": amount, "description":description})

  def withdraw (self, amount, description = ""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description":description})
      return True
    else:
      return False

  def get_balance(self):
    return sum(item["amount"] for item in self.ledger)

  def transfer(self, amount, budget_category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {budget_category.category}")
      budget_category.deposit(amount, f"Transfer from {self.category}")
      return True
    else: 
      return False

  def __str__(self):
    title = f"{self.category:*^30}\n"
    items = ""
    total = 0
    for item in self.ledger:
      description = item["description"][:23]
      amount = "{:.2f}".format(item["amount"])
      items += f"{description}{amount:>30}\n"
      total += item["amount"]
    output = title + items + "Total: {:.2f}".format(total)
    return output


def create_spend_chart(categories):
  chart = "Percentage spent by category\n"
  spent_percentage = []
 
  # Calculate the percentage spent for each category
  total_withdrawals = sum(category.get_balance() for category in categories)
  for category in categories:
    spent_percentage = (category.get_balance() / total_withdrawals) * 100
    spent_percentage.append(spent_percentage)

# Create the horizontal bars in the chart
  for i in range(100, -1, -10):
    chart += str(i).rjust(3) + "| "
    for spent_percentage in spent_percentage:
      chart +="o " if spent_percentage >= i else " "
    chart +="\n"

# Add the horizontal line and category names
  chart += "    ----------\n"
  max_category_name_length = max(len(category.category) for category in categories)
  for i in range(max_category_name_length):
    chart += "   "
    for category in categories:
      if i < len(category.category):
        chart += category.category[i] + "  "
      else:
        chart += "  "
    if i < max_category_name_length - 1:
      chart += "\n"

  return chart.rstrip()
