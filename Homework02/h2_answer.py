get_data(file_name):
    my_file = open(file_name)

    for line in my_file:
        words = line.split()
        day = words[0]
        melon = words[1]
        status = words[2]
        print day.upper(), melon.upper(), status.upper()
    my_file.close()

def main():
    print "WEEK 1"
    get_data("week1.csv")
    print "WEEK 2"
    get_data("week2.csv")
    print "WEEK 3"
    get_data("week3.csv")

if __name__ == "__main__":
    main()