'''Init, GUI construction'''

import logic
import tkinter as tk
from tkinter.constants import LEFT


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
        for F in (StartPage, TextLogin):
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

        lbl_title = tk.Label(self, text='Title')
        lbl_title.pack()
        self.btn_start_login = tk.Button(self, text='Login Page', command=lambda: self.controller.show_frame('TextLogin'))
        self.btn_start_login.pack()
        


class TextLogin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        lbl_page_title = tk.Label(self, text='Login')
        lbl_page_title.pack()
        self.input_frame = tk.Frame(self)
        self.input_frame.pack()
        
        lbl_username = tk.Label(self.input_frame, text='Username:')
        lbl_username.grid(column=0, row=0, pady=5)
        
        self.ent_username = tk.Entry(self.input_frame)
        self.ent_username.grid(column=1, row=0, pady=5)
        
        lbl_password = tk.Label(self.input_frame, text='Password:')
        lbl_password.grid(column=0, row=1, pady=5)
        
        self.ent_password = tk.Entry(self.input_frame)
        self.ent_password.grid(column=1, row=1, pady=5)
        self.btn_login = tk.Button(self, text='Login', command='')

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



if __name__ == '__main__':
    
    app = Gui()
    app.minsize(800, 400)
    app.mainloop()
