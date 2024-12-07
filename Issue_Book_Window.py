import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
import random
from datetime import datetime, timedelta
import time

#Global Variables
member_info_flag=False
book_info_flag=False
book_available=0

def issue_book_Form(center_frame):

    # Set color palette
    primary_color = "#6A5ACD"  # Slate blue
    secondary_color = "#7D7DD7"  # Lighter purple
    fg_color = "#E8EAF6"  # Light greyish-blue for background
    text_color = "#2E2E2E"  # Dark grey for text
    white_color = "#FFFFFF"  # White for labels and buttons
    button_hover_color = "#4040A1"  # Button hover color
    font_type = ("Georgia", 15, "bold")  # Stylish modern font for buttons
    label_font_type = ("Georgia", 14)  # Modern font for labels
    data_font_type=("Consolas", 14, "bold")

    # Create the main form frame
    new_frame = ctk.CTkFrame(center_frame, fg_color=fg_color, corner_radius=15, border_width=2)
    new_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")

    # Add title label (centered)
    title_label = ctk.CTkLabel(new_frame, text="📘 Issue Book Form", font=("Georgia", 22, "bold"), text_color="black")
    title_label.place(relx=0.5, rely=0.04, anchor="center")

    # Create a form frame
    form_frame = ctk.CTkFrame(new_frame, fg_color="white", corner_radius=10)
    form_frame.place(relx=0.5, rely=0.525, relwidth=0.95, relheight=0.9, anchor="center")

    def search_member():
        global member_info_flag
        member_id = member_id_entry.get()
        if member_id!="":
            member_data = []
            try:
                connector = mysql.connector.connect(host="localhost", user="root", password="12345678", database="Library_Database")
                cursor = connector.cursor()
                sql = 'SELECT Name, Contact_Number, Email FROM PROFILES WHERE Member_ID = %s'
                cursor.execute(sql, (member_id,))
                member_data = cursor.fetchall()
                cursor.close()
            except Exception as e:
                messagebox.showerror("Error", e)
                
            if member_data:
                messagebox.showinfo("Info Message", "Member Info Found!")
                member_name.configure(text=member_data[0][0],text_color="Green")
                member_contact_number.configure(text=member_data[0][1],text_color="Green")
                member_email.configure(text=member_data[0][2],text_color="Green")
                
                member_info_flag=True
            else:
                messagebox.showerror("Not Found", f"No Information available with {member_id} Member_ID!")
                member_name.configure(text="NULL",text_color="RED")
                member_contact_number.configure(text="NULL",text_color="RED")
                member_email.configure(text="NULL",text_color="RED")
                
                member_info_flag=False
        else:
            messagebox.showinfo("Info Message", "Please, Enter the Member Id")
            
            member_info_flag=False

        print("member_inf0,_flag", member_info_flag)

    def search_book():
        global book_available
        global book_info_flag
        book_id = book_id_entry.get()
        if book_id!="":
            book_data = []
            try:
                connector = mysql.connector.connect(host="localhost", user="root", password="12345678", database="Library_Database")
                cursor = connector.cursor()
                sql = 'SELECT title, author, Number_of_Books FROM BOOKS WHERE Book_ID = %s'
                cursor.execute(sql, (book_id,))
                book_data = cursor.fetchall()
                cursor.close()
            except Exception as e:
                messagebox.showerror("Error", e)
                
            if book_data:
                messagebox.showinfo("Info Message", "Book Info Found!")
                book_title.configure(text=book_data[0][0],text_color="Green")
                book_author.configure(text=book_data[0][1],text_color="Green")

                if book_data[0][2]>=1:
                    book_quantity.configure(text=book_data[0][2],text_color="Green")
                    book_info_flag=True
                    book_available = book_data[0][2]
                    print(book_available)
                else:
                    book_quantity.configure(text=book_data[0][2],text_color="RED")
                    book_info_flag=False
                    messagebox.showwarning("Waring", "Book Not Available at this moment!")
        
                
            else:
                messagebox.showerror("Not Found", f"No Information available with {book_id} Book_ID!")
                book_title.configure(text="NULL",text_color="RED")
                book_author.configure(text="NULL",text_color="RED")
                book_quantity.configure(text="NULL",text_color="RED")
                
                book_info_flag=False
        else:
            messagebox.showinfo("Info Message", "No Book_ID entered,please enter the Book_Id")
            
            book_info_flag=False

        print("book_inf0_flag", book_info_flag)
    # Member Info Section
    member_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
    member_frame.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.25, anchor="n")
    
    member_label = ctk.CTkLabel(member_frame, text="🔑 Member Info", font=("Georgia", 18, "bold"))
    member_label.place(relx=0.5, rely=0.05, anchor="center")
    
    member_id_label = ctk.CTkLabel(member_frame, text="Member ID:", font=label_font_type)
    member_id_label.place(relx=0.1, rely=0.275)
    
    member_id_entry = ctk.CTkEntry(member_frame, placeholder_text="Enter Member ID", font=data_font_type)
    member_id_entry.place(relx=0.4, rely=0.275, relwidth=0.25)

    member_search_button = ctk.CTkButton(member_frame, text="Search", font=label_font_type, command=search_member)
    member_search_button.place(relx=0.75, rely=0.275)

    member_name_label = ctk.CTkLabel(member_frame, text="Member Name:", font=label_font_type)
    member_name_label.place(relx=0.1, rely=0.475)
    
    member_name = ctk.CTkLabel(member_frame, text="", font=data_font_type)
    member_name.place(relx=0.4, rely=0.475)

    member_contact_number_label = ctk.CTkLabel(member_frame, text="Contact Number:", font=label_font_type)
    member_contact_number_label.place(relx=0.1, rely=0.675)
    
    member_contact_number = ctk.CTkLabel(member_frame, text="", font=data_font_type)
    member_contact_number.place(relx=0.4, rely=0.675)

    member_email_label = ctk.CTkLabel(member_frame, text="E-Mail:", font=label_font_type)
    member_email_label.place(relx=0.1, rely=0.875)
    
    member_email = ctk.CTkLabel(member_frame, text="", font=data_font_type)
    member_email.place(relx=0.4, rely=0.875)
    

    # Book Info Section
    book_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
    book_frame.place(relx=0.5, rely=0.35, relwidth=0.9, relheight=0.25, anchor="n")
    
    book_label = ctk.CTkLabel(book_frame, text="📚 Book Info", font=("Georgia", 18, "bold"))
    book_label.place(relx=0.5, rely=0.05, anchor="center")
    
    book_id_label = ctk.CTkLabel(book_frame, text="Book ID:", font=label_font_type)
    book_id_label.place(relx=0.1, rely=0.275)
    
    book_id_entry = ctk.CTkEntry(book_frame, placeholder_text="Enter Book ID", font=data_font_type)
    book_id_entry.place(relx=0.4, rely=0.275, relwidth=0.25)
    
    book_search_button = ctk.CTkButton(book_frame, text="Search", font=label_font_type, command=search_book)
    book_search_button.place(relx=0.75, rely=0.275)

    book_title_label = ctk.CTkLabel(book_frame, text="Book Title:", font=label_font_type)
    book_title_label.place(relx=0.1, rely=0.475)
    
    book_title = ctk.CTkLabel(book_frame, text="", font=data_font_type)
    book_title.place(relx=0.4, rely=0.475)

    book_author_label = ctk.CTkLabel(book_frame, text="Book Author:", font=label_font_type)
    book_author_label.place(relx=0.1, rely=0.675)
    
    book_author = ctk.CTkLabel(book_frame, text="", font=data_font_type)
    book_author.place(relx=0.4, rely=0.675)

    book_quantity_label = ctk.CTkLabel(book_frame, text="Books Available:", font=label_font_type)
    book_quantity_label.place(relx=0.1, rely=0.875)
    
    book_quantity = ctk.CTkLabel(book_frame, text="", font=data_font_type)
    book_quantity.place(relx=0.4, rely=0.875)


    # Date Info Section
    date_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
    date_frame.place(relx=0.5, rely=0.65, relwidth=0.9, relheight=0.2, anchor="n")

    date_label = ctk.CTkLabel(date_frame, text="📅 Issue & Due Dates", font=("Georgia", 18, "bold"))
    date_label.place(relx=0.5, rely=0.05, anchor="center")

    issue_date_label = ctk.CTkLabel(date_frame, text="Issue Date:", font=label_font_type)
    issue_date_label.place(relx=0.45, rely=0.4, anchor="e")

    issue_date=time.strftime('%Y-%m-%d')

    issue_date_value = ctk.CTkLabel(date_frame, text=issue_date, font=data_font_type, text_color="Green")
    issue_date_value.place(relx=0.55, rely=0.4, anchor="w")

    due_date_label = ctk.CTkLabel(date_frame, text="Due Date:", font=label_font_type)
    due_date_label.place(relx=0.45, rely=0.6, anchor="e")

    due_date=(datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
    
    due_date_value = ctk.CTkLabel(date_frame, text=due_date, font=data_font_type, text_color="Green")
    due_date_value.place(relx=0.55, rely=0.6, anchor="w")

    # Action Buttons Section
    button_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
    button_frame.place(relx=0.5, rely=0.8, relwidth=0.9, relheight=0.15, anchor="n")

    def generate_token_number():
        token_number = str(random.randint(10000000000, 99999999999))
        return token_number

    def check_issue(member_id, book_id):
        issue_data=[]
        try:
            connector = mysql.connector.connect(host="localhost", user="root", password="12345678", database="Library_Database")
            cursor = connector.cursor()
            sql ="select * from books_issue where member_id = %s and book_id  =%s"     
            cursor.execute(sql, (member_id, book_id))
            issue_data=cursor.fetchall()
            connector.commit()
            cursor.close()
        except Exception as e:
            messagebox.showerror("Error", e)

        if issue_data!=[] and issue_data[0][4]=="Issue":
            messagebox.showwarning("Warning", f"Book already Issued on {issue_data[0][2]} with Token Number {issue_data[0][5]}. Cannot be issued.")
            return False
        else:
            return True


    def issue_book():
        print("OK: , member_info_flag and book_info_flag and book_available", member_info_flag , book_info_flag, book_available)
        member_id=member_id_entry.get()
        book_id=book_id_entry.get()
        if member_info_flag and book_info_flag:
            book_issued = check_issue(member_id, book_id)
            if book_available>0:

                if book_issued:
                    
                    try:
                        connector = mysql.connector.connect(host="localhost", user="root", password="12345678", database="Library_Database")
                        cursor = connector.cursor()
                        sql = "INSERT INTO BOOKS_ISSUE VALUES(%s,%s,%s,%s,%s,%s,%s)"
                        token_number=generate_token_number()
                        cursor.execute(sql, (member_id, book_id, issue_date, due_date, "Issue", token_number, ""))
                        connector.commit()
                        cursor.close()

                        try:
                            connector = mysql.connector.connect(host="localhost", user="root", password="12345678", database="Library_Database")
                            cursor = connector.cursor()
                            sql ="""UPDATE BOOKS SET Number_of_Books=%s WHERE book_id=%s"""
                    
                            cursor.execute(sql, (book_available-1, book_id))
                            connector.commit()
                            cursor.close()
                        except Exception as e:
                            messagebox.showerror("Error", e)
                
                        messagebox.showinfo("Success Message", f"Successfully Book Issued with Token Number {token_number}")
                        new_frame.destroy()
                    except Exception as e:
                        messagebox.showerror("Error", e)
            else:
                messagebox.showwarning("Warning", "Book not available. Cannot be issued.")

        else:
            messagebox.showwarning("Warning", "Please enter valid Member_ID and Book_ID before issuing.")
                
                
    
    issue_button = ctk.CTkButton(button_frame, text="Issue Book", fg_color=primary_color, hover_color=button_hover_color, command=issue_book)
    issue_button.place(relx=0.2, rely=0.5, relwidth=0.2)

    reset_button = ctk.CTkButton(button_frame, text="Reset", fg_color="Red", hover_color=button_hover_color)
    reset_button.place(relx=0.575, rely=0.5, relwidth=0.2)

if __name__ == "__main__":
    issue_book_Form(center_frame)
