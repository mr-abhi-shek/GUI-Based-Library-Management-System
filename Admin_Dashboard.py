import customtkinter
from PIL import Image, ImageTk
from datetime import datetime
import mysql.connector
import tkinter.messagebox as messagebox

import Add_Book_Window
import Edit_Book_Window
import Delete_Book_Window
import Search_Book_Window

import Add_Member_Window
import Edit_Member_Window
import Delete_Member_Window
import Search_Member_Window

import Issue_Book_Window
import Return_Book_Window


def Dashoard_Admin_Window(login_id, pwd):
    customtkinter.set_appearance_mode("light")
    Dashoard_Admin_Window = customtkinter.CTk()

    # Setting window dimensions
    width, height = Dashoard_Admin_Window.winfo_screenwidth(), Dashoard_Admin_Window.winfo_screenheight()
    Dashoard_Admin_Window.geometry(f"{int(width/1.2)}x{int(height/1.2)}")

    Dashoard_Admin_Window.title("Library Management System ADMIN Dashboard")

    # Light Color Scheme
    primary_color = "#7A9E9F"  # Muted Sky Blue
    secondary_color = "#5B9FCC"  # Muted Light Magenta

    # Button Background Color
    button_bg = "#A3D1E8"  # Soft Aqua Blue

    # Frames Color
    left_frame_color = "#FFFFFF"  # Light Gray for the left frame (softer than white)
    center_frame_color = "#7A9E9F"  # Very light gray for the center frame
    right_frame_color = "#FFFFFF"  # Light Gray for the right frame

    # Button style updates
    button_font = ("Courier New", 14, "bold")
    button_text_color = "#FFFFFF"  # White for button text
    button_fg_color = "#9999CC"  # Light blue
    button_hover_color = "#6A5ACD"  # Hover color: lavender

    # Section Label Configuration
    section_label_font = ("Verdana", 13, "bold")  # Section label font: Verdana, Bold, 16px
    label_text_color = "#2E4053"  # Steel Gray for labels

    label_font = ("Montserrat", 14, "bold")
    entry_font = ("Consolas", 14, "bold")


    # Left frame for the sections
    left_frame = customtkinter.CTkFrame(Dashoard_Admin_Window, fg_color=left_frame_color, corner_radius=15, border_width=4, border_color=primary_color)
    left_frame.place(relx=0.02,rely=0.5,relwidth=0.15,relheight=0.95,anchor="w")

    # Center frame for the content
    center_frame = customtkinter.CTkFrame(Dashoard_Admin_Window, fg_color="white", corner_radius=20, border_width=4, border_color="orange")
    center_frame.place(relx=0.1875,rely=0.5,relwidth=0.625, relheight=0.98, anchor="w")

    # Right frame for settings
    right_frame = customtkinter.CTkFrame(Dashoard_Admin_Window, fg_color=right_frame_color, corner_radius=15, border_width=4, border_color="#333333")
    right_frame.place(relx=0.98,rely=0.5,relwidth=0.15, relheight=0.95, anchor="e")

    #creating a frame for Content_frame in the center_frame
    content_frame = customtkinter.CTkFrame(center_frame,
                                           fg_color="#CCCCFF",
                                            border_width=4,# Light purple for inner frame
                                         corner_radius=20)
    content_frame.place(relx=0.5, rely=0.5, relwidth=0.98, relheight=0.98, anchor="center")




    # === Book Management Section ===
    book_section_label = customtkinter.CTkLabel(left_frame, text="📚 Book Management", font=section_label_font, text_color=label_text_color)
    book_section_label.place(relx=0.5, rely=0.05, anchor="center")

    def destroy_widgets():
        for widget in content_frame.winfo_children():
            widget.destroy()

    def add_book():
        destroy_widgets()
        Add_Book_Window.add_book_form(content_frame)

    add_book_button = customtkinter.CTkButton(left_frame, text="Add Book", font=button_font, fg_color=button_fg_color, text_color=button_text_color,
                                              hover_color=button_hover_color, corner_radius=10, command=add_book)
    add_book_button.place(relx=0.5, rely=0.12, relwidth=0.8, anchor="center")

    def edit_book():
        
        destroy_widgets()
        Edit_Book_Window.edit_book_form(content_frame)

    edit_book_button = customtkinter.CTkButton(left_frame, text="Edit Book", font=button_font, fg_color=button_fg_color, text_color=button_text_color,
                                               hover_color=button_hover_color, corner_radius=10, command=edit_book)
    edit_book_button.place(relx=0.5, rely=0.18, relwidth=0.8, anchor="center")

    def delete_book():
        # Placeholder for delete book function
        destroy_widgets()
        Delete_Book_Window.delete_book_form(content_frame)

    delete_book_button = customtkinter.CTkButton(left_frame, text="Delete Book", font=button_font, fg_color=button_fg_color, text_color=button_text_color,
                                                 hover_color=button_hover_color, corner_radius=10, command=delete_book)
    delete_book_button.place(relx=0.5, rely=0.24, relwidth=0.8, anchor="center")

    def search_book():
        # Placeholder for search book function
        destroy_widgets()
        Search_Book_Window.book_search_Form(content_frame)

    search_book_button = customtkinter.CTkButton(left_frame, text="Search Book", font=button_font, fg_color=button_fg_color, text_color=button_text_color,
                                                 hover_color=button_hover_color, corner_radius=10, command=search_book)
    search_book_button.place(relx=0.5, rely=0.30, relwidth=0.8, anchor="center")

    # === Member Management Section ===
    member_section_label = customtkinter.CTkLabel(left_frame, text="👤 Member Management", font=section_label_font, text_color=label_text_color)
    member_section_label.place(relx=0.5, rely=0.40, anchor="center")

    def add_member():
        # Placeholder for add member function
        destroy_widgets()
        Add_Member_Window.add_member_form(content_frame)

    add_member_button = customtkinter.CTkButton(left_frame, text="Add Member", font=button_font, fg_color=button_fg_color, text_color=button_text_color,
                                                hover_color=button_hover_color, corner_radius=10, command=add_member)
    add_member_button.place(relx=0.5, rely=0.47, relwidth=0.8, anchor="center")

    def edit_member():
        # Placeholder for edit member function
        destroy_widgets()
        Edit_Member_Window.edit_member_form(content_frame)

    edit_member_button = customtkinter.CTkButton(left_frame, text="Edit Member", font=button_font, fg_color=button_fg_color, text_color=button_text_color,
                                                 hover_color=button_hover_color, corner_radius=10, command=edit_member)
    edit_member_button.place(relx=0.5, rely=0.53, relwidth=0.8, anchor="center")

    def delete_member():
        # Placeholder for delete member function
        destroy_widgets()
        Delete_Member_Window.delete_member_form(content_frame)

    delete_member_button = customtkinter.CTkButton(left_frame, text="Delete Member", font=button_font, fg_color=button_fg_color, text_color=button_text_color,
                                                   hover_color=button_hover_color, corner_radius=10, command=delete_member)
    delete_member_button.place(relx=0.5, rely=0.59, relwidth=0.8, anchor="center")

    def view_member():
        # Placeholder for view member function
        destroy_widgets()
        Search_Member_Window.member_search_Form(content_frame,Dashoard_Admin_Window)

    view_member_button = customtkinter.CTkButton(left_frame, text="View Member", font=button_font, fg_color=button_fg_color, text_color=button_text_color,
                                                 hover_color=button_hover_color, corner_radius=10, command=view_member)
    view_member_button.place(relx=0.5, rely=0.65, relwidth=0.8, anchor="center")

    # === Book Issuance/Return Section ===
    issue_return_label = customtkinter.CTkLabel(left_frame, text="🔄 Book Issuance/Return", font=section_label_font, text_color=label_text_color)
    issue_return_label.place(relx=0.5, rely=0.75, anchor="center")

    def issue_book():
        # Placeholder for issue book function
        # Placeholder for view member function
        destroy_widgets()
        Issue_Book_Window.issue_book_Form(content_frame)


    issue_book_button = customtkinter.CTkButton(left_frame, text="Issue Book", font=button_font, fg_color=button_fg_color, text_color=button_text_color,
                                                hover_color=button_hover_color, corner_radius=10, command=issue_book)
    issue_book_button.place(relx=0.5, rely=0.82, relwidth=0.8, anchor="center")

    def return_book():
        # Placeholder for return book function
        destroy_widgets()
        Return_Book_Window.return_book_Form(content_frame)

    return_book_button = customtkinter.CTkButton(left_frame, text="Return Book", font=button_font, fg_color=button_fg_color, text_color=button_text_color,
                                                 hover_color=button_hover_color, corner_radius=10, command=return_book)
    return_book_button.place(relx=0.5, rely=0.88, relwidth=0.8, anchor="center")

    # === Member Management Section ===
    my_section_label = customtkinter.CTkLabel(right_frame, text="👤 Profile Section", font=section_label_font, text_color=label_text_color)
    my_section_label.place(relx=0.5, rely=0.05, anchor="center")


    # Populate form with my profile data

    def populate_my_profile():
        new_frame= customtkinter.CTkFrame(content_frame, fg_color="white", corner_radius=20)
        new_frame.place(relx=0.5,rely=0.5,relwidth=0.9, relheight=0.8, anchor="center")
        fields={}
        # Creating Label for Welcome Message
        account_information_label = customtkinter.CTkLabel(content_frame, text="ADMIN Account Information", 
                                                font=("Rockwell Extra Bold", 24), text_color="Black")
        account_information_label.place(relx=0.5, rely=0.05, anchor="center")
            
        data_list=[("Member_ID", "Password", "Role", "Name", "Contact_Number", "Email", "DOB", "Communication_Address", "Registartion_Date", "profile_image")]
        try:
            connector=mysql.connector.connect(host="localhost", user="root", password="12345678", database="Library_Database")
            # Creating a Cursor for MySQL
            cursor = connector.cursor()
            cursor.execute("SELECT * FROM PROFILES WHERE Member_ID = %s AND Password = %s ", (login_id, pwd))
            data_list=cursor.fetchall()
            cursor.close()
            
            print(data_list)
        except Exception as e:
            messagebox.showerror("Error",e)

        # Create labels and entries for other fields and pre-populate them with fetched data
        fields.update({
            "Member_ID": customtkinter.CTkLabel(new_frame, text=data_list[0][0], font=entry_font,bg_color="#CCCCFF", corner_radius=20),
            "Password": customtkinter.CTkLabel(new_frame, text=data_list[0][1], font=entry_font,bg_color="#CCCCFF", corner_radius=20),
            "Profile Type": customtkinter.CTkLabel(new_frame, text=data_list[0][2], font=entry_font,bg_color="#CCCCFF", corner_radius=20),
            "Full Name": customtkinter.CTkLabel(new_frame, text=data_list[0][3], font=entry_font,bg_color="#CCCCFF", corner_radius=20),
            "Contact_Number": customtkinter.CTkLabel(new_frame,  text=data_list[0][4], font=entry_font,bg_color="#CCCCFF", corner_radius=20),
            "Email": customtkinter.CTkLabel(new_frame,  text=data_list[0][5], font=entry_font,bg_color="#CCCCFF", corner_radius=20),
            "Date of Birth": customtkinter.CTkLabel(new_frame, text=data_list[0][6], font=entry_font,bg_color="#CCCCFF", corner_radius=20),
            "Communication_Address": customtkinter.CTkLabel(new_frame,text=data_list[0][7], font=entry_font, bg_color="#CCCCFF", corner_radius=20),
            "Registartion_Date": customtkinter.CTkLabel(new_frame, text=data_list[0][8], font=entry_font,bg_color="#CCCCFF", corner_radius=20),
            "Gender": customtkinter.CTkLabel(new_frame, text=data_list[0][10], font=entry_font,bg_color="#CCCCFF", corner_radius=20),
            "Occupation": customtkinter.CTkLabel(new_frame, text=data_list[0][11], font=entry_font,bg_color="#CCCCFF", corner_radius=20)
        })

        y = 0.35
        for label_text, entry in fields.items():
            label = customtkinter.CTkLabel(new_frame, text=label_text, bg_color="#CCCCFF", font=label_font, text_color="#34495e")
            label.place(relx=0.475, rely=y, anchor="e", relwidth=0.4, relheight=0.05)
            entry.place(relx=0.525, rely=y, anchor="w", relwidth=0.4, relheight=0.05)
            y += 0.055

        # Label for the image
        image_label = customtkinter.CTkLabel(new_frame, text="Profile Image", font=entry_font, fg_color=primary_color, compound="top", text_color="black")
        image_label.place(relx=0.5, rely=0.15, relwidth=0.25, relheight=0.3, anchor="center")

        # Preload cover image if available
        if data_list[0][9]:
            try: 
                img = Image.open(data_list[0][9])
                print("\nImage : ", data_list[0][9])
                img = img.resize((125, 125))
                img = ImageTk.PhotoImage(img)
                image_label.configure(image=img, fg_color="transparent")
                image_label.image = img
            except Exception as e:
                messagebox.showerror("Image Loading Error!", e)

    def my_profile():
        destroy_widgets()
        populate_my_profile()

    my_profile_button = customtkinter.CTkButton(right_frame, text="My Profile", font=button_font, fg_color=button_fg_color, text_color=button_text_color,
                                              hover_color=button_hover_color, corner_radius=10, command=my_profile)
    my_profile_button.place(relx=0.5, rely=0.12, relwidth=0.8, anchor="center")


    def close_button():
        Dashoard_Admin_Window.destroy()

    close_button = customtkinter.CTkButton(right_frame, text="Close", font=button_font, fg_color=button_fg_color, text_color=button_text_color,
                                                 hover_color=button_hover_color, corner_radius=10, command=close_button)
    close_button.place(relx=0.5, rely=0.18, relwidth=0.8, anchor="center")
    
    # Running the window loop
    Dashoard_Admin_Window.mainloop()

if __name__ == "__main__":
    Dashoard_Admin_Window(login_id, pwd)
