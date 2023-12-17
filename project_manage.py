# import database module
import csv
import random
from database import CSV, DB, Table


# define a function called initializing


def initializing():
    my_db = DB()
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
    my_db.insert(login_tb)
    my_db.insert(project_tb)
    my_db.insert(advisor_pending_tb)
    my_db.insert(member_pending_tb)
    return my_db


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

    def see_request(self):
        for i in self.data3.filter(lambda x: x['to_be_member'] == self.username).table:
            for j in self.data2.table:
                if i['ProjectID'] == j['ProjectID']:
                    print(f"Project name: {j['Title']} , ID: {j['ProjectID']} request to become a member.")
        print()

    def answer_request(self):
        for i in self.data3.filter(lambda x: x['to_be_member'] == self.username).table:
            for j in self.data2.table:
                if i['ProjectID'] == j['ProjectID']:
                    ans = input(f"Project name {j['Title']} , ProjectID: {j['ProjectID']} (accept / deny): ")
                    if ans == 'accept':
                        if j['Member1'] is None or j['Member1'] == '':
                            self.data2.update_row('ProjectID', j['ProjectID'], 'Member1', self.username)
                            self.data3.update_row('to_be_member', self.username, 'Response', ans)
                            self.data1.update_row('ID', self.ID, 'role', 'member')
                            print("You have already joined.")
                        elif j['Member2'] is None or j['Member2'] == '':
                            self.data2.update_row('ProjectID', j['ProjectID'], 'Member2', self.username)
                            self.data3.update_row('to_be_member', self.username, 'Response', ans)
                            self.data1.update_row('ID', self.ID, 'role', 'member')
                            print("You have already joined.")
                        elif (j['Member1'] is not None or j['Member1'] != '') and (
                                j['Member2'] is not None or j['Member2'] != ''):
                            print("Members are full. Unable to get in.")
                    if ans == 'deny':
                        self.data3.update_row('to_be_member', self.username, 'Response', ans)
                    else:
                        print()

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
        print(self.project_dict)


class Leader:
    def __init__(self):
        self.ID = val[0]
        self.data1 = data.search('login')
        self.data2 = data.search('project')
        self.data3 = data.search('member_pending_request')
        self.data4 = data.search('advisor_pending_request')
        self.member_request = {}
        self.advisor_request = {}
        for i in self.data1.filter(lambda x: x['ID'] == self.ID).table:
            self.member_name = i['username']
        for j in self.data2.filter(lambda x: x['Lead'] == self.member_name).table:
            self.project_id = j['ProjectID']
            self.status = j['Status']
            self.project = j

    def see_project_status(self):
        member_status = self.data3.filter(lambda x: x['ProjectID'] == self.project_id) \
            .select(['to_be_member', 'Response'])
        advisor_status = (self.data4.filter(lambda x: x['ProjectID'] == self.project_id)
                          .select(['to_be_advisor', 'Response']))
        print(f'Project status: {self.project}\nMember status: {member_status}\nAdvisor status: {advisor_status}')
        if self.status == 'approve':
            print('project is evaluating by faculty')
        if self.status == 'disapprove':
            print(f'project is disapprove., Please edit and submit again.')
        if '/10' in self.status:
            print("Project is successful!")

    def edit_project_status(self):
        self.data2.update_row('ProjectID', self.project_id, 'Status', 'In progress')

    def sent_member_request(self):
        student_filter = self.data1.filter(lambda x: x['role'] == 'student').select(['username'])
        print(student_filter)
        member_name = input('sent member request to username: ')
        self.member_request['ProjectID'] = self.project_id
        self.member_request['to_be_member'] = member_name
        self.member_request['Response'] = 'Pending'
        self.member_request['Response_date'] = '17-12-23'
        self.data3.insert_row(self.member_request)

    def sent_advisor_request(self):
        advisor_filter = self.data1.filter(lambda x: x['role'] == 'faculty').select(['username'])
        print(advisor_filter)
        advisor_name = input('sent advisor request to username: ')
        self.advisor_request['ProjectID'] = self.project_id
        self.advisor_request['to_be_advisor'] = advisor_name
        self.advisor_request['Response'] = 'Pending'
        self.advisor_request['Response_date'] = '17-12-23'
        self.data4.insert_row(self.advisor_request)

    def submit_project(self):
        if (self.project['Member1'] != '' and self.project['Member2'] != '' and self.project['Advisor'] != ''
                and self.project['Status'] == 'In progress'):
            self.data2.update_row('ProjectID', self.project_id, 'Status', 'submit')
            print("project is submitted.")
        else:
            print("Project is incomplete.")


