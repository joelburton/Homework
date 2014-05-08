def main():
    my_file = open("original_file.dat")
    days = []
    for line in my_file:
        words = line.split()
        day = words[0]
        days.append(day)

    my_file.close

    my_file = open("original_file.dat")
    melon_types = []
    for line in my_file:
        words = line.split()
        melon = words[0]
        melon_types.append(melon_type)

    my_file.close

    my_file = open("original_file.dat")
    statuses = []
    for line in my_file:
        words = line.split()
        status = words[0]
        statuses.append(status)

    my_file.close

    for i in range(len(days)):
        print days[i], melon_types[i], statuses[i]


if __name__ == "__main__":
    main()
