"""Init, GUI construction"""


import tkinter as tk
from datetime import datetime
from tkinter import messagebox
from tkinter import ttk

import logic


class Gui(tk.Tk):
    """GUI controller for program, shows class frames, inits and manages
    frame classes """

    def __init__(self, *args, **kwargs):
        """Creates gui, base container frame, inits class frames"""

        # Initialise tkinter
        tk.Tk.__init__(self, *args, **kwargs)

        self.session_id = None
        container = tk.Frame(self) # Create a frame to fit the classes into
        container.pack(side='top', fill='both', expand=True)
        # Allow frame to expand to classes
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # Dictionary to place classes into

        # Iterate through a list of classes, initialising them
        for F in (StartPage, Login, SignUp, StudentMenu, TeacherMenu,
                  LogoutMenu, UserSearch, EditSearchUsers, SignSearch,
                  EditUser, SignIn, SignOut, SignHistory):

            # Initialise frame and assign reference 'frame' to frame
            frame = F(parent=container, controller=self)
            self.frames[F.__name__] = frame  # F.__name__ gets name of class,
            # it then assigns the class reference to dictionary key
            frame.grid(row=0, column=0, sticky='nsew')  # Grid and let expand

        # Page setup
        self.title("6th Form Sign System")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """Raise specified frame class: page_name"""

        frame = self.frames[page_name]
        frame.tkraise()  # raises frame of argument

    def set_session_id(self, session_id):
        """"Assign id to session, used for when signing in and out"""

        self.session_id = session_id


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

        self.btn_start_login = tk.Button(self, text='Login Page', command=lambda: self.controller.show_frame('Login'))
        self.btn_start_login.pack(pady=3)

        self.btn_signup = tk.Button(self, text='Sign up', command=lambda: self.controller.show_frame('SignUp'))
        self.btn_signup.pack(pady=3)

        # temp for debugging

        btn_student_menu = tk.Button(self, text='Student Menu', command=lambda: self.controller.show_frame('StudentMenu'))
        btn_student_menu.pack(pady=3)

        btn_teacher_menu = tk.Button(self, text='Teacher Menu', command=lambda: self.controller.show_frame('TeacherMenu'))
        btn_teacher_menu.pack(pady=3)

        btn_logout_menu = tk.Button(self, text='Logout', command=lambda: self.controller.show_frame('LogoutMenu'))
        btn_logout_menu.pack(pady=3)

        btn_user_search_menu = tk.Button(self, text='User Search', command=lambda: self.controller.show_frame('UserSearch'))
        btn_user_search_menu.pack(pady=3)

        btn_sign_search_menu = tk.Button(self, text='Sign Search', command=lambda: self.controller.show_frame('SignSearch'))
        btn_sign_search_menu.pack(pady=3)

        btn_sign_history = tk.Button(self, text='Sign History', command=lambda: self.controller.show_frame('SignHistory'))
        btn_sign_history.pack(pady=3)

        btn_edit_search = tk.Button(self, text='Edit Search', command=lambda:self.controller.show_frame('EditSearchUsers'))
        btn_edit_search.pack(pady=3)


