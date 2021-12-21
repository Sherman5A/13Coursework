"""Init, GUI construction"""

import tkinter as tk
from tkinter.constants import NW
import logic


class Gui(tk.Tk):
    """GUI controller for program, shows class frames, inits and manages frame classes"""

    def __init__(self, *args, **kwargs):
        """Creates gui, base container frame, inits class frames"""
        
        tk.Tk.__init__(self, *args, **kwargs)
        # initialise tkinter

        container = tk.Frame(self) # create a frame to fit the classes into 
        container.pack(side='top', fill='both', expand=True)
        # allow frame to expand to classes
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {} # dictionary to place classes into

        # iterate through a list of classes, intialising them
        for F in (StartPage, TextLogin, SignUp, StudentMenu, TeacherMenu, LogoutMenu, UserSearch, EditSearchUsers, SignSearch, EditUser, SignIn, SignOut, SignHistory):
            
            # initialise frame and assign reference 'frame' to frame
            frame = F(parent=container, controller=self) 
            self.frames[F.__name__] = frame # F.__name__ gets name of class, it then assgins the class reference to dictionary key
            frame.grid(row=0, column=0, sticky='nsew') # grid and let expand

        # page setup
        self.title("6th Form Sign System")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """Raise specified frame classs: page_name"""

        frame = self.frames[page_name]
        frame.tkraise() # raises frame of arguement


class StartPage(tk.Frame):
    """Start page for program, offers sign in, quit buttons"""

    def __init__(self, parent, controller):
        """Initialise class values and create GUI elements"""
        # initialse frame
        tk.Frame.__init__(self, parent) # start tk frame class
        self.controller = controller

        # create GUI elements
        lbl_title = tk.Label(self, text='Start Page:')
        lbl_title.pack(pady=10)

        self.btn_start_login = tk.Button(self, text='Login Page', command=lambda: self.controller.show_frame('TextLogin'))
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
        
        btn_EditSearchUsers = tk.Button(self, text='dafsa', command=lambda: self.controller.show_frame('EditSearchUsers'))
        btn_EditSearchUsers.pack(pady=3)
     

class TextLogin(tk.Frame):
    """Page to login to system"""
    
    def __init__(self, parent, controller):
        """Initialise class values and create GUI elements"""
        
        # initialise frame
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
        btn_login = tk.Button(self, text='Login', command='')
        btn_login.pack(pady=3)

        btn_return_start_page = tk.Button(self, text='Return to start page', command=lambda: self.controller.show_frame('StartPage'))
        btn_return_start_page.pack(pady=3)

    def login_check(self):
        """Checks username and password"""
        input_username = self.ent_username.get()
        print(input_username)
        input_password = self.ent_password.get()
        print(input_username)
        if logic.check_login_creds(input_username, input_password):
            self.controller.show_frame('StudentMenu')
        else:
            pass


class SignUp(tk.Frame):
    """Page for students to sign up to login system"""

    def __init__(self, parent, controller):
        """Initialise class values and create GUI elements"""
        
        # initialise frame
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # gui creation
        lbl_signup_title = tk.Label(self, text='Sign up')
        lbl_signup_title.pack(pady=10)

        frame_user_input = tk.Frame(self)
        frame_user_input.pack()

        lbl_first_name = tk.Label(frame_user_input, text='First Name:')
        lbl_first_name.grid(row=0, column=0, pady=3)

        self.ent_first_name = tk.Entry(frame_user_input)
        self.ent_first_name.grid(row=0, column=1, pady=3)

        lbl_second_name = tk.Label(frame_user_input, text='Last name:')
        lbl_second_name.grid(row=1, column=0, pady=3)

        self.ent_second_name = tk.Entry(frame_user_input)
        self.ent_second_name.grid(row=1, column=1, pady=3)

        lbl_year_group = tk.Label(frame_user_input, text='Year group:')
        lbl_year_group.grid(row=2, column=0)

        year_groups = ['12', '13']
        self.year_value = tk.StringVar(frame_user_input, value='Select a year group')

        self.menu_year_group = tk.OptionMenu(frame_user_input, self.year_value, *year_groups)
        self.menu_year_group.grid(row=2, column=1, sticky='ew', pady=3)
        self.menu_year_group.config(width=16)

        lbl_form_group = tk.Label(frame_user_input, text='Form group:')
        lbl_form_group.grid(row=3, column=0)
        
        self.form_value = tk.StringVar(frame_user_input, value='Select a form group')
        form_list = ['A', 'B', 'C', 'D', 'E', 'D', 'F']
        
        self.menu_form_group = tk.OptionMenu(frame_user_input, self.form_value, *form_list)
        self.menu_form_group.grid(row=3, column=1, sticky='ew', pady=3)
        self.menu_form_group.config(width=16)

        lbl_username = tk.Label(frame_user_input, text='Username:')
        lbl_username.grid(row=4, column=0, pady=3)

        self.ent_username = tk.Entry(frame_user_input)
        self.ent_username.grid(row=4, column=1, pady=3)

        # <3 <3

        lbl_password = tk.Label(frame_user_input, text='Password:')
        lbl_password.grid(row=5, column=0, pady=3)

        self.ent_password = tk.Entry(frame_user_input, show='*')
        self.ent_password.grid(row=5, column=1, pady=3)

        lbl_password_repeat = tk.Label(frame_user_input, text='Repeat Password:')
        lbl_password_repeat.grid(row=6, column=0, pady=3)

        self.ent_password_repeat = tk.Entry(frame_user_input, show='*')
        self.ent_password_repeat.grid(row=6, column=1, pady=3)

        btn_confirm = tk.Button(self, text='Confirm sign up', command='')
        btn_confirm.pack(pady=5)

        btn_return_start = tk.Button(self, text= 'Return to start page', command=lambda: self.controller.show_frame('StartPage'))
        btn_return_start.pack(pady=3)

    def create_account(self):
        account_variables = {}
        account_variables['first_name'] = self.ent_first_name.get().lower()
        account_variables['second_name'] = self.ent_second_name.get().lower()
        account_variables['year_group'] = self.year_value.get().lower()
        account_variables['form_group'] = self.form_value.get().lower()
        account_variables['username'] = self.ent_username.get()
        account_variables['password'] = self.ent_password.get()
        account_variables['password_repreat'] = self.ent_password_repeat.get()
        logic.create_user(account_variables)



