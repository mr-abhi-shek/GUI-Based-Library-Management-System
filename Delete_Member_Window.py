import customtkinter
from tkinter import StringVar
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
import mysql.connector
import useable_module
import Populate_Member_Info

def delete_member_form(content_frame):

    # Colors and Fonts
    primary_color = "#9bb2e5"  
    button_bg = "#FF8C00"  # Dark Orange
    frame_bg = "#F0F0F0"  # Light Gray
    label_font = ("Montserrat", 14, "bold")
    entry_font = ("Consola", 14)

    # Create main frame with border, shadow, and 3D effect
    main_frame = customtkinter.CTkFrame(content_frame, fg_color=primary_color, corner_radius=20)
    main_frame.place(relx=0.5,rely=0.5,relwidth=1, relheight=1, anchor="center")

    # Create main frame with border, shadow, and 3D effect
    update_main_frame = customtkinter.CTkFrame(main_frame, fg_color=primary_color, corner_radius=20)
    update_main_frame.place(relx=0.5, rely=0.55, relwidth=0.9,relheight=0.725,anchor="center")#relx=0.5,rely=0.5,relwidth=0.98, relheight=0.98, anchor="center"
    

    # Add heading label with an icon
    heading_Label = customtkinter.CTkLabel(main_frame, text="📚 Delete Member Account", font=("Georgia", 22, "bold"), text_color="#010B13")
    heading_Label.place(relx=0.5, rely=0.055, anchor="center")

    # Section to enter the unique Book ID
    member_id_label = customtkinter.CTkLabel(main_frame, text="Enter Unique Member ID", font=label_font, text_color="black")
    member_id_label.place(relx=0.35, rely=0.1275, anchor="e", relwidth=0.25)
    
    member_id_entry = customtkinter.CTkEntry(main_frame, font=entry_font)
    member_id_entry.place(relx=0.4, rely=0.1275, anchor="w", relwidth=0.25)

    # Variables to hold book information fields (initialized empty until book is fetched)
    fields = {}
    
    # Function to fetch existing book data
    def fetch_member_data(member_id):
        try:
            connector = mysql.connector.connect(host="localhost", user="root", password="12345678", database="Library_Database")
            cursor = connector.cursor()
            sql = "SELECT * FROM PROFILES WHERE member_id = %s"
            cursor.execute(sql, (member_id,))
            member_data = cursor.fetchone()
            cursor.close()
            if member_data:
                #book_id_entry.configure(state="disable")
                Populate_Member_Info.populate_member_form(member_id,member_data, update_main_frame)  # Call function to populate form with book data
            else:
                for widget in update_main_frame.winfo_children():
                    widget.destroy()
                update_main_frame.configure( border_width=0, corner_radius=0, fg_color=primary_color)
                messagebox.showerror("Error", "Member ID not found!")
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching Member data: {e}")

    
        # Save updated book function with confirmation pop-up
        def delete_info(member_id):
            if confirm_checkbox.get()=="1":
                try:
                    connector = mysql.connector.connect(host="localhost", user="root", password="12345678", database="Library_Database")
                    cursor = connector.cursor()
                    sql ="""
                            DELETE from PROFILES
                            WHERE
                            member_id=%s
                        """
                    response=messagebox.askyesno("Delete Request Confirmation", "Warning: This action cannot be undone!\nDo you want to delete member account?")
                    if response:
                        cursor.execute(sql, (member_id,))
                        connector.commit()
                        cursor.close()

                        messagebox.showinfo("Member Account Deleted", "Member Account Deleted from Database Successfully!")
                        main_frame.destroy()
                            
                except Exception as e:
                    messagebox.showerror("Error", f"Error Deleting: {e}")
            else:
                messagebox.showinfo("I agree ...... ", "Select the Checkbox.")


        # Confirmation checkbox
        confirm_var = StringVar(value="0")
        confirm_checkbox = customtkinter.CTkCheckBox(update_main_frame, text="I understand that this action is irreversible.",
                                           variable=confirm_var, onvalue="1", offvalue="0", 
                                           font=("Georgia", 13, "bold"), text_color="#C40234")
        confirm_checkbox.place(relx=0.5, rely=0.8, anchor="center")

        # Warning Label
        warning_label = customtkinter.CTkLabel(update_main_frame, text="Warning: This action cannot be undone!",
                                     font=("Georgia", 13, "bold"), text_color="#C40234")
        warning_label.place(relx=0.5, rely=0.85, anchor="center")
                                                


        

        # Add hover effects on buttons
        delete_button = customtkinter.CTkButton(update_main_frame, text="🗑 Delete", fg_color="RED", command=lambda : delete_info(member_id), hover_color="#C40234")
        delete_button.place(relx=0.3, rely=0.925, anchor="e", relwidth=0.15)

        cancel_button = customtkinter.CTkButton(update_main_frame, text="❌ Cancel", command=main_frame.destroy, hover_color="Green")
        cancel_button.place(relx=0.75, rely=0.925, anchor="w", relwidth=0.15)


    # Button to fetch the book data based on entered Book ID
    fetch_button = customtkinter.CTkButton(main_frame, text="🔍 Fetch Info", fg_color=button_bg, hover_color="#FF4500", command=lambda: fetch_member_data(member_id_entry.get()))
    fetch_button.place(relx=0.7275, rely=0.1275, anchor="w", relwidth=0.15)

    # Footer Section
    footer_label = customtkinter.CTkLabel(main_frame, text="Library Management System v1.0 | Need Help? Contact support@library.com", 
                                      font=("Arial", 12), text_color="#010B13")
    footer_label.place(relx=0.5, rely=0.95, anchor="center")

#===========================

if __name__ == "__main__":
    delete_member_form(content_frame)
