# import database module
import csv
import random
from database import CSV, DB, Table


# define a function called initializing


def initializing():
    my_DB = DB()
    csv1 = CSV('login.csv')
    csv2 = CSV('project.csv')
    csv3 = CSV('advisor_pending_request.csv')
    csv4 = CSV('member_pending_request.csv')
    login_ = csv1.read_csv()
    project = csv2.read_csv()
    advisor_pending = csv3.read_csv()
    member_pending = csv4.read_csv()
    login_tb = Table('login', login_)
    project_tb = Table('project', project)
    advisor_pending_tb = Table('advisor_pending_request', advisor_pending)
    member_pending_tb = Table('member_pending_request', member_pending)
    my_DB.insert(login_tb)
    my_DB.insert(project_tb)
    my_DB.insert(advisor_pending_tb)
    my_DB.insert(member_pending_tb)
    return my_DB


# here are things to do in this function:

# create an object to read all csv files that will serve as a persistent state for this program

# create all the corresponding tables for those csv files

# see the guide how many tables are needed

# add all these tables to the database


# define a function called login

def login():
    user = []
    init = initializing()
    login_info = init.search('login')
    username = input("Enter username: ")
    password = input("Enter password: ")
    for i in login_info.table:
        if username == i['username'] and password == i['password']:
            user.append(i['ID'])
            user.append(i['role'])
            return user
    return None


# here are things to do in this function:
# add code that performs a login task
# ask a user for a username and password
# returns [ID, role] if valid, otherwise returning None

# define a function called exit


def exit():
    my_file1 = open('login.csv', 'w')
    my_file2 = open('project.csv', 'w')
    my_file3 = open('advisor_pending_request.csv', 'w')
    my_file4 = open('member_pending_request.csv', 'w')
    writer1 = csv.writer(my_file1)
    writer2 = csv.writer(my_file2)
    writer3 = csv.writer(my_file3)
    writer4 = csv.writer(my_file4)
    writer1.writerow(['ID', 'username', 'password', 'role'])
    writer2.writerow(['ProjectID', 'Title', 'Lead', 'Member1', 'Member2', 'Advisor', 'Status'])
    writer3.writerow(['ProjectID', 'to_be_advisor', 'Response', 'Response_date'])
    writer4.writerow(['ProjectID', 'to_be_member', 'Response', 'Response_date'])
    for dictionary in data.search('login').table:
        writer1.writerow(dictionary.values())
    for dictionary in data.search('project').table:
        writer2.writerow(dictionary.values())
    for dictionary in data.search('advisor_pending_request').table:
        writer3.writerow(dictionary.values())
    for dictionary in data.search('member_pending_request').table:
        writer4.writerow(dictionary.values())
    my_file1.close()
    my_file2.close()
    my_file3.close()
    my_file4.close()


def new_project_ID():
    ID = ''
    for i in range(6):
        num = random.randint(0, 9)
        ID += str(num)
    return ID


class Student:
    def __init__(self):
        self.ID = val[0]
        self.projectID = new_project_ID()
        self.data1 = data.search('login')
        self.data2 = data.search('project')
        self.data3 = data.search('member_pending_request')
        self.project_dict = {}
        self.name_project = []
        for i in self.data1.filter(lambda x: x['ID'] == self.ID).table:
            self.username = i['username']

    def see_request(self):  # no complete
        for i in self.data3.filter(lambda x: x['to_be_member'] == self.ID).table:
            for j in self.data2.table:
                if i['ProjectID'] == j['ProjectID']:
                    print(f"Project name: {j['Title']} ,ID: {j['ProjectID']} Send a request.")

    def answer_request(self):
        for i in self.data3.filter(lambda x: x['to_be_member'] == self.ID).table:
            for j in self.data2.table:
                if i['ProjectID'] == j['ProjectID']:
                    ans = input(f"Project name {j['Title']} ,ID: {j['ProjectID']} (accept / deny)")
                    if ans == 'accept':
                        self.data3.update_row('ProjectID', i['ProjectID'], 'Response', ans)
                        if j['Member1'] is None:
                            self.data2.update_row('ProjectID', j['ProjectID'], 'Member1', self.username)
                        else:
                            self.data2.update_row('ProjectID', j['ProjectID'], 'Member2', self.username)


                            
    def create_new_project(self):
        self.data1.update_row('ID', self.ID, 'role', 'lead')
        title = input("Input project name: ")
        self.project_dict['ProjectID'] = self.projectID
        self.project_dict['Title'] = title
        self.project_dict['Lead'] = self.username
        self.project_dict['Member1'] = None
        self.project_dict['Member2'] = None
        self.project_dict['Advisor'] = None
        self.project_dict['Status'] = 'Pending'
        self.data2.insert_row(self.project_dict)