class SignUp(tk.Frame):
    """Page for students to sign up to login system"""

    def __init__(self, parent, controller):
        """Initialise class values and create GUI elements"""

        # Initialise frame
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # GUI creation
        lbl_signup_title = tk.Label(self, text='Sign up')
        lbl_signup_title.pack(pady=10)

        frame_user_input = tk.Frame(self)
        frame_user_input.pack()

        lbl_first_name = tk.Label(frame_user_input, text='First Name:')
        lbl_first_name.grid(row=0, column=0, pady=3)

        self.entries = []  # Entries, StringVars stored in list for easier .get()

        self.ent_first_name = tk.Entry(frame_user_input)
        self.ent_first_name.grid(row=0, column=1, pady=3)
        self.entries.append(self.ent_first_name)

        lbl_second_name = tk.Label(frame_user_input, text='Last name:')
        lbl_second_name.grid(row=1, column=0, pady=3)

        self.ent_second_name = tk.Entry(frame_user_input)
        self.ent_second_name.grid(row=1, column=1, pady=3)
        self.entries.append(self.ent_second_name)

        lbl_year_group = tk.Label(frame_user_input, text='Year group:')
        lbl_year_group.grid(row=2, column=0)

        year_groups = ['12', '13']
        self.year_value = tk.StringVar(frame_user_input, value='')
        self.entries.append(self.year_value)

        self.menu_year_group = tk.OptionMenu(frame_user_input, self.year_value, *year_groups)
        self.menu_year_group.grid(row=2, column=1, sticky='ew', pady=3)
        self.menu_year_group.config(width=16)

        lbl_form_group = tk.Label(frame_user_input, text='Form group:')
        lbl_form_group.grid(row=3, column=0)

        form_list = ['A', 'B', 'C', 'D', 'E', 'D', 'F']
        self.form_value = tk.StringVar(frame_user_input, value='')
        self.entries.append(self.form_value)

        self.menu_form_group = tk.OptionMenu(frame_user_input, self.form_value, *form_list)
        self.menu_form_group.grid(row=3, column=1, sticky='ew', pady=3)
        self.menu_form_group.config(width=16)

        lbl_username = tk.Label(frame_user_input, text='Username:')
        lbl_username.grid(row=4, column=0, pady=3)

        self.ent_username = tk.Entry(frame_user_input)
        self.ent_username.grid(row=4, column=1, pady=3)
        self.entries.append(self.ent_username)

        # <3 <3

        lbl_password = tk.Label(frame_user_input, text='Password:')
        lbl_password.grid(row=5, column=0, pady=3)

        self.ent_password = tk.Entry(frame_user_input, show='*')
        self.ent_password.grid(row=5, column=1, pady=3)
        self.entries.append(self.ent_password)

        lbl_password_repeat = tk.Label(frame_user_input, text='Repeat Password:')
        lbl_password_repeat.grid(row=6, column=0, pady=3)

        self.ent_password_repeat = tk.Entry(frame_user_input, show='*')
        self.ent_password_repeat.grid(row=6, column=1, pady=3)
        self.entries.append(self.ent_password_repeat)

        btn_confirm = tk.Button(self, text='Confirm sign up', command=lambda: self.create_account())
        btn_confirm.pack(pady=5)

        btn_return_start = tk.Button(self, text= 'Return to start page', command=lambda: self.controller.show_frame('StartPage'))
        btn_return_start.pack(pady=3)

    def create_account(self):
        """Collects user inputs and creates user account"""

        account_variables = {}
        # Tuple to hold dict keys
        account_dict_keys = ('first_name', 'second_name', 'year_group',
                             'form_group', 'username', 'password',
                             'password_repeat')

        for count, i in enumerate(self.entries):  # Get values and place in dictionary.
            if count <= 3:
                account_variables[account_dict_keys[count]] = i.get().lower()
            else:
                account_variables[account_dict_keys[count]] = i.get()

        account_variables['access_level'] = 'student'

        create_user_result = logic.create_user(account_variables)
        # Show error / success message
        if create_user_result:
            messagebox.showinfo('Success', 'User was created')
        else:
            messagebox.showerror('Failure', 'Field: {} \n{}'.format(create_user_result[1], create_user_result[2]))


class Login(tk.Frame):
    """Page to log in to system"""

    def __init__(self, parent, controller):
        """Initialise class values and create GUI elements"""

        # Initialise frame
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create GUI elements
        lbl_page_title = tk.Label(self, text='Login')
        lbl_page_title.pack()
        self.input_frame = tk.Frame(self)
        self.input_frame.pack()

        lbl_username = tk.Label(self.input_frame, text='Username:')
        lbl_username.grid(column=0, row=0, pady=3)

        self.ent_username = tk.Entry(self.input_frame)
        self.ent_username.grid(column=1, row=0, pady=3)

        lbl_password = tk.Label(self.input_frame, text='Password:')
        lbl_password.grid(column=0, row=1, pady=3)

        self.ent_password = tk.Entry(self.input_frame, show='*')
        self.ent_password.grid(column=1, row=1, pady=3)
        btn_login = tk.Button(self, text='Login', command=lambda: self.login_check())
        btn_login.pack(pady=3)

        btn_return_start_page = tk.Button(self, text='Return to start page', command=lambda: self.controller.show_frame('StartPage'))
        btn_return_start_page.pack(pady=3)

    def login_check(self):
        """Checks username and password"""

        input_username = self.ent_username.get()
        input_password = self.ent_password.get()
        login_result = logic.login(input_username, input_password)
        print(login_result)
        if not login_result:
            messagebox.showerror('Failure', 'Incorrect username or password')
        else:
            account_info = {}
            account_dict_keys = ('id', 'access_level', 'first_name',
                                 'second_name', 'year_group',
                                 'form_group', 'username', 'password')
            
            for count, i in enumerate(login_result[1][0]):
                account_info[account_dict_keys[count]] = i

            print(account_info)
            self.controller.set_session_id(account_info['id'])
            print(self.controller.session_id)

            if account_info['access_level'] == 'student':
                self.controller.frames['StudentMenu'].user_configure(account_info)
                self.controller.show_frame('StudentMenu')
            else:
                self.controller.frames['TeacherMenu'].user_configure(account_info)
                self.controller.show_frame('TeacherMenu')            


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

        # May add function: btn_view_permissions = tk.Button(
        # frame_student_actions, text='View user permissions', command='')

        self.btn_user_logout = tk.Button(self, text='Logout of program', command=lambda: self.logout())
        self.btn_user_logout.pack(pady=3)

    def user_configure(self, user_info):
        """Configures the StudentMenu to the logged in student"""
        self.student_name.set('{} {}'.format(user_info['first_name'], 
                                             user_info['second_name']).title())

    def logout(self):
        """Logs out of sql database"""

        class_name = type(self).__name__
        self.controller.frames['LogoutMenu'].set_calling_class(class_name)
        self.controller.show_frame('LogoutMenu')


