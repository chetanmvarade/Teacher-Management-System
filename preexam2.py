from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
import smtplib
import ssl

class Teacher:
    def __init__(self, root):
        self.root = root
        self.root.title("PREEXAMINATION SYSTEM")
        self.root.geometry("500x600")
        self.root.maxsize(width=900, height=600)

        self.manage_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        self.manage_frame.pack(fill=BOTH, expand=1)

        # Manage Teacher Frame
        self.UID_no_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.contactno_var = StringVar()
        self.subject_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        m_title = Label(self.manage_frame, text="Manage Teacher",
                        bg="crimson",
                        fg="white",
                        font=("times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_uidno = Label(self.manage_frame, text="UID NO *",
                          bg="crimson",
                          fg="white",
                          font=("times new roman", 20, "bold"))
        lbl_uidno.grid(row=1, column=0, pady=10, sticky="w")

        txt_uidno = Entry(self.manage_frame,
                          textvariable=self.UID_no_var,
                          font=("times new roman", 20, "bold"),
                          bd=5, relief=GROOVE)
        txt_uidno.grid(row=1, column=1, pady=10, padx=4, sticky="w")

        lbl_name = Label(self.manage_frame, text="Name.",
                         bg="crimson",
                         fg="white",
                         font=("times new roman ", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, sticky="w")

        txt_name = Entry(self.manage_frame,
                         textvariable=self.name_var,
                         font=("times new roman", 20, "bold"),
                         bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=4, sticky="w")

        lbl_email = Label(self.manage_frame, text="Email",
                          bg="crimson",
                          fg="white",
                          font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, sticky="w")

        txt_email = Entry(self.manage_frame, textvariable=self.email_var,
                          font=("times new roman", 20, "bold"),
                          bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=4, sticky="w")

        lbl_contactno = Label(self.manage_frame, text="Contact No.",
                              bg="crimson",
                              fg="white",
                              font=("times new roman", 20, "bold"))
        lbl_contactno.grid(row=4, column=0, pady=10, sticky="w")

        txt_contactno = Entry(self.manage_frame, textvariable=self.contactno_var,
                              font=("times new roman", 20, "bold"),
                              bd=5, relief=GROOVE)
        txt_contactno.grid(row=4, column=1, pady=10, padx=4, sticky="w")

        lbl_subject = Label(self.manage_frame,
                            text="Subject",
                            bg="crimson",
                            fg="white",
                            font=("times new roman", 20, "bold"))
        lbl_subject.grid(row=5, column=0, pady=10, sticky="w")

        combo_subject = ttk.Combobox(self.manage_frame,
                                     textvariable=self.subject_var,
                                     font=("times new roman", 20, "bold"),
                                     state="readonly")
        combo_subject['values'] = ("php programming", "Python programming",
                                   "computer network", "Operating system",
                                   "Cloud computing", "Data science")

        combo_subject.grid(row=5, column=1, pady=5, padx=1, sticky="w")

        btn_Frame = Frame(self.manage_frame, bd=4, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=15, y=400, width=400)

        Addbtn = Button(btn_Frame, text="Add", width=10,
                        command=self.add_teachers)
        Addbtn.grid(row=0, column=0, padx=10, pady=10)

        updatebtn = Button(btn_Frame, text="Update", width=10,
                           command=self.update_data)
        updatebtn.grid(row=0, column=2, padx=10, pady=10)

        deletebtn = Button(btn_Frame, text="Delete", width=10,
                           command=self.delete_data)
        deletebtn.grid(row=0, column=3, padx=10, pady=10)

        clearbtn = Button(btn_Frame, text="Clear", width=10,
                          command=self.clear)
        clearbtn.grid(row=0, column=4, padx=10, pady=10)

        email_Frame = Frame(self.manage_frame, bd=4, relief=RIDGE, bg="crimson")
        email_Frame.place(x=100, y=510, width=230)
        sendmailbtn = Button(email_Frame, text="Send mail", width=10,
                             command=self.send_email)
        sendmailbtn.grid(row=0, column=0, padx=10, pady=10)

        next_btn = Button(self.manage_frame, text="Next", width=10, command=self.switch_to_search_page)
        next_btn.place(x=230, y=523)


        # Search Frame
        self.search_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")

        lbl_search = Label(self.search_frame, text="Search By.", bg="crimson",
                           fg="white", font=("times new roman", 13, "bold"))
        lbl_search.grid(row=0, column=0, pady=20, padx=20, sticky="w")

        combo_search = ttk.Combobox(self.search_frame,
                                    textvariable=self.search_by,
                                    font=("times new roman", 13, "bold"),
                                    width=10, state="readonly")
        combo_search['values'] = ("UID_no", "Name")
        combo_search.grid(row=0, column=1, pady=10, padx=20)

        txt_search = Entry(self.search_frame,
                           textvariable=self.search_txt,
                           font=("times new roman", 10, "bold"), width=20,
                           bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(self.search_frame, text="Search",
                           width=10, pady=5,
                           command=self.search_data)
        searchbtn.grid(row=0, column=3, padx=10, pady=10)

        showallbtn = Button(self.search_frame, text="Show all",
                            width=10, pady=5,
                            command=self.fetch_data)
        showallbtn.grid(row=0, column=4, padx=10, pady=10)

        Table_Frame = Frame(self.search_frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=830, height=500)
        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Teacher_table = ttk.Treeview(Table_Frame,
                                          columns=("UID_no", "name", "email", "contactno", "subject"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Teacher_table.xview)
        scroll_y.config(command=self.Teacher_table.yview)

        self.Teacher_table.heading("UID_no", text="Uid_no.")
        self.Teacher_table.heading("name", text="Name.")
        self.Teacher_table.heading("email", text="Email.")
        self.Teacher_table.heading("contactno", text="Contact No.")
        self.Teacher_table.heading("subject", text="Subject.")
        self.Teacher_table['show'] = 'headings'
        self.Teacher_table.column("UID_no", width=100)
        self.Teacher_table.column("name", width=100)
        self.Teacher_table.column("email", width=100)
        self.Teacher_table.column("contactno", width=100)
        self.Teacher_table.column("subject", width=100)
        self.Teacher_table.pack(fill=BOTH, expand=1)
        self.Teacher_table.bind("<ButtonRelease-1>", self.get_cursor)

        back_btn = Button(self.search_frame, text="Back", width=10,pady=5, command=self.switch_to_manage_page)
        back_btn.grid(row=0, column=10, padx=10, pady=10)

        self.fetch_data()

    def switch_to_manage_page(self):
        self.clear()
        self.search_frame.pack_forget()
        self.manage_frame.pack(fill=BOTH, expand=1)

    def switch_to_search_page(self):
        self.clear()
        self.manage_frame.pack_forget()
        self.search_frame.pack(fill=BOTH, expand=1)

    def add_teachers(self):
        if self.UID_no_var.get() == "" or self.name_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return
        try:
            con = pymysql.connect(host="localhost",
                                  user='root', password='',
                                  database='preexam')
            cur = con.cursor()
            cur.execute("INSERT INTO teachers VALUES (%s,%s,%s,%s,%s)",
                        (self.UID_no_var.get(),
                         self.name_var.get(),
                         self.email_var.get(),
                         self.contactno_var.get(),
                         self.subject_var.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Teacher information added successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)

    def send_email(self):
        user_email = self.email_var.get()
        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email = "chetanvarade123@gmail.com"  # Replace with your email
        password = 'qwertyuiopasdfgh'  # Replace with your email password
        context = ssl.create_default_context()
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        try:
            server.starttls(context=context)  # Secure the connection
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, user_email,
                            "Subject:{}\n{}".format('PreExam', 'Thanks for your support'))
        except Exception as e:
            messagebox.showerror("Error", f"Due to {str(e)}", parent=self.root)
        finally:
            server.quit()

    def fetch_data(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='',
                                  database='preexam')
            cur = con.cursor()
            cur.execute("SELECT * FROM teachers")
            rows = cur.fetchall()
            self.Teacher_table.delete(*self.Teacher_table.get_children())
            for row in rows:
                self.Teacher_table.insert("", END, values=row)
            con.commit()
            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)

    def clear(self):
        self.UID_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.contactno_var.set("")
        self.subject_var.set("")

    def get_cursor(self, ev):
        cursor_row = self.Teacher_table.focus()
        contents = self.Teacher_table.item(cursor_row)
        row = contents['values']
        self.UID_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.contactno_var.set(row[3])
        self.subject_var.set(row[4])

    def update_data(self):
        if self.UID_no_var.get() == "" or self.name_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                update = messagebox.askyesno("Update", "Are you sure you want to update data", parent=self.root)
                if update > 0:
                    con = pymysql.connect(host='localhost', user='root', password='', database='preexam')
                    cur = con.cursor()
                    cur.execute("UPDATE teachers SET name=%s,email=%s,contactno=%s,subject=%s WHERE uid_no=%s",
                                (self.name_var.get(),
                                 self.email_var.get(),
                                 self.contactno_var.get(),
                                 self.subject_var.get(),
                                 self.UID_no_var.get()))
                else:
                    if not update:
                        return
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success", "Teacher data updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)

    def delete_data(self):
        if self.UID_no_var.get() == "":
            messagebox.showerror("Error", "UID number is required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Are you sure you want to delete this data?", parent=self.root)
                if delete > 0:
                    con = pymysql.connect(host='localhost', user='root', password='', database='preexam')
                    cur = con.cursor()
                    sql = "DELETE FROM teachers WHERE uid_no=%s"
                    value = (self.UID_no_var.get(),)
                    cur.execute(sql, value)
                else:
                    if not delete:
                        return
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Delete", "Teacher data has been deleted", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)

    def search_data(self):
        if self.search_txt.get() == "":
            messagebox.showerror("Error", "Please enter a search term", parent=self.root)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', database='preexam')
                cur = con.cursor()
                cur.execute(f"SELECT * FROM teachers WHERE {str(self.search_by.get())} LIKE '%{str(self.search_txt.get())}%'")
                rows = cur.fetchall()
                self.Teacher_table.delete(*self.Teacher_table.get_children())
                for row in rows:
                    self.Teacher_table.insert('', END, values=row)
                con.commit()
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Teacher(root)
    root.mainloop()

