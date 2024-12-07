import customtkinter as ctk
from tkinter import Scrollbar, StringVar, messagebox
import mysql.connector
from PIL import Image, ImageTk  # For image handling
import time
import tkinter as tk
from tkinter import ttk
import threading
def member_search_Form(center_frame, Library_Window):

    # Set color palette
    primary_color = "#6A5ACD"  # Slate blue
    secondary_color = "#7D7DD7"  # Lighter purple
    fg_color = "#E8EAF6"  # Light greyish-blue for background
    text_color = "#2E2E2E"  # Dark grey for text
    white_color = "#FFFFFF"  # White for labels and buttons
    button_hover_color = "#4040A1"  # Button hover color
    font_type = ("Georgia", 13, "bold")  # Stylish modern font for buttons
    label_font_type = ("Georgia", 12, "underline")  # Modern font for labels

    # Create the main form frame
    new_frame = ctk.CTkFrame(center_frame, fg_color=fg_color, corner_radius=15, border_width=2)
    new_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")

    # Add title label (centered)
    title_label = ctk.CTkLabel(new_frame, text="🔍 Search Book Information", font=("Georgia", 22, "bold"), text_color="black")
    title_label.place(relx=0.5, rely=0.05, anchor="center")

    # Create a search form frame
    search_form_frame = ctk.CTkFrame(new_frame, fg_color="white", corner_radius=10)

    # Add section title label
    account_list_label = ctk.CTkLabel(search_form_frame, text="📂 Accounts List", font=("consolas", 22, "bold"), text_color="black", corner_radius=5)

    fields={}

    def show_book_details(member_id):
        print("Member_ID : ", member_id)
        label_font = ("Montserrat", 14, "bold")
        entry_font = ("Consola", 14)
        search_by_button.configure(state="disable")
        show_detail_frame = ctk.CTkFrame(new_frame, 
                                     fg_color="white",  
                                     corner_radius=20)
        show_detail_frame.place(relx=0.5, rely=0.575, relwidth=0.95, relheight=0.8, anchor="center")

        try:
            connector = mysql.connector.connect(host="localhost", user="root", password="12345678", database="Library_Database")
            cursor = connector.cursor()
            sql = "Select * FROM PROFILES WHERE Member_ID = %s"
            cursor.execute(sql,(member_id,))
            member_data = cursor.fetchone()
            print(member_data)
            cursor.close()
        except Exception as e:
            messagebox.showerror("Error", e)

        # Add section title label
        title_label = ctk.CTkLabel(show_detail_frame, text=f"📂 ({member_data[0]}) Account Information",
                                       font=("Consolas", 18, "bold"),
                                       text_color="Black",
                                        corner_radius=5)
        title_label.place(relx=0.5, rely=0.05, anchor="center")
            

        fields.update({
            "Member_ID": ctk.CTkEntry(show_detail_frame,textvariable=StringVar(value=member_data[0]),  font=entry_font, state="disable"),
            "Password": ctk.CTkEntry(show_detail_frame,textvariable=StringVar(value=member_data[1]),  font=entry_font,  state="disable"),
            "Role": ctk.CTkEntry(show_detail_frame, textvariable=StringVar(value=member_data[2]),font=entry_font,  state="disable"),
            "Name": ctk.CTkEntry(show_detail_frame, textvariable=StringVar(value=member_data[3]), font=entry_font,  state="disable"),
            "Contact_Number": ctk.CTkEntry(show_detail_frame,textvariable=StringVar(value=member_data[4]), font=entry_font,  state="disable"),
            "Email": ctk.CTkEntry(show_detail_frame,textvariable=StringVar(value=member_data[5]), font=entry_font, state="disable"),
            "DOB": ctk.CTkEntry(show_detail_frame,textvariable=StringVar(value=member_data[6]), font=entry_font, state="disable"),
            "Communication_Address": ctk.CTkEntry(show_detail_frame,textvariable=StringVar(value=member_data[7]), font=entry_font,  state="disable"),
            "Registartion_Date": ctk.CTkEntry(show_detail_frame,textvariable=StringVar(value=member_data[8]), font=entry_font, state="disable"),
            "Gender": ctk.CTkEntry(show_detail_frame,textvariable=StringVar(value=member_data[10]), font=entry_font,  state="disable"),
            "Occupation": ctk.CTkEntry(show_detail_frame,textvariable=StringVar(value=member_data[11]), font=entry_font, state="disable"),
        })

        y = 0.15
        for label_text, entry in fields.items():
            label = ctk.CTkLabel(show_detail_frame, text=label_text, font=label_font, text_color="#34495e")
            label.place(relx=0.35, rely=y, anchor="e", relwidth=0.25)
            entry.place(relx=0.4, rely=y, anchor="w", relwidth=0.25)
            y += 0.065

        # Label for the image
        image_label = ctk.CTkLabel(show_detail_frame, text="\nProfile\nImage", fg_color=primary_color, compound="top", text_color="black")
        image_label.place(relx=0.7, rely=0.4, relwidth=0.25, relheight=0.4, anchor="w")

        profile_image=member_data[9]
        
        # Preload cover image if available
        
        if profile_image:
            try:
                img = Image.open(profile_image)
                img = img.resize((150, 150))
                img = ImageTk.PhotoImage(img)
                image_label.configure(image=img, fg_color="transparent")
                image_label.image = img
            except Exception as e:
                messagebox.showerror("Loading Image ...... ", e)

        # Function to copy text from the disabled entry when the button is clicked
        def copy_text():
        
            # Copy the content of the entry box to the clipboard
            show_detail_frame.clipboard_clear()
            show_detail_frame.clipboard_append(member_id)
        
            # Show a message to inform the user
            messagebox.showinfo("Copied", "Text has been copied to clipboard!")

        # Create a button to copy text
        copy_button = ctk.CTkButton(show_detail_frame, text="Copy Member_ID", fg_color="orange", command=copy_text)
        copy_button.place(relx=0.7, rely=0.15, anchor="w",relwidth=0.25)


        def close():
            show_detail_frame.destroy()
            search_by_button.configure(state="normal")

        cancel_button = ctk.CTkButton(show_detail_frame, text="❌ Close", command=close, hover_color="Green")
        cancel_button.place(relx=0.5, rely=0.925, anchor="center", relwidth=0.15)

        messagebox.showinfo("Message", "You can copy Member_ID by CTRL-c")


    # Create a scrollable frame function
    def create_scrollable_frame(root, color, radius):
        main_frame = ctk.CTkFrame(root, fg_color=color, corner_radius=radius)
        canvas = ctk.CTkCanvas(main_frame, bg=color)
        canvas.grid(row=0, column=0, sticky="nsew")

        h_scrollbar = Scrollbar(main_frame, orient="horizontal", command=canvas.xview)
        v_scrollbar = Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        h_scrollbar.grid(row=1, column=0, sticky="ew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")

        canvas.configure(xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set)

        scrollable_frame = ctk.CTkFrame(canvas, fg_color=color, corner_radius=radius)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        def configure_scroll_region(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        scrollable_frame.bind("<Configure>", configure_scroll_region)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        return [scrollable_frame, main_frame]

    frame_list = create_scrollable_frame(search_form_frame, "#AFDBF5", 20)
    scrollable_frame = frame_list[0]
    main_frame = frame_list[1]

    def Search_button():
        threading.Thread(target=run_search).start()  # Start the search in a separate thread

    # The actual search function (long-running task)
    def run_search():
        search_option = search_by_menu.get()
        detail = detail_EntryBox.get()

        if search_option != "Select by Detail":
            book_data = []
            try:
                connector = mysql.connector.connect(host="localhost", user="root", password="12345678", database="Library_Database")
                cursor = connector.cursor()
                sql = f'SELECT Member_ID, Name, Contact_Number, Email FROM PROFILES WHERE {search_option} like "{detail}%"'
                cursor.execute(sql)
                member_data = cursor.fetchall()
                cursor.close()
            except Exception as e:
                messagebox.showerror("Error", e)
                return

            if member_data:
                try:
                    for widget in search_form_frame.winfo_children():
                        widget.place_forget()

                    for widget in scrollable_frame.winfo_children():
                        widget.destroy()
                except Exception as e:
                    messagebox.showerror("Error", e)

                search_form_frame.place(relx=0.5, rely=0.575, relwidth=0.95, relheight=0.8, anchor="center")

                progress_var = tk.IntVar()
                progress = len(member_data)

                progress_bar = ttk.Progressbar(search_form_frame, variable=progress_var, maximum=progress)
                progress_bar.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.5)

                x, y = 1, 0


                headings = ["Member_ID", "Full Name", "Contact_Number", "Email"]
                for i, heading in enumerate(headings):
                    label = ctk.CTkLabel(scrollable_frame, text=heading, font=font_type, text_color="Black", fg_color=white_color, corner_radius=8)
                    label.grid(row=0, column=i, padx=20, pady=15)

                for i, row in enumerate(member_data):
                    member_id_button = ctk.CTkButton(scrollable_frame, text=row[0], font=("Consolas", 12, "bold", "underline"),
                                                     text_color="white", fg_color="black", corner_radius=8, width=50,
                                                     command=lambda row_value=row[0]: show_book_details(row_value))
                    member_id_button.grid(row=x, column=0, padx=15, pady=10)

                    for column in range(1, 4):
                        label = ctk.CTkLabel(scrollable_frame, text=row[column], font=label_font_type, text_color=text_color,
                                             fg_color=white_color, corner_radius=8)
                        label.grid(row=x, column=column, padx=15, pady=10)

                    progress_var.set(i + 1)
                    search_form_frame.update_idletasks()
                    x += 1
                progress_bar.place_forget()
                account_list_label.place(relx=0.5, rely=0.045, anchor="center")
                main_frame.place(relx=0.5, rely=0.53, relwidth=0.95, relheight=0.875, anchor="center")

                messagebox.showinfo("Information", "You can view information of Member by clicking on the Book_ID button.")
                

            else:
                search_form_frame.place_forget()
                messagebox.showinfo("Search", f"No Member Information found for given {detail}!")
        else:
            messagebox.showwarning("Warning", "Select an option for searching")

    # Search by options
    search_by_var = StringVar(value="Select by Detail")
    search_by_options = ["Member_ID", "Name", "Contact_Number", "Email"]

    # Search by dropdown
    search_by_menu = ctk.CTkOptionMenu(new_frame, values=search_by_options, variable=search_by_var, fg_color=primary_color)
    search_by_menu.place(relx=0.0975, rely=0.125, anchor="w", relwidth=0.225)

    # Entry box for entering detail
    detail_EntryBox = ctk.CTkEntry(new_frame, placeholder_text="Enter Info", font=font_type, text_color="Black")
    detail_EntryBox.place(relx=0.4, rely=0.125, anchor="w", relwidth=0.225)

    # Search button
    search_by_button = ctk.CTkButton(new_frame, text="Search", font=font_type, fg_color=primary_color, command=Search_button)
    search_by_button.place(relx=0.675, rely=0.125, anchor="w", relwidth=0.225)

if __name__ == "__main__":
    member_search_Form(center_frame, Library_Window)
