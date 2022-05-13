"""Editing sign in and outs"""

from datetime import datetime
from tkinter import Y, ttk

import logic
import validation
from main import tk, messagebox


class SignSearch(tk.Frame):
    """Search for sign in / outs by ID, date, and time"""

    def __init__(self, parent, controller):
        """"Initialise class values and creates GUI elements"""

        tk.Frame.__init__(self, parent)
        self.controller = controller

        # GUI creation
        # Configuring the search with terms.

        self.search_config_frame = tk.Frame(self)
        self.search_config_frame.pack(side='left', anchor='nw', padx=10)

        title_frame = tk.Frame(self.search_config_frame, relief='groove', borderwidth=2)
        title_frame.pack(fill='both', anchor='nw', pady=(3, 6))

        lbl_search_title = tk.Label(title_frame, text='Sign Search')
        lbl_search_title.pack()

        self.btn_change_sign_search = tk.Button(title_frame, text='Go to user search', command=lambda: self.controller.show_frame('UserSearch'))
        self.btn_change_sign_search.pack(pady=3)

        search_term_frame = tk.Frame(self.search_config_frame, relief='groove', borderwidth=2)
        search_term_frame.pack(fill='both', anchor='nw')

        self.entries = []  # List to store Entries and StringVars to .get() later

        lbl_sign_in_out = tk.Label(search_term_frame, text='Sign type:')
        lbl_sign_in_out.grid(row=0, column=0, sticky='nsew', pady=(5, 3))

        self.sign_value = tk.StringVar(search_term_frame, value='Both')
        sign_types = ['Both', 'Sign in', 'Sign out']

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

        lbl_sign_out_type = tk.Label(search_term_frame, text='Sign out type:')
        lbl_sign_out_type.grid(row=3, column=0, sticky='nsew', pady=3)

        sign_out_value = tk.StringVar(search_term_frame, value='')
        self.entries.append(sign_out_value)
        sign_out_list = ['', 'Going home', 'Breaktime', 'Lunchtime']

        menu_sign_out_type = tk.OptionMenu(search_term_frame, sign_out_value,
                                           *sign_out_list)
        menu_sign_out_type.config(width='17')
        menu_sign_out_type.grid(row=3, column=1, sticky='ew', pady=3)

        lbl_date_search = tk.Label(search_term_frame, text='Date:\n(format YYYY-MM-DD)')
        lbl_date_search.grid(row=4, column=0, sticky='nsew', pady=3)

        ent_date_search = tk.Entry(search_term_frame)
        self.entries.append(ent_date_search)
        ent_date_search.grid(row=4, column=1, sticky='nsew', pady=3)

        # List of all possible hours.
        # Create list of values to 24, single digits have an extra 0 on the
        # left.
        hour_list = [f'{i:02}' for i in range(24)]
        # Insert a 0 to allow the user to leave the time blank
        hour_list.insert(0, '')

        # List of all possible minutes.
        # Create list of values to 60, single digits have an extra 0 on the
        # left.
        minute_second_list = [f'{i:02}' for i in range(60)]
        minute_second_list.insert(0, '')

        lbl_time_from = tk.Label(search_term_frame, text='From time:')
        lbl_time_from.grid(row=5, column=0, sticky='nsew', pady=3)

        # Frame to store the from time Optionboxes and StringVars.
        frame_from_time = tk.Frame(search_term_frame)
        frame_from_time.grid(row=5, column=1, sticky='nsew', pady=3)

        self.from_time = []  # List to manage .get()s easier.
        from_hour_value = tk.StringVar(frame_from_time, value='')
        from_minute_value = tk.StringVar(frame_from_time, value='')
        from_second_value = tk.StringVar(frame_from_time, value='')
        # Add the string vars to a list to .get() later
        self.from_time.extend((from_hour_value, from_minute_value,
                               from_second_value))

        # Explains how to format the time.
        lbl_time_format = tk.Label(frame_from_time, text='HH:MM:SS')
        lbl_time_format.grid(row=0, column=0, columnspan=3, sticky='nsew')

        # Time from
        combo_hour_from = ttk.Combobox(frame_from_time, textvariable=from_hour_value, values=hour_list, state='readonly', width=3)
        combo_hour_from.grid(row=1, column=0, sticky='nsew', padx=2)
        combo_minute_from = ttk.Combobox(frame_from_time, textvariable=from_minute_value, values=minute_second_list, state='readonly', width=3)
        combo_minute_from.grid(row=1, column=1, sticky='nsew', padx=2)
        combo_second_from = ttk.Combobox(frame_from_time, textvariable=from_second_value, values=minute_second_list, state='readonly', width=3)
        combo_second_from.grid(row=1, column=2, sticky='nsew', padx=2)

        # Frame to store the to time Optionboxes and StringVars.
        frame_to_time = tk.Frame(search_term_frame)
        frame_to_time.grid(row=6, column=1, sticky='nsew', pady=3)

        lbl_time_to = tk.Label(search_term_frame, text='To time:')
        lbl_time_to.grid(row=6, column=0, sticky='nsew', pady=3)

        self.to_time = []  # List to manage .get()s easier.
        to_hour_value = tk.StringVar(frame_to_time, value='')
        to_minute_value = tk.StringVar(frame_to_time, value='')
        to_second_value = tk.StringVar(frame_to_time, value='')
        # Add the string vars to a list to .get() later
        self.to_time.extend((to_hour_value, to_minute_value, to_second_value))

        # Time to, together with time from, they make a range of times to search in.
        combo_hour_to = ttk.Combobox(frame_to_time, textvariable=to_hour_value, values=hour_list, width=3, state='readonly')
        combo_hour_to.grid(row=0, column=0, sticky='nsew', padx=2)
        combo_minute_to = ttk.Combobox(frame_to_time, textvariable=to_minute_value, values=minute_second_list, state='readonly', width=3)
        combo_minute_to.grid(row=0, column=1, sticky='nsew', padx=2)
        combo_second_to = ttk.Combobox(frame_to_time, textvariable=to_second_value, values=minute_second_list, state='readonly', width=3)
        combo_second_to.grid(row=0, column=2, sticky='nsew', padx=2)

        # Buttons to manage search

        btn_begin_search = tk.Button(search_term_frame, text='Search', command=lambda: self.start_sign_search())
        btn_begin_search.grid(row=7, column=0, columnspan=2, sticky='ew', pady=3)

        btn_clear_search_results = tk.Button(search_term_frame, text='Clear', command=lambda: self.clear_search_results())
        btn_clear_search_results.grid(row=8, column=0, columnspan=2, sticky='ew', pady=3)

        btn_return_main =tk.Button(search_term_frame, text='Return to main menu', command=lambda: self.controller.show_frame(self.controller.default_menu))
        btn_return_main.grid(row=9, column=0, columnspan=2, sticky='ew', pady=5)

        # Result of the search

        search_result_frame = tk.Frame(self, relief='groove', borderwidth=2)
        search_result_frame.pack(side='left', anchor='ne', fill='both', expand=True, padx=(0, 5), pady=(3, 5))

        lbl_format_explanation = tk.Label(search_result_frame,
                                          text='Order of elements: \n Sign '
                                               'ID, Date, Time, Student ID, '
                                               'Sign Out Type (If applicable)')
        lbl_format_explanation.pack()

        # Scroll bar for the listbox
        scroll_sign_results = tk.Scrollbar(search_result_frame)
        scroll_sign_results.pack(side='right', fill='y', padx=(0,2))

        self.list_search_results = tk.Listbox(search_result_frame, yscrollcommand=scroll_sign_results.set)
        self.list_search_results.pack(side='left', fill='both', expand=True,
                                      padx=(2, 2))

    def clear_search_results(self):
        """Clears the list box of all entries"""

        self.list_search_results.delete(0, tk.END)

    def start_sign_search(self):
        """Start sign search with defined parameters"""

        # Clear the list box.
        self.clear_search_results()
        
        # Check if date box was populated.
        if len(self.entries[3].get()) != 0:
            # Check if date exists when using it in a search. Raise error if the date does not exist.
            if not validation.date_format_check(self.entries[3].get()):
                messagebox.showerror('Failure', 'Date format incorrect or non-existent date')
                return

        # Get whether the user selected to search sign ins, sign outs, or both.
        # Then call the respective function.
        sign_in_or_out = self.sign_value.get().lower()
        if sign_in_or_out == '' or sign_in_or_out == 'both':
            # If both is selected, sign out and sign are called and their 
            # results are combined.
            self.search_signs('sign out')
            self.search_signs('sign in')
        else:
            # Otherwise, only the selected database in 'sign_in_or_out' is searched.
            self.search_signs(sign_in_or_out)

    def search_signs(self, sign_in_or_out):
        """"Search and show sign ins"""

        # Tuple to hold dict keys.
        search_keys = ('sign_out_id', 'student_id', 'sign_out_type', 'date')
        search_terms = {}

        for count, i in enumerate(self.entries):
            if (i.get()) == '':  # If search term empty, do not include in dict.
                continue
            search_terms[search_keys[count]] = i.get()  # Add to dict if the search term is not empty.

        # If time is empty, skip entering time into dict.
        if '' not in [i.get() for i in self.to_time] and '' not in [t.get() for t in self.from_time]:

            # Create strings of the to and from times.
            from_time = ':'.join([i.get() for i in self.from_time])
            to_time = ':'.join([i.get() for i in self.to_time])

            # Convert the strings into time types, allowing for time comparisons.
            dt_from_time = datetime.strptime(from_time, '%H:%M:%S').time()
            dt_to_time = datetime.strptime(to_time, '%H:%M:%S').time()

            # Compares two times. Can't have a time range between times with a
            # negative difference. Example, Can't have 150 <= x <= 130.
            if dt_to_time <= dt_from_time:
                messagebox.showerror('Error', 'From is greater than to time')
                return
            time_tuple = (from_time, to_time)  # Add times to tuple.
            # Perform the sign search with the time search.
            search_results = logic.search_signs(sign_in_or_out, search_terms, time_tuple)
        else:

            # Perform the sign search without the time search.
            search_results = logic.search_signs(sign_in_or_out, search_terms)

        # Add search results to result listbox.
        for i in search_results:
            self.list_search_results.insert(tk.END, ', '.join(map(str, i)))


