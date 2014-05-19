def main():

    print "WEEK 1"
    my_file = open(get_data("week1.csv"))

    for line in my_file:
        words = line.split()
        day = words[1]
        melon = words[1]
        status = words[1]
        print day, melon, status
    my_file.close()

    print "WEEK 2"
    my_file = open(get_data("week2.csv"))

    for line in my_file:
        words = line.split()
        day = words[1]
        melon = words[1]
        status = words[1]
        print day, melon, status
    my_file.close()

    print "WEEK 3"
    my_file = open(get_data("week3.csv"))

    for line in my_file:
        words = line.split()
        day = words[1]
        melon = words[1]
        status = words[1]
        print day, melon, status
    my_file.close()



if __name__ == "__main__":
    main()