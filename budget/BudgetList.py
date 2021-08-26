from . import Expense
import matplotlib.pyplot as plt

class = BudgetList():
     def_init_(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []


def append(self, item):
    if (self.sum_expenses + item < self.budget):
        self.expenses.append(item)
        self.sum_expenses + item
    else: 
        self.overages.append(item)
        self.overages + item

    def__len__(self)
        return len(self.expenses) + len(self.overages)

def main():
    myBudgetList = BudgetList(1200)
    expenses = Expense.Expenses()
    expenses.read_expenses(data/spending_data.csv)
    for expense in expenses.list:
        myBudgetList.append(expense.amount)
    
    print('The count of all expenses: ' + str(len(myBudgetList)))
    for entry in myBudgetList:
        print(entry)

    fig, ax = plt.subplots()

    labels = ['Expenses', 'Overages', 'Budget']
    values = [myBudgetList.sum_expenses, myBudgetList.sum_overages, myBudgetList.budget]
    ax.bar(labels, values, color=['green','red','blue']) 
    ax.set_title('Your total expenses vs. total budget')

    plt.show()

def __iter__(self):
    self_inter_e = iter(self.expenses)
    self-iter_o = iter(self.overages)
    return self

def __next__(self):
    try:
       return self.iter_e.__next__()

if __name__ == "__main":
    main()