class TeacherMenu(StudentMenu):
    """GUI Menu for teacher, has elevated permissions over student menu"""

    def __init__(self, parent, controller):
        """Initialise class values and create initial GUI elements"""

        self.controller = controller
        StudentMenu.__init__(self, parent, controller)

        # GUI creation

        self.btn_user_logout.destroy()

        frame_teacher_actions = tk.Frame(self)
        frame_teacher_actions.pack()

        btn_manual_sign = tk.Button(frame_teacher_actions, text='Manual sign students', command='')
        btn_manual_sign.grid(row=2, column=0, sticky='ew', padx=3)

        btn_search_attendance = tk.Button(frame_teacher_actions, text='View student history', command='')
        btn_search_attendance.grid(row=2, column=1, sticky='ew', pady=3, padx=3)

        btn_edit_student = tk.Button(frame_teacher_actions, text='Edit student info', command='')
        btn_edit_student.grid(row=3, column=0, sticky='ew', pady=3, padx=3)

        btn_view_permissions = tk.Button(frame_teacher_actions, text='View user permissions', command='')
        btn_view_permissions.grid(row=3, column=1, sticky='ew', pady=3, padx=3)

        self.btn_user_logout = tk.Button(self, text='Logout of program', command=lambda: self.logout())
        self.btn_user_logout.pack(pady=3)


class LogoutMenu(tk.Frame):
    """Confirms whether user wants to log out"""

    def __init__(self, parent, controller):
        """Initialise class values and create GUI elements"""

        tk.Frame.__init__(self, parent)
        self.controller = controller

        # GUI creation

        lbl_logout_confirm_title = tk.Label(self, text='Are you sure you want to logout:')
        lbl_logout_confirm_title.pack(pady=(10,0))

        logout_btn_frame = tk.Frame(self)
        logout_btn_frame.pack(fill='both', expand=True, pady=10)

        tk.Grid.columnconfigure(logout_btn_frame, 0, weight=1)
        tk.Grid.columnconfigure(logout_btn_frame, 1, weight=1)
        tk.Grid.rowconfigure(logout_btn_frame, 0, weight=1)

        self.btn_logout_confim = tk.Button(logout_btn_frame, text='Logout', command=lambda: self.logout())
        self.btn_logout_confim.grid(row=0, column=0, sticky='nsew', padx=(25,5), pady=(6,5))

        self.btn_logout_cancel = tk.Button(logout_btn_frame, text='Cancel', command=lambda: self.controller.show_frame(self.caller))
        self.btn_logout_cancel.grid(row=0, column=1, sticky='nsew', padx=(5,25), pady=(6,5))

    def set_calling_class(self, caller):
        self.caller = caller

    def logout(self):
        """Logs out of sql database"""

        # Log out of SQL.
        self.controller.show_frame('StartPage')


