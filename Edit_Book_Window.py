import customtkinter
from tkinter import StringVar
import tkinter.messagebox as messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import mysql.connector
import useable_module

def edit_book_form(content_frame):

    # Colors and Fonts
    primary_color = "#E6E6FA"  
    button_bg = "#FF8C00"  # Dark Orange
    frame_bg = "#F0F0F0"  # Light Gray
    label_font = ("Montserrat", 13, "bold")
    entry_font = ("Montserrat", 13)

    # Create main frame with border, shadow, and 3D effect
    main_frame = customtkinter.CTkFrame(content_frame, fg_color="#E6E6FA", corner_radius=20)
    main_frame.place(relx=0.5,rely=0.5,relwidth=1, relheight=1, anchor="center")

    # Create main frame with border, shadow, and 3D effect
    update_main_frame = customtkinter.CTkFrame(main_frame, fg_color="#E6E6FA", corner_radius=20)
    update_main_frame.place(relx=0.5, rely=0.55, relwidth=0.9,relheight=0.725,anchor="center")#relx=0.5,rely=0.5,relwidth=0.98, relheight=0.98, anchor="center"
    

    # Add heading label with an icon
    heading_Label = customtkinter.CTkLabel(main_frame, text="📚 Update Book Information", font=("Georgia", 22, "bold"), text_color="#010B13")
    heading_Label.place(relx=0.5, rely=0.055, anchor="center")

    # Section to enter the unique Book ID
    book_id_label = customtkinter.CTkLabel(main_frame, text="Enter Unique Book ID", font=label_font, text_color="#34495e")
    book_id_label.place(relx=0.35, rely=0.125, anchor="e", relwidth=0.2)
    
    book_id_entry = customtkinter.CTkEntry(main_frame, font=entry_font)
    book_id_entry.place(relx=0.4, rely=0.125, anchor="w", relwidth=0.25)

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
        (title, author, publisher, pub_date, genre, language, pages, edition, quantity, price, book_id, cover_image) = book_data

        # Create Dropdown Menus (CTkOptionMenu) for Genre, Language, Edition fields
        genre_options = ["Fiction", "Non-fiction", "Science Fiction", "Fantasy",
                     "Biography/Autobiography","Science & technology","Religion & spirituality",
                     "Philosophy","Humanities & social sciences","History"]
        language_options = ["Hindi","English", "Spanish", "French", "German", "Chinese"]
        edition_options = ["First", "Second", "Third", "Fourth", "Fifth", "Other"]

        # Create labels and entries for other fields and pre-populate them with fetched data
        fields.update({
            "Title": customtkinter.CTkEntry(update_main_frame, font=entry_font, placeholder_text="Title"),
            "Author(s)": customtkinter.CTkEntry(update_main_frame, font=entry_font, placeholder_text="Author(s)"),
            "Publisher": customtkinter.CTkEntry(update_main_frame, font=entry_font, placeholder_text="Publisher"),
            "Publication Date": customtkinter.CTkEntry(update_main_frame, font=entry_font, placeholder_text="YYYY-MM-DD"),
            "Genre": customtkinter.CTkOptionMenu(update_main_frame, values=genre_options, font=entry_font),
            "Language": customtkinter.CTkOptionMenu(update_main_frame, values=language_options, font=entry_font),
            "Number of Pages": customtkinter.CTkEntry(update_main_frame, font=entry_font, placeholder_text="Number of Pages"),
            "Edition": customtkinter.CTkOptionMenu(update_main_frame, values=edition_options, font=entry_font),
            "Number of Books": customtkinter.CTkEntry(update_main_frame, font=entry_font, placeholder_text="Quantity"),
            "Price": customtkinter.CTkEntry(update_main_frame, font=entry_font, placeholder_text="Price"),
        })

        # Pre-fill form fields with fetched data
        fields["Title"].insert(0, title)
        fields["Author(s)"].insert(0, author)
        fields["Publisher"].insert(0, publisher)
        fields["Publication Date"].insert(0, pub_date)
        fields["Genre"].set(genre)
        fields["Language"].set(language)
        fields["Number of Pages"].insert(0, pages)
        fields["Edition"].set(edition)
        fields["Number of Books"].insert(0, quantity)
        fields["Price"].insert(0, price)

        y = 0.1
        for label_text, entry in fields.items():
            label = customtkinter.CTkLabel(update_main_frame, text=label_text, font=label_font, text_color="#34495e")
            label.place(relx=0.35, rely=y, anchor="e", relwidth=0.25)
            entry.place(relx=0.4, rely=y, anchor="w", relwidth=0.25)
            y += 0.075

        # Label for the image
        image_label = customtkinter.CTkLabel(update_main_frame, text="Cover Image", fg_color=primary_color, compound="top", text_color="black")
        image_label.place(relx=0.7, rely=0.3, relwidth=0.25, relheight=0.4, anchor="w")

        # Preload cover image if available
        if cover_image:
            img = Image.open(cover_image)
            img = img.resize((190, 220))
            img = ImageTk.PhotoImage(img)
            image_label.configure(image=img, text="", fg_color="transparent")
            image_label.image = img


        # Image upload section
        def upload_cover_image():
            file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
            if file_path:
                img = Image.open(file_path)
                img = img.resize((190, 220))
                img = ImageTk.PhotoImage(img)
                image_label.configure(image=img, text="", fg_color="transparent")
                image_label.image = img
                return file_path
            return cover_image  # Return existing cover image path if no new image is selected


        # Save updated book function with confirmation pop-up
        def save_book(book_id):
            updated_book_data = {field: entry.get() for field, entry in fields.items()}
            updated_cover_image = upload_cover_image()
            if useable_module.is_valid_string(updated_book_data["Title"]):
                if useable_module.is_valid_string(updated_book_data["Author(s)"]):
                    if useable_module.is_valid_string(updated_book_data["Publisher"]):
                        if useable_module.verify_date(updated_book_data["Publication Date"]):
                            if updated_book_data["Genre"]:
                                if updated_book_data["Language"]:
                                    if updated_book_data["Number of Pages"].isdigit():
                                        if updated_book_data["Edition"]:
                                            if updated_book_data["Number of Books"].isdigit():
                                                if updated_book_data["Price"].isdigit():
                                                    try:
                                                        connector = mysql.connector.connect(host="localhost", user="root", password="12345678", database="Library_Database")
                                                        cursor = connector.cursor()
                                                        sql = """
                                                                UPDATE BOOKS
                                                                SET title=%s, author=%s, publisher=%s, Publication_Date=%s,
                                                                genre=%s, language=%s, Number_of_Pages=%s,
                                                                edition=%s, Number_of_Books=%s, price=%s,
                                                                cover_image=%s
                                                                WHERE book_id=%s
                                                            """
                                                        response=messagebox.askyesno("Book Registration", "Do you want to update book information?")
                                                        if response:
                                                            cursor.execute(sql, (*updated_book_data.values(), updated_cover_image, book_id))
                                                            connector.commit()
                                                            cursor.close()

                                                            messagebox.showinfo("Book Updated", f"Book '{updated_book_data['Title']}' updated successfully!")
                                                            main_frame.destroy()
                                                            
                                                    except Exception as e:
                                                        messagebox.showerror("Error", f"Error updating book: {e}")
                                                else:
                                                    messagebox.showerror("Error","Enter Valid Price in Numbers")
                                            else:
                                                messagebox.showerror("Error","Enter Quantity of Books in Number")
                                        else:
                                            messagebox.showerror("Error","Select Edition from Option Menu")
                                    else:
                                        messagebox.showerror("Error","Enter Quantity of Pages in Number")
                                else:
                                    messagebox.showerror("Error","Select Language from Option Menu")
                            else:
                                messagebox.showerror("Error","Select Genre from Option Menu")
                        else:
                            messagebox.showerror("Error","Enter Publication Date in YYYY-MM-DD Format")
                    else:
                        messagebox.showerror("Error","Enter Valid Publisher in Alphabets")
                else:
                    messagebox.showerror("Error","Enter Valid Author(s) in Alphabets")
            else:
                messagebox.showerror("Error","Enter Valid Title in Alphabets")

            

        # Add hover effects on buttons
        save_button = customtkinter.CTkButton(update_main_frame, text="💾 Update", fg_color=button_bg, command=lambda : save_book(book_id), hover_color="#FF4500")
        save_button.place(relx=0.3, rely=0.875, anchor="e", relwidth=0.15)

        cancel_button = customtkinter.CTkButton(update_main_frame, text="❌ Cancel", command=main_frame.destroy, hover_color="#FF4500")
        cancel_button.place(relx=0.75, rely=0.875, anchor="w", relwidth=0.15)

        messagebox.showinfo("Information", "You can change and save information.")

    # Button to fetch the book data based on entered Book ID
    fetch_button = customtkinter.CTkButton(main_frame, text="🔍 Fetch Book", fg_color=button_bg, hover_color="#FF4500", command=lambda: fetch_book_data(book_id_entry.get()))
    fetch_button.place(relx=0.7275, rely=0.125, anchor="w", relwidth=0.15)

    # Footer Section
    footer_label = customtkinter.CTkLabel(main_frame, text="Library Management System v1.0 | Need Help? Contact support@library.com", 
                                      font=("Arial", 12), text_color="#010B13")
    footer_label.place(relx=0.5, rely=0.95, anchor="center")


if __name__ == "__main__":
    edit_book_form(content_frame)