class Member:
    def __init__(self):
        self.ID = val[0]
        self.data1 = data.search('login')
        self.data2 = data.search('project')
        self.data3 = data.search('member_pending_request')
        self.data4 = data.search('advisor_pending_request')
        for i in self.data1.filter(lambda x: x['ID'] == self.ID).table:
            self.member_name = i['username']
        for j in self.data2.filter(
                lambda x: x['Member1'] == self.member_name or x['Member2'] == self.member_name).table:
            self.project_id = j['ProjectID']
            self.status = j['Status']
            self.project = j

    def see_project_status(self):
        # member_status = self.data3.filter(lambda x: x['ProjectID'] == self.project_id) \
        #     .select(['to_be_member', 'Response'])
        # advisor_status = (self.data4.filter(lambda x: x['ProjectID'] == self.project_id)
        #                   .select(['to_be_advisor', 'Response']))
        print(f'Project status: {self.project}')
        if self.status == 'approve':
            print('project is evaluating by faculty')
        if self.status == 'disapprove':
            print(f'project is disapprove., Please edit and submit again.')
        if '/10' in self.status:
            print("Project is successful!")

    def do_project(self):
        self.data2.update_row('ProjectID', self.project_id, 'Status', 'In progress')


class Admin:
    def __init__(self):
        self.ID = val[0]
        self.data1 = data.search('login')
        self.data2 = data.search('project')
        self.data3 = data.search('member_pending_request')
        self.data4 = data.search('advisor_pending_request')
        self.edit_name = ''
        self.role_who = ''
        self.name_person = ''

    def see(self):
        print("(1.)login table\n(2.)project table\n(3.)member_pending_request table\n(4.)advisor_pending_request")
        num = int(input("choose number: "))
        if num == 1:
            print(self.data1)
        if num == 2:
            print(self.data2)
        if num == 3:
            print(self.data3)
        if num == 4:
            print(self.data4)

    def edit(self):
        print("(1.)login table\n(2.)project table\n(3.)member_pending_request table\n(4.)advisor_pending_request")
        num = int(input("Select the table number you want to edit: "))

        if num == 1:
            print(self.data1.select(['ID', 'username']))
            id_who = input("Please select login ID: ")
            key_edit = input("Please select the key you want to edit (ID), (username), (password), (role): ")
            old_value = self.data1.filter(lambda x: x['ID'] == id_who).select(key_edit)
            value_edit = input(f"Edit value {old_value} to: ")
            for i in self.data1.filter(lambda x: x['ID'] == id_who).table:
                self.edit_name = i['username']  # login table
            if key_edit == 'ID':
                self.data1.update_row('ID', id_who, key_edit, value_edit)
            if key_edit == 'username':
                for i in self.data1.filter(lambda x: x['ID'] == id_who).table:
                    self.role_who = i['role']
                    if self.role_who == 'lead':  # 1,2
                        self.data1.update_row('ID', id_who, key_edit, value_edit)
                        self.data2.update_row('Lead', self.edit_name, 'Lead', value_edit)
                    if self.role_who == 'member':  # 1,2,3
                        self.data1.update_row('ID', id_who, key_edit, value_edit)
                        if self.data2.filter(lambda x: x['Member1'] == self.edit_name):
                            self.data2.update_row('Member1', self.edit_name, 'Member1', value_edit)
                        if self.data2.filter(lambda x: x['Member2'] == self.edit_name):
                            self.data2.update_row('Member2', self.edit_name, 'Member2', value_edit)
                        self.data3.update_row('to_be_member', self.edit_name, 'to_be_member', value_edit)
                    if self.role_who == 'student':  # 1
                        self.data1.update_row('ID', id_who, key_edit, value_edit)
                    if self.role_who == 'faculty':
                        self.data1.update_row('ID', id_who, key_edit, value_edit)
                        self.data4.update_row('to_be_advisor', self.edit_name, 'to_be_advisor', value_edit)
                    if self.role_who == 'advisor':  # 1,2,4
                        self.data1.update_row('ID', id_who, key_edit, value_edit)
                        self.data2.update_row('Advisor', self.edit_name, 'Advisor', value_edit)
                        self.data4.update_row('to_be_advisor', self.edit_name, 'to_be_advisor', value_edit)
            if key_edit == 'password':
                self.data1.update_row('ID', id_who, key_edit, value_edit)
            if key_edit == 'role':
                self.data1.update_row('ID', id_who, key_edit, value_edit)

        if num == 2:
            print(self.data2.select(['ProjectID']))
            project_ID = input("Please select project ID: ")
            key_edit = input("Please select the key you want to edit (ProjectID), (Title), (Lead), (Member1), "
                             "(Member2), (Advisor), (Status): ")
            old_value = self.data2.filter(lambda x: x['ProjectID'] == project_ID).select(key_edit)
            value_edit = input(f"Edit value {old_value} to: ")
            if key_edit == 'ProjectID':  # 2,3,4
                self.data2.update_row('ProjectID', project_ID, key_edit, value_edit)
                self.data3.update_row('ProjectID', project_ID, key_edit, value_edit)
                self.data4.update_row('ProjectID', project_ID, key_edit, value_edit)
            if key_edit == 'Title':  # 2
                self.data2.update_row('ProjectID', project_ID, key_edit, value_edit)
            if key_edit == 'Lead':  # 1,2
                for i in self.data2.filter(lambda x: x['ProjectID'] == project_ID).table:
                    self.name_person = i['Lead']
                self.data2.update_row('ProjectID', project_ID, key_edit, value_edit)
                self.data1.update_row('username', self.name_person, 'username', value_edit)
            if key_edit == 'Member1':  # 1,2,3
                for i in self.data2.filter(lambda x: x['ProjectID'] == project_ID).table:
                    self.name_person = i['Member1']
                self.data2.update_row('ProjectID', project_ID, key_edit, value_edit)
                self.data1.update_row('username', self.name_person, 'username', value_edit)
                self.data3.update_row('to_be_member', self.name_person, 'to_be_member', value_edit)
            if key_edit == 'Member2':  # 1,2,3
                for i in self.data2.filter(lambda x: x['ProjectID'] == project_ID).table:
                    self.name_person = i['Member2']
                self.data2.update_row('ProjectID', project_ID, key_edit, value_edit)
                self.data1.update_row('username', self.name_person, 'username', value_edit)
                self.data3.update_row('to_be_member', self.name_person, 'to_be_member', value_edit)
            if key_edit == 'Advisor':  # 1,2,4
                for i in self.data2.filter(lambda x: x['ProjectID'] == project_ID).table:
                    self.name_person = i['Advisor']
                self.data2.update_row('ProjectID', project_ID, key_edit, value_edit)
                self.data1.update_row('username', self.name_person, 'username', value_edit)
                self.data4.update_row('to_be_advisor', self.name_person, 'to_be_advisor', value_edit)
            if key_edit == 'Status':  # 2
                self.data2.update_row('ProjectID', project_ID, key_edit, value_edit)

        if num == 3:
            print(self.data3.select(['ProjectID', 'to_be_member']))
            project_ID = input("Please select project ID: ")
            print(self.data3.filter(lambda x: x['ProjectID'] == project_ID).select(['to_be_member']))
            name_mem = input(f"Please select name member request from ProjectID {project_ID}: ")
            key_edit = input("Please select the key you want to edit (ProjectID), (to_be_member), "
                             "(Response), (Response_date): ")
            old_value = self.data3.filter(lambda x: x['ProjectID'] == project_ID
                                                    and x['to_be_member'] == name_mem).select(key_edit)
            value_edit = input(f"Edit value {old_value} to: ")
            if self.data3.filter(lambda x: x['ProjectID'] == project_ID
                                           and x['to_be_member'] == name_mem):
                if key_edit == 'ProjectID':
                    self.data2.update_row('ProjectID', project_ID, key_edit, value_edit)
                    self.data3.update_row('ProjectID', project_ID, key_edit, value_edit)
                    self.data4.update_row('ProjectID', project_ID, key_edit, value_edit)
                if key_edit == 'to_be_member':
                    self.data3.update_row('to_be_member', name_mem, key_edit, value_edit)
                    self.data1.update_row('username', name_mem, 'username', value_edit)
                    if self.data2.filter(lambda x: x['Member1'] == name_mem):
                        self.data2.update_row('Member1', name_mem, 'Member1', value_edit)
                    if self.data2.filter(lambda x: x['Member2'] == name_mem):
                        self.data2.update_row('Member2', name_mem, 'Member2', value_edit)
                if key_edit == 'Response':
                    self.data3.update_row('to_be_member', name_mem, key_edit, value_edit)
                if key_edit == 'Response_date':
                    self.data3.update_row('to_be_member', name_mem, key_edit, value_edit)

        if num == 4:
            print(self.data4.select(['ProjectID', 'to_be_advisor']))
            project_ID = input("Please select project ID: ")
            print(self.data4.filter(lambda x: x['ProjectID'] == project_ID).select(['to_be_advisor']))
            name_adv = input(f"Please select name advisor request from ProjectID {project_ID}: ")
            key_edit = input("Please select the key you want to edit (ProjectID), (to_be_advisor), "
                             "(Response), (Response_date): ")
            old_value = self.data4.filter(lambda x: x['ProjectID'] == project_ID
                                           and x['to_be_advisor'] == name_adv).select(key_edit)
            value_edit = input(f"Edit value {old_value} to: ")
            if self.data4.filter(lambda x: x['ProjectID'] == project_ID
                                           and x['to_be_advisor'] == name_adv):
                if key_edit == 'ProjectID':
                    self.data2.update_row('ProjectID', project_ID, key_edit, value_edit)
                    self.data3.update_row('ProjectID', project_ID, key_edit, value_edit)
                    self.data4.update_row('ProjectID', project_ID, key_edit, value_edit)
                if key_edit == 'to_be_advisor':
                    self.data4.update_row('to_be_advisor', name_adv, key_edit, value_edit)
                    self.data1.update_row('username', name_adv, 'username', value_edit)
                    if self.data2.filter(lambda x: x['Advisor'] == name_adv):
                        self.data2.update_row('Advisor', name_adv, 'Advisor', value_edit)
                if key_edit == 'Response':
                    self.data4.update_row('to_be_member', name_adv, key_edit, value_edit)
                if key_edit == 'Response_date':
                    self.data4.update_row('to_be_member', name_adv, key_edit, value_edit)