class UserSearch(tk.Frame):
    """Search for students by name, id, username, year group, and form"""

    def __init__(self, parent, controller):
        """Initialise class values and create GUI elements"""

        tk.Frame.__init__(self, parent)
        self.controller = controller

        # GUI creation

        self.search_config_frame = tk.Frame(self)
        self.search_config_frame.pack(side='left', anchor='nw', padx=10)

        title_frame = tk.Frame(self.search_config_frame, relief='groove', borderwidth=2)
        title_frame.pack(fill='both', anchor='nw', pady=(3, 15))

        lbl_search_title = tk.Label(title_frame, text='User Search')
        lbl_search_title.pack()

        self.btn_change_sign_search = tk.Button(title_frame, text='Go to sign search', command=lambda: self.controller.show_frame('SignSearch'))
        self.btn_change_sign_search.pack(pady=3)

        search_term_frame = tk.Frame(self.search_config_frame, relief='groove', borderwidth=2)
        search_term_frame.pack(fill='both', anchor='nw')

        lbl_search_info = tk.Label(search_term_frame, text="Leave entries you don't want to search empty")
        lbl_search_info.grid(row=0, column=0, sticky='nsew', pady=(10,3), columnspan=2)

        self.entries = [] # List to store variables to .get() later.

        lbl_id_search = tk.Label(search_term_frame, text='Student ID:')
        lbl_id_search.grid(row=1, column=0, sticky='nsew', pady=3)

        self.ent_id_search = tk.Entry(search_term_frame)
        self.ent_id_search.grid(row=1, column=1, sticky='nsew', pady=3)
        self.entries.append(self.ent_id_search)

        lbl_fname_search = tk.Label(search_term_frame, text='First name:')
        lbl_fname_search.grid(row=2, column=0, sticky='nsew', pady=3)

        self.ent_fname_search = tk.Entry(search_term_frame)
        self.ent_fname_search.grid(row=2, column=1, sticky='nsew', pady=3)
        self.entries.append(self.ent_fname_search)

        lbl_sec_name_search = tk.Label(search_term_frame, text='Second name:')
        lbl_sec_name_search.grid(row=3, column=0, sticky='nsew', pady=3)

        self.ent_sec_name_search = tk.Entry(search_term_frame)
        self.ent_sec_name_search.grid(row=3, column=1, sticky='nsew', pady=3)
        self.entries.append(self.ent_sec_name_search)

        lbl_year_search = tk.Label(search_term_frame, text='Year group:')
        lbl_year_search.grid(row=4, column=0, sticky='nsew', pady=3)

        self.year_value = tk.StringVar(search_term_frame, value='')
        self.entries.append(self.year_value)
        year_list = ['','12', '13']

        self.menu_year_search = tk.OptionMenu(search_term_frame, self.year_value, *year_list)
        self.menu_year_search.config(width='17')
        self.menu_year_search.grid(row=4, column=1, sticky='nsew', pady=3)

        lbl_form_search = tk.Label(search_term_frame, text='Form group:')
        lbl_form_search.grid(row=5, column=0, sticky='nsew', pady=3)

        self.form_value = tk.StringVar(search_term_frame, value='')
        self.entries.append(self.form_value)
        form_list = ['', 'A', 'B', 'C', 'D', 'E', 'D', 'F']

        self.menu_form_search = tk.OptionMenu(search_term_frame, self.form_value, *form_list)
        self.menu_form_search.config(width='17')
        self.menu_form_search.grid(row=5, column=1, sticky='ew', pady=3)

        lbl_username_search = tk.Label(search_term_frame, text='Username:')
        lbl_username_search.grid(row=6, column=0, sticky='nsew', pady=3)

        self.ent_username_search = tk.Entry(search_term_frame)
        self.ent_username_search.grid(row=6, column=1, sticky='nsew', pady=3)
        self.entries.append(self.ent_username_search)

        btn_begin_search = tk.Button(search_term_frame, text='Search', command=lambda: self.search_users())
        btn_begin_search.grid(row=7, column=0, columnspan=2, sticky='ew', pady=3)

        btn_clear_results = tk.Button(search_term_frame, text='Clear', command=lambda: self.clear_listbox())
        btn_clear_results.grid(row=8, column=0, columnspan=2, sticky='ew', pady=5)

        btn_return_main = tk.Button(search_term_frame, text='Return to main menu', command=lambda: self.controller.show_frame('StudentMenu'))
        btn_return_main.grid(row=9, column=0, columnspan=2, sticky='ew', pady=5)

        search_result_frame = tk.Frame(self, relief='groove', borderwidth=2)
        search_result_frame.pack(side='left', anchor='ne', fill='both', expand=True, padx=(0, 5), pady=(3,5))

        lbl_format_explanation = tk.Label(search_result_frame, text='Order of elements: \n ID, First Name, Second Name, Year Group, Form Group, Username, Password')
        lbl_format_explanation.pack()
        scroll_sign_history = tk.Scrollbar(search_result_frame)
        scroll_sign_history.pack(side='right', fill='y', padx=(0,2))

        self.list_search_results = tk.Listbox(search_result_frame, yscrollcommand=scroll_sign_history.set)
        self.list_search_results.pack(side='left', fill='both', expand=True, padx=(2,2))

    def clear_listbox(self):
        """Clears the list box of all entries"""

        self.list_search_results.delete(0, tk.END)

    def search_users(self):
        """Searches using input terms from GUI"""

        self.clear_listbox()

        # Tuple to hold dict keys.
        search_keys = ('id', 'first_name', 'second_name', 'year_group', 'form_group', 'username', 'password')
        search_terms = {}
        for count, i in enumerate(self.entries):
            if (i.get()) == '':  # If input is empty, do not create dictionary entry.
                continue
            search_terms[search_keys[count]] = i.get()

        search_results = logic.search_users(search_terms)
        for i in search_results:
            self.list_search_results.insert(tk.END, ', '.join(map(str, i)))


