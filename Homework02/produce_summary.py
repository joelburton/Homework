
def melon_count(day_number, path):
    print "Day %d" % day_number
    the_file = open(path, "r")
    for line in the_file:
        line = line.rstrip()
        line = line.upper()
        words = line.split(',')

        melon = words[0]
        count = words[1]
        amount = words[2]
        
        print ("Delivered %s %ss for total of $%s" % (
            count, melon, amount)).upper()
    the_file.close()

    print


# for path in ["file2", "file3"]:
#     melon_count(path)

melon_count(1, "./um-deliveries-20140519.csv")
melon_count(2, "um-deliveries-20140520.csv")
melon_count(3, "um-deliveries-20140521.csv")







