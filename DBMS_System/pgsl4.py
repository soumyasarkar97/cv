from re import I
from time import time
from types import NoneType
import mysql.connector
#import bcrypt
import sys
import time
import os
import csv
import datetime
from pathlib import Path
import json
import platform
import bcrypt
import getpass
from tabulate import tabulate


def connect():
  mydb = mysql.connector.connect(
    database="pgsl4",
    host="localhost",
    user="root",
    password="cpdl1997$",
    port="3306"
  )
  if mydb.is_connected():
    print('Connection successful')
  return mydb

mydb=connect()
mycursor = mydb.cursor(buffered=True) #buffered=True used to solve unread result found issue -> mysql.connector.errors.InternalError: Unread result found
global_userid=''

def login(type):
    user_operating_system = platform.uname()[0]
    clear_command=''
    if(user_operating_system=='Windows'):
      clear_command='cls'
    else:
      clear_command='clear' #For Linux and MacOS users
    clear = lambda: os.system(clear_command)
    clear()

    try:
        mycursor.execute('SELECT COUNT(*) FROM current_session;')
        current_users=mycursor.fetchone()[0]
        if(current_users>0):
            print('Could not add new session as someone is already logged in. Try again later.\nRedirecting...')
            # adding 5 seconds time delay
            time.sleep(5)
            return '2'
    except Exception as err:
        print('Not able to log in now. Try again later.\nRedirecting...')
        #print\(err\)
        # adding 5 seconds time delay
        time.sleep(5)
        return '0'


    user_id=input("Enter UserID: ")

    try:
        mycursor.execute('SELECT pwd FROM login_details WHERE user_id=%s AND user_type=%s;', (user_id, type))
        hashed_pwd = mycursor.fetchone()[0].encode('utf-8')
    except Exception as err:
        print('Could not verify password. Try again later.\nRedirecting...')
        #print\(err\)
        # adding 5 seconds time delay
        time.sleep(5)
        return '2'
    #_bytes=hashed_pwd.encode('utf-8')

    # Hashing the password
    #hashed_pwd = bcrypt.hashpw(_bytes, bcrypt.gensalt())

    pwd=getpass.getpass("Enter Password: ")

    pwd=pwd.encode('utf-8')

    if bcrypt.checkpw(pwd,hashed_pwd):
        try:
            curr_time = time.strftime('%Y-%m-%d %H:%M:%S')
            mycursor.execute('INSERT INTO current_session VALUES(%s,%s);', (user_id, curr_time)); 
        except Exception as err:
            print('Could not add new session. Try again later.\nRedirecting...')
            #print\(err\)
            # adding 5 seconds time delay
            time.sleep(5)
            return '0'
        mydb.commit()
        return user_id
    else:
        return '0'

def login_screen(type):
    user_operating_system = platform.uname()[0]
    clear_command=''
    if(user_operating_system=='Windows'):
      clear_command='cls'
    else:
      clear_command='clear' #For Linux and MacOS users
    while(1):
        clear = lambda: os.system(clear_command)
        clear()
        print("""Please select action
    1. Enter UserID and Password
    2. Go back to main screen
        """)
        inp=input("Enter your choice: ")
        
        if(inp=='1'):
            result=login(type) # result is userid 
            if (result not in ('0','2')):
                print("Login Successful")
                time.sleep(3)
                return result
                #print msg login sucessful
            elif (result=='2'):
                continue
            else:
                print("Incorrect UserID/Password. Please try again")
                time.sleep(3)
                continue
        elif(inp=='2'):
            return '0'
        
        else:
            print("Please enter valid input")
            time.sleep(3)
            continue

def main_screen():
    user_operating_system = platform.uname()[0]
    clear_command=''
    if(user_operating_system=='Windows'):
      clear_command='cls'
    else:
      clear_command='clear' #For Linux and MacOS users
    inp=0
    while(1):
        clear = lambda: os.system(clear_command)
        clear()
        print("""Welcome to AIMS portal
    
    Please select your Role
    1. Student
    2. Faculty
    3. Staff

    4. Exit
        """)
        inp=input("Enter your choice: ")

        if(inp not in ('1','2','3','4')):
            print("Please enter valid input.")
            time.sleep(3)
            continue

        elif(inp=='4'):
            break
        elif(inp=='1'):
            res=login_screen(3) #res is userid
            if(res!='0'):
                c_sem = input("Enter current semester: ")
                c_year = input("Enter current year: ")
                student_actions(res, c_sem, c_year)
            else:
                continue
            
        elif(inp=='2'):
            res=login_screen(2)
            if(res!='0'):
                faculty_actions(res)
                pass
            else:
                continue
            
        elif(inp=='3'):
            res=login_screen(1)
            if(res!='0'):
                staff_actions(res)
            else:
                continue
            
############################################################### STUDENT SECTION ###############################################################   