class EditSearchUsers(UserSearch):

    def __init__(self, parent, controller):

        self.controller = controller
        UserSearch.__init__(self, parent, controller)

        frame_start_edit = tk.Frame(self.search_config_frame, relief='groove', borderwidth=2)
        frame_start_edit.pack(pady=3, expand=True, fill='both')

        btn_start_user_edit = tk.Button(frame_start_edit, text='Start edit', command=lambda: self.controller.show_frame('EditUser'))
        btn_start_user_edit.pack(pady=3, expand=True, fill='both')


class SignSearch(tk.Frame):
    """Search for sign in / outs by ID, date, and time"""

    def __init__(self, parent, controller):
        """"Intitialse class values and creates GUI elements"""

        tk.Frame.__init__(self, parent)
        self.controller = controller

        # GUI creation

        self.search_config_frame = tk.Frame(self)
        self.search_config_frame.pack(side='left', anchor='nw', padx=10)

        title_frame = tk.Frame(self.search_config_frame, relief='groove', borderwidth=2)
        title_frame.pack(fill='both', anchor='nw', pady=(3, 15))

        lbl_search_title = tk.Label(title_frame, text='Sign Search')
        lbl_search_title.pack()

        btn_change_sign_search = tk.Button(title_frame, text='Go to user search', command=lambda: self.controller.show_frame('UserSearch'))
        btn_change_sign_search.pack(pady=3)

        search_term_frame = tk.Frame(self.search_config_frame, relief='groove', borderwidth=2)
        search_term_frame.pack(fill='both', anchor='nw')

        self.entries = [] # List to store variables to .get() later

        lbl_sign_in_out = tk.Label(search_term_frame, text='Sign type:')
        lbl_sign_in_out.grid(row=0, column=0, sticky='nsew', pady=(5, 3))

        self.sign_value = tk.StringVar(search_term_frame, value='Both')
        sign_types = ['', 'Both', 'Sign in', 'Sign out']

        menu_sign_in_out = tk.OptionMenu(search_term_frame, self.sign_value, *sign_types)
        menu_sign_in_out.config(width='17')
        menu_sign_in_out.grid(row=0, column=1, sticky='nsew', pady=(5, 3))

        lbl_id_search = tk.Label(search_term_frame, text='Sign ID:')
        lbl_id_search.grid(row=1, column=0, sticky='nsew', pady=3)

        ent_id_search = tk.Entry(search_term_frame)
        ent_id_search.grid(row=1, column=1, sticky='nsew', pady=3)
        self.entries.append(ent_id_search)

        lbl_student_id_search = tk.Label(search_term_frame, text='Student ID:')
        lbl_student_id_search.grid(row=2, column=0, sticky='nsew', pady=3)

        ent_student_id_search = tk.Entry(search_term_frame)
        ent_student_id_search.grid(row=2, column=1, sticky='nsew', pady=3)
        self.entries.append(ent_student_id_search)

        lbl_sign_out_out_type = tk.Label(search_term_frame, text='Sign out type:')
        lbl_sign_out_out_type.grid(row=3, column=0, sticky='nsew', pady=3)

        sign_out_value = tk.StringVar(search_term_frame, value='')
        self.entries.append(sign_out_value)
        sign_out_list = ['', 'Going home', 'Lunch / Break']

        menu_sign_out_type = tk.OptionMenu(search_term_frame, sign_out_value,
                                           *sign_out_list)
        menu_sign_out_type.config(width='17')
        menu_sign_out_type.grid(row=3, column=1, sticky='ew', pady=3)

        lbl_date_search = tk.Label(search_term_frame, text='Date:\n(format YYYY-MM-DD)')
        lbl_date_search.grid(row=4, column=0, sticky='nsew', pady=3)

        ent_date_search = tk.Entry(search_term_frame)
        self.entries.append(ent_date_search)
        ent_date_search.grid(row=4, column=1, sticky='nsew', pady=3)

        # Create list of values to 24, single digits have an extra 0 on the
        # left.
        hour_list = [f"{i:02}" for i in range(24)]
        hour_list.insert(0, '')
        # Create list of values to 60, single digits have an extra 0 on the
        # left.
        minute_second_list = [f"{i:02}" for i in range(60)]
        minute_second_list.insert(0, '')

        lbl_time_from = tk.Label(search_term_frame, text='From time:')
        lbl_time_from.grid(row=5, column=0, sticky='nsew', pady=3)

        frame_from_time = tk.Frame(search_term_frame)
        frame_from_time.grid(row=5, column=1, sticky='nsew', pady=3)

        self.from_time = [] # List to manage .get()s easier.
        from_hour_value = tk.StringVar(frame_from_time, value='')
        from_minute_value = tk.StringVar(frame_from_time, value='')
        from_second_value = tk.StringVar(frame_from_time, value='')
        self.from_time.extend((from_hour_value, from_minute_value,
                               from_second_value))

        lbl_time_format = tk.Label(frame_from_time, text='HH:MM:SS')
        lbl_time_format.grid(row=0, column=0, columnspan=3, sticky='nsew')

        combo_hour_from = ttk.Combobox(frame_from_time, textvariable=from_hour_value, values=hour_list, state='readonly', width=3)
        combo_hour_from.grid(row=1, column=0, sticky='nsew', padx=2)
        combo_minute_from = ttk.Combobox(frame_from_time, textvariable=from_minute_value, values=minute_second_list, state='readonly', width=3)
        combo_minute_from.grid(row=1, column=1, sticky='nsew', padx=2)
        combo_second_from = ttk.Combobox(frame_from_time, textvariable=from_second_value, values=minute_second_list, state='readonly', width=3)
        combo_second_from.grid(row=1, column=2, sticky='nsew', padx=2)

        frame_to_time = tk.Frame(search_term_frame)
        frame_to_time.grid(row=6, column=1, sticky='nsew', pady=3)

        lbl_time_to = tk.Label(search_term_frame, text='To time:')
        lbl_time_to.grid(row=6, column=0, sticky='nsew', pady=3)

        self.to_time = [] # List to manage .get()s easier.
        to_hour_value = tk.StringVar(frame_to_time, value='')
        to_minute_value = tk.StringVar(frame_to_time, value='')
        to_second_value = tk.StringVar(frame_to_time, value='')
        self.to_time.extend((to_hour_value, to_minute_value, to_second_value))

        combo_hour_to = ttk.Combobox(frame_to_time, textvariable=to_hour_value, values=hour_list, width=3, state='readonly')
        combo_hour_to.grid(row=0, column=0, sticky='nsew', padx=2)
        combo_minute_to = ttk.Combobox(frame_to_time, textvariable=to_minute_value, values=minute_second_list, state='readonly', width=3)
        combo_minute_to.grid(row=0, column=1, sticky='nsew', padx=2)
        combo_second_to = ttk.Combobox(frame_to_time, textvariable=to_second_value, values=minute_second_list, state='readonly', width=3)
        combo_second_to.grid(row=0, column=2, sticky='nsew', padx=2)

        btn_begin_search = tk.Button(search_term_frame, text='Search', command=lambda: self.start_sign_search())
        btn_begin_search.grid(row=7, column=0, columnspan=2, sticky='ew', pady=3)

        btn_return_main =tk.Button(search_term_frame, text='Return to main menu', command=lambda: self.controller.show_frame('StudentMenu'))
        btn_return_main.grid(row=8, column=0, columnspan=2, sticky='ew', pady=5)

        search_result_frame = tk.Frame(self, relief='groove', borderwidth=2)
        search_result_frame.pack(side='left', anchor='ne', fill='both', expand=True, padx=(0, 5), pady=(3, 5))

        lbl_format_explanation = tk.Label(search_result_frame, text='Order of elements: \n Sign ID, Date, Time, Student ID, Sign Out Type (If applicable)')
        lbl_format_explanation.pack()
        scroll_sign_history = tk.Scrollbar(search_result_frame)
        scroll_sign_history.pack(side='right', fill='y', padx=(0,2))

        self.list_search_results = tk.Listbox(search_result_frame, yscrollcommand=scroll_sign_history.set)
        self.list_search_results.pack(side='left', fill='both', expand=True,
                                      padx=(2, 2))

    def clear_listbox(self):
        """Clears the list box of all entries"""

        self.list_search_results.delete(0, tk.END)

    def start_sign_search(self):
        """Start sign search with defined parameters"""

        self.clear_listbox()

        if len(self.entries[3].get()) != 0:
            if logic.Validation.date_format_check(self.entries[3].get()) == False:
                messagebox.showerror('Failure', 'Date format incorrect')
                return

        sign_in_or_out = self.sign_value.get().lower()
        if sign_in_or_out == '' or sign_in_or_out == 'both':
            self.search_signs('sign out')
            self.search_signs('sign in')
        else:
            self.search_signs(sign_in_or_out)

    def search_signs(self, sign_in_or_out):
        """"Search and show sign ins"""

        # Tuple to hold dict keys.
        search_keys = ('sign_out_id', 'student_id', 'sign_out_type', 'date')
        search_terms = {}

        for count, i in enumerate(self.entries):
            if (i.get()) == '':  # If search term empty, do not include in dict.
                continue
            search_terms[search_keys[count]] = i.get()  # Add to dict.

        # If date is empty, skip entering dates into dict.
        if '' not in [i.get() for i in self.to_time] and '' not in [t.get() for t in self.from_time]:

            # Create strings of times.
            from_time = ':'.join([i.get() for i in self.from_time])
            to_time = ':'.join([i.get() for i in self.to_time])

            # Convert string into time type, allows comparison.
            dt_from_time = datetime.strptime(from_time, '%H:%M:%S').time()
            dt_to_time = datetime.strptime(to_time, '%H:%M:%S').time()

            # Compares two times. Can't have a time range between times with a
            # negative difference. Example, Can't have 150 <= x <= 130.
            if dt_to_time <= dt_from_time:
                messagebox.showerror('Error', 'From is greater than to time')

            time_tuple = (from_time, to_time) # Add times to dict.
            search_results = logic.search_signs(sign_in_or_out, search_terms, time_tuple)
        else:
            search_results = logic.search_signs(sign_in_or_out, search_terms)

        for i in search_results:
            self.list_search_results.insert(tk.END, ', '.join(map(str, i)))


