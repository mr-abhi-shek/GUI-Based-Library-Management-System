import customtkinter as ctk
from tkinter import messagebox, StringVar
import mysql.connector
import random
from datetime import datetime, timedelta
import time

def return_book_Form(center_frame):
    # Set colors, fonts, etc. (same as in issue_book_form)
    primary_color = "#6A5ACD"
    secondary_color = "#7D7DD7"
    fg_color = "#E8EAF6"
    text_color = "#2E2E2E"
    white_color = "#FFFFFF"
    button_hover_color = "#4040A1"
    font_type = ("Georgia", 15, "bold")
    label_font_type = ("Georgia", 14)
    data_font_type = ("Consolas", 14, "bold")

    # Create return book form frame
    return_frame = ctk.CTkFrame(center_frame, fg_color=fg_color, corner_radius=15, border_width=2)
    return_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")

    # Title
    title_label = ctk.CTkLabel(return_frame, text="📘 Return Book Form", font=("Georgia", 22, "bold"), text_color="black")
    title_label.place(relx=0.5, rely=0.04, anchor="center")

    # Return book frame
    form_frame = ctk.CTkFrame(return_frame, fg_color="white", corner_radius=10)
    form_frame.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.75, anchor="center")

    # Book search section (Token or Book ID)
    token_label = ctk.CTkLabel(form_frame, text="🔑 Token Number:", font=label_font_type)
    token_label.place(relx=0.1, rely=0.05)

    token_entry = ctk.CTkEntry(form_frame, placeholder_text="Enter Token Number", font=data_font_type)
    token_entry.place(relx=0.4, rely=0.05, relwidth=0.2)

    # Search Button
    search_button = ctk.CTkButton(form_frame, text="Search", font=label_font_type, command=lambda: search_issued_book(token_entry.get()))
    search_button.place(relx=0.65, rely=0.05)

    info_frame = ctk.CTkFrame(form_frame, fg_color="white", corner_radius=10)
    info_frame.place(relx=0.5, rely=0.525, relwidth=0.95, relheight=0.8, anchor="center")

    # Display book and member details after search
    book_info_label = ctk.CTkLabel(form_frame, text="", font=data_font_type)
    book_info_label.place(relx=0.1, rely=0.3)

    def show_info(member_id, book_id, issue_date, due_date, status, info_frame):

        
        # Book search section (Token or Book ID)
        member_id_label = ctk.CTkLabel(info_frame, text="Member ID:", font=label_font_type)
        member_id_label.place(relx=0.25, rely=0.1)

        member_id_entry = ctk.CTkEntry(info_frame, textvariable=StringVar(value=member_id), font=data_font_type,state="disable")
        member_id_entry.place(relx=0.55, rely=0.1, relwidth=0.25)

        book_id_label = ctk.CTkLabel(info_frame, text="Book ID", font=label_font_type)
        book_id_label.place(relx=0.25, rely=0.25)

        book_id_entry = ctk.CTkEntry(info_frame, textvariable=StringVar(value=book_id), font=data_font_type,state="disable")
        book_id_entry.place(relx=0.55, rely=0.25, relwidth=0.25)

        issue_date_label = ctk.CTkLabel(info_frame, text="Issue Date:", font=label_font_type)
        issue_date_label.place(relx=0.25, rely=0.4)

        issue_date_entry = ctk.CTkEntry(info_frame, textvariable=StringVar(value=issue_date), font=data_font_type,state="disable")
        issue_date_entry.place(relx=0.55, rely=0.4, relwidth=0.25)

        due_date_label = ctk.CTkLabel(info_frame, text="Issue Date:", font=label_font_type)
        due_date_label.place(relx=0.25, rely=0.55)

        due_date_entry = ctk.CTkEntry(info_frame, textvariable=StringVar(value=due_date), font=data_font_type,state="disable")
        due_date_entry.place(relx=0.55, rely=0.55, relwidth=0.25)

        status_label = ctk.CTkLabel(info_frame, text="Status:", font=label_font_type)
        status_label.place(relx=0.25, rely=0.7)

        status_entry = ctk.CTkEntry(info_frame, textvariable=StringVar(value=status), font=data_font_type,state="disable")
        status_entry.place(relx=0.55, rely=0.7, relwidth=0.25)

        # Return Button
        return_button = ctk.CTkButton(info_frame, text="Return Book", font=label_font_type, fg_color=primary_color, hover_color=button_hover_color, command=return_book)
        return_button.place(relx=0.5, rely=0.9, anchor="center")
        
    def destroy_widgets(info_frame):
        try:
            for widget in info_frame.winfo_children():
                widget.destroy()
        except:
            pass
    
    # Search function for finding issued book
    def search_issued_book(token_number):
        if token_number != "":
            try:
                connector = mysql.connector.connect(host="localhost", user="root", password="12345678", database="Library_Database")
                cursor = connector.cursor()
                sql = 'SELECT Member_ID, Book_ID, Issue_Date, Due_Date, Status FROM BOOKS_ISSUE WHERE Token_Number = %s AND Status = %s'
                cursor.execute(sql, (token_number, "Issue"))
                issued_data = cursor.fetchone()
                cursor.close()

                if issued_data:
                    member_id, book_id, issue_date, due_date, status = issued_data
                    # Display book and member information
                    #book_info_label.configure(text=f"Book ID: {book_id}\nMember ID: {member_id}\nIssue Date: {issue_date}\nDue Date: {due_date}")
                    destroy_widgets(info_frame)
                    show_info(member_id, book_id, issue_date, due_date, status, info_frame)
                else:
                    messagebox.showerror("Not Found", f"No active book issued for Token Number {token_number}.")
            except Exception as e:
                messagebox.showerror("Error", e)
        else:
            messagebox.showwarning("Warning", "Please enter the Token Number.")

    # Return book function
    def return_book():
        token_number = token_entry.get()
        if token_number:
            try:
                connector = mysql.connector.connect(host="localhost", user="root", password="12345678", database="Library_Database")
                cursor = connector.cursor()
                
                # Mark the book as returned
                sql = """UPDATE BOOKS_ISSUE SET Status = %s, Return_Date = %s WHERE Token_Number = %s"""
                return_date = datetime.now().strftime('%Y-%m-%d')
                cursor.execute(sql, ("Returned", return_date, token_number))
                connector.commit()

                # Update book quantity in the BOOKS table
                sql = "UPDATE BOOKS SET Number_of_Books = Number_of_Books + 1 WHERE Book_ID = (SELECT Book_ID FROM BOOKS_ISSUE WHERE Token_Number = %s)"
                cursor.execute(sql, (token_number,))
                connector.commit()

                messagebox.showinfo("Success", "Book returned successfully!")
                cursor.close()

                # Reset form
                token_entry.delete(0, 'end')
                book_info_label.configure(text="")
                destroy_widgets(info_frame)

            except Exception as e:
                messagebox.showerror("Error", e)
        else:
            messagebox.showwarning("Warning", "Please enter a valid Token Number.")

if __name__ == "__main__":
    return_book_Form(center_frame)
