log_file = open("um-server-01.log")

def sales_reports(log_file):
	for line in my_file:
	    line = line.rstrip()
	    day = line[0:3]
	    if day == "Tue":
	        print line





def main(log_file):
	sales_reports(log_file)


if __name__ == '__main__':	
	main(log_file)