class EditUser(tk.Frame):
    """Edit search result"""

    def __init__(self, parent, controller):
        """"Initialise class values and creates GUI elements"""

        tk.Frame.__init__(self, parent)
        self.controller = controller

        # gui creation

        lbl_edit_title = tk.Label(self, text='Edit Table Entry')
        lbl_edit_title.pack()

        self.frame_edit_terms = tk.Frame(self)
        self.frame_edit_terms.pack()

        lbl_fname = tk.Label(self.frame_edit_terms, text='First name:')
        lbl_fname.grid(row=0, column=0, pady=3)

        self.fname_value = tk.StringVar(self.frame_edit_terms, value='First name placeholder')
        self.ent_fname = tk.Entry(self.frame_edit_terms, textvariable=self.fname_value)
        self.ent_fname.grid(row=0, column=1, pady=3)

        lbl_sname = tk.Label(self.frame_edit_terms, text='Second name:')
        lbl_sname.grid(row=1, column=0, pady=3)

        self.sname_value = tk.StringVar(self.frame_edit_terms, value='Second name placeholder')
        self.ent_sname = tk.Entry(self.frame_edit_terms, textvariable=self.sname_value)
        self.ent_sname.grid(row=1, column=1, pady=3)

        lbl_year_group = tk.Label(self.frame_edit_terms, text='Year group:')
        lbl_year_group.grid(row=2, column=0)

        self.year_group_value = tk.StringVar(self.frame_edit_terms, value='Year group placeholder')
        year_values = ['12', '13']
        self.menu_year_group = tk.OptionMenu(self.frame_edit_terms, self.year_group_value, *year_values)
        self.menu_year_group.config(width='20')
        self.menu_year_group.grid(row=2, column=1)

        lbl_form_group = tk.Label(self.frame_edit_terms, text='Form group:')
        lbl_form_group.grid(row=3, column=0)

        self.form_group_value = tk.StringVar(self.frame_edit_terms, value='Form group placeholder')
        form_values = ['A', 'B', 'C', 'D', 'E', 'F']
        self.menu_form_group = tk.OptionMenu(self.frame_edit_terms, self.form_group_value, *form_values)
        self.menu_form_group.config(width='20')
        self.menu_form_group.grid(row=3, column=1)

        lbl_username = tk.Label(self.frame_edit_terms, text='Username:')
        lbl_username.grid(row=4, column=0)

        self.username_value = tk.StringVar(self.frame_edit_terms, value='Username')
        self.ent_username = tk.Entry(self.frame_edit_terms, textvariable=self.username_value)
        self.ent_username.grid(row=4, column=1)

        lbl_password = tk.Label(self.frame_edit_terms, text='Password')
        lbl_password.grid(row=5, column=0)

        self.password_value = tk.StringVar(self.frame_edit_terms, value='Password')
        self.ent_password = tk.Entry(self.frame_edit_terms, textvariable=self.password_value)
        self.ent_password.grid(row=5, column=1)

        btn_confirm_edit = tk.Button(self.frame_edit_terms, text='Confirm edit', command='')
        btn_confirm_edit.grid(row=6, column=0, columnspan=2, pady=10)

        btn_exit = tk.Button(self.frame_edit_terms, text='Return to search:', command=lambda:self.controller.show_frame('UserSearch'))
        btn_exit.grid(row=7, column=0, columnspan=2, pady=3)


