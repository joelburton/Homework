def main():

    # Day 1
    print "Day 1"
    my_file = open("um-deliveries-20140519.csv")

    for line in my_file:
        line = line.rstrip()
        words = line.split(',')
        
        melon = words[0]
        count = words[0]
        amount = words[0]
        
        print "Delivered %s %ss for a total of: $%s" % (count, melon, amount)
    my_file.close()
    print "\n",

    # Day 2
    print "Day 2"
    my_file = open("um-deliveries-20140520.csv")

    for line in my_file:
        line = line.rstrip()
        words = line.split(',')
        
        melon = words[0]
        count = words[0]
        amount = words[0]
        
        print "Delivered %s %ss for a total of: $%s" % (count, melon, amount)
    my_file.close()
    print "\n",

    # Day 3
    print "Day 3"
    my_file = open("um-deliveries-20140521.csv")

    for line in my_file:
        line = line.rstrip()
        words = line.split(',')
        
        melon = words[0]
        count = words[0]
        amount = words[0]
        
        print "Delivered %s %ss for a total of: $%s" % (count, melon, amount)
    my_file.close()
    print "\n",

if __name__ == "__main__":
    main()