"""Searching users, and editing account details"""

import logic
from main import tk, messagebox


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
        title_frame.pack(fill='both', anchor='nw', pady=(3, 6))

        lbl_search_title = tk.Label(title_frame, text='User Search')
        lbl_search_title.pack()

        self.btn_change_sign_search = tk.Button(title_frame, text='Go to sign search', command=lambda: self.controller.show_frame('SignSearch'))
        self.btn_change_sign_search.pack(pady=3)

        search_term_frame = tk.Frame(self.search_config_frame, relief='groove', borderwidth=2)
        search_term_frame.pack(fill='both', anchor='nw')

        lbl_search_info = tk.Label(search_term_frame, text="Leave entries you don't want to search empty")
        lbl_search_info.grid(row=0, column=0,columnspan=2, sticky='nsew', pady=3)

        self.entries = [] # List to store variables to .get() later.

        lbl_id_search = tk.Label(search_term_frame, text='Student ID:')
        lbl_id_search.grid(row=1, column=0, sticky='nsew', pady=3)

        ent_id_search = tk.Entry(search_term_frame)
        ent_id_search.grid(row=1, column=1, sticky='nsew', pady=3)
        self.entries.append(ent_id_search)

        lbl_access_level_search = tk.Label(search_term_frame, text='Access Level:')
        lbl_access_level_search.grid(row=2, column=0, sticky='nsew', pady=3)

        self.access_value = tk.StringVar(search_term_frame)
        self.entries.append(self.access_value)
        # Access tiers that are available to the user.
        access_tiers = ['', 'student', 'teacher']

        menu_access_search = tk.OptionMenu(search_term_frame, self.access_value, *access_tiers)
        menu_access_search.config(width='17')
        menu_access_search.grid(row=2, column=1, sticky='nsew', pady=3)

        lbl_fname_search = tk.Label(search_term_frame, text='First name:')
        lbl_fname_search.grid(row=3, column=0, sticky='nsew', pady=3)

        ent_fname_search = tk.Entry(search_term_frame)
        ent_fname_search.grid(row=3, column=1, sticky='nsew', pady=3)
        self.entries.append(ent_fname_search)

        lbl_sec_name_search = tk.Label(search_term_frame, text='Second name:')
        lbl_sec_name_search.grid(row=4, column=0, sticky='nsew', pady=3)

        ent_sec_name_search = tk.Entry(search_term_frame)
        ent_sec_name_search.grid(row=4, column=1, sticky='nsew', pady=3)
        self.entries.append(ent_sec_name_search)

        lbl_year_search = tk.Label(search_term_frame, text='Year group:')
        lbl_year_search.grid(row=5, column=0, sticky='nsew', pady=3)

        self.year_value = tk.StringVar(search_term_frame, value='')
        self.entries.append(self.year_value)
        # Year groups that are avaiable to the user.
        year_list = ['','12', '13']

        menu_year_search = tk.OptionMenu(search_term_frame, self.year_value, *year_list)
        menu_year_search.config(width='17')
        menu_year_search.grid(row=5, column=1, sticky='nsew', pady=3)

        lbl_form_search = tk.Label(search_term_frame, text='Form group:')
        lbl_form_search.grid(row=6, column=0, sticky='nsew', pady=3)

        self.form_value = tk.StringVar(search_term_frame, value='')
        self.entries.append(self.form_value)
        # Form groups that are available to the user.
        form_list = ['', 'A', 'B', 'C', 'D', 'E', 'D', 'F']

        menu_form_search = tk.OptionMenu(search_term_frame, self.form_value, *form_list)
        menu_form_search.config(width='17')
        menu_form_search.grid(row=6, column=1, sticky='ew', pady=3)

        lbl_username_search = tk.Label(search_term_frame, text='Username:')
        lbl_username_search.grid(row=7, column=0, sticky='nsew', pady=3)

        ent_username_search = tk.Entry(search_term_frame)
        ent_username_search.grid(row=7, column=1, sticky='nsew', pady=3)
        self.entries.append(ent_username_search)

        # Buttons for searching, clearing, and exiting out of the menu.

        btn_begin_search = tk.Button(search_term_frame, text='Search', command=lambda: self.search_users())
        btn_begin_search.grid(row=8, column=0, columnspan=2, sticky='ew', pady=3)

        btn_clear_results = tk.Button(search_term_frame, text='Clear', command=lambda: self.clear_search_results())
        btn_clear_results.grid(row=9, column=0, columnspan=2, sticky='ew', pady=5)

        btn_return_main = tk.Button(search_term_frame, text='Return to main menu', command=lambda: self.controller.show_frame(self.controller.default_menu))
        btn_return_main.grid(row=10, column=0, columnspan=2, sticky='ew', pady=5)

        # Widgets where the search output is displayed. 

        search_result_frame = tk.Frame(self, relief='groove', borderwidth=2)
        search_result_frame.pack(side='left', anchor='ne', fill='both', expand=True, padx=(0, 5), pady=(3,5))

        lbl_format_explanation = tk.Label(search_result_frame, text='Order of elements: \n ID, Access Level, First Name, Second Name, Year Group, Form Group, Username, Password')
        lbl_format_explanation.pack()

        # Scroll bar which is assigned to list_search_results.
        scroll_sign_history = tk.Scrollbar(search_result_frame)
        scroll_sign_history.pack(side='right', fill='y', padx=(0,2))

        # Lists all of the search results.
        self.list_search_results = tk.Listbox(search_result_frame, yscrollcommand=scroll_sign_history.set)
        self.list_search_results.pack(side='left', fill='both', expand=True, padx=(2,2))

    def clear_search_results(self):
        """Clears the list box of all entries"""

        self.list_search_results.delete(0, tk.END)

    def search_users(self):
        """Searches using input terms from GUI"""

        self.clear_search_results()

        # Tuple to hold dict keys.
        search_keys = ('id', 'access_level', 'first_name', 'second_name', 'year_group',
                       'form_group', 'username', 'password')
        search_terms = {}  # Dictionary that stores the items to search by.

        # Iterate through the input widgets, and get the text currently inside them.
        for count, i in enumerate(self.entries):
            if (i.get()) == '':  # If input is empty, do not create dictionary entry.
                continue
            # If the input is not empty, add it to the dictionary.
            search_terms[search_keys[count]] = i.get()

        # Execute the database search
        search_results = logic.search_users(search_terms)
        
        # Add the results of the database search to the ouput listbox.
        for i in search_results:
            self.list_search_results.insert(tk.END, ', '.join(map(str, i)))


