import csv
#introduction

def main():
    print('Hello Everyone! This is our Data analysis code for the given sales file')
    file = open("sales.csv")
    filename = open('sales.csv', 'r')

    csvreader = csv.reader(file)
    csv_reader = csv.DictReader(filename)

#making a list
    header = next(csvreader)
    print(header)
    rows = []
    for row in csvreader:
        rows.append(row)
    print(rows)
    month = []
    sale = []
    expense = []
    months_year =[]
    total_sale =[]
    total_expense = []

    for col in csv_reader:
        month.append(col["month"])
        sale.append(col["sales"])
        expense.append(col['expenditure'])
        tm = str(col['month'])
        ts = int(col['sales'])
        te = int(col['expenditure'])
        months_year.append(tm)
        total_sale.append(ts)
        total_expense.append(te)
    print(month)
    print(sale)
    print(expense)

#calculations
    total = sum(total_sale)
    print(" TOTAL SALE for the Year 2018 is" +' '+ str(total))
    tot_exp = sum(total_expense)
    print(" TOTAL EXPENDITURE for the Year 2018 is" +' '+ str(tot_exp))
    average_sale = total / len(total_sale)
    print(' Average Sale for the year 2018 is {}' .format(average_sale))
    print(' Number of sales for the year 2018 is {}'.format(len(total_sale)))
    print(' Highest sale for the year 2018 is {}'.format(max(total_sale)))
    print(' Lowest sale for the year 2018 is {}'.format(min(total_sale)))


    #Calculate Profit or Loss
    expense_amount = float(input(" Please Enter the Expenditure: "))
    sale_amount = float(input(" Please Enter the Sales Amount: "))

    if (expense_amount > sale_amount):
            amount = expense_amount - sale_amount
            print("Total Loss Amount = {0}".format(amount))
    elif (sale_amount > expense_amount):
            amount = sale_amount - expense_amount
            print("Total Profit = {0}".format(amount))
    else:
            print("No Profit No Loss!!!")

    # graph depicting sales vs expenditure in each month in 2018
    import matplotlib.pyplot as plt
    import numpy as np

    w = 0.4
    x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sales = [6226, 1521, 1842, 2051, 1728, 2138, 7479, 4434, 3615, 5472, 7224, 1812]
    expenditure = [3808, 3373, 3965, 1098, 3046, 2258, 2084, 2799, 1649, 1116, 1431, 3532]

    bar1 = np.arange(len(x))
    bar2 = [i + w for i in bar1]

    plt.bar(bar1, sales, w, label="sales")
    plt.bar(bar2, expenditure, w, label="expenditure")

    plt.xlabel("Month")
    plt.ylabel("Sales, Expenditure")
    plt.title("Sales vs Expenditure in 2018")
    plt.xticks(bar1 + w / 2, x)
    plt.legend()
    plt.show()

    print("Thank you!")


main()
