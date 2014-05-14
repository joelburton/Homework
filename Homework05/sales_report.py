
def main():
    salespeople = []
    melons_sold = []

    f = open("salesreport.csv")
    for line in f:
        entries = line.split(",")
        salesperson = entries[0]
        melons = entries[2]

        if salesperson in salespeople:
            position = salespeople.index(salesperson)
            melons_sold[position] += melons
        else:
            salespeople.append(salesperson)
            melons_sold.append(melons)


    for i in salespeople:
        print salespeople[i], melons[i]



if __name__ == "__main__":
    main()