#TESTED AND WORKING -> FULLY TESTED
def register_course_student(s_id, current_sem, current_year):
  c_id = input("Enter CourseID of the course in which you want to Register: ")
  #sql query to find whether eligible or not
  np=0 
  p=0
  sum_grade=0.0
  no_of_courses=0
  sum_credits_currrent=0
  c=0
  cnt=0
  ########################## NP=P check ##########################
  try:
      mycursor.execute('SELECT COUNT(*) FROM prereq WHERE c_id = %s;', (c_id,)); 
      np = int(mycursor.fetchone()[0])
  except Exception as err:
      print('Retrieval failed due to incorrect details. Try again.\nRedirecting...')
      #print\(err\)
      # adding 5 seconds time delay
      time.sleep(5)
      return
  try:
      mycursor.execute('SELECT COUNT(*) FROM student_course_mapping WHERE s_id = %s AND c_id IN (SELECT prereq_c_id FROM pgsl4.prereq WHERE c_id = %s);', (s_id, c_id)); 
      p = int(mycursor.fetchone()[0])
  except Exception as err:
      print('Retrieval failed due to incorrect details. Try again.\nRedirecting...')
      #print\(err\)
      # adding 5 seconds time delay
      time.sleep(5)
      return
  if(np!=p):
      print('Did not pass the criteria for prerequisites. Please try something else.\nRedirecting...')
      time.sleep(5)
      return

  ########################## 1.25*AVG>=SUM+C check ##########################
  try:
      mycursor.execute('SELECT SUM(grade) FROM student_course_mapping WHERE s_id = %s AND sem < %s AND sem > %s AND year < %s AND year > %s AND status IN (0, 2);', (str(s_id), int(current_sem), int(current_sem)-3, int(current_year), int(current_year)-2)); 
      sum_grade = mycursor.fetchone()[0]
      if(sum_grade is None):
        sum_grade = 0
      else:
        sum_grade = float(sum_grade)
  except Exception as err:
      print('Retrieval failed due to incorrect details. Try again.\nRedirecting...')
      print(err)
      # adding 5 seconds time delay
      time.sleep(5)
      return
  try:
      mycursor.execute('SELECT COUNT(*) FROM student_course_mapping WHERE s_id = %s AND sem < %s AND sem > %s AND year < %s AND year > %s AND status IN (0, 2);', (s_id, int(current_sem), int(current_sem)-3, int(current_year), int(current_year)-2)); 
      # if(mycursor.fetchone()[0]!=None):
      no_of_courses = int(mycursor.fetchone()[0])
  except Exception as err:
      print('Retrieval failed due to incorrect details. Try again.\nRedirecting...')
      print(err)
      # adding 5 seconds time delay
      time.sleep(5)
      return
  if(no_of_courses!=0):
    avg_credits_earned = sum_grade/no_of_courses
  else:
    avg_credits_earned=16 #if student has not taken any courses so far then he can take at max 16 credits
  
  try:
      mycursor.execute('SELECT SUM(C) from course_catalogue WHERE c_id IN (SELECT c_id FROM student_course_mapping WHERE s_id=%s AND sem = %s AND year = %s);', (s_id, current_sem, current_year))
      res = mycursor.fetchone()[0]
      if(res is None):
        sum_credits_currrent=0
      else:
        sum_credits_currrent = int(res)
        
  except Exception as err:
      print('Retrieval failed due to incorrect details. Try again.\nRedirecting...')
      #print\(err\)
      # adding 5 seconds time delay
      time.sleep(5)
      return
  try:
      mycursor.execute('SELECT C from course_catalogue WHERE c_id = %s;', (c_id,))
      c = int(mycursor.fetchone()[0])
  except Exception as err:
      print('Retrieval failed due to incorrect details. Try again.\nRedirecting...')
      #print\(err\)
      # adding 5 seconds time delay
      time.sleep(5)
      return
  if(1.25*avg_credits_earned<sum_credits_currrent+c):
      print('Course credit limit exceeded (Current credits ',sum_credits_currrent+c, ', Credit Limit ', 1.25*avg_credits_earned,'). Please try something else.\nRedirecting...')
      time.sleep(5)
      return
  elif(sum_credits_currrent+c>16):
      print('Course credit limit exceeded (Current credits ',sum_credits_currrent+c, ', Credit Limit 16). Please try something else.\nRedirecting...')
      time.sleep(5)
      return
    
    ########################## CGPA check ##########################
  scp=0.0
  sc=0
  #Sum of grade*credit for student SCP
  try:
      mycursor.execute("""
      SELECT SUM(cp.credit_product) AS sum_credit_product FROM (
      SELECT s.c_id, s.grade*c.C AS credit_product
      FROM student_course_mapping s
      INNER JOIN course_catalogue c
      ON s.c_id = c.c_id WHERE s.s_id = %s AND s.status IN (0,2)) cp;
      """, (s_id,)); 
  except Exception as err:
      print('Could not fetch information due to incorrect details. Try again.')
      print(err)
      # adding 5 seconds time delay
      time.sleep(5)
      return
  scp = mycursor.fetchone()[0]
  #sum of credits of all courses which the student has taken and not dropped/not current course SC
  try:
      mycursor.execute('SELECT sum(C) FROM course_catalogue WHERE c_id IN (SELECT c_id FROM student_course_mapping WHERE s_id = %s and status IN (0, 2));', (s_id,)); 
  except Exception as err:
      print('2 Could not fetch information due to incorrect details. Try again.')
      #print\(err\)
      # adding 5 seconds time delay
      time.sleep(5)
      return
  sc = mycursor.fetchone()[0]
  cgpa =0
  if(sc!=0):
      cgpa = round(scp/sc,2)
  else:
      cgpa = 0
  try:
      mycursor.execute('SELECT min_gpa FROM faculty_course_mapping WHERE c_id=%s;', (c_id,))
  except Exception as err:
      print('Could not fetch information due to incorrect details. Try again.')
      #print\(err\)
      # adding 5 seconds time delay
      time.sleep(5)
      return
  try:
    min_cgpa_req = mycursor.fetchone()[0]
  except Exception as err:
    print('This course was not offered by anyone.\nRedirecting...')
    #print\(err\)
    # adding 5 seconds time delay
    time.sleep(5)
    return
  if(cgpa<min_cgpa_req):
      print('You do not meet the minimum CGPA requirements.\nRedirecting...')
      time.sleep(5)
      return
  
  ########################## CNT=0 check ##########################
  try:
      mycursor.execute('SELECT COUNT(*) from student_course_mapping WHERE s_id = %s AND c_id = %s AND status IN (0,1);', (s_id, c_id))
      cnt = int(mycursor.fetchone()[0])
  except Exception as err:
      print('Retrieval failed due to incorrect details. Try again.\nRedirecting...')
      #print\(err\)
      # adding 5 seconds time delay
      time.sleep(5)
      return
  if(cnt>0):
      print('Course already taken. Please try something else.\nRedirecting...')
      time.sleep(5)
      return

  print('You are eligible to take the course. Adding the course to your bucket list...')
  time.sleep(3)
  try:
      mycursor.execute('INSERT INTO student_course_mapping VALUES (%s,%s,%s,%s,1,null);', (s_id, c_id, current_sem, current_year))
  except Exception as err:
      print('Could not add course due to some issue. Try again.\nRedirecting...')
      #print\(err\)
      # adding 5 seconds time delay
      time.sleep(5)
      return
  mydb.commit()
  print('Successfully added course to your course b1ucket.\nRedirecting...')
  time.sleep(5)
  return

