"""Account processes: logging in, signing up, logout"""

from main import tk, messagebox
import logic

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

        self.entries = []  # Entries, StringVars stored in list for easier .get()

        lbl_first_name = tk.Label(frame_user_input, text='First Name:')
        lbl_first_name.grid(row=0, column=0, pady=3)

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
        print(create_user_result)
        if create_user_result == True:
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
            messagebox.showerror('Failure', 'Incorrect username or password / No accounts created')
        else:
            account_info = {}
            account_dict_keys = ('id', 'access_level', 'first_name',
                                 'second_name', 'year_group',
                                 'form_group', 'username', 'password')

            for count, i in enumerate(login_result[1][0]):
                account_info[account_dict_keys[count]] = i

            print(account_info)
            self.controller.set_session_id(account_info['id'], account_info)
            print(self.controller.session_id)
            print(self.controller.default_menu)

            if account_info['access_level'] == 'student':
                self.controller.frames['StudentMenu'].user_configure(account_info)
                self.controller.show_frame('StudentMenu')
            else:
                self.controller.frames['TeacherMenu'].user_configure(account_info)
                self.controller.show_frame('TeacherMenu')


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

        self.btn_logout_cancel = tk.Button(logout_btn_frame, text='Cancel', command=lambda: self.controller.show_frame(self.controller.default_menu))
        self.btn_logout_cancel.grid(row=0, column=1, sticky='nsew', padx=(5, 25), pady=(6, 5))

    def logout(self):
        """Logs out of sql database"""

        # Resetting pages clears all entry boxes and inputs. Therefore, the new
        # user cannot access the previous person's inputs. Moreover, it resets 
        # all class attributes
        self.controller.reset_pages()