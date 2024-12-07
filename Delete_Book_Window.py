import customtkinter
from tkinter import StringVar
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
import mysql.connector
import useable_module

def delete_book_form(content_frame):

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
    heading_Label = customtkinter.CTkLabel(main_frame, text="📚 Delete Book Information", font=("Georgia", 22, "bold"), text_color="#010B13")
    heading_Label.place(relx=0.5, rely=0.055, anchor="center")

    # Section to enter the unique Book ID
    book_id_label = customtkinter.CTkLabel(main_frame, text="Enter Unique Book ID", font=label_font, text_color="black")
    book_id_label.place(relx=0.35, rely=0.1275, anchor="e", relwidth=0.2)
    
    book_id_entry = customtkinter.CTkEntry(main_frame, font=entry_font)
    book_id_entry.place(relx=0.4, rely=0.1275, anchor="w", relwidth=0.25)

    # Variables to hold book information fields (initialized empty until book is fetched)
    fields = {}
    
    # Function to fetch existing book data
    def fetch_book_data(book_id):
        try:
            connector = mysql.connector.connect(host="localhost", user="root", password="12345678", database="Library_Database")
            cursor = connector.cursor()
            sql = "SELECT * FROM BOOKS WHERE book_id = %s"
            cursor.execute(sql, (book_id,))
            book_data = cursor.fetchone()
            cursor.close()
            if book_data:
                #book_id_entry.configure(state="disable")
                populate_book_form(book_id,book_data)  # Call function to populate form with book data
            else:
                for widget in update_main_frame.winfo_children():
                    widget.destroy()
                update_main_frame.configure( border_width=0, corner_radius=0, fg_color=primary_color)
                messagebox.showerror("Error", "Book ID not found!")
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching book data: {e}")

    # Populate form with book data
    def populate_book_form(book_id,book_data):
        
        update_main_frame.configure( border_width=1, corner_radius=50, fg_color="white", border_color="white")

        print(book_data)
        
        # Create labels and entries for other fields and pre-populate them with fetched data
        fields.update({
            "Book_ID": customtkinter.CTkEntry(update_main_frame,textvariable=StringVar(value=book_id),  font=entry_font, state="disable"),
            "Title": customtkinter.CTkEntry(update_main_frame,textvariable=StringVar(value=book_data[0]),  font=entry_font,  state="disable"),
            "Author(s)": customtkinter.CTkEntry(update_main_frame, textvariable=StringVar(value=book_data[1]),font=entry_font,  state="disable"),
            "Publisher": customtkinter.CTkEntry(update_main_frame, textvariable=StringVar(value=book_data[2]), font=entry_font,  state="disable"),
            "Publication Date": customtkinter.CTkEntry(update_main_frame,textvariable=StringVar(value=book_data[3]), font=entry_font,  state="disable"),
            "Genre": customtkinter.CTkEntry(update_main_frame,textvariable=StringVar(value=book_data[4]), font=entry_font, state="disable"),
            "Language": customtkinter.CTkEntry(update_main_frame,textvariable=StringVar(value=book_data[5]), font=entry_font, state="disable"),
            "Number of Pages": customtkinter.CTkEntry(update_main_frame,textvariable=StringVar(value=book_data[6]), font=entry_font,  state="disable"),
            "Edition": customtkinter.CTkEntry(update_main_frame,textvariable=StringVar(value=book_data[7]), font=entry_font, state="disable"),
            "Number of Books": customtkinter.CTkEntry(update_main_frame,textvariable=StringVar(value=book_data[8]), font=entry_font,  state="disable"),
            "Price": customtkinter.CTkEntry(update_main_frame,textvariable=StringVar(value=book_data[9]), font=entry_font, state="disable"),
        })

        y = 0.075
        for label_text, entry in fields.items():
            label = customtkinter.CTkLabel(update_main_frame, text=label_text, font=label_font, text_color="#34495e")
            label.place(relx=0.35, rely=y, anchor="e", relwidth=0.25)
            entry.place(relx=0.4, rely=y, anchor="w", relwidth=0.25)
            y += 0.065

        # Label for the image
        image_label = customtkinter.CTkLabel(update_main_frame, text="Cover\nImage", fg_color=primary_color, compound="top", text_color="black")
        image_label.place(relx=0.7, rely=0.25, relwidth=0.25, relheight=0.4, anchor="w")

        cover_image=book_data[11]
        
        # Preload cover image if available
        
        if cover_image:
            try:
                img = Image.open(cover_image)
                img = img.resize((150, 150))
                img = ImageTk.PhotoImage(img)
                image_label.configure(image=img, fg_color="transparent")
                image_label.image = img
            except Exception as e:
                messagebox.showerror("Loading Image ...... ", e)


        # Save updated book function with confirmation pop-up
        def delete_book(book_id):
            if confirm_checkbox.get()=="1":
                try:
                    connector = mysql.connector.connect(host="localhost", user="root", password="12345678", database="Library_Database")
                    cursor = connector.cursor()
                    sql ="""
                            DELETE from BOOKS
                            WHERE title=%s AND author=%s AND publisher=%s AND Publication_Date=%s AND
                            genre=%s AND language=%s AND Number_of_Pages=%s AND
                            edition=%s AND Number_of_Books=%s AND price=%s AND
                            book_id=%s AND cover_image=%s
                        """
                    response=messagebox.askyesno("Delete Request Confirmation", "Warning: This action cannot be undone!\nDo you want to delete book information?")
                    if response:
                        cursor.execute(sql, book_data)
                        connector.commit()
                        cursor.close()

                        messagebox.showinfo("Book Information Deleted", "Book Deleted from Database Successfully!")
                        main_frame.destroy()
                            
                except Exception as e:
                    messagebox.showerror("Error", f"Error updating book: {e}")
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
        delete_button = customtkinter.CTkButton(update_main_frame, text="🗑 Delete", fg_color="RED", command=lambda : delete_book(book_id), hover_color="#C40234")
        delete_button.place(relx=0.3, rely=0.925, anchor="e", relwidth=0.15)

        cancel_button = customtkinter.CTkButton(update_main_frame, text="❌ Cancel", command=main_frame.destroy, hover_color="Green")
        cancel_button.place(relx=0.75, rely=0.925, anchor="w", relwidth=0.15)


    # Button to fetch the book data based on entered Book ID
    fetch_button = customtkinter.CTkButton(main_frame, text="🔍 Fetch Book", fg_color=button_bg, hover_color="#FF4500", command=lambda: fetch_book_data(book_id_entry.get()))
    fetch_button.place(relx=0.7275, rely=0.1275, anchor="w", relwidth=0.15)

    # Footer Section
    footer_label = customtkinter.CTkLabel(main_frame, text="Library Management System v1.0 | Need Help? Contact support@library.com", 
                                      font=("Arial", 12), text_color="#010B13")
    footer_label.place(relx=0.5, rely=0.95, anchor="center")

if __name__ == "__main__":
    delete_book_form(content_frame)
