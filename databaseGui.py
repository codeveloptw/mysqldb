from tkinter import *
import mysql.connector


def sql_connect():
    conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',
    database = 'testdb',
    )
    return conn

def clear_entry():
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    user_id.delete(0, END)


def submin():
    conn = sql_connect()
    c = conn.cursor()
    # CREATE TABLE address (f_name VARCHAR(255), l_name VARCHAR(255), address VARCHAR(255), city VARCHAR(255), state VARCHAR(255), zipcode VARCHAR(255), user_id INTEGER AUTO_INCREMENT PRIMARY key)
    if f_name.get():
        sqlStuff = "INSERT INTO address (f_name, l_name, address, city, state, zipcode) VALUES (%s, %s, %s, %s, %s, %s)"
        record = (f_name.get(), l_name.get(), address.get(), city.get(), state.get(), zipcode.get())
        # print(sqlStuff, record)
        c.execute(sqlStuff, record)
        conn.commit()
        conn.close()

        f_name.delete(0, END)
        l_name.delete(0, END)
        address.delete(0, END)
        city.delete(0, END)
        state.delete(0, END)
        zipcode.delete(0, END)


def delete():
    conn = sql_connect()
    c = conn.cursor()
    c.execute('DELETE FROM address WHERE user_id = ' +  delete_box.get())
    conn.commit()
    conn.close()


def query():
    conn = sql_connect()
    c = conn.cursor()
    c.execute('SELECT * FROM address')
    records = c.fetchall()
    print(records)
    print_records = ''
    for record in records:
        print_records += str(record[0]) +' '+ str(record[1]) + '    ' + '\t' +  str(record[6])+ '\n'

    query_label = Label(window, text=print_records)
    query_label.grid(row=12, column=0, columnspan=3)
    conn.commit()
    conn.close()


def select():
    conn = sql_connect()
    c = conn.cursor()
    c.execute('SELECT * FROM address WHERE user_id = ' +  user_id.get())
    records = c.fetchall()
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

    f_name.insert(0,records[0][0])
    l_name.insert(0,records[0][1])

    address.insert(0,records[0][2])
    city.insert(0,records[0][3])
    state.insert(0,records[0][4])
    zipcode.insert(0,records[0][5])
    conn.commit()
    conn.close()


def update():
    conn = sql_connect()
    c = conn.cursor()
    sqlStuff = "UPDATE address SET f_name = %s, l_name = %s, address = %s, city = %s, state = %s, zipcode = %s WHERE user_id = + %s"
    record = (f_name.get(), l_name.get(), address.get(), city.get(), state.get(), zipcode.get(), user_id.get())
    print(record)
    c.execute(sqlStuff, record)
    conn.commit()
    conn.close()


# window
window = Tk()
window.title('Data Base')
window.geometry('340x400')
window.config(padx=10, pady=10)

# Entry
f_name = Entry(window, width=30)
f_name.grid(row=0, column=1, columnspan=2, padx=20)
l_name = Entry(window, width=30)
l_name.grid(row=1, column=1, columnspan=2)
address = Entry(window, width=30)
address.grid(row=2, column=1, columnspan=2)
city = Entry(window, width=30)
city.grid(row=3, column=1, columnspan=2)
state = Entry(window, width=30)
state.grid(row=4, column=1, columnspan=2)
zipcode = Entry(window, width=30)
zipcode.grid(row=5, column=1, columnspan=2)
user_id = Entry(window, width=20)
user_id.grid(row=8, column=1)

# Label
f_name_label = Label(window, text='First Name')
f_name_label.grid(row=0, column=0)
l_name_label = Label(window, text='Last Name')
l_name_label.grid(row=1, column=0)
address_label = Label(window, text='Address')
address_label.grid(row=2, column=0)
city_label = Label(window, text='City')
city_label.grid(row=3, column=0)
state_label = Label(window, text='State')
state_label.grid(row=4, column=0)
zipcode_label = Label(window, text='Zip Code')
zipcode_label.grid(row=5, column=0)
delete_label = Label(window, text='Id Number')
delete_label.grid(row=8, column=0)

# Button
submit_btn = Button(window, text='Add Record', command=submin)
submit_btn.grid(row=6, column=0, columnspan=3, padx=10, pady=10, ipadx=100)
query_btn = Button(window, text='Query', command=query)
query_btn.grid(row=7, column=0, columnspan=3, padx=10, pady=10, ipadx=116)
delete_btn = Button(window, text='Delete', command=delete)
delete_btn.grid(row=9, column=0, padx=2, pady=2, ipadx=10)
selete_btn = Button(window, text='Select', command=select)
selete_btn.grid(row=9, column=1, padx=2, pady=2, ipadx=10)
update_btn = Button(window, text='Update', command=update)
update_btn.grid(row=9, column=2, padx=2, pady=2, ipadx=10)

window.mainloop()