class EditSearchUsers(UserSearch):

    def __init__(self, parent, controller):
        """Inherit UserSerach, initialise class values and create GUI elements."""

        self.controller = controller
        UserSearch.__init__(self, parent, controller)

        # Destroy unneeded widgets left over from inhertiance.
        self.btn_change_sign_search.destroy()

        frame_start_edit = tk.Frame(self.search_config_frame, relief='groove', borderwidth=2)
        frame_start_edit.pack(pady=3, expand=True, fill='both')

        btn_start_user_edit = tk.Button(frame_start_edit, text='Start edit', command=lambda: self.prepare_edit())
        btn_start_user_edit.pack(pady=3, expand=True, fill='both')

    def prepare_edit(self):
        """Get's info of selected user and passes it to the EditUser class."""

        # Get the position of the line the cursor has clicked.
        line_selected = self.list_search_results.curselection()

        # If the user has not selected a line, show an error message.
        if len(line_selected) == 0:
            messagebox.showerror('Failure', 'Please select a user before editing entry.')
        else:
            # First to last, getting cursor value so first and last are the same.
            # The .get() returns a iterable with only 1 value, so [0] is used.
            selected_user = self.list_search_results.get(line_selected[0], line_selected[0])[0]
            # Search keys for dictionary.
            search_keys = ('id', 'access_level', 'first_name', 'second_name', 'year_group',
                           'form_group', 'username', 'password')
            user_info = {}
            # zip iterates through two iterables at once. It makes adding to dictionary easier.
            for (key, value) in zip(search_keys, selected_user.split(', ')):
                user_info[key] = value
            # Fill the edit menu with the values in the dictionary.
            self.controller.frames['EditUser'].fill_string_vars(user_info, 'EditSearchUsers')
            self.controller.show_frame('EditUser')  # Show edit menu.


