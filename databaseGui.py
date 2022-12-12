from tkinter import *
import mysql.connector


def submin():
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        database = 'testdb',
        )
    c = conn.cursor()
    # c.execute('INSERT INTO address VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)',
    #     {
    #         'f_name': f_name.get(),
    #         'l_name': l_name.get(),
    #         'address': address.get(),
    #         'city': city.get(),
    #         'state': state.get(),
    #         'zipcode': zipcode.get()
    #     }
    # )

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


def query():
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        database = 'testdb',
        )
    c = conn.cursor()
    c.execute('SELECT * FROM address')
    records = c.fetchall()
    print(records)
    conn.commit()
    conn.close()



# window
window = Tk()
window.title('Data Base')
window.geometry('340x400')
window.config(padx=10, pady=10)

# Entry
f_name = Entry(window, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(window, width=30)
l_name.grid(row=1, column=1)
address = Entry(window, width=30)
address.grid(row=2, column=1)
city = Entry(window, width=30)
city.grid(row=3, column=1)
state = Entry(window, width=30)
state.grid(row=4, column=1)
zipcode = Entry(window, width=30)
zipcode.grid(row=5, column=1)

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

# Button
submit_btn = Button(window, text='Add Record', command=submin)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)
query_btn = Button(window, text='Query', command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=120)



window.mainloop()