class StudentMenu(tk.Frame):
    """GUI menu for student access, provdies less options than teacher"""

    def __init__(self, parent, controller):
        """Initialise class values and create initial GUI elements"""
        
        # initialise frame 
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # gui creation
        # string var for student name, allows text to change
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

        # may add function: 
        # btn_view_permissions = tk.Button(frame_stuent_actions, text='View user permissions', command='')

        self.btn_user_logout = tk.Button(self, text='Logout of program', command=lambda: self.logout())
        self.btn_user_logout.pack(pady=3)

    def student_configure(self, student_name):
        """Configures the StudentMenu to the logged in student"""
        self.student_name.set(value=student_name)

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
        # gui creation
        # string var for student name, allows text to change

        # self.teacher_name = tk.StringVar(self, value='Teacher Name')

        # lbl_teacher_title = tk.Label(self, textvariable=self.teacher_name)
        # lbl_teacher_title.pack(pady=5)
        self.btn_user_logout.destroy()

        frame_teacher_actions = tk.Frame(self)
        frame_teacher_actions.pack()

        btn_manual_sign = tk.Button(frame_teacher_actions, text='Manual sign students', command='')
        btn_manual_sign.grid(row=2, column=0, sticky='ew', padx=3)

        btn_search_attendence = tk.Button(frame_teacher_actions, text='View student history', command='')
        btn_search_attendence.grid(row=2, column=1, sticky='ew', pady=3, padx=3)

        btn_edit_student = tk.Button(frame_teacher_actions, text='Edit student info', command='')
        btn_edit_student.grid(row=3, column=0, sticky='ew', pady=3, padx=3)

        # may add function: 
        btn_view_permissions = tk.Button(frame_teacher_actions, text='View user permissions', command='')
        btn_view_permissions.grid(row=3, column=1, sticky='ew', pady=3, padx=3)

        self.btn_user_logout = tk.Button(self, text='Logout of program', command=lambda: self.logout())
        self.btn_user_logout.pack(pady=3)   

    def teacher_configure(self, teacher_name):
        """Configure the TeacherMenu to the logged in student"""
        self.teacher_name.set(teacher_name)


class LogoutMenu(tk.Frame):
    """Confirms whether user wants to logout"""

    def __init__(self, parent, controller):
        """Intialise class values and create GUI elements"""

        tk.Frame.__init__(self, parent)
        self.controller = controller

        # gui creation

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
        # log out of sql
        self.controller.show_frame('StartPage')


