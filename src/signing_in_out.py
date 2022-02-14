"""Sign in and out of school + history"""

import logic
from main import tk, messagebox


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

        btn_cancel = tk.Button(self, text='Cancel', command=lambda: self.controller.show_frame(self.controller.default_menu))
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

        btn_cancel = tk.Button(self, text='Cancel', command=lambda: self.controller.show_frame(self.controller.default_menu))
        btn_cancel.pack(pady=(15, 20), padx=50, expand=True, fill='both')

    def start_sign_out(self):
        """"Start sign out"""
        if self.sign_value.get() == '':
            messagebox.showerror('Failure', 'Fill in the sign out reason')
        else: 
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

        btn_return = tk.Button(frame_menu, text='Return to menu', command=lambda: self.controller.show_frame(self.controller.default_menu))
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

    def clear_search_results(self):
        """Clears the list box of all entries"""

        self.list_sign_history.delete(0, tk.END)

    def view_history(self):
        """View all sign in / outs"""
        self.clear_search_results()
        history_list = logic.sign_history()
        for i in  history_list:
            i = list(i)
            # The length of sign out lists is 5, whereas sign in lists have a
            # a length of 4. Can tell the difference between lists
            if len(i) == 4:
                i.insert(0, 'Sign In')
                self.list_sign_history.insert(tk.END, '  ,  '.join(map(str, i)))
            elif len(i) == 5:
                i.insert(0, 'Sign Out')
                self.list_sign_history.insert(tk.END, '  ,  '.join(map(str, i)))