#TESTED AND WORKING -> FULLY TESTED
def deregister_course_student(s_id, current_sem, current_year):
#   s_id = input('Enter your student ID: ')
  c_id=input("Enter CourseID of the course which you want to Deregister: ")
  #check if course can be deregistered
  try:
    mycursor.execute('SELECT status FROM student_course_mapping WHERE s_id=%s AND c_id = %s;', (s_id, c_id));
    if(mycursor.rowcount==0):
        print("This course was not taken by the student.\nRedirecting...")
        time.sleep(5)
        return
    status=mycursor.fetchone()[0]
    if(status!=1):
        print("This course was not taken by the student this semester and hence cannot be deregistered.\nRedirecting...")
        time.sleep(5)
        return
  except Exception as err:
    print('Could not deregister course due to incorrect details. Try again.')
    #print\(err\)
    # adding 5 seconds time delay
    time.sleep(5)
    return
  try:
    mycursor.execute('UPDATE student_course_mapping SET status = 3, grade = null WHERE s_id=%s AND c_id = %s AND status = 1 ;', (s_id, c_id)); 
  except Exception as err:
    print('Could not deregister course due to incorrect details. Try again.')
    #print\(err\)
    # adding 5 seconds time delay
    time.sleep(5)
    return
  mydb.commit()
  print('Successfully removed course from your course b1ucket.\nRedirecting...')
  time.sleep(5)
  return


# def print_function(rec):
#     if(len(rec)==0):
#         print('There are no records.\Redirecting...')
#         return
#     jSon_string_output=''
#     for i in rec:
#       s_name = i[0]
#       sem = i[5]
#       year = i[6]
#       list=("{\n\t{\n\t\t'Name': "+s_name+"\n\t}\n\t{\n\t\t'Semester': "+str(sem)+"\n\t}\n\t{\n\t\t'Year': "+str(year)+"\n\t}\n").expandtabs(4)
#       status=''
#       if(i[4]==0):
#         status='Passed'
#       elif(i[4]==1):
#         status='Currently Enrolled'
#       elif(i[4]==2):
#         status='Failed'
#       elif(i[4]==3):
#         status='Withdrawn'
      
#       list += ("\t{\n\t\t{\n\t\t\t'Course ID': "+str(i[1])+"\n\t\t},\n\t\t{\n\t\t\t'Course  Name': "+str(i[2])+"\n\t\t},\n\t\t{\n\t\t\t'Grade': "+str(i[3])+"\n\t\t},\n\t\t{\n\t\t\t'Status': "+status+"\n\t\t}\n\t}\n").expandtabs(4)
#       list+='}'
#       jSon_string_output+=list+'\n'
#     file = open('OUTPUT.txt', "w")
#     file.write(jSon_string_output)
#     file.close()
#     print('Please find output on OUTPUT.txt.\nRedirecting...')
#     time.sleep(5)

def print_function(rec):
    print(rec)
    print('*******************************************')
    for i in rec:
        print(tabulate(i))
    return

