def main():

    print "\n",
    print "WEEK 1"
    print "Date\t\tTotal Orders\tMelons Delivered"
    print "-------------------------------------------"
    log_file = open("um-deliveries-20140507.csv")
    # first line of log file contains headers, skip it
    headers = log_file.readline()

    total_orders = 0.0
    total_melons = 0
    last_date = ''
    
    for line in log_file:
        words = line.rstrip().split(",")
        day = words[0]
        melon_count = words[1]
        order_total = words[2]

        if day != last_date and last_date != '':
            print "%s\t$%0.2f\t%d melons" % (last_date, total_orders, total_melons)
        
        total_orders += float(order_total)
        total_melons += int(melon_count)
        last_date = day
        
    print "%s\t$%0.2f\t%d melons" % (last_date, total_orders, total_melons)
        
    log_file.close()

    print "\n",
    print "WEEK 2"
    print "Date\t\tTotal Orders\tMelons Delivered"
    print "-------------------------------------------"
    log_file = open("um-deliveries-20140514.csv")
    # first line of log file contains headers, skip it
    headers = log_file.readline()

    total_orders = 0.0
    total_melons = 0
    last_date = ''
    
    for line in log_file:
        words = line.rstrip().split(",")
        day = words[0]
        melon_count = words[1]
        order_total = words[2]

        if day != last_date and last_date != '':
            print "%s\t$%0.2f\t%d melons" % (last_date, total_orders, total_melons)
        
        
        total_orders += float(order_total)
        total_melons += int(melon_count)
        last_date = day
        
    print "%s\t$%0.2f\t%d melons" % (last_date, total_orders, total_melons)
        
    log_file.close()

    print "\n",
    print "WEEK 3"
    print "Date\t\tTotal Orders\tMelons Delivered"
    print "-------------------------------------------"
    log_file = open("um-deliveries-20140521.csv")
    # first line of log file contains headers, skip it
    headers = log_file.readline()

    total_orders = 0.0
    total_melons = 0
    last_date = ''
    
    for line in log_file:
        words = line.rstrip().split(",")
        day = words[0]
        melon_count = words[1]
        order_total = words[2]

        if day != last_date and last_date != '':
            print "%s\t$%0.2f\t%d melons" % (last_date, total_orders, total_melons)
        
        total_orders += float(order_total)
        total_melons += int(melon_count)
        last_date = day
        
    print "%s\t$%0.2f\t%d melons" % (last_date, total_orders, total_melons)
        
    log_file.close()



if __name__ == "__main__":
    main()