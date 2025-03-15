import mysql.connector
# Connect to the database
mydb = mysql.connector.connect(host="Localhost",username="root",password="opencv@re",database="college")
print(mydb)
mycursor = mydb.cursor()
# mycursor.execute("DROP TABLE IF EXISTS CUSTOMER")
# mycursor.execute("""
#                  CREATE TABLE CUSTOMER(
#                      NAME VARCHAR(30),
#                      AGE INT,
#                      EMAIL VARCHAR(50)PRIMARY KEY)""")
# mycursor.execute("USE COLLEGE")
mycursor.execute("""INSERT INTO CUSTOMER(NAME,AGE,EMAIL)
    VALUES
    ("VINDHYAWASAN",20,"ASINGH128VE@GMAIL.COM"),
    ("SHUBHAM", 16,"SHUBHAM128VE@GMAIL.COM")""")

# mycursor.execute("""
#     INSERT INTO CUSTOMER (NAME, AGE, EMAIL)
#     VALUES
#     ("VINDHYAWASAN", 20, "ASINGH128VE@GMAIL.COM"),
#     ("SHUBHAM", 16, "SHUBHAM128VE@GMAIL.COM")
# """)
mydb.commit()
print(mycursor.rowcount,"recrod insert")

for x in mycursor:
    print(x)
    # pass