#TESTED AND WORKING -> FULLY TESTED
def view_grades_student(s_id, current_sem, current_year):
    print("""Do you want to:
    1. View all your grades
    2. View a particular subject

     """)
    inp=input("Enter your choice: ")
    if(inp not in ('1','2')):
        print('Wrong input. Try again.')
        time.sleep(3)
        return
    #res=[('Name','Course ID', 'Course Name', 'Grade', 'Status', 'Semester', 'Year')]
    if(inp=='1'):
        try:
            mycursor.execute("""SELECT s.name, sc.c_id, c.cname, sc.grade, sc.status, sc.sem, sc.year 
            FROM student_course_mapping sc
            INNER JOIN student s
            ON s.s_id = sc.s_id
            INNER JOIN course_catalogue c
            ON sc.c_id = c.c_id
            WHERE s.s_id=%s;""", (s_id,)) 
        except Exception as err:
            print('Could not retrieve grade due to incorrect details. Try again.')
            #print\(err\)
            # adding 5 seconds time delay
            time.sleep(5)
            return
        all_g=mycursor.fetchall()
        all_g=[list(e) for e in all_g]
        for i in all_g:
            if(i[4]==0):
                i[4]='Passed'
            elif(i[4]==2):
                i[4]='Failed'
            elif(i[4]==3):
                i[4]='Withdrawn'
        res=[e[0] for e in all_g]
        res=list(set(res))

        for i in res:
            print("\nStudent Name: ",i)
            temp_g=[e[1:] for e in all_g if e[0]==i]
            print(tabulate(temp_g, headers=['Course_ID','Course Name','Grade','Status', 'Semester','Year'], tablefmt='psql'))
            print('\n')

        while(1):
            inp=input()
            if(inp==''):
                break
    elif(inp=='2'):
        c_id = input('Enter your course ID: ')
        try:
            mycursor.execute("""SELECT s.name, sc.c_id, c.cname, sc.grade, sc.status, sc.sem, sc.year 
            FROM student_course_mapping sc
            INNER JOIN student s
            ON s.s_id = sc.s_id
            INNER JOIN course_catalogue c
            ON sc.c_id = c.c_id
            WHERE s.s_id=%s AND sc.c_id=%s;""", (s_id, c_id)); 
        except Exception as err:
            print('Could not retrieve grade due to incorrect details. Try again.')
            #print\(err\)
            # adding 5 seconds time delay
            time.sleep(5)
            return
        all_g=mycursor.fetchall()
        all_g=[list(e) for e in all_g]
        for i in all_g:
            if(i[4]==0):
                i[4]='Passed'
            elif(i[4]==2):
                i[4]='Failed'
            elif(i[4]==3):
                i[4]='Withdrawn'
        res=[e[0] for e in all_g]
        res=list(set(res))

        for i in res:
            print("\nStudent Name: ",i)
            temp_g=[e[1:] for e in all_g if e[0]==i]
            print(tabulate(temp_g, headers=['Course_ID','Course Name','Grade','Status', 'Semester','Year'], tablefmt='psql'))
            print('\n')

        while(1):
            inp=input()
            if(inp==''):
                break

#TESTED AND WORKING -> FULLY TESTED
def view_cgpa(s_id, current_sem, current_year):
#   s_id = input('Enter your student ID: ')
  scp=0.0
  sc=0
  #Sum of grade*credit for student SCP
  try:
      mycursor.execute("""
      SELECT SUM(cp.credit_product) AS sum_credit_product FROM (
      SELECT s.c_id, s.grade*c.C AS credit_product
      FROM student_course_mapping s
      INNER JOIN course_catalogue c
      ON s.c_id = c.c_id WHERE s.s_id = %s AND s.status IN (0,2)) cp;
      """, (s_id,)); 
  except Exception as err:
      print('1 Could not fetch information due to incorrect details. Try again.')
      #print\(err\)
      # adding 5 seconds time delay
      time.sleep(5)
      return
  scp = mycursor.fetchone()[0]
  #sum of credits of all courses which the student has taken and not dropped/not current course SC
  try:
      mycursor.execute('SELECT sum(C) FROM course_catalogue WHERE c_id IN (SELECT c_id FROM student_course_mapping WHERE s_id = %s and status IN (0, 2));', (s_id,)); 
  except Exception as err:
      print('2 Could not fetch information due to incorrect details. Try again.')
      #print\(err\)
      # adding 5 seconds time delay
      time.sleep(5)
      return
  sc = mycursor.fetchone()[0]
  if(sc!=0):
      print('CGPA: ' + str(round(scp/sc,2)))
  else:
      print('Student has not taken any course which he/she has completed/not dropped. Please try again.')
  time.sleep(5)
  return

#TESTED AND WORKING -> FULLY TESTED
def student_actions(s_id, current_sem, current_year):
  user_operating_system = platform.uname()[0]
  clear_command=''
  if(user_operating_system=='Windows'):
    clear_command='cls'
  else:
    clear_command='clear' #For Linux and MacOS users  
  inp=0
  while(1):
      clear = lambda: os.system(clear_command)
      clear()
      print("""Please select action
      1. Register Course
      2. Deregister Course
      3. View Grades
      4. View CGPA
      5. Logout
         """)
      inp=input("Enter your choice: ")
      if(inp=='1'):
        register_course_student(s_id, current_sem, current_year)
      elif(inp=='2'):
        deregister_course_student(s_id, current_sem, current_year)
      elif(inp=='3'):
        view_grades_student(s_id, current_sem, current_year)
      elif(inp=='4'):
        view_cgpa(s_id, current_sem, current_year)
      elif(inp=='5'):
        try:
            mycursor.execute('DELETE FROM current_session WHERE user_id=%s;', (s_id,)); 
        except Exception as err:
            print('Could not logout. Try again later.\nRedirecting...')
            #print\(err\)
            # adding 5 seconds time delay
            time.sleep(5)
        mydb.commit()
        print('Logged Out.\nRedirecting...')
        time.sleep(2)
        break
      else:
        print('Wrong input. Try again.\nRedirecting...')
        time.sleep(3)

