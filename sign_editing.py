"""Editing sign in and outs"""

from datetime import datetime
from tkinter import ttk

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

        self.entries = [] # List to store variables to .get() later

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
        hour_list = [f'{i:02}' for i in range(24)]
        hour_list.insert(0, '')
        # Create list of values to 60, single digits have an extra 0 on the
        # left.
        minute_second_list = [f'{i:02}' for i in range(60)]
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

        btn_clear_search_results = tk.Button(search_term_frame, text='Clear', command=lambda: self.clear_search_results())
        btn_clear_search_results.grid(row=8, column=0, columnspan=2, sticky='ew', pady=3)

        btn_return_main =tk.Button(search_term_frame, text='Return to main menu', command=lambda: self.controller.show_frame(self.controller.default_menu))
        btn_return_main.grid(row=9, column=0, columnspan=2, sticky='ew', pady=5)

        search_result_frame = tk.Frame(self, relief='groove', borderwidth=2)
        search_result_frame.pack(side='left', anchor='ne', fill='both', expand=True, padx=(0, 5), pady=(3, 5))

        lbl_format_explanation = tk.Label(search_result_frame,
                                          text='Order of elements: \n Sign '
                                               'ID, Date, Time, Student ID, '
                                               'Sign Out Type (If applicable)')
        lbl_format_explanation.pack()
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

        self.clear_search_results()

        if len(self.entries[3].get()) != 0:
            if not validation.date_format_check(self.entries[3].get()):
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


class EditSignSearch(SignSearch):

    def __init__(self, parent, controller):

        self.controller = controller
        SignSearch.__init__(self, parent, controller)

        self.btn_change_sign_search.destroy()

        frame_start_edit = tk.Frame(self.search_config_frame, relief='groove', borderwidth=2)
        frame_start_edit.pack(pady=3, expand=True, fill='both')

        btn_start_user_edit = tk.Button(frame_start_edit, text='Start edit', command=lambda: self.prepare_edit())
        btn_start_user_edit.pack(pady=3, expand=True, fill='both')

    def prepare_edit(self):
        """Get's info of selected user and passes it to the EditUser class"""

        line_selected = self.list_search_results.curselection()

        if len(line_selected) == 0:
            messagebox.showerror('Failure', 'Please select a sign before editing entry.')
        else:

            selected_user = self.list_search_results.get(line_selected[0], line_selected[0])[0]
            search_keys = ('sign_in_id', 'date', 'time', 'student_id')
            sign_info = {}
            for (key, value) in zip(search_keys, selected_user.split(', ')):
                sign_info[key] = value

            if len(sign_info) == 4:
                print(sign_info)
                self.controller.frames['EditSignIn'].fill_string_vars(sign_info)
                self.controller.show_frame('EditSignIn')
            else:
                pass


class EditSignIn(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.entries = []

        edit_values_frame = tk.Frame(self)
        edit_values_frame.pack()

        self.sign_in_id = tk.StringVar(edit_values_frame)

        lbl_sign_in_id = tk.Label(edit_values_frame, textvariable=self.sign_in_id)
        lbl_sign_in_id.grid(row=0, column=0, columnspan=2, sticky='nsew', pady=3)

        lbl_student_id = tk.Label(edit_values_frame, text='Student ID')
        lbl_student_id.grid(row=1, column=0, sticky='nsew', pady=3)

        self.student_id_value = tk.StringVar(edit_values_frame)
        self.entries.append(self.student_id_value)
        ent_student_id = tk.Entry(edit_values_frame, textvariable=self.student_id_value)
        ent_student_id.grid(row=1, column=1, sticky='nsew', pady=3)

        lbl_date = tk.Label(edit_values_frame, text='Date:')
        lbl_date.grid(row=2, column=0, sticky='nsew', pady=3)

        self.date = tk.StringVar(edit_values_frame)
        self.entries.append(self.student_id_value)
        ent_date = tk.Entry(edit_values_frame, textvariable=self.date)
        ent_date.grid(row=2, column=1, sticky='nsew', pady=3)

        lbl_time = tk.Label(edit_values_frame, text='Time:')
        lbl_time.grid(row=3, column=0, sticky='nsew', pady=3)

        self.time = tk.StringVar(self)
        self.entries.append(self.time)
        ent_time = tk.Entry(edit_values_frame, textvariable=self.time)
        ent_time.grid(row=3, column=1, sticky='nsew', pady=3)

        btn_confirm_edit = tk.Button(edit_values_frame, text='Confirm edit', command=lambda: self.edit_sign_in())
        btn_confirm_edit.grid(row=4, column=0, columnspan=2, sticky='nsew', pady=3)

        btn_delete_user = tk.Button(edit_values_frame, text='Delete', command=lambda: self.delete_sign_in())
        btn_delete_user.grid(row=5, column=0, columnspan=2, sticky='nsew', pady=3)

        btn_exit = tk.Button(edit_values_frame, text='Return to search:', command=lambda:self.controller.show_frame(self.controller.show_frame('EditSignSearch')))
        btn_exit.grid(row=6, column=0, columnspan=2, sticky='nsew', pady=3)

    def fill_string_vars(self, sign_in_info):
        
        self.sign_in_info = sign_in_info
        self.sign_in_id.set('Sign In ID: {}'.format(sign_in_info['sign_in_id']))
        self.student_id_value.set(sign_in_info['student_id'])
        self.date.set(sign_in_info['date'])
        self.time.set(sign_in_info['time'])

    def edit_sign_in(self):
        """Collects user inputs and edits the user's account"""

        edited_values = {}
        sign_in_id = self.sign_in_info['sign_in_id']
        # Tuple to hold dict keys
        account_dict_keys = ('student_id', 'date', 'time')

        for count, i in enumerate(self.entries):  # Get values and place in dictionary
                edited_values[account_dict_keys[count]] = i.get()

        logic.edit_sign_in(sign_in_id, edited_values)

    def delete_sign_in(self):
        """Delete the sign in entry from the database"""

        sign_in_id = self.sign_in_info['sign_in_id']
        logic.delete_sign_in(sign_in_id)
        self.controller.show_frame('EditSignSearch')

    