print "Day 1"
the_file = open("um-deliveries-20140519.txt", "r")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]
        
    print "Delivered %s %ss for total of $%s" % (count, melon, amount)
the_file.close()


print "Day 2"
the_file = open("um-deliveries-20140520.txt", "r")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]
        
    print "Delivered %s %ss for total of $%s" % (count, melon, amount)
the_file.close()


print "Day 3"
the_file = open("um-deliveries-20140521.txt", "r")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]
        
    print "Delivered %s %ss for total of $%s" % (count, melon, amount)
the_file.close()    