class EditSignSearch(SignSearch):
    """Menu that allows user to select sign in / out entry to edit"""

    def __init__(self, parent, controller):

        self.controller = controller
        # Inheriting the SignSearch class, don't have to write all of the SignSearch class again.
        SignSearch.__init__(self, parent, controller)

        self.btn_change_sign_search.destroy()  # Button inherited through SignSearch is not required, deletes it.

        # Adding required buttons which were not already in SignSearch
        # Button to access the edit menu

        frame_start_edit = tk.Frame(self.search_config_frame, relief='groove', borderwidth=2)
        frame_start_edit.pack(pady=3, expand=True, fill='both')

        btn_start_sign_edit = tk.Button(frame_start_edit, text='Start edit', command=lambda: self.prepare_edit())
        btn_start_sign_edit.pack(pady=3, expand=True, fill='both')

    def prepare_edit(self):
        """Get's info of selected user and passes it to the EditSign class"""

        # Get the position of the line the user clicked on.
        line_selected = self.list_search_results.curselection()


        # If the user has not selected a line, show an error message.
        if len(line_selected) == 0:
            messagebox.showerror('Failure', 'Please select a sign before editing entry.')

        else:
            # The arguments are to select the first and last values in the listbox, only want to get the cursor value so first and last are the same.
            # The .get() returns an iterable with only 1 value, so [0] is used.
            selected_sign = self.list_search_results.get(line_selected[0], line_selected[0])[0]

            # Defining dict keys for a sign in or out. Sign in and outs require different keys, so if an if statement is used.
            if len(selected_sign.split(', ')) == 4:  # Dict keys for a sign in.
                # Tuple of dictionary keys for sign in search dictionary. Allows the function to identify what each variable is in the database.
                sign_dict_keys = ('sign_in_id', 'date', 'time', 'student_id')
            else:  # Tuple of dictionary keys for sign out search dictionary. Allows the function to identify what each variable is in the database.
                sign_dict_keys = ('sign_out_id', 'date', 'time', 'student_id', 'sign_out_type')


            # Dictionary that will contain the selected sign in / outs information. Will be passed into edit function to populate the menu
            sign_info = {}

            # Iterates through the entry box's values and their names at the
            # same time. zip iterates through two iterables at once. It makes adding to dictionary faster
            for (key, value) in zip(sign_dict_keys, selected_sign.split(', ')):
                sign_info[key] = value

            if len(sign_info) == 4:  # Menus to show and populate if the selected option is a sign in.
                
                # Populate edit menu boxes
                self.controller.frames['EditSignIn'].fill_string_vars(sign_info)
                # Show edit meun
                self.controller.show_frame('EditSignIn')
            else:  # Menus to show and populate if the selected option is a sign out.
                
                # Populate edit menu boxes
                self.controller.frames['EditSignOut'].fill_string_vars(sign_info)
                # Show edit menu
                self.controller.show_frame('EditSignOut')