class Lead:
    def __init__(self):
        self.ID = val[0]
        self.data1 = data.search('login')
        self.data2 = data.search('project')
        self.data3 = data.search('member_pending_request')
        self.data4 = data.search('advisor_pending-request')
        self.member_request = {}
        for i in self.data1.filter(lambda x: x['ID'] == self.ID).table:
            self.username = i['username']
        for j in self.data2.filter(lambda x: x['Lead'] == self.ID).table:
            self.project_id = j['ProjectID']
            self.status = j['Status']

    def see_status(self):
        member_status = self.data3.filter(lambda x: x['ProjectID'] == self.project_id)\
            .select(['to_be_member', 'Response'])
        advisor_status = ''
        print(f'Project status: {self.status}\nMember status: {member_status}\nAdvisor status: ')

    def update_status_project(self):
        self.data2.update_row('ProjectID', self.project_id, 'Status', 'In progress')

    def sent_member_request(self):
        student_filter = self.data1.filter(lambda x: x['role'] == 'student').select(['ID', 'username'])
        print(student_filter)
        username = input('sent member request to username: ')
        self.member_request['ProjectID'] = self.project_id
        self.member_request['to_be_member'] = username
        self.member_request['Response'] = 'Pending'
        self.member_request['Response_date'] = '17-12-23'
        self.data3.insert_row(self.member_request)

    def sent_advisor_request(self):
        pass


# here are things to do in this function:
# write out all the tables that have been modified to the corresponding csv files
# By now, you know how to read in a csv file and transform it into a list of dictionaries.
# For this project, you also need to know how to do the reverse
# , i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above


data = initializing()
print(data.search('login').table)
val = login()
while val is None:
    print("Your username or password is incorrect, Please try again.")
    print()
    val = login()
print(val)
# based on the return value for login, activate the code
# that performs activities according to the role defined for that person_id

if val[1] == 'admin':
    pass
# see and do admin related activities

elif val[1] == 'student':
    person = Student()
    print("What do you want to do.\n1. See member request\n2. Create new project\n0. Exit")
    see_and_do = int(input("Enter number: "))
    while see_and_do != 0:
        if see_and_do == 1:
            person.see_request()
        elif see_and_do == 2:
            person.create_new_project()
            print(data.search('project'))
        else:
            print()
        print("What do you want to do.\n1. See member request\n2. Create new project\n0. Exit")
        see_and_do = int(input("Enter number: "))

# see and do student related activities
elif val[1] == 'member':
    pass
# see and do member related activities
elif val[1] == 'lead':
    person2 = Lead()
    print("What do you want to do.\n1.See project status\n2.Update status\n3.Sent member request"
          "\n4.Sent advisor request\n0. Exit")
    see_and_do = int(input("Enter number: "))
    while see_and_do != 0:
        if see_and_do == 1:
            person2.see_status()
        if see_and_do == 2:
            person2.update_status_project()
        if see_and_do == 3:
            person2.sent_member_request()
        if see_and_do == 4:
            pass
        print()
        print("What do you want to do.\n1.See project status\n2.Update status\n3.Sent member request"
              "\n4.Sent advisor request\n0. Exit")
        see_and_do = int(input("Enter a number: "))
# see and do lead related activities
# elif val[1] = 'faculty':
# see and do faculty related activities
# elif val[1] = 'advisor':
# see and do advisor related activities

# once everything is done, make a call to the exit function
exit()

# test = new_project_ID()
# print(test)