############################################################### STAFF SECTION ###############################################################

#TESTED AND WORKING -> FULLY TESTED
def staff_actions(staff_id):
    user_operating_system = platform.uname()[0]
    clear_command=''
    if(user_operating_system=='Windows'):
      clear_command='cls'
    else:
      clear_command='clear' #For Linux and MacOS users
    inp=0
    while(1):
        clear = lambda: os.system(clear_command)
        clear()
        print("""Please select action:
        1. Edit Course Catalogue
        2. View Transcript Of All Students
        3. Download Transcript as .txt File
        4. Logout\n
        """)
        inp=input("Enter your choice: ")
        if(inp=='1'):
            edit_course_catalogue(staff_id)
        elif(inp=='2'):
            view_transcript_all_students(staff_id)
        elif(inp=='3'):
            download_transcript_particular(staff_id)
        elif(inp=='4'):
            try:
                mycursor.execute('DELETE FROM current_session WHERE user_id=%s;', (staff_id,)); 
            except Exception as err:
                print('Could not logout. Try again later.\nRedirecting...')
                #print\(err\)
                # adding 5 seconds time delay
                time.sleep(5)
            mydb.commit()
            print('Logged Out.\nRedirecting...')
            time.sleep(2)
            break
            
        else:
            print('Wrong input. Try again.')
            time.sleep(3)

#TESTED AND WORKING ->  FULLY TESTED
def edit_course_catalogue(staff_id):
    if(staff_id!='staff.dean'):
        print("You are not authorized to edit the course.\Redirecting...")
        time.sleep(3)
        return
    c_id = input("Enter course ID: ")
    cname = input("Enter course name: ")
    L = int(input("Enter lecture hours: "))
    T = int(input("Enter tutorial hours: "))
    P = int(input("Enter practical hours: "))
    S = 2*L + P/2 -T
    C = L + P/2
    no_of_prereq = int(input("Enter number of prerequisites: "))
    prereq_list=[]
    for i in range (0, no_of_prereq):
        prereq_list.append(input("Enter prerequisite "+str(i+1)+": "))
        try:
            mycursor.execute('SELECT COUNT(*) FROM pgsl4.course_catalogue WHERE c_id=%s;', (prereq_list[i],))
            res=mycursor.fetchone()[0]
            if(res==0):
                print('Course doesn\'t exist. Please try again.\nRedirecting...')
                time.sleep(5)
                return
        except Exception as err:
            print('Validation failed. Try again.')
            #print\(err\)
            # adding 5 seconds time delay
            time.sleep(5)
            return

    try:
        mycursor.execute('SELECT COUNT(*) FROM pgsl4.course_catalogue WHERE c_id=%s;', (c_id,))
    except Exception as err:
        print('Validation failed. Try again.')
        #print\(err\)
        # adding 5 seconds time delay
        time.sleep(5)
        return
    count = int(mycursor.fetchone()[0])
    if(count!=0):
      print('Course already exists. Please try again.\nRedirecting...')
      time.sleep(5)
      return

    try:
        mycursor.execute('INSERT INTO pgsl4.course_catalogue VALUES (%s, %s, %s, %s, %s, %s, %s);', (c_id, cname, L, T, P, S, C))
    except Exception as err:
        print('Insertion failed. Please try again.\nRedirecting...')
        #print\(err\)
        # adding 5 seconds time delay
        time.sleep(5)
        return
    
    for i in prereq_list:    
        try:
            mycursor.execute('INSERT INTO pgsl4.prereq VALUES (%s, %s);', (c_id, i))
        except Exception as err:
            print('Insertion failed. Please try again.\nRedirecting...')
            #print\(err\)
            # adding 5 seconds time delay
            time.sleep(5)
            return

    mydb.commit()
    print("Insertion successful.\nRedirecting...")
    time.sleep(5)
    return

# #TESTED AND WORKING ->  FULLY TESTED
# def print_function(rec):
#     if(len(rec)==0):
#         print('There are no records')
#         time.sleep(5)
#         return
#     jSon_string_output=''
#     for i in rec:
#       s_name = i[0]
#       sem = i[5]
#       year = i[6]
#       list=("{\n\t{\n\t\t'Name': "+s_name+"\n\t}\n\t{\n\t\t'Semester': "+str(sem)+"\n\t}\n\t{\n\t\t'Year': "+str(year)+"\n\t}\n").expandtabs(4)
#       status=''
#       if(i[4]==0):
#         status='Passed'
#       elif(i[4]==1):
#         status='Currently Enrolled'
#       elif(i[4]==2):
#         status='Failed'
#       elif(i[4]==3):
#         status='Withdrawn'
      
