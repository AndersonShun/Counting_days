import datetime
import sys

def check_input():
    pass

def get_new_date():
    new_date = raw_input("In YYYY-MM-DD format: ")

    # put some checks here to make sure format is correct/date not in the future
    return new_date  # must be string

def change_date():
    date_choice_input = raw_input("1. Use today's date.\n2. Enter defrosting date.\n>>")
    if date_choice_input == "1":
        with open("defrost_date.txt", "w") as dd:
            dd.write(datetime.date.today().isoformat())
        check_age()
    elif date_choice_input == "2":
        with open("defrost_date.txt", "w") as dd:
            dd.write(get_new_date())
        check_age()
    else:
        sys.exit(0)

def check_age():
    with open("defrost_date.txt", "r") as from_file:
        full_date = from_file.read()
    #look for datetime format - can take yyyy-mm-dd directly?
    #checks for appropriate input as well here

    defrost_year = int(full_date[0:4])
    defrost_month = int(full_date[5:7])
    defrost_day = int(full_date[8:10])

    defrosted = datetime.date(defrost_year, defrost_month, defrost_day)
    today = datetime.date.today()
    delta = today - defrosted

    if delta < datetime.timedelta(16):
        result = "fine for experiments"
    else:
        result = "throw them away and get new ones"

    print "The DKO 23-47 cells were defrosted on %s.\nToday is %s." % (str(defrosted), str(today))
    print "They have been growing for %r days since defrosting - %s.\n" % (delta.days, result)

    choice = raw_input("1. Change defrosting date.\n2. Check age again.\n3. Quit.\n>>")

    if choice == "1":
        change_date()
    elif choice == "2":
        check_age()
    else:
        sys.exit(0)

if __name__ == "__main__":
    print "\033[1m" + "Days Since Defrosting DKO Cells" + "\033[0m"  # makes a nice bold title
    check_age()