"""Init, GUI construction"""

import tkinter as tk
from tkinter import messagebox
from sign_editing import *
from user_editing import *
from signing_in_out import *
from account_processes import *
from main_menus import *


class Gui(tk.Tk):
    """GUI controller for program, shows class frames, inits and manages
    frame classes """

    def __init__(self, *args, **kwargs):
        """Creates gui, base container frame, inits class frames"""

        # Initialise tkinter.
        tk.Tk.__init__(self, *args, **kwargs)

        self.session_id, self.user_info = None, None
        self.container = tk.Frame(self) # Create a frame to fit the classes into.
        self.container.pack(side='top', fill='both', expand=True)
        # Allows frame to expand to classes size.
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # Dictionary to place classes into.

        # Iterate through a list of classes, initialising them
        for F in (StartPage, Login, SignUp, StudentMenu, TeacherMenu,
                  LogoutMenu, UserSearch, EditSearchUsers, SignSearch,
                  EditUser, SignIn, SignOut, SignHistory, EditSignSearch, 
                  EditSignIn, EditSignOut):

            # Initialise frame and assign reference 'frame' to frame.
            frame = F(parent=self.container, controller=self)
            self.frames[F.__name__] = frame  # F.__name__ gets name of class,
            # it then assigns the class reference to dictionary key.
            frame.grid(row=0, column=0, sticky='nsew')  # Grid and let frames expand.

        # Page setup
        self.title('6th Form Sign System')
        self.show_frame('StartPage')

    def show_frame(self, page_name):
        """Raise specified frame class: page_name"""
        frame = self.frames[page_name]
        frame.tkraise()  # Raises frame of argument.

    def set_session_id(self, session_id, user_info):
        """"Assign id to session, used for when signing in and out"""

        self.session_id, self.user_info  = session_id, user_info
        if self.user_info['access_level'] == 'student':
            self.default_menu = 'StudentMenu'
        else:
            self.default_menu = 'TeacherMenu'

    def reset_pages(self):
        """Resets all frames, making their fields blank"""

        self.session_id, self.user_info, self.default_menu = None, None, None
        self.frames = {}

        for F in (StartPage, Login, SignUp, StudentMenu, TeacherMenu,
                  LogoutMenu, UserSearch, EditSearchUsers, SignSearch,
                  EditUser, SignIn, SignOut, SignHistory):

            # Initialise frame and assign reference 'frame' to frame
            frame = F(parent=self.container, controller=self)
            self.frames[F.__name__] = frame  # F.__name__ gets name of class,
            # it then assigns the class reference to dictionary key
            frame.grid(row=0, column=0, sticky='nsew')  # Grid and let expand

        self.show_frame('StartPage')


if __name__ == '__main__':

    app = Gui()
    app.minsize(800, 400)
    app.mainloop()
