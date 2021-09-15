'''Init, GUI construction'''

import logic
import tkinter as tk
from tkinter.constants import COMMAND, LEFT


class Gui(tk.Tk):
    '''GUI for program'''

    def __init__(self, *args, **kwargs):
        '''Creates gui, a base frame, inits class frames'''
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, TextLogin, SignUp):
            frame = F(parent=container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.title("Sign System")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Switch to specified frame classs'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    '''Start page for program, offers sign in, quit buttons'''

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        lbl_title = tk.Label(self, text='Start Page:')
        lbl_title.pack(pady=10)
        self.btn_start_login = tk.Button(self, text='Login Page', command=lambda: self.controller.show_frame('TextLogin'))
        self.btn_start_login.pack(pady=3)

        
        self.btn_signup = tk.Button(self, text='Sign up', command=lambda: self.controller.show_frame('SignUp'))
        self.btn_signup.pack(pady=3)
        


class TextLogin(tk.Frame):

    def __init__(self, parent, controller):
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
        
        self.ent_password = tk.Entry(self.input_frame)
        self.ent_password.grid(column=1, row=1, pady=3)
        btn_login = tk.Button(self, text='Login', command='')
        btn_login.pack(pady=3)

        btn_retrun_start_page = tk.Button(self, text='Return to start page', command=lambda: self.controller.show_frame('StartPage'))
        btn_retrun_start_page.pack(pady=3)

    def login_check(self):
        '''Checks username and password'''
        input_username = self.ent_username.get()
        print(input_username)
        input_password = self.ent_password.get()
        print(input_username)
        if logic.check_login_creds(input_username, input_password):
            pass
        else:
            pass

class SignUp(tk.Frame):

    def __init__(self, parent, controller):
        '''Initialise class values and create GUI elements'''
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # gui creation
        lbl_signup_title = tk.Label(self, text='Sign up')
        lbl_signup_title.pack(pady=10)

        user_input_frame = tk.Frame(self)
        user_input_frame.pack()


        lbl_first_name = tk.Label(user_input_frame, text='First Name:')
        lbl_first_name.grid(row=0, column=0, pady=4)

        self.ent_first_name = tk.Entry(user_input_frame)
        self.ent_first_name.grid(row=0, column=1, pady=4)

        lbl_second_name = tk.Label(user_input_frame, text='Last name:')
        lbl_second_name.grid(row=1, column=0, pady=4)

        self.ent_second_name = tk.Entry(user_input_frame)
        self.ent_second_name.grid(row=1, column=1, pady=4)

        lbl_year_group = tk.Label(user_input_frame, text='Year group:')
        lbl_year_group.grid(row=2, column=0)

        year_groups = ['12', '13']
        year_value = tk.StringVar(user_input_frame, value='Select a year group')

        self.menu_year_group = tk.OptionMenu(user_input_frame, year_value, *year_groups)
        self.menu_year_group.grid(row=2, column=1, sticky='ew', pady=3)

        lbl_form_group = tk.Label(user_input_frame, text='Form group:')
        lbl_form_group.grid(row=3, column=0)
        
        form_value = tk.StringVar(user_input_frame, value='Select a form group')
        form_list = ['A', 'B', 'C', 'D', 'E', 'D', 'F']
        
        self.menu_form_group = tk.OptionMenu(user_input_frame, form_value, *form_list)
        self.menu_form_group.grid(row=3, column=1, sticky='ew', pady=3)

        lbl_username = tk.Label(user_input_frame, text='Username:')
        lbl_username.grid(row=4, column=0, pady=3)

        self.ent_username = tk.Entry(user_input_frame)
        self.ent_username.grid(row=4, column=1, pady=3)

        #<3 <3

        lbl_password = tk.Label(user_input_frame, text='Password:')
        lbl_password.grid(row=5, column=0, pady=3)

        self.ent_password = tk.Entry(user_input_frame, show='*')
        self.ent_password.grid(row=5, column=1, pady=3)

        lbl_password_repeat = tk.Label(user_input_frame, text='Repeat Password:')
        lbl_password_repeat.grid(row=6, column=0, pady=3)

        self.ent_password_repeat = tk.Entry(user_input_frame, show='*')
        self.ent_password_repeat.grid(row=6, column=1, pady=3)

        btn_confirm = tk.Button(self, text='Sign up', command='')
        btn_confirm.pack(pady=5)

        btn_return_start = tk.Button(self, text= 'Return to start page', command=lambda: self.controller.show_frame('StartPage'))
        btn_return_start.pack(pady=3)
        

if __name__ == '__main__':
    
    app = Gui()
    app.minsize(800, 400)
    app.mainloop()
