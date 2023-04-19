# File tktest
# Author: Heikki Jarvinen, Paul Tynell
# Description: second try at making tkinter ui


import tkinter
import customtkinter
from dict_manipulator import return_dict
from recommend_testing import get_recommendation

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#Setup
root = customtkinter.CTk()
root.title("Movie recommendations")

#Size
root.geometry("800x600")

#Widgets
def trendingButton():
    clickLabel = customtkinter.CTkLabel(master=root, text="These are your movie recommendations:", font=("Arial", 14))
    clickLabel.pack(pady=10)
    output = return_dict()
    text = tkinter.Text(master=root, height=13, width=61, font=("Arial", 10))
    text.insert(tkinter.END, str(output))
    text.pack(pady=10)
    scrollbar = tkinter.Scrollbar(master=root, command=text.yview)
    text.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

def recommendButton():
    clickLabel = customtkinter.CTkLabel(master=root, text="These are your movie recommendations:", font=("Arial", 14))
    clickLabel.pack(pady=10)
    output = get_recommendation("Toy Story 1995")
    text = tkinter.Text(master=root, height=13, width=61, font=("Arial", 10))
    text.insert(tkinter.END, str(output))
    text.pack(pady=10)
    scrollbar = tkinter.Scrollbar(master=root, command=text.yview)
    text.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

def get_user_input():
    input_window = customtkinter.CTkToplevel(root)
    input_window.title("Get recommendations")
    input_label = customtkinter.CTkLabel(input_window, text="Enter a movie:")
    input_label.pack(side=customtkinter.TOP)
    input_box = customtkinter.CTkEntry(input_window)
    input_box.pack(side=customtkinter.TOP)
    def search_button():
        output_text.delete('1.0', customtkinter.END)
        result = get_recommendation(input_box.get())
        output_text.insert(customtkinter.END, result)
        input_window.destroy()
    button = customtkinter.CTkButton(input_window, text="Search", command=search_button)
    button.pack(side=customtkinter.TOP)


label1 = customtkinter.CTkLabel(master=root, text="Movie recommendations", font=("Arial", 15))
button1 = customtkinter.CTkButton(master=root, text="Get trending movies", command=trendingButton, font=("Arial", 14))
button2 = customtkinter.CTkButton(master=root, text="Get my recommendation!", command=get_user_input, font=("Arial", 14))
quit_button = customtkinter.CTkButton(master=root, text="Exit", font=("Arial", 10), command=root.quit)

output_text = customtkinter.CTkTextbox(root, width=700)
output_text.pack(side=customtkinter.BOTTOM)

#Inserts
label1.pack(pady=20)
button1.pack(pady=10)
button2.pack(pady=10)
quit_button.pack(pady=20)

root.mainloop()


