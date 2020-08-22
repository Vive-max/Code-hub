import mysql.connector
mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               password='guru',
                               database='mysql'
                               )

cur=mydb.cursor()

n1=eval(input('enter a book_id \n'))
n2=eval(input('enter the name of book \n '))
n3=eval(input('enter the price of book \n'))

admin="insert into book (book_id,book_name,book_prices)values(%s,%s,%s)"
book_details=(n1,n2,n3)
cur.execute(admin,book_details)
mydb.commit()