class UserSearch(tk.Frame):
    """Search for students by name, id, username, year group, and form"""

    def __init__(self, parent, controller):
        """Intitialise class values and create GUI elements"""

        tk.Frame.__init__(self, parent)
        self.controller = controller

        # gui creation

        self.search_config_frame = tk.Frame(self)
        self.search_config_frame.pack(side='left', anchor=NW, padx=10)

        title_frame = tk.Frame(self.search_config_frame, relief='groove', borderwidth=2)
        title_frame.pack(fill='both', anchor=NW, pady=(3, 15))

        lbl_search_title = tk.Label(title_frame, text='User Search')
        lbl_search_title.pack()

        self.btn_change_sign_search = tk.Button(title_frame, text='Go to sign search', command=lambda: self.controller.show_frame('SignSearch'))
        self.btn_change_sign_search.pack(pady=3)

        search_term_frame = tk.Frame(self.search_config_frame, relief='groove', borderwidth=2)
        search_term_frame.pack(fill='both', anchor=NW)

        lbl_id_search = tk.Label(search_term_frame, text='Student ID:')
        lbl_id_search.grid(row=0, column=0, sticky='nsew', pady=(10, 3))

        self.ent_id_search = tk.Entry(search_term_frame)
        self.ent_id_search.grid(row=0, column=1, sticky='nsew', pady=(10, 3))

        lbl_fname_search = tk.Label(search_term_frame, text='First name:')
        lbl_fname_search.grid(row=1, column=0, sticky='nsew', pady=3)

        self.ent_fname_search = tk.Entry(search_term_frame)
        self.ent_fname_search.grid(row=1, column=1, sticky='nsew', pady=3)

        lbl_sec_name_search = tk.Label(search_term_frame, text='Second name:')
        lbl_sec_name_search.grid(row=2, column=0, sticky='nsew', pady=3)

        self.ent_sec_name_search = tk.Entry(search_term_frame)
        self.ent_sec_name_search.grid(row=2, column=1, sticky='nsew', pady=3)

        lbl_year_search = tk.Label(search_term_frame, text='Year group:')
        lbl_year_search.grid(row=3, column=0, sticky='nsew', pady=3)

        self.year_value = tk.StringVar(search_term_frame, value='Select a year group')
        year_list = ['12', '13']

        self.menu_year_search = tk.OptionMenu(search_term_frame, self.year_value, *year_list)
        self.menu_year_search.config(width='17')
        self.menu_year_search.grid(row=3, column=1, sticky='nsew', pady=3)

        lbl_form_search = tk.Label(search_term_frame, text='Form group:')
        lbl_form_search.grid(row=4, column=0, sticky='nsew', pady=3)

        self.form_value = tk.StringVar(search_term_frame, value='Select a form group')
        form_list = ['A', 'B', 'C', 'D', 'E', 'D', 'F']
        
        self.menu_form_search = tk.OptionMenu(search_term_frame, self.form_value, *form_list)
        self.menu_form_search.config(width='17')
        self.menu_form_search.grid(row=4, column=1, sticky='ew', pady=3)

        lbl_username_search = tk.Label(search_term_frame, text='Username:')
        lbl_username_search.grid(row=5, column=0, sticky='nsew', pady=3)

        self.ent_username_search = tk.Entry(search_term_frame)
        self.ent_username_search.grid(row=5, column=1, sticky='nsew', pady=3)

        self.btn_begin_search = tk.Button(search_term_frame, text='Search', command='')
        self.btn_begin_search.grid(row=6, column=0, columnspan=2, sticky='ew', pady=3)

        btn_return_main =tk.Button(search_term_frame, text='Return to main menu', command=lambda: self.controller.show_frame('StudentMenu'))
        btn_return_main.grid(row=7, column=0, columnspan=2, sticky='ew', pady=5)


class EditSearchUsers(UserSearch):

    def __init__(self, parent, controller):

        self.controller = controller
        UserSearch.__init__(self, parent, controller)
        
        frame_start_edit = tk.Frame(self.search_config_frame, relief='groove', borderwidth=2)
        frame_start_edit.pack(pady=3, expand=True, fill='both')
    
        btn_start_user_edit = tk.Button(frame_start_edit, text='Start User Search', command=lambda: self.controller.show_frame('EditUser'))
        btn_start_user_edit.pack(pady=3, expand=True, fill='both')


