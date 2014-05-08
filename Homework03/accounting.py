def main():
    f = open("melon_logs.log")
    # input = aggregate melons
    
    melon_tallies = {"musk": 0, "honeydew": 0, "bitter": 0}
    for line in f:
        data = line.split(":")
        melon_type = data[3]
        melon_count = int(data[4])

        melon_tallies[melon_type] += melon_count
    f.close()

    total_revenue = 0
    melon_prices = {
            "musk": 1.15,
            "honeydew": 2.30,
            "bitter": 0.5
            }
    total_revenue = 0
    for melon_type, melon_count in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_count
        total_revenue += revenue

    f = open("melon_logs.log")
    total_spend = 0
    for line in f:
        data = line.split(":")
        if data[0] == "SPEND":
            amt = float(data[1])
            total_spend += amt

    total_income = total_revenue - total_spend
    if total_income <= 0:
        color = '\033[91m'
    else:
        color = '\033[92m'
    print "We made this much money:", color + "%f"%total_income + '\033[0m'


if __name__ == "__main__":
    main()
