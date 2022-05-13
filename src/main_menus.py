"""Main menus for navigation"""

from main import tk

class StartPage(tk.Frame):
    """Start page for program, offers sign in, quit buttons"""

    def __init__(self, parent, controller):
        """Initialise class values and create GUI elements"""

        # Initialise frame.
        tk.Frame.__init__(self, parent) # Start tk frame class.
        self.controller = controller

        # Create GUI elements.

        # Create label that shows the text ‘Start Page:’
        lbl_title = tk.Label(self, text='Start Page:')
        lbl_title.pack(pady=10)
        # Pack the label with vertical padding of 10.

        self.btn_start_login = tk.Button(self, text='Login', command=lambda: self.controller.show_frame('Login'))
        # Create a button that when pressed, shows the login menu.
        # The button has the text ‘Login’.
        self.btn_start_login.pack(pady=10, padx=25, expand=True, fill='both')
        # Pack the button, and make it expand depending on the windows
        # size, and available space. Give the button both horizontal
        # and vertical padding.

        self.btn_signup = tk.Button(self, text='Sign up', command=lambda: self.controller.show_frame('SignUp'))
        # Create a button that when pressed, shows the Sign Up menu. 
        # The button has the text ‘Sign Up’.

        self.btn_signup.pack(pady=10, padx=25, expand=True, fill='both')
        # Pack the button


class StudentMenu(tk.Frame):
    """GUI menu for student access, provides fewer options than teacher"""

    def __init__(self, parent, controller):
        """Initialise class values and create initial GUI elements"""

        # Initialise frame .
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # GUI creation.

        # String var for student name, allows text to change with
        # .set() and text can be retrieved with .get().
        self.student_name = tk.StringVar(self, value='Student Name')

        # Label that uses the string variable above. If the string 
        # variable’s value changes, so will the labels text.
        lbl_student_title = tk.Label(self, textvariable=self.student_name)
        lbl_student_title.pack(pady=5)

        # Create a frame that contains other tkinter elements.
        frame_student_actions = tk.Frame(self)
        frame_student_actions.pack(pady=3)

        # Buttons to navigate through the program.

        # Button that shows the SignIn page when pressed. The button 
        # has the text ‘Sign into school’.
        btn_school_sign_in = tk.Button(frame_student_actions, text='Sign into school', command=lambda: self.controller.show_frame('SignIn'))
        btn_school_sign_in.grid(row=0, column=0, sticky='ew', pady=3, padx=3)

        # Button that shows the SignOut page when pressed. The button 
        # has the text ‘Sign out of school’.
        btn_school_sign_out = tk.Button(frame_student_actions, text='Sign out of school', command=lambda: self.controller.show_frame('SignOut'))
        btn_school_sign_out.grid(row=0, column=1, sticky='ew', pady=3, padx=3)

        # Button that shows the SignHistory page when clicked. The 
        # button has the text ‘View sign in / out history.
        btn_view_attendence = tk.Button(frame_student_actions, text='View sign in / out history', command=lambda: self.controller.show_frame('SignHistory'))
        btn_view_attendence.grid(row=1, column=0, sticky='ew', pady=3, padx=3, columnspan=2)

        btn_edit_user = tk.Button(frame_student_actions, text='Edit My Details', command=lambda: self.edit_user())
        btn_edit_user.grid(row=2, column=0, sticky='ew', pady=3, padx=3, columnspan=2)

        self.btn_user_logout = tk.Button(self, text='Logout of manager', command=lambda: self.controller.show_frame('LogoutMenu'))
        self.btn_user_logout.pack(pady=3)

    def edit_user(self):
        """Edit the own user's profile"""

        # When the edit user button is pressed, the edit user menu is  filled
        # with  the current user’s information though the fill_string_vars 
        # function. Also, tells the function that the menu was called from
        #  this menu
        self.controller.frames['EditUser'].fill_string_vars(self.user_info, self.__class__.__name__)
        self.controller.show_frame('EditUser')  # Show the EditUser frame.

    def user_configure(self, user_info):
        """Changes the StudentMenu name field to the currently logged in
        student's name"""

        self.user_info = user_info
        # Set the label, ‘lbl_student_title’ to the logged in users current name. 
        self.student_name.set('ID: {}\nName: {} {}'.format(user_info['id'], user_info['first_name'],
                                             user_info['second_name']).title())


class TeacherMenu(StudentMenu):
    """GUI Menu for teacher, has elevated permissions over student menu"""

    def __init__(self, parent, controller):
        """Initialise class values and create initial GUI elements"""

        # Inherit student menu
        self.controller = controller
        # Initialise the inherited student menu, taking its GUI 
        # elements.
        StudentMenu.__init__(self, parent, controller)

        # GUI creation

        self.btn_user_logout.destroy()  # Delete button to replace at later line

        frame_teacher_actions = tk.Frame(self)
        frame_teacher_actions.pack()

        # Buttons to navigate through the menu.

        # Button that opens the UserSearch menu when clicked. The 
        # button has the text, ‘User Search’.
        btn_user_search = tk.Button(frame_teacher_actions, text='User Search', command=lambda: self.controller.show_frame('UserSearch'))
        btn_user_search.grid(row=2, column=0, sticky='ew', pady=3, padx=3)

        btn_edit_student = tk.Button(frame_teacher_actions, text='Edit user info', command=lambda: self.controller.show_frame('EditSearchUsers'))
        btn_edit_student.grid(row=2, column=1, sticky='ew', pady=3, padx=3)

        btn_sign_search = tk.Button(frame_teacher_actions, text='Sign in / out search', command=lambda: self.controller.show_frame('SignSearch'))
        btn_sign_search.grid(row=3, column=0, sticky='ew', pady=3, padx=3)

        btn_edit_signs = tk.Button(frame_teacher_actions, text='Edit sign ins/outs', command=lambda: self.controller.show_frame('EditSignSearch'))
        btn_edit_signs.grid(row=3, column=1, sticky='ew', pady=3, padx=3)

        self.btn_user_logout = tk.Button(self, text='Logout of program', command=lambda: self.controller.show_frame('LogoutMenu'))
        self.btn_user_logout.pack(pady=3)
