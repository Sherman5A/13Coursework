"""Init, GUI construction"""

import tkinter as tk
import logic


class Gui(tk.Tk):
    """GUI controller for program, shows class frames, inits and manages frame classes"""

    def __init__(self, *args, **kwargs):
        """Creates gui, base container frame, inits class frames"""
        
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, TextLogin, SignUp, StudentMenu, TeacherMenu, LogoutMenu):
            frame = F(parent=container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.title("6th Form Sign System")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """Raise specified frame classs: page_name"""
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    """Start page for program, offers sign in, quit buttons"""

    def __init__(self, parent, controller):
        """Initialise class values and create GUI elements"""
        # initialse frame
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.config(bg='#00ff93')

        # create GUI elements
        lbl_title = tk.Label(self, text='Start Page:')
        lbl_title.pack(pady=10)

        self.btn_start_login = tk.Button(self, text='Login Page', command=lambda: self.controller.show_frame('TextLogin'), fg='yellow', bg='#00ff93')
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
     

class TextLogin(tk.Frame):
    """Page to login to system"""
    
    def __init__(self, parent, controller):
        """Initialise class values and create GUI elements"""
        
        # initialise frame
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.config(bg='#f0ff00')

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
        
        self.config(bg='pink')
        # gui creation
        lbl_signup_title = tk.Label(self, text='Sign up')
        lbl_signup_title.pack(pady=10)

        frame_user_input = tk.Frame(self)
        frame_user_input.pack()


        lbl_first_name = tk.Label(frame_user_input, text='First Name:')
        lbl_first_name.grid(row=0, column=0, pady=4)

        self.ent_first_name = tk.Entry(frame_user_input)
        self.ent_first_name.grid(row=0, column=1, pady=4)

        lbl_second_name = tk.Label(frame_user_input, text='Last name:')
        lbl_second_name.grid(row=1, column=0, pady=4)

        self.ent_second_name = tk.Entry(frame_user_input)
        self.ent_second_name.grid(row=1, column=1, pady=4)

        lbl_year_group = tk.Label(frame_user_input, text='Year group:')
        lbl_year_group.grid(row=2, column=0)

        year_groups = ['12', '13']
        year_value = tk.StringVar(frame_user_input, value='Select a year group')

        self.menu_year_group = tk.OptionMenu(frame_user_input, year_value, *year_groups)
        self.menu_year_group.grid(row=2, column=1, sticky='ew', pady=3)

        lbl_form_group = tk.Label(frame_user_input, text='Form group:')
        lbl_form_group.grid(row=3, column=0)
        
        form_value = tk.StringVar(frame_user_input, value='Select a form group')
        form_list = ['A', 'B', 'C', 'D', 'E', 'D', 'F']
        
        self.menu_form_group = tk.OptionMenu(frame_user_input, form_value, *form_list)
        self.menu_form_group.grid(row=3, column=1, sticky='ew', pady=3)

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


class StudentMenu(tk.Frame):
    """GUI menu for student access, provdies less options than teacher"""

    def __init__(self, parent, controller):
        """Initialise class values and create initial GUI elements"""
        
        # initialise frame 
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.config(bg='#ff0093')

        # gui creation
        # string var for student name, allows text to change
        self.student_name = tk.StringVar(self, value='Student Name')

        lbl_student_title = tk.Label(self, textvariable=self.student_name)
        lbl_student_title.pack(pady=5)

        frame_student_actions = tk.Frame(self)
        frame_student_actions.pack(pady=3)

        btn_school_sign_in = tk.Button(frame_student_actions, text='Sign into school', command='')
        btn_school_sign_in.grid(row=0, column=0, sticky='ew', pady=3, padx=3)

        btn_school_sign_out = tk.Button(frame_student_actions, text='Sign out of school', command='')
        btn_school_sign_out.grid(row=0, column=1, sticky='ew', pady=3, padx=3)

        btn_view_attendence = tk.Button(frame_student_actions, text='View sign in / out history', command='')
        btn_view_attendence.grid(row=1, column=0, sticky='ew', pady=3, padx= 3 )

        # may add function: 
        # btn_view_permissions = tk.Button(frame_stuent_actions, text='View user permissions', command='')

        btn_user_logout = tk.Button(self, text='Logout of program', command=lambda: self.logout())
        btn_user_logout.pack(pady=3)

    def student_configure(self, student_name):
        """Configures the StudentMenu to the logged in student"""
        self.student_name.set(value=student_name)

    def logout(self):
        """Logs out of sql database"""
        # self.controller.show_frame('Logout')
        # print(type(self).__name__)
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

        self.config(bg='#492852')

        frame_teacher_actions = tk.Frame(self)
        frame_teacher_actions.pack(pady=3)

        btn_manual_sign = tk.Button(frame_teacher_actions, text='Manual sign students', command='')
        btn_manual_sign.grid(row=2, column=0, sticky='ew', pady=3, padx=3)

        btn_search_attendence = tk.Button(frame_teacher_actions, text='View student history', command='')
        btn_search_attendence.grid(row=2, column=1, sticky='ew', pady=3, padx=3)

        btn_edit_student = tk.Button(frame_teacher_actions, text='Edit student info', command='')
        btn_edit_student.grid(row=3, column=0, sticky='ew', pady=3, padx=3)

        # may add function: 
        btn_view_permissions = tk.Button(frame_teacher_actions, text='View user permissions', command='')
        btn_view_permissions.grid(row=3, column=1, sticky='ew', pady=3, padx=3)

        # btn_user_logout = tk.Button(self, text='Logout of program', command=lambda: self.controller.show_frame('Logout'))
        # btn_user_logout.pack(pady=3)

    def teacher_configure(self, teacher_name):
        """Configure the TeacherMenu to the logged in student"""
        self.teacher_name.set(teacher_name)
    
    # def logout(self):
    #     # self.controller.show_frame('Logout')
    #     # print(type(self).__name__)
    #     class_name = type(self).__name__
    #     self.controller.frames['LogoutMenu'].set_calling_class(class_name)
    #     # self.controller.show_frame('LogoutMenu')



class LogoutMenu(tk.Frame):
    """Confirms whether user wants to logout"""

    def __init__(self, parent, controller):
        """Intialise class values and create intialise GUI elements"""

        tk.Frame.__init__(self, parent)
        self.controller = controller

        # gui creation

        lbl_logout_confirm_title = tk.Label(self, text='Are you sure you want to logout')
        lbl_logout_confirm_title.pack()

        logout_btn_frame = tk.Frame(self)
        logout_btn_frame.pack(fill='both', expand=True, pady=5)

        tk.Grid.columnconfigure(logout_btn_frame, 0, weight=1)
        tk.Grid.columnconfigure(logout_btn_frame, 1, weight=1)
        tk.Grid.rowconfigure(logout_btn_frame, 0, weight=1)

        self.btn_logout_confim = tk.Button(logout_btn_frame, text='Logout', command='')
        self.btn_logout_confim.grid(row=0, column=0, sticky='nsew', padx=5)

        self.btn_logout_cancel = tk.Button(logout_btn_frame, text='Cancel', command=lambda: self.controller.show_frame(self.caller))
        self.btn_logout_cancel.grid(row=0, column=1, sticky='nsew', padx=5)

    def set_calling_class(self, caller):
        self.caller = caller
        print(self.caller)

    def logout(self):
        """Logs out of sql database"""
        # log out of sql
        self.controller.show_frame('StartPage')


if __name__ == '__main__':
    
    app = Gui()
    app.minsize(800, 400)
    app.mainloop()