#       list += ("\t{\n\t\t{\n\t\t\t'Course ID': "+str(i[1])+"\n\t\t},\n\t\t{\n\t\t\t'Course  Name': "+str(i[2])+"\n\t\t},\n\t\t{\n\t\t\t'Grade': "+str(i[3])+"\n\t\t},\n\t\t{\n\t\t\t'Status': "+status+"\n\t\t}\n\t}\n").expandtabs(4)
#       list+='}'
#       jSon_string_output+=list+'\n'
#     file = open('OUTPUT.txt', "w")
#     file.write(jSon_string_output)
#     file.close()
#     print('Please find output on OUTPUT.txt.\nRedirecting...')
#     time.sleep(5)

#TESTED AND WORKING -> FULLY TESTED
def view_transcript_all_students(staff_id):
    res=[('Name','Course ID', 'Course Name', 'Grade', 'Status', 'Semester', 'Year')]
    s_id=input("Enter Student ID: ")
    try:
        mycursor.execute("""SELECT s.name, sc.c_id, c.cname, sc.grade, sc.status, sc.sem, sc.year 
          FROM student_course_mapping sc
          INNER JOIN student s
          ON s.s_id = sc.s_id
          INNER JOIN course_catalogue c
          ON sc.c_id = c.c_id
          WHERE sc.status<>1 AND s.s_id=%s
          ORDER BY sc.year, sc.sem;""", (s_id,))
    except Exception as err:
        print('Retrieval failed. Try again.\nRedirecting...')
        #print\(err\)
        # adding 5 seconds time delay
        time.sleep(5)
        return
    all_g=mycursor.fetchall()
    all_g=[list(e) for e in all_g]
    for i in all_g:
        if(i[4]==0):
            i[4]='Passed'
        elif(i[4]==2):
            i[4]='Failed'
        elif(i[4]==3):
            i[4]='Withdrawn'
    res=[e[0] for e in all_g]
    res=list(set(res))
    
        

    print("\nStudent Name: ",res[0])
    for i in res:
        temp_g=[e[1:] for e in all_g if e[0]==i]
        print(tabulate(temp_g, headers=['Course_ID','Course Name','Grade','Status', 'Semester','Year'], tablefmt='psql'))
        print('\n')

    while(1):
        inp=input()
        if(inp==''):
            break

    return

# #TESTED AND WORKING -> FULLY TESTED
# def output_file(rec, s_id):
#     jSon_string_output=''
#     for i in rec:
#       s_name = i[0][0]
#       sem = i[0][5]
#       year = i[0][6]
#       list=("{\n\t{\n\t\t'Name': "+s_name+"\n\t}\n\t{\n\t\t'Semester': "+str(sem)+"\n\t}\n\t{\n\t\t'Year': "+str(year)+"\n\t}\n").expandtabs(4)
#       for j in i:
#         status=''
#         if(j[4]==0):
#           status='Passed'
#         elif(j[4]==1):
#           status='Currently Enrolled'
#         elif(j[4]==2):
#           status='Failed'
#         elif(j[4]==3):
#           status='Withdrawn'
        
#         list += ("\t{\n\t\t{\n\t\t\t'Course ID': "+str(j[1])+"\n\t\t},\n\t\t{\n\t\t\t'Course  Name': "+str(j[2])+"\n\t\t},\n\t\t{\n\t\t\t'Grade': "+str(j[3])+"\n\t\t},\n\t\t{\n\t\t\t'Status': "+status+"\n\t\t}\n\t}\n").expandtabs(4)
#       list+='}'
#       jSon_string_output+=list+'\n'

#     now = datetime.datetime.now()
#     date_string = now.strftime("%d%m%Y%H%M%S")
#     fname = s_id+'_Transcript_'+date_string+'.txt'
#     file = open(fname, "w")
#     file.write(jSon_string_output)
#     file.close()
#     filepath= str(Path.cwd())+'/'+fname
#     print("File is available at: "+filepath)
#     print("Redirecting...")
#     time.sleep(10)
#     return


#TESTED AND WORKING -> FULLY TESTED
def output_file(rec, s_id):
    now = datetime.datetime.now()
    date_string = now.strftime("%d%m%Y%H%M%S")
    fname = s_id+'_Transcript_'+date_string+'.txt'
    file = open(fname, "w")
    for i in rec:
        file.write(tabulate(rec, headers = 'firstrow'))
    file.close()
    filepath= str(Path.cwd())+'/'+fname
    print("File is available at: "+filepath)
    print("Redirecting...")
    time.sleep(10)
    return


