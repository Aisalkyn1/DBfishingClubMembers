import json
import random
import pickle
import ast


class Member():
    def __init__(self, lname, fname, saddress, pnumber, prize, mtype):
        self.lname = lname
        self.fname = fname
        self.saddress = saddress
        self.pnumber = pnumber
        self.prize = prize
        self.mtype = mtype

    def get_data(self):
        member = {"lname": self.lname, "fname": self.fname, "saddress": self.saddress, "pnumber": self.pnumber,
                  "prize": self.prize, "mtype": self.mtype}
        return str(member)


def display_members(m):
    for key, value in m.items():
        value = ast.literal_eval(value)
        print(
            f"{key} {value['lname']} {value['fname']} {value['saddress']} {value['pnumber']} {value['prize']} {value['mtype']}")


def addmember(m):
    add = "1"
    while add == "1":
        lname = input("Please enter last name: ")
        while len(lname)== 0 or len(lname) > 30:
            print("Invalid input. Try again.")
            lname = input("Please enter last name: ")
        fname = input("Please enter first name: ")
        while len(fname)== 0 or len(fname) > 30:
            print("Invalid input. Try again.")
            fname = input("Please enter first name: ")
        saddress = input("Please enter street address: ")
        while len(saddress)== 0 or len(saddress) > 50:
            print("Invalid input. Try again.")
            saddress = input("Please enter street address: ")
        pnumber = input("Please enter phone number: ")
        while len(pnumber)== 0 or len(pnumber) > 12:
            print("Invalid input. Try again.")
            pnumber = input("Please enter phone number: ")
        prize = float(input("Please enter prize money(0 to 5000.00 inclusive): "))
        while 0 > prize or prize > 5000.00:
            print("Invalid input. Try again!")
            prize = float(input("Please enter prize money(0 to 5000.00 inclusive): "))            
        mtype = input("Please enter membership type (full or associate): ")
        while mtype not in ("full", "associate"):
            mtype = input("Wrong input.Please enter membership type (full or associate): ")
        mid = random.randint(1, 999)
        while mid in m:
            mid = random.randint(1, 999)
        if mid not in m:
            print("Member ID is: ", mid)
        member = Member(lname, fname, saddress, pnumber, prize, mtype)
        m[str(mid)] = member.get_data()
        add = input("Please choose 1 - add member \n 2 - exit: ")
    return 'asd'


def load_member():
    try:
        with open("members.dat", "rb") as db:
            data = pickle.load(db)
    except IOError as e:
        print(e)
    else:
        return data


def exitsave(m):
    with open("members.dat", "wb") as db:
        pickle.dump(m, db)


def search_member(m):
    sm = input("Please enter member ID: ")
    r = m.get(sm, "Member not found")
    print(r)


def delete_m(m):
    s = input("Enter member ID you want to delete the details: ")
    if s in m:
        del m[s]
        print("Member deleted!")
    else:
        print("Not found. Sorry!")


def update_m(m):
    key = input("\nEnter the member ID you want change details: ")
    choice = None

    while key in m:
        choice = input("""\nPlease select option that you want to update:
              1 - Change last Name
              2 - Change first Name
              3 - Change street address
              4 - Change phone number
              5 - Change money prize
              6 - Change Membership type
              0 - Go to main menu
:""")

        member = ast.literal_eval(m[key])
        if choice == "1":
            lname = input("\nPlease enter new last name: ")
            member['lname'] = lname
        elif choice == "2":
            fname = input("\nPlease enter new first name: ")
            member['fname'] = fname
        elif choice == "3":
            saddress = input("\nPlease enter new street address: ")
            member['saddress'] = saddress
        elif choice == "4":
            pnumber = input("\nPlease enter new phone number: ")
            member['pnumber'] = pnumber
        elif choice == "5":
            prize = input("\nPlease enter new money prize: ")
            member['prize'] = prize
        elif choice == "6":
            mtype = input("\nPlease enter new membership type: ")
            member['mtype'] = mtype
        elif choice == "0":
            break
        else:
            print("Invalid input. Try again!")
        m[key] = str(member)
        exitsave(m)
    else:
        print("\nMember ID not found!")


def mainmenu():
    choice = None
    m = load_member()
    display_members(m)
    while choice != '0':
        print("""
        Member Maintenance
        0 - Exit
        1 - Add a member
        2 - Search for a member
        3 - Delete a member
        4 - Update a member
        5 - Display a member's report
        """)

        choice = input("Please choose the option: ")

        if choice == '0':
            exitsave(m)
            print("See you later.")
        elif choice == '1':
            addmember(m)
        elif choice == '2':
            search_member(m)
        elif choice == '3':
            delete_m(m)
        elif choice == '4':
            update_m(m)
        elif choice == '5':
            display_members(m)


mainmenu()

("\n\nPress the enter key to exit.")