class SignIn(tk.Frame):
    """Record sign in to of school (not the program"""

    def __init__(self, parent, controller):
        """"Initialise class values and creates GUI elements"""

        tk.Frame.__init__(self, parent)
        self.controller = controller

        # GUI creation

        lbl_sign_in_title = tk.Label(self, text='Sign In')
        lbl_sign_in_title.pack(pady=20)

        btn_sign_in = tk.Button(self, text='Sign In', command=lambda: self.start_sign_in())
        btn_sign_in.pack(pady=10, padx=25, expand=True, fill='both')

        btn_cancel = tk.Button(self, text='Cancel', command=lambda: self.controller.show_frame('StudentMenu'))
        btn_cancel.pack(pady=10, padx=25, expand=True, fill='both')

    def start_sign_in(self):
        """"Start a sign in"""

        logic.create_sign_in(str(self.controller.session_id))


class SignOut(tk.Frame):
    """Record sign out of school (not the program)"""

    def __init__(self, parent, controller):
        """Initialise class values and creates GUI elements"""

        tk.Frame.__init__(self, parent)
        self.controller = controller

        # GUI creation

        lbl_sign_out_title = tk.Label(self, text='Sign Out')
        lbl_sign_out_title.pack(pady=20)

        frame_sign_out_type = tk.Frame(self)
        frame_sign_out_type.pack()

        lbl_sign_out_type = tk.Label(frame_sign_out_type, text='Sign out reason:')
        lbl_sign_out_type.grid(row=0, column=0)

        self.sign_value = tk.StringVar(frame_sign_out_type, value='')

        sign_out_types = ['Breaktime', 'Lunchtime', 'Going home']

        self.menu_sign_out_type = tk.OptionMenu(frame_sign_out_type, self.sign_value, *sign_out_types)
        self.menu_sign_out_type.config(width='17')
        self.menu_sign_out_type.grid(row=0, column=1)

        btn_sign_out = tk.Button(self, text='Sign out', command=lambda: self.start_sign_out())
        btn_sign_out.pack(pady=(15, 0), padx=50, expand=True, fill='both')

        btn_cancel = tk.Button(self, text='Cancel', command=lambda: self.controller.show_frame('StudentMenu'))
        btn_cancel.pack(pady=(15, 20), padx=50, expand=True, fill='both')

    def start_sign_out(self):
        """"Start sign out"""
        if self.sign_value.get() == '':
            messagebox.showerror('Failure', 'Fill in the sign out reason')
        logic.create_sign_out(str(self.controller.session_id), self.sign_value.get())