class Faculty:
    def __init__(self):
        self.ID = val[0]
        self.data1 = data.search('login')
        self.data2 = data.search('project')
        self.data3 = data.search('member_pending_request')
        self.data4 = data.search('advisor_pending_request')
        for i in self.data1.filter(lambda x: x['ID'] == self.ID).table:
            self.username = i['username']
        for j in self.data2.filter(lambda x: x['Status'] == 'approve').table:
            self.project_id = j['ProjectID']
            self.project = j

    def see_request_advisor(self):
        for i in self.data4.filter(lambda x: x['to_be_advisor'] == self.username).table:
            for j in self.data2.table:
                if i['ProjectID'] == j['ProjectID']:
                    print(f"Project name: {j['Title']} , ID: {j['ProjectID']} have been asked to become advisor.")

    def answer_request_advisor(self):
        for i in self.data4.filter(lambda x: x['to_be_advisor'] == self.username).table:
            for j in self.data2.table:
                if i['ProjectID'] == j['ProjectID']:
                    ans = input(f"Project name {j['Title']} , ProjectID: {j['ProjectID']} (accept / deny): ")
                    if ans == 'accept':
                        if j['Advisor'] is None or j['Advisor'] == '':
                            self.data2.update_row('ProjectID', j['ProjectID'], 'Advisor', self.username)
                            self.data4.update_row('to_be_advisor', self.username, 'Response', ans)
                            self.data1.update_row('ID', self.ID, 'role', 'advisor')
                            print("You're a advisor.")
                        elif j['Advisor'] is not None or j['Member1'] != '':
                            print("This project already have advisor.")
                    if ans == 'deny':
                        self.data4.update_row('to_be_advisor', self.username, 'Response', ans)
                    else:
                        print()

    def see_approve_projects(self):
        project_filter = self.data2.filter(lambda x: x['Status'] == 'approve').table
        if not project_filter:
            print("no approve project")
        else:
            print(project_filter)

    def evaluator_project(self):
        project_filter = self.data2.filter(lambda x: x['Status'] == 'approve').table
        if not project_filter:
            print("no approve project")
        else:
            num = int(input(f"Evaluate Project {self.project['Title']} on a score of 10.: "))
            if not (0 <= num <= 10):
                raise ValueError
            score = str(num) + '/10'
            self.data2.update_row('ProjectID', self.project_id, 'Status', score)
            print("finish evaluate project!")


