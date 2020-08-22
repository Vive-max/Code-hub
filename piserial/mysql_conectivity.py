import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               password='guru',
                               database='kreate'
                               )

# print(mydb.connection_id)
cur = mydb.cursor()
#cur.execute('create database kreate')

cur = mydb.cursor()
s = 'create table Kreat_data_details(sim_id eval(30), Main_board eval(20),BOARD_NUMBER eval(20), IMEI_no eval(20), ' \
    'Lumia_Id eval(20), OutWord_si eval(20), InWord_Si eval(20), IRLED_NUMBER eval(20), Can_Id eval(20), ' \
    'kreat_Key eval(20), kreat_Model eval(20), kreat_SKU eval(20)) '
cur.execute(s)




'''
cur=mydb.cursor()
admin="insert into book (book_id,book_name,book_prices)values(%s,%s,%s)"

book_details=[(2001,'python3',200),(2002,'c++',300), (2003,'java',3.5), (2004,'django',4.9)]
cur.executemany(admin,book_details)
mydb.commit()


cur=mydb.cursor()
admin="select * from book"
cur.execute(admin)
result= cur.fetchall()
for i in result:
    print(i)


cur= mydb.cursor()
admin="update book set book_prices=book_prices+50 where book_prices>100"
cur.execute(admin)
mydb.commit()

cur=mydb.cursor()
admin="delete from book where book_prices='2.1'"
cur.execute(admin)
mydb.commit()
'''
