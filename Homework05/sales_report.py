"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.

"""

def main():
    salespeople = []
    melons_sold = []

    f = open("sales_report.csv")
    for line in f:
        line = line.rstrip()
        entries = line.split(",")
        salesperson = entries[0]
        melons = int(entries[2])

        if salesperson in salespeople:
            position = salespeople.index(salesperson)
            melons_sold[position] += melons
        else:
            salespeople.append(salesperson)
            melons_sold.append(melons)


    for i in range(len(salespeople)):
        print "%s sold %d melons" % (salespeople[i], melons_sold[i])



if __name__ == "__main__":
    main()
