# Final project for 2023's 219114/115 Programming I

# My final project include 
1) database.py file consist of
   - class CSV it can open and read file from file.csv and change file to dict
   - class DB  it is a collection of all database.
   - class Table it receive data from CSV ,table name to make or edit the table
2) project_manage.py consist of
   - class Student can see and accept member request , create new project
   - class Leader can see and edit project status , sent member and advisor request , submit a project
   - class Member can see and edit project status
   - class Admin can see and edit all data in the table.
   - class Faculty can see and accept advisor request , see approve project , evaluator project
   - class Advisor can see and approve a submitted project
3) persons.csv, login.csv, project.csv, member_pending_request.csv, advisor_pending_request.csv
   - all of these are file.csv that store database in each part of it.

# A description on how to compile and run your project.
- It starts with login to student role. and have created a project. After that, log out.
- Log back in the leader's role. and sent a member request to other students and send a request to the faculty 
to become project advisors. Finally, update the project status.It will change to 'In progress'. After that, log out.
- Login to a student role to see who has requested member and accept the request. After that, log out.
- Login to a faculty role to see who has requested to be a project advisor. and accept the request. After that, log out.
- Login to a leader role. View the status of All projects If the project has 2 members and 1 advisor. Leaders will be 
able to submit projects. But if it's not complete, it will say that the project is not complete. After that, log out.
- Login to advisor role. to see who has submitted a project If there is, can it be approved or not?
If approved, the project will be sent to others in the faculty for evaluator. 
But if not approved The project will be sent back to the students in project for editing and resubmission. 
After that, log out.
- Login to the faculty roll. and view approved projects You can do an evaluator to give a score. 
 The project is now complete!. After that, log out.

# A table detailing each role and its actions
https://docs.google.com/spreadsheets/d/1g2O8QVkVzORM-bqu99-KILa1GhYcovKutM99qoWv-W0/edit#gid=0
# A list of missing features and outstanding bugs
   - answer_member_request and answer_advisor if it has more than 1 project request when answer and logout in 
member_pending_request and advisor_pending_request,It will show the same last answer
   - in Admin role,I haven't created a 'insert a row into table' function yet