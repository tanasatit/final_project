# import database module
from database import CSV, DB, Table


# define a funcion called initializing


def initializing():
    csv1 = CSV('persons.csv')
    persons = csv1.read_csv()
    my_DB = DB()
    person_tb = Table('persons', persons)
    my_DB.insert(person_tb)
    cvs2 = CSV('login.csv')
    login_ = cvs2.read_csv()
    login_tb = Table('login', login_)
    my_DB.insert(login_tb)
    return my_DB


# here are things to do in this function:

# create an object to read all csv files that will serve as a persistent state for this program

# create all the corresponding tables for those csv files

# see the guide how many tables are needed

# add all these tables to the database


# define a function called login

def login():
    data = initializing()
    l = data.search('login')
    print(l)
    username = input("username: ")
    password = input("password: ")
    id_role = []
    for i in l.table:
        if i['username'] == username and i['password'] == password:
            id_role.append(i['ID'])
            id_role.append(i['role'])
            return id_role
    return None


# here are things to do in this function:
# add code that performs a login task
# ask a user for a username and password
# returns [person_id, role] if valid, otherwise returning None

# define a function called exit


def exit():
    return


# here are things to do in this function: write out all the tables that have been modified to the corresponding csv
# files By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project,
# you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the
# link below for a tutorial on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
val = login()
if val is None:
    print("Your username or password is incorrect.")
else:
    print(val)

# based on the return value for login, activate the code that performs activities according to the role defined for
# that person_id

# if val[1] == 'admin':
# # see and do admin related activities
#
# elif val[1] == 'student':
# # see and do student related activities
# elif val[1] == 'member':
# # see and do member related activities
# elif val[1] == 'lead':
# # see and do lead related activities
# elif val[1] == 'faculty':
# # see and do faculty related activities
# elif val[1] == 'advisor':
# # see and do advisor related activities

# once everyhthing is done, make a call to the exit function
exit()