class EditSignIn(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.entries = []  # List of entries make .get() easier.

        # Frame contains the boxes that edit the sign in entry.
        edit_values_frame = tk.Frame(self)
        edit_values_frame.pack()

        # Displays the sign in's ID.
        self.sign_in_id = tk.StringVar(edit_values_frame)
        # Label to prevent users from editing the value. IDs are uneditable as the user may overwrite other entries.
        lbl_sign_in_id = tk.Label(edit_values_frame, textvariable=self.sign_in_id)
        lbl_sign_in_id.grid(row=0, column=0, columnspan=2, sticky='nsew', pady=3)

        lbl_student_id = tk.Label(edit_values_frame, text='Student ID:')
        lbl_student_id.grid(row=1, column=0, sticky='nsew', pady=3)

        self.student_id_value = tk.StringVar(edit_values_frame)
        self.entries.append(self.student_id_value)
        ent_student_id = tk.Entry(edit_values_frame, textvariable=self.student_id_value)
        ent_student_id.grid(row=1, column=1, sticky='nsew', pady=3)

        lbl_date = tk.Label(edit_values_frame, text='Date:')
        lbl_date.grid(row=2, column=0, sticky='nsew', pady=3)

        self.date_value = tk.StringVar(edit_values_frame)
        self.entries.append(self.date_value)
        ent_date = tk.Entry(edit_values_frame, textvariable=self.date_value)
        ent_date.grid(row=2, column=1, sticky='nsew', pady=3)

        lbl_time = tk.Label(edit_values_frame, text='Time:')
        lbl_time.grid(row=3, column=0, sticky='nsew', pady=3)

        self.time_value = tk.StringVar(self)
        self.entries.append(self.time_value)
        ent_time = tk.Entry(edit_values_frame, textvariable=self.time_value)
        ent_time.grid(row=3, column=1, sticky='nsew', pady=3)

        btn_confirm_edit = tk.Button(edit_values_frame, text='Confirm edit', command=lambda: self.edit_sign_in())
        btn_confirm_edit.grid(row=4, column=0, columnspan=2, sticky='nsew', pady=3)

        btn_delete_user = tk.Button(edit_values_frame, text='Delete', command=lambda: self.delete_sign_in())
        btn_delete_user.grid(row=5, column=0, columnspan=2, sticky='nsew', pady=3)

        btn_exit = tk.Button(edit_values_frame, text='Return to search:', command=lambda: self.controller.show_frame('EditSignSearch'))
        btn_exit.grid(row=6, column=0, columnspan=2, sticky='nsew', pady=3)

    def fill_string_vars(self, sign_in_info):

        self.sign_in_info = sign_in_info

        # Fill in StringVars with the passed dictionary's values by the key's assigned.
        self.sign_in_id.set('Sign In ID: {}'.format(self.sign_in_info['sign_in_id']))
        self.student_id_value.set(sign_in_info['student_id'])
        self.date_value.set(sign_in_info['date'])
        self.time_value.set(sign_in_info['time'])

    def edit_sign_in(self):
        """Collects user inputs and edits the user's account"""

        # Checks if date exists and that it's in the correct format
        if not validation.date_format_check(self.date_value.get()):
            messagebox.showerror('Failure', 'Date format incorrect or non-existent date')
            return

        # Checks that the time exists and that it's in the correct format
        if not validation.time_format_check(self.time_value.get()):
            messagebox.showerror('Failure', 'Time format incorrect or non-existent time')
            return

        edited_values = {}
        sign_in_id = self.sign_in_info['sign_in_id']
        # Tuple to hold dict keys. Dict keys used to assign the edited values labels. 
        # Without them values would have to be edited through order, which could cause problems as an incorrectly ordered list
        # would change the wrong values, e.g date being set to name.
        sign_in_edited_dict_keys = ('student_id', 'date', 'time')

        for count, i in enumerate(self.entries):  # Get values and place in dictionary
                edited_values[sign_in_edited_dict_keys[count]] = i.get()
        
        # Edit the sign in with the specified ID
        logic.edit_sign_in(sign_in_id, edited_values)

    def delete_sign_in(self):
        """Delete the sign in entry from the database"""

        sign_in_id = self.sign_in_info['sign_in_id']
        # Delete the sign in with the specified ID
        logic.delete_sign_in(sign_in_id)
        # Return to the search menu after deleting the entry.
        self.controller.show_frame('EditSignSearch')


class EditSignOut(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Frame contains the boxes that edit the sign out entry.
        edit_values_frame = tk.Frame(self)
        edit_values_frame.pack()

        # Displays the sign out's ID.
        self.sign_out_id = tk.StringVar(edit_values_frame)
        # Label used to prevent users from editing the value. IDs are uneditable as the user may overwrite other entries.
        lbl_sign_out_id = tk.Label(edit_values_frame, textvariable=self.sign_out_id)
        lbl_sign_out_id.grid(row=0, column=0, columnspan=2)

        lbl_student_id = tk.Label(edit_values_frame, text='Sign Out ID:')
        lbl_student_id.grid(row=1, column=0, sticky='nsew', pady=3)

        self.entries = []

        self.student_id_value = tk.StringVar(edit_values_frame)
        self.entries.append(self.student_id_value)
        ent_student_id = tk.Entry(edit_values_frame, textvariable=self.student_id_value)
        ent_student_id.grid(row=1, column=1, sticky='nsew', pady=3)

        lbl_date_value = tk.Label(edit_values_frame, text='Date:')
        lbl_date_value.grid(row=2, column=0, stick='nsew', pady=3)

        self.date_value = tk.StringVar(edit_values_frame)
        self.entries.append(self.date_value)
        ent_date_value = tk.Entry(edit_values_frame, textvariable=self.date_value)
        ent_date_value.grid(row=2, column=1, sticky='nsew', pady=3)

        lbl_time = tk.Label(edit_values_frame, text='Time:')
        lbl_time.grid(row=3, column=0, sticky='nsew', pady=3)

        self.time_value = tk.StringVar(edit_values_frame)
        self.entries.append(self.time_value)
        ent_time_value = tk.Entry(edit_values_frame, textvariable=self.time_value)
        ent_time_value.grid(row=3, column=1, sticky='nsew', pady=3)

        lbl_sign_out_type = tk.Label(edit_values_frame, text='Sign out type:')
        lbl_sign_out_type.grid(row=4, column=0, sticky='nsew', pady=3)

        self.sign_out_type = tk.StringVar(edit_values_frame)
        self.entries.append(self.sign_out_type)
        sign_out_types = ['Breaktime', 'Lunchtime', 'Going home']

        menu_sign_out_type = tk.OptionMenu(edit_values_frame, self.sign_out_type, *sign_out_types)
        menu_sign_out_type.config(width=17)
        menu_sign_out_type.grid(row=4, column=1)

        btn_confirm_edit = tk.Button(edit_values_frame, text='Confirm edit', command=lambda: self.edit_sign_out())
        btn_confirm_edit.grid(row=5, column=0, columnspan=2, sticky='nsew', pady=3)

        btn_delete_user = tk.Button(edit_values_frame, text='Delete', command=lambda: self.delete_sign_out())
        btn_delete_user.grid(row=6, column=0, columnspan=2, sticky='nsew', pady=3)

        btn_exit = tk.Button(edit_values_frame, text='Return to search:', command=lambda: self.controller.show_frame('EditSignSearch'))
        btn_exit.grid(row=7, column=0, columnspan=2, sticky='nsew', pady=3)

    def fill_string_vars(self, sign_out_info):

        # Fill in the StringVars with the passed dictionary's values.
        self.sign_out_info = sign_out_info
        self.sign_out_id.set('Sign Out ID: {}'.format(sign_out_info['sign_out_id']))
        self.student_id_value.set(sign_out_info['student_id'])
        self.date_value.set(sign_out_info['date'])
        self.time_value.set(sign_out_info['time'])
        self.sign_out_type.set(sign_out_info['sign_out_type'])

    def edit_sign_out(self):
        """Collects user inputs and edits the user's account"""

        # Checks if the date exists and that it's in the correct format
        if not validation.date_format_check(self.date_value.get()):
            messagebox.showerror('Failure', 'Date format incorrect or non-existent date')
            return

        # Checks if the time exists and that it's in the correct format
        if not validation.time_format_check(self.time_value.get()):
            messagebox.showerror('Failure', 'Time format incorrect or non-existent time')
            return

        edited_values = {}
        sign_out_id = self.sign_out_info['sign_out_id']
        # Tuple to hold dict keys
        account_dict_keys = ('student_id', 'date', 'time', 'sign_out_type')

        for count, i in enumerate(self.entries):  # Get values and place in dictionary
                edited_values[account_dict_keys[count]] = i.get()

        # Edit the sign out with the specified ID
        logic.edit_sign_out(sign_out_id, edited_values)

    def delete_sign_out(self):
        """Delete the sign in entry from the database"""

        sign_out_id = self.sign_out_info['sign_out_id']
        # Delete the sign out with the specified ID
        logic.delete_sign_out(sign_out_id)
        # Return to the search menu after deleting the entry.
        self.controller.show_frame('EditSignSearch')