class EditUser(tk.Frame):
    """Edit the selected user."""

    def __init__(self, parent, controller):
        """"Initialise class values and create GUI elements."""

        tk.Frame.__init__(self, parent)
        # Define user info in main init class before assigning 
        # it to value in a method.
        self.user_info = None
        self.controller = controller

        # GUI creation.

        lbl_edit_title = tk.Label(self, text='Edit Table Entry')
        lbl_edit_title.pack()

        # Wigets for editing the user's information

        self.frame_edit_terms = tk.Frame(self)
        self.frame_edit_terms.pack()

        # List to store the .get()-able widgets.
        self.entries = []

        self.account_id = tk.StringVar(self.frame_edit_terms)
        lbl_id = tk.Label(self.frame_edit_terms, textvariable=self.account_id)
        lbl_id.grid(row=0, column=0, columnspan=2, pady=3)

        lbl_access_level = tk.Label(self.frame_edit_terms, text='Access Level:')
        lbl_access_level.grid(row=1, column=0, pady=3)

        self.access_value = tk.StringVar(self.frame_edit_terms)
        self.entries.append(self.access_value)

        # Access values to choose from.
        access_values = ['teacher', 'student']
        
        menu_access_value = tk.OptionMenu(self.frame_edit_terms, self.access_value, *access_values)
        menu_access_value.config(width='20')
        menu_access_value.grid(row=1, column=1, pady=3)

        lbl_fname = tk.Label(self.frame_edit_terms, text='First name:')
        lbl_fname.grid(row=2, column=0, pady=3)

        self.fname_value = tk.StringVar(self.frame_edit_terms)
        self.entries.append(self.fname_value)
        ent_fname = tk.Entry(self.frame_edit_terms, textvariable=self.fname_value)
        ent_fname.grid(row=2, column=1, pady=3, sticky='nsew')

        lbl_sname = tk.Label(self.frame_edit_terms, text='Second name:')
        lbl_sname.grid(row=3, column=0, pady=3)

        self.sname_value = tk.StringVar(self.frame_edit_terms)
        self.entries.append(self.sname_value)
        ent_sname = tk.Entry(self.frame_edit_terms, textvariable=self.sname_value)
        ent_sname.grid(row=3, column=1, pady=3, sticky='nsew')

        lbl_year_group = tk.Label(self.frame_edit_terms, text='Year group:')
        lbl_year_group.grid(row=4, column=0, pady=3)

        self.year_group_value = tk.StringVar(self.frame_edit_terms)
        self.entries.append(self.year_group_value)
        
        # Year values to choose from.
        year_values = ['12', '13']
        menu_year_group = tk.OptionMenu(self.frame_edit_terms, self.year_group_value, *year_values)
        menu_year_group.config(width='20')
        menu_year_group.grid(row=4, column=1, pady=3)

        lbl_form_group = tk.Label(self.frame_edit_terms, text='Form group:')
        lbl_form_group.grid(row=5, column=0, pady=3)

        self.form_group_value = tk.StringVar(self.frame_edit_terms)
        self.entries.append(self.form_group_value)

        # Form values to choose from.
        form_values = ['A', 'B', 'C', 'D', 'E', 'F']
        menu_form_group = tk.OptionMenu(self.frame_edit_terms, self.form_group_value, *form_values)
        menu_form_group.config(width='20')
        menu_form_group.grid(row=5, column=1, pady=3)

        lbl_username = tk.Label(self.frame_edit_terms, text='Username:')
        lbl_username.grid(row=6, column=0, pady=3)

        self.username_value = tk.StringVar(self.frame_edit_terms)
        self.entries.append(self.username_value)
        ent_username = tk.Entry(self.frame_edit_terms, textvariable=self.username_value)
        ent_username.grid(row=6, column=1, pady=3, sticky='nsew')

        lbl_password = tk.Label(self.frame_edit_terms, text='Password')
        lbl_password.grid(row=7, column=0, pady=3)

        self.password_value = tk.StringVar(self.frame_edit_terms)
        self.entries.append(self.password_value)
        ent_password = tk.Entry(self.frame_edit_terms, textvariable=self.password_value)
        ent_password.grid(row=7, column=1, pady=3, sticky='nsew')

        # Buttons

        btn_confirm_edit = tk.Button(self.frame_edit_terms, text='Confirm edit', command=lambda: self.edit_account())
        btn_confirm_edit.grid(row=8, column=0, columnspan=2, pady=3, sticky='nsew')

        btn_delete_user = tk.Button(self.frame_edit_terms, text='Delete', command=lambda: self.delete_user())
        btn_delete_user.grid(row=9, column=0, columnspan=2, pady=3, sticky='nsew')

        btn_exit = tk.Button(self.frame_edit_terms, text='Cancel', command=lambda:self.controller.show_frame(self.caller))
        btn_exit.grid(row=10, column=0, columnspan=2, pady=3, sticky='nsew')

    def fill_string_vars(self, user_info, caller):
        """Fill string variables with selected user"""

        self.user_info = user_info
        self.caller = caller
        # Setting string var values.
        self.account_id.set('Account ID: {}'.format(user_info['id']))
        self.access_value.set(user_info['access_level'])
        self.fname_value.set(user_info['first_name'])
        self.sname_value.set(user_info['second_name'])
        self.year_group_value.set(user_info['year_group'])
        self.form_group_value.set(user_info['form_group'])
        self.username_value.set(user_info['username'])
        self.password_value.set(user_info['password'])

    def edit_account(self):
        """Collects user inputs and edits the user's account"""

        edited_values = {}
        user_id = self.user_info['id']
        # Tuple to hold dict keys
        account_dict_keys = ('access_level', 'first_name', 'second_name',
                             'year_group', 'form_group', 'username', 'password')

        # Check that user has sufficient permissions to change their access level.
        if self.access_value.get() == 'teacher' and self.user_info['access_level'] == 'student' and self.caller == 'StudentMenu':
            messagebox.showerror('Insufficient Permissions', 'Students cannot change their permissions to teacher level.')

        # If the user has sufficient permissions, commit the edit changes to the database. 
        else:
            for count, i in enumerate(self.entries):  # Get values and place in dictionary.
                if count <= 3:  # Converts first and second name to lowercase
                    edited_values[account_dict_keys[count]] = i.get().lower()
                else:  # Rest of values are not converted to lowercase.
                    edited_values[account_dict_keys[count]] = i.get()
            logic.edit_user(user_id, edited_values)  # Write to the database

    def delete_user(self):
        """Deletes the user defined in the instance's user_info['id']."""

        user_id = self.user_info['id']
        logic.delete_user(user_id)
        self.controller.show_frame('EditSearchUsers')
