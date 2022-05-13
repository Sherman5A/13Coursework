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

        # Set the session id and user info to None. Also make them 
        # instance variables.
        self.session_id, self.user_info = None, None

        self.container = tk.Frame(self) # Create a frame to fit the classes into.
        self.container.pack(side='top', fill='both', expand=True)
        # Allows frame to expand to classes size.
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # Dictionary to place classes into.

        # Iterate through a list all of the GUI pages, initialising them
        for F in (StartPage, Login, SignUp, StudentMenu, TeacherMenu,
                  LogoutMenu, UserSearch, EditSearchUsers, SignSearch,
                  EditUser, SignIn, SignOut, SignHistory, EditSignSearch, 
                  EditSignIn, EditSignOut):

            # Initialise frame and assign reference 'frame' to frame.
            frame = F(parent=self.container, controller=self)
            # F.__name__ gets name of class, it then assigns 
            # the created instances's reference to a 
            # dictionary key with the name of the class.
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky='nsew')  # Grid and let frames expand.
            
        # Page setup, set the title bar to the following string.
        self.title('6th Form Sign System')
        # Show the 6th form start page.
        self.show_frame('StartPage')

    def show_frame(self, page_name):
        """Raise specified frame class: page_name"""

        # Get the frame defined in the argument and assign it’s  reference to 
        # variable ‘frame’.
        frame = self.frames[page_name]
        # Raise the frame over others, so it appears on the user’s screen.
        frame.tkraise()  # Raises frame in argument.

    def set_session_id(self, session_id, user_info):
        """"Assign id to session, used for when signing in and out"""

        # Set the session id and user info from None to the values 
        # defined in the arguments.
        self.session_id, self.user_info  = session_id, user_info
        
        # If the newly logged in session has an access level student 
        # or teacher, a respective application-wide student or teacher 
        # flag is set. This limits what the user can and can’t do.
        if self.user_info['access_level'] == 'student':
            self.default_menu = 'StudentMenu'
        else:
            self.default_menu = 'TeacherMenu'

    def reset_pages(self):
        """Resets all frames, making their fields blank"""

        # Reset all the variables to the ones defined in init.

        self.session_id, self.user_info, self.default_menu = None, None, None
        self.frames = {}

        for F in (StartPage, Login, SignUp, StudentMenu, TeacherMenu,
                  LogoutMenu, UserSearch, EditSearchUsers, SignSearch,
                  EditUser, SignIn, SignOut, SignHistory):

            # Initialise frame and assign reference 'frame' to frame
            frame = F(parent=self.container, controller=self)
            self.frames[F.__name__] = frame  
            # F.__name__ gets name of class, it then assigns 
            # the created instances's reference to a 
            # dictionary key with the name of the class.
            frame.grid(row=0, column=0, sticky='nsew')  # Grid and let expand.

        self.show_frame('StartPage')


# Do not run any of the code here unless the file is directly run
# If the Python file is ran as a module, then __name__ is not set to main
# and the code is not run.
if __name__ == '__main__':
    # Create an instance of the above class
    app = Gui()
    app.minsize(800, 400) # Define a minimum size for the GUI
    app.mainloop()