class SignHistory(tk.Frame):
    """"Record history of sign ins and outs"""

    def __init__(self, parent, controller):
        """Initialise class values and creates GUI elements"""

        tk.Frame.__init__(self, parent)
        self.controller = controller

        # GUI creation

        lbl_sign_history_title = tk.Label(self, text='Sign in / out history')
        lbl_sign_history_title.pack()

        frame_menu = tk.Frame(self)
        frame_menu.pack()

        btn_return = tk.Button(frame_menu, text='Return to menu', command=lambda: self.controller.show_frame('StudentMenu'))
        btn_return.grid(row=0, column=0, pady=3, padx=2)

        btn_view_history = tk.Button(frame_menu, text='View Sign History', command=lambda: self.view_history())
        btn_view_history.grid(row=0, column=1, pady=3, padx=2)

        lbl_result_format = tk.Label(self, text='Format:\nSign in / out, Sign ID, Sign date, Sign time, Student ID, Sign out type (if applicable)')
        lbl_result_format.pack(pady=2)

        frame_sign_history = tk.Frame(self, relief='groove', borderwidth=2)
        frame_sign_history.pack(expand=True, fill='both')

        scroll_sign_history = tk.Scrollbar(frame_sign_history)
        scroll_sign_history.pack(side='right', fill='y')

        self.list_sign_history = tk.Listbox(frame_sign_history,  yscrollcommand=scroll_sign_history.set)
        self.list_sign_history.pack(side='left', fill='both', expand=True)

        scroll_sign_history.config(command=self.list_sign_history.yview)

    def view_history(self):
        """View all sign in / outs"""

        history_list = logic.sign_history()
        for i in  history_list:
            i = list(i)
            if len(i) == 4:
                i.insert(0, 'Sign In')
                self.list_sign_history.insert(tk.END, '  ,  '.join(map(str, i)))
            elif len(i) == 5:
                i.insert(0, 'Sign Out')
                self.list_sign_history.insert(tk.END, '  ,  '.join(map(str, i)))


if __name__ == '__main__':

    app = Gui()
    app.minsize(800, 400)
    app.mainloop()
