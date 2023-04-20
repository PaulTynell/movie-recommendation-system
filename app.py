# File app.py
# Author: Heikki Jarvinen
# Description: main ui for app

import customtkinter
from movie_recommender import get_recommendation
from dict_manipulator import return_dict

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Creating a class for the app
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Initializing window
        self.title("Movie recommendation system")
        self.geometry(f"{1100}x{500}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Get trending", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.sidebar_frame, dynamic_resizing=False,
                                                        values=["movie", "tv"])
        self.optionmenu_1.grid(row=1, column=0, padx=20, pady=10)
        self.optionmenu_2 = customtkinter.CTkOptionMenu(self.sidebar_frame, dynamic_resizing=False,
                                                        values=["day", "week"])
        self.optionmenu_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Search", command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter a movie")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text="Search", text_color=("gray10", "#DCE4EE"), command=self.search_movies)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create a label for main entry
        self.entry_label = customtkinter.CTkLabel(self, text="Search a movie and get recommendations based on it!", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.entry_label.grid(row=2, column=1, padx=20, pady=(20, 10))

    # Change window appearance
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # Change scaling
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    # pressing sidebar button displays days/weeks trending tv/movie
    def sidebar_button_event(self):
        format = self.optionmenu_1.get()
        time = self.optionmenu_2.get()
        self.textbox.insert("0.0", f"This {time}s trending {format}:\n\n" + f"{return_dict(format, time)}\n\n")

    # pressing search button finds the movie and displays recommended movies
    def search_movies(self):
        movie_name = self.entry.get()
        recommendations = get_recommendation(movie_name)
        self.textbox.insert("0.0", f"Your movie recommendations based on {movie_name}:\n\n" + f"{recommendations}\n\n")


if __name__ == "__main__":
    app = App()
    app.mainloop()