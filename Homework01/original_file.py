def main():
    my_file = open("original_file.dat")
    for line in my_file:
        day = line[0:3]
        if day == "Tue":
            print line

if __name__ == "__main__":
    main()