#TESTED AND WORKING -> FULLY TESTED
def download_transcript_particular(staff_id):
    res=[('Name','Course ID', 'Course Name', 'Grade', 'Status', 'Semester', 'Year')]
    s_id = str(input("Enter student ID: "))
    # sem=0
    # try:
    #     mycursor.execute('SELECT MAX(sem) FROM student_course_mapping WHERE s_id = %s;', (s_id,)); 
    #     sem = mycursor.fetchone()[0]
    #     print("Current semester is: "+str(int(sem)+1))
    # except Exception as err:
    #     print(' Retrieval failed due to incorrect details. Please try again.\nRedirecting...')
    #     #print\(err\)
    #     # adding 5 seconds time delay
    #     time.sleep(5)
    #     return
    # for i in range (1, int(current_sem)+1):
    #     try:
    #         mycursor.execute("""SELECT s.name, sc.c_id, c.cname, sc.grade, sc.status, sc.sem, sc.year 
    #         FROM student_course_mapping sc
    #         INNER JOIN student s
    #         ON s.s_id = sc.s_id
    #         INNER JOIN course_catalogue c
    #         ON sc.c_id = c.c_id
    #         WHERE s.s_id = %s AND sc.sem = %s
    #         AND sc.status<>1
    #         ORDER BY sc.year, sc.sem;""", (s_id, str(i)))
            
    #     except Exception as err:
    #         print('Retrieval failed. Please try again.\nRedirecting...')
    #         #print\(err\)
    #         # adding 5 seconds time delay
    #         time.sleep(5)
    #         return
    #     res.append(mycursor.fetchall())

    try:
        mycursor.execute("""SELECT s.name, sc.c_id, c.cname, sc.grade, sc.status, sc.sem, sc.year 
          FROM student_course_mapping sc
          INNER JOIN student s
          ON s.s_id = sc.s_id
          INNER JOIN course_catalogue c
          ON sc.c_id = c.c_id
          WHERE sc.status<>1 AND s.s_id=%s
          ORDER BY sc.year, sc.sem;""", (s_id,))
    except Exception as err:
        print('Retrieval failed. Try again.\nRedirecting...')
        #print\(err\)
        # adding 5 seconds time delay
        time.sleep(5)
        return
    all_g=mycursor.fetchall()
    all_g=[list(e) for e in all_g]
    for i in all_g:
        if(i[4]==0):
            i[4]='Passed'
        elif(i[4]==2):
            i[4]='Failed'
        elif(i[4]==3):
            i[4]='Withdrawn'
    res=[e[0] for e in all_g]
    res=list(set(res))

    now = datetime.datetime.now()
    date_string = now.strftime("%d%m%Y%H%M%S")
    fname = s_id+'_Transcript_'+date_string+'.txt'
    file = open(fname, "a")
    file.write("Student Name: " + str(res[0])+"\n")
    for i in res:
        temp_g=[e[1:] for e in all_g if e[0]==i]
        file.write(tabulate(temp_g, headers=['Course_ID','Course Name','Grade', 'Status','Semester','Year'], tablefmt='psql'))
        file.write('\n')

    file.close()
    filepath= str(Path.cwd())+'/'+fname
    print("File is available at: "+filepath)
    print("Redirecting...")
    time.sleep(10)
    #create a .txt file as output file (OLD)
    # now = datetime.now()
    # date_string = now.strftime("%d%m%Y%H%M%S")
    # fname = s_id+'_Transcript_'+date_string+'.txt'
    # with open(fname, "w", newline="") as o:
    #     writer = csv.writer(o)
    #     writer.writerows(rec)
    
    # filepath= Path.cwd()+'\\'+fname
    # print("File is available at: "+filepath)

    #create a .txt file as output file (NEW)
    
    return

############################################################### FACULTY SECTION ###############################################################

#TESTED AND WORKING
def offer_course(userid, sem, year):
    user_operating_system = platform.uname()[0]
    clear_command=''
    if(user_operating_system=='Windows'):
      clear_command='cls'
    else:
      clear_command='clear' #For Linux and MacOS users
    clear = lambda: os.system(clear_command)
    clear()
    try:
        mycursor.execute("SELECT c_id FROM course_catalogue WHERE c_id NOT IN (SELECT c_id FROM faculty_course_mapping);")
    except Exception as err:
        print('Could not verify. Try again later.\nRedirecting...')
        #print\(err\)
        # adding 5 seconds time delay
        time.sleep(5)
        return
    avail_cid = []
    tmp = mycursor.fetchall()
    for x in tmp:
        avail_cid.append(x[0])
    offer_id=input("Enter Course ID which you want to offer: ")
    if(offer_id in avail_cid):
        min_gpa=input("Enter minimum GPA that a student should have to take this course: ")
        try:
            mycursor.execute('INSERT INTO faculty_course_mapping VALUES (%s, %s, %s, %s, %s);', (offer_id, userid,min_gpa, sem, year))
        except Exception as err:
            print('Could not add course. Try again later.\nRedirecting...')
            #print\(err\)
            # adding 5 seconds time delay
            time.sleep(5)
            return
        mydb.commit()
        print("Course added successfully!")
        time.sleep(3)
    else:
        print("Cannot offer this course. Please choose among the courses that are currently not offered for this semester.")
        time.sleep(3)

def all_grades():
    mycursor.execute('''SELECT s.name, sc.c_id, c.cname, sc.grade, sc.status, sc.sem, sc.year 
          FROM student_course_mapping sc
          INNER JOIN student s
          ON s.s_id = sc.s_id
          INNER JOIN course_catalogue c
          ON sc.c_id = c.c_id
          WHERE sc.status<>1
          ORDER BY sc.year, sc.sem;
    ''')
    all_g=mycursor.fetchall()
    all_g=[list(e) for e in all_g]
    for i in all_g:
        if(i[4]==0):
            i[4]='Passed'
        elif(i[4]==2):
            i[4]='Failed'
        elif(i[4]==3):
            i[4]='Withdrawn'
    res=[e[0] for e in all_g]
    res=list(set(res))
    

    for i in res:
        print("\nStudent Name: ",i)
        temp_g=[e[1:] for e in all_g if e[0]==i]
        print(tabulate(temp_g, headers=['Course_ID','Course Name','Grade','Status', 'Semester','Year'], tablefmt='psql'))
        print('\n')

    while(1):
        inp=input()
        if(inp==''):
            break

