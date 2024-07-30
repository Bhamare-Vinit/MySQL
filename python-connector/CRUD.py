import mysql.connector

#to create database
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='Vinit@2002',
#     database='pythonsql')
#create the object of cursor 
#cursor object is used to execute the mysql query
# cur=mydb.cursor()
# cur.execute("CREATE DATABASE pythonSQL")



#to create table
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='Vinit@2002',
#     database='pythonsql')
# cur=mydb.cursor()
# query="CREATE TABLE book(bookid integer(4),title varchar(20),price float(5,2))"
# cur.execute(query)



# Enter fixed data
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='Vinit@2002',
#     database='pythonsql')
# cur=mydb.cursor()
# query="INSERT INTO book (bookid,title,price) VALUES (%s,%s,%s)"
# para=(1,'Tale of Vinit',999)
# cur.execute(query,para)
# # commit is used to saved changes while performing CRUD operations
# mydb.commit()



# Enter fixed multipe data
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='Vinit@2002',
#     database='pythonsql')
# cur=mydb.cursor()
# query="INSERT INTO book (bookid,title,price) VALUES(%s,%s,%s)"
# para=[(3,'MAhabharat',99),(4,'Geeta',900),(5,'Ramayana',500)]
# #Executemant takes query and list of tuple
# cur.executemany(query,para)
# # commit is used to saved changes while performing CRUD operations
# mydb.commit()



#Enter user input data
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='Vinit@2002',
#     database='pythonsql')
# bookid=int(input("Enter the bookid:"))
# name=input ("Enter the name of book:")
# price=int(input("Enter the price of book:"))
# cur=mydb.cursor()
# query=f"INSERT INTO book (bookid,title,price) VALUES {bookid,name,price}"
# cur.execute(query)
# # commit is used to saved changes while performing CRUD operations
# mydb.commit()



#Fetch data from database
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='Vinit@2002',
#     database='pythonsql')
# cur=mydb.cursor()
# query="SELECT * from book"
# cur.execute(query)
# #fetch all function fetch all data from cursor and stored it in variable
#we get data in form of list having multiple tuples
# result1=cur.fetchall()
# # print(result1)
# print(f"+{'-'*17}+{'-'*17}+{'-'*17}+")
# for i in result1:
#     print(f"| {i[0]:^15} | {i[1]:^15} | {i[2]:^15} |")
#     print(f"+{'-'*17}+{'-'*17}+{'-'*17}+")



# Update values in database
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='Vinit@2002',
#     database='pythonsql')
# cur=mydb.cursor()
# query="UPDATE book SET price=price+10 WHERE price<900"
# cur.execute(query)
# mydb.commit()
# query="SELECT * from book"
# cur.execute(query)
# #fetch all function fetch all data from cursor and stored it in variable
# # we get data in form of list having multiple tuples
# result1=cur.fetchall()
# # print(result1)
# print(f"+{'-'*17}+{'-'*17}+{'-'*17}+")
# for i in result1:
#     print(f"| {i[0]:^15} | {i[1]:^15} | {i[2]:^15} |")
#     print(f"+{'-'*17}+{'-'*17}+{'-'*17}+")



# Delete values in database
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='Vinit@2002',
#     database='pythonsql')
# cur=mydb.cursor()
# query="DELETE FROM book WHERE price>900"
# cur.execute(query)
# mydb.commit()

