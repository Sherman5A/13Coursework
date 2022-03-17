"""Main menus for navigation"""

from cgitb import text
from main import tk

class StartPage(tk.Frame):
    """Start page for program, offers sign in, quit buttons"""

    def __init__(self, parent, controller):
        """Initialise class values and create GUI elements"""
        # initialise frame
        tk.Frame.__init__(self, parent) # start tk frame class
        self.controller = controller

        # create GUI elements
        lbl_title = tk.Label(self, text='Start Page:')
        lbl_title.pack(pady=10)

        self.btn_start_login = tk.Button(self, text='Login', command=lambda: self.controller.show_frame('Login'))
        self.btn_start_login.pack(pady=10, padx=25, expand=True, fill='both')

        self.btn_signup = tk.Button(self, text='Sign up', command=lambda: self.controller.show_frame('SignUp'))
        self.btn_signup.pack(pady=10, padx=25, expand=True, fill='both')


class StudentMenu(tk.Frame):
    """GUI menu for student access, provides fewer options than teacher"""

    def __init__(self, parent, controller):
        """Initialise class values and create initial GUI elements"""

        # Initialise frame 
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # GUI creation
        # String var for student name, allows text to change.
        self.student_name = tk.StringVar(self, value='Student Name')

        lbl_student_title = tk.Label(self, textvariable=self.student_name)
        lbl_student_title.pack(pady=5)

        frame_student_actions = tk.Frame(self)
        frame_student_actions.pack(pady=3)

        btn_school_sign_in = tk.Button(frame_student_actions, text='Sign into school', command=lambda: self.controller.show_frame('SignIn'))
        btn_school_sign_in.grid(row=0, column=0, sticky='ew', pady=3, padx=3)

        btn_school_sign_out = tk.Button(frame_student_actions, text='Sign out of school', command=lambda: self.controller.show_frame('SignOut'))
        btn_school_sign_out.grid(row=0, column=1, sticky='ew', pady=3, padx=3)

        btn_view_attendence = tk.Button(frame_student_actions, text='View sign in / out history', command=lambda: self.controller.show_frame('SignHistory'))
        btn_view_attendence.grid(row=1, column=0, sticky='ew', pady=3, padx=3, columnspan=2)

        btn_edit_user = tk.Button(frame_student_actions, text='Edit My Details', command=lambda: self.edit_user())
        btn_edit_user.grid(row=2, column=0, sticky='ew', pady=3, padx=3, columnspan=2)

        self.btn_user_logout = tk.Button(self, text='Logout of manager', command=lambda: self.controller.show_frame('LogoutMenu'))
        self.btn_user_logout.pack(pady=3)

    def edit_user(self):
        self.controller.frames['EditUser'].fill_string_vars(self.user_info, self.__class__.__name__)
        self.controller.show_frame('EditUser')

    def user_configure(self, user_info):
        """Changes the StudentMenu name field to the currently logged in 
        student's name"""
        self.user_info = user_info
        # Set the label to display the user's name and ID
        self.student_name.set('ID: {}\nName: {} {}'.format(user_info['id'], user_info['first_name'],
                                             user_info['second_name']).title())


class TeacherMenu(StudentMenu):
    """GUI Menu for teacher, has elevated permissions over student menu"""

    def __init__(self, parent, controller):
        """Initialise class values and create initial GUI elements"""

        # Inherit student menu
        self.controller = controller
        StudentMenu.__init__(self, parent, controller)

        # GUI creation
        
        self.btn_user_logout.destroy()  # Delete button to replace at later date

        frame_teacher_actions = tk.Frame(self)
        frame_teacher_actions.pack()

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
