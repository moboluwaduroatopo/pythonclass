
import mysql.connector

mycon=mysql.connector.connect(host="localhost",user='root',passwd='',database='pythoncbt_db')
# print(mycon)
mycursor=mycon.cursor()
# To create database from code
# mycursor.execute("CREATE DATABASE pythoncbt_db")
# To show all database name in phpmyadmin
# mycursor.execute('SHOW DATABASES')
# for x in mycursor:
# 	print(x)
# to create table
# mycursor.execute("CREATE TABLE question (question_id INT(4), q_name VARCHAR(50), optiona VARCHAR(30), optionb VARCHAR(30), optionc VARCHAR(30), optiond VARCHAR(30), ans VARCHAR(30))")
#to give id AUTO_INCREMENT
 # mycursor.execute("ALTER TABLE user CHANGE user_id user_id INT(4) AUTO_INCREMENT PRIMARY KEY")
#to add column
 # mycursor.execute("ALTER TABLE user ADD pass VARCHAR(50) ")
# truncate table 'user'
 # account_info id,customer_id,pin,acct_number,amount
 # customers id,name,address,phone,password 

# sqlf="SELECT FROM user limit 4 offset 6 where user_name=%s" 
user_name=input('Enter user_name')
password=input('Enter passwd')
# sql="INSERT INTO user(user_name,password) VALUES(%s,%s)"
# val=[(user_name,password)]
# # mycursor.execute(sql, val)
# mycursor.executemany(sql,val)
# mycon.commit()
# sqlf="SELECT * FROM user limit 12 offset 5 " 
# mycursor.execute(sqlf)
# result=mycursor.fetchall()
# for x in result:
# 	print(x)
sqlf="SELECT * FROM user where user_name=%s and password=%s"
val1=(user_name,password)
mycursor.execute(sqlf,val1)
result=mycursor.fetchall()
print(result)
res=result[0]
print(res[0])

print(mycursor.rowcount,'record inserted successfuly')
# print(ses)