class SignSearch(tk.Frame):
    """Search for sign in / outs by ID, date, and time"""

    def __init__(self, parent, controller):
        """"Intitialse class values and creates GUI elements"""

        tk.Frame.__init__(self, parent)
        self.controller = controller

        # gui creation

        self.search_config_frame = tk.Frame(self)
        self.search_config_frame.pack(side='left', anchor=NW, padx=10)

        title_frame = tk.Frame(self.search_config_frame, relief='groove', borderwidth=2)
        title_frame.pack(fill='both', anchor=NW, pady=(3, 15))

        lbl_search_title = tk.Label(title_frame, text='Sign Search')
        lbl_search_title.pack()

        self.btn_change_sign_search = tk.Button(title_frame, text='Go to user search', command=lambda: self.controller.show_frame('UserSearch'))
        self.btn_change_sign_search.pack(pady=3)

        search_term_frame = tk.Frame(self.search_config_frame, relief='groove', borderwidth=2)
        search_term_frame.pack(fill='both', anchor=NW)

        lbl_sign_in_out = tk.Label(search_term_frame, text='Sign type:')
        lbl_sign_in_out.grid(row=0, column=0, sticky='nsew', pady=(5, 3))

        self.sign_value = tk.StringVar(search_term_frame, value='Sign in or out')
        sign_types = ['Sign in', 'Sign out']

        self.menu_sign_in_out = tk.OptionMenu(search_term_frame, self.sign_value, *sign_types)
        self.menu_sign_in_out.config(width='17')
        self.menu_sign_in_out.grid(row=0, column=1, sticky='nsew', pady=(5, 3))

        lbl_id_search = tk.Label(search_term_frame, text='Student ID:')
        lbl_id_search.grid(row=1, column=0, sticky='nsew', pady=3)

        self.ent_id_search = tk.Entry(search_term_frame)
        self.ent_id_search.grid(row=1, column=1, sticky='nsew', pady=3)

        lbl_sign_out_out_type = tk.Label(search_term_frame, text='Sign out type:')
        lbl_sign_out_out_type.grid(row=2, column=0, sticky='nsew', pady=3)

        self.sign_out_value = tk.StringVar(search_term_frame, value='Sign out only')
        sign_out_list = ['Going home', 'Lunch / Break', 'Sign in']
        
        self.menu_sign_out_type = tk.OptionMenu(search_term_frame, self.sign_out_value, *sign_out_list)
        self.menu_sign_out_type.config(width='17')
        self.menu_sign_out_type.grid(row=2, column=1, sticky='ew', pady=3)

        lbl_date_search = tk.Label(search_term_frame, text='Date:')
        lbl_date_search.grid(row=3, column=0, sticky='nsew', pady=3)

        self.ent_date_search = tk.Entry(search_term_frame)
        self.ent_date_search.grid(row=3, column=1, sticky='nsew', pady=3)

        self.btn_begin_search = tk.Button(search_term_frame, text='Search', command='')
        self.btn_begin_search.grid(row=4, column=0, columnspan=2, sticky='ew', pady=3)

        btn_return_main =tk.Button(search_term_frame, text='Return to main menu', command=lambda: self.controller.show_frame('StudentMenu'))
        btn_return_main.grid(row=5, column=0, columnspan=2, sticky='ew', pady=5)


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
    """Record sign into of school (not the program"""

    def __init__(self, parent, controller):
        """"Intitialse class values and creates GUI elements"""

        tk.Frame.__init__(self, parent)
        self.controller = controller

        # gui creation

        lbl_sign_in_title = tk.Label(self, text='Sign In')
        lbl_sign_in_title.pack(pady=20)

        btn_sign_in = tk.Button(self, text='Sign In', command='')
        btn_sign_in.pack(pady=10, padx=25, expand=True, fill='both')

        btn_cancel = tk.Button(self, text='Cancel', command=lambda: self.controller.show_frame('StudentMenu'))
        btn_cancel.pack(pady=10, padx=25, expand=True, fill='both')


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

        self.sign_value = tk.StringVar(frame_sign_out_type, value='Sign out type')

        sign_out_types = ['Breaktime / Lunchtime', 'Going home']

        self.menu_sign_out_type = tk.OptionMenu(frame_sign_out_type, self.sign_value, *sign_out_types)
        self.menu_sign_out_type.config(width='17')
        self.menu_sign_out_type.grid(row=0, column=1)

        btn_sign_out = tk.Button(self, text='Sign out', command='')
        btn_sign_out.pack(pady=(15, 0), padx=50, expand=True, fill='both')

        btn_cancel = tk.Button(self, text='Cancel', command=lambda: self.controller.show_frame('StudentMenu'))
        btn_cancel.pack(pady=(15, 20), padx=50, expand=True, fill='both')     


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
        btn_return.pack(pady=3)

        frame_sign_history = tk.Frame(self, relief='groove', borderwidth=2)
        frame_sign_history.pack(expand=True, fill='both')

        scroll_sign_history = tk.Scrollbar(frame_sign_history)
        scroll_sign_history.pack(side='right', fill='y')

        list_sign_history = tk.Listbox(frame_sign_history,  yscrollcommand=scroll_sign_history.set)
        list_sign_history.pack(side='left', fill='both', expand=True)

        for line in range(1, 26):
            list_sign_history.insert(tk.END, "Geeks " + str(line))
        
        scroll_sign_history.config(command=list_sign_history.yview)


if __name__ == '__main__':
    
    app = Gui()
    app.minsize(800, 400)
    app.mainloop()