def upload_grades(f_id):
    path = '/home/cpdl/Assignments/VSC_Projects/iitroparassignments_1013/PG Software Lab/Assignment4/grade_upload/grades.csv'
    if(os.path.exists(path) is False):
        print('File does not exist.\nRedirecting...')
        time.sleep(3)
        return
    pflag1=0
    pflag2=0
    flag=0
    with open (path, 'r') as f:
        reader = csv.reader(f)
        columns = next(reader) 
        query = 'UPDATE student_course_mapping SET grade = %s, status = %s WHERE s_id=%s AND c_id=%s AND status=%s;'
        for data in reader:
            #print((int(data[5]), int(data[4]), data[0], data[1], 1))
            #check if prof can upload that grade
            try:
                mycursor.execute('SELECT COUNT(*) FROM faculty_course_mapping WHERE c_id=%s AND f_id=%s;', (data[1], f_id))
            except Exception as err:
                print('Could not access database. Try again later.\nRedirecting...')
                print(err)
                # adding 5 seconds time delay
                time.sleep(5)
            count = mycursor.fetchone()[0]
            if(count==0):
                if(pflag1==0):
                    print('Illegal Entry. Please enter only your course grades.\nRedirecting...')
                    pflag1=1
            else:
                #check if student has taken that course
                try:
                    mycursor.execute('SELECT COUNT(*) FROM student_course_mapping WHERE c_id=%s AND s_id=%s AND status=1;', (data[1], data[0],))
                except Exception as err:
                    print('Could not access database. Try again later.\nRedirecting...')
                    print(err)
                    # adding 5 seconds time delay
                    time.sleep(5)
                count = mycursor.fetchone()[0]
                if(count==0):
                    if(pflag2==0):
                        print('Illegal Entry. Please only enter grades of students who took your course.\nRedirecting...')
                        pflag2=1
                else:
                    try:
                        mycursor.execute(query, (int(data[5]), int(data[4]), data[0], data[1], 1))
                    except Exception as err:
                        print('Could not insert grades. Try again later.\n')
                        print(err)
                        # adding 5 seconds time delay
                        time.sleep(5)
                        return
                    mydb.commit()
                    flag=1
    if(flag and pflag1==0 and pflag2==0):
        print("Upload successful!")
    elif(flag and (pflag1!=0 or pflag2!=0)):
        print("Upload successful for some students!")
    else:
        print("Upload not successful!")
    time.sleep(3)

# def upload_grades():
#     path = '/home/cpdl/Assignments/VSC_Projects/iitroparassignments_1013/PG Software Lab/Assignment4/grade_upload/grades.csv'
#     if(os.path.exists(path) is False):
#         print('File does not exist.\nRedirecting...')
#         time.sleep(3)
#         return
#     with open (path, 'r') as f:
#         reader = csv.reader(f)
#         columns = next(reader) 
#         query = 'UPDATE student_course_mapping SET grade = %s, status = %s WHERE s_id=%s AND c_id=%s AND status=%s;'
#         for data in reader:
#             print((int(data[5]), int(data[4]), data[0], data[1], 1))
#             try:
#                 mycursor.execute(query, (int(data[5]), int(data[4]), data[0], data[1], 1))
#             except Exception as err:
#                 print('Could not insert grades. Try again later.\nRedirecting...')
#                 print(err)
#                 # adding 5 seconds time delay
#                 time.sleep(5)
#                 return
#             mydb.commit()
#     print("Upload successful!")
#     time.sleep(3)

def faculty_actions(userid):
    inp=0
    while(1):
        user_operating_system = platform.uname()[0]
        clear_command=''
        if(user_operating_system=='Windows'):
            clear_command='cls'
        else:
            clear_command='clear' #For Linux and MacOS users
        clear = lambda: os.system(clear_command)
        clear()
        print("Welcome, ",userid)
        print("""\nPlease select action
    1. Offer a course
    2. View grades of all students
    3. Upload grades from .csv file
    4. Logout
     """)
        inp=input()
        if(inp not in ('1','2','3','4','5')):
            print("Please enter valid input")
            continue

        elif(inp=='4'):
            try:
                mycursor.execute('DELETE FROM current_session WHERE user_id=%s;', (userid,)); 
            except Exception as err:
                print('Could not logout. Try again later.\nRedirecting...')
                #print\(err\)
                # adding 5 seconds time delay
                time.sleep(5)
            mydb.commit()
            print('Logged Out.\nRedirecting...')
            time.sleep(2)
            break

        elif(inp=='1'):
            c_sem = input("Enter current semester: ")
            c_year = input("Enter current year: ")
            offer_course(userid, c_sem, c_year)
            
        elif(inp=='2'):
            all_grades()
            
        elif(inp=='3'):
            upload_grades(userid)

main_screen()




        