class Advisor:
    def __init__(self):
        self.ID = val[0]
        self.data1 = data.search('login')
        self.data2 = data.search('project')
        self.data3 = data.search('member_pending_request')
        self.data4 = data.search('advisor_pending_request')
        for i in self.data1.filter(lambda x: x['ID'] == self.ID).table:
            self.username = i['username']
        for j in self.data2.filter(lambda x: x['Advisor'] == self.username).table:
            self.project_id = j['ProjectID']
            self.project = j

    def see(self):
        project_filter = self.data2.filter(lambda x: x['Status'] == 'submit' and x['Advisor'] == self.username).table
        if not project_filter:
            print('no submitted project')
        print(project_filter)

    def sent_approve(self):
        ans = input(f"Project: {self.project['Title']}, ProjectID: {self.project_id} (approve / disapprove): ")
        if ans == 'approve':
            print("project is approve")
            self.data2.update_row('Advisor', self.username, 'Status', ans)
        if ans == 'disapprove':
            print("project is disapprove.")  # , Please edit and resubmit
            self.data2.update_row('Advisor', self.username, 'Status', ans)


# here are things to do in this function:
# write out all the tables that have been modified to the corresponding csv files
# By now, you know how to read in a csv file and transform it into a list of dictionaries.
# For this project, you also need to know how to do the reverse
# , i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

data = initializing()
# print(data.search('login').select(['username', 'password', 'role']))
val = login()
while val is None:
    print("Your username or password is incorrect, Please try again.")
    print()
    val = login()
print(val)
# based on the return value for login, activate the code
# that performs activities according to the role defined for that person_id

if val[1] == 'admin':
    person0 = Admin()
    print("What would you like to do.\n1.See data\n2.Edit data\n0. Exit")
    see_and_do = int(input("Enter number: "))
    while see_and_do != 0:
        print()
        if see_and_do == 1:
            person0.see()
        if see_and_do == 2:
            person0.edit()
        print()
        print("What would you like to do.\n1.See data\n2.Edit data\n0. Exit")
        see_and_do = int(input("Enter a number: "))
# see and do admin related activities

elif val[1] == 'student':
    person = Student()
    print("What would you like to do.\n1. See member request\n2.Answer member request\n3. Create new project\n0. Exit")
    see_and_do = int(input("Enter number: "))
    while see_and_do != 0:
        print()
        if see_and_do == 1:
            person.see_request()
        elif see_and_do == 2:
            person.answer_request()
        elif see_and_do == 3:
            person.create_new_project()
        else:
            print()
        print("What would you like to do.\n1. See member request\n2.Answer member request"
              "\n3. Create new project\n0. Exit")
        see_and_do = int(input("Enter number: "))

# see and do student related activities
elif val[1] == 'member':
    person2 = Member()
    print("What would you like to do.\n1.See project status\n2.Edit project\n0. Exit")
    see_and_do = int(input("Enter number: "))
    while see_and_do != 0:
        print()
        if see_and_do == 1:
            person2.see_project_status()
        if see_and_do == 2:
            person2.do_project()
        print()
        print("What would you like to do.\n1.See project status\n2.Edit project\n0. Exit")
        see_and_do = int(input("Enter a number: "))
# see and do member related activities
elif val[1] == 'lead':
    person3 = Leader()
    print("What would you like to do.\n1.See project status\n2.Edit project\n3.Sent member request"
          "\n4.Sent advisor request\n5. Submit a project\n0. Exit")
    see_and_do = int(input("Enter number: "))
    while see_and_do != 0:
        print()
        if see_and_do == 1:
            person3.see_project_status()
        if see_and_do == 2:
            person3.edit_project_status()
        if see_and_do == 3:
            person3.sent_member_request()
        if see_and_do == 4:
            person3.sent_advisor_request()
        if see_and_do == 5:
            person3.submit_project()
        print()
        print("What would you like to do.\n1.See project status\n2.Edit project\n3.Sent member request"
              "\n4.Sent advisor request\n5. Submit a project\n0. Exit")
        see_and_do = int(input("Enter a number: "))

# see and do lead related activities
elif val[1] == 'faculty':
    person4 = Faculty()
    print("What would you like to do.\n1.See advisor request\n2.Answer advisor request"
          "\n3.See approve project\n4.Evaluate project\n0. Exit")
    see_and_do = int(input("Enter number: "))
    while see_and_do != 0:
        print()
        if see_and_do == 1:
            person4.see_request_advisor()
        if see_and_do == 2:
            person4.answer_request_advisor()
        if see_and_do == 3:
            person4.see_approve_projects()
        if see_and_do == 4:
            person4.evaluator_project()
        print()
        print("What would you like to do.\n1.See advisor request\n2.Answer advisor request"
              "\n3.See approve project\n4.Evaluate project\n0. Exit")
        see_and_do = int(input("Enter a number: "))

# see and do faculty related activities
elif val[1] == 'advisor':
    person5 = Advisor()
    print("What would you like to do.\n1.See submitted project \n2.Approve project\n0. Exit")
    see_and_do = int(input("Enter number: "))
    while see_and_do != 0:
        print()
        if see_and_do == 1:
            person5.see()
        if see_and_do == 2:
            person5.sent_approve()
        print()
        print("What would you like to do.\n1.See submitted project \n2.Approve project\n0. Exit")
        see_and_do = int(input("Enter a number: "))

# see and do advisor related activities

# once everything is done, make a call to the exit function
exit()
