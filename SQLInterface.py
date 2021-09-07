import sqlite3

from sqlite3 import Error


def create_connection(db_file):
    database_connect = None
    try:
        database_connect = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return database_connect


def create_table(connection, sql_command):
    try:
        cursor = connection.cursor()
        cursor.execute(sql_command)
    except Error as e:
        print(e)


def create_project(conn, project):

    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def create_task(conn, task):

    sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

    return cur.lastrowid


def update_task(conn, task):
    sql = ''' UPDATE tasks
                SET priority = ? ,
                    begin_date = ? ,
                    end_date = ?
                WHERE id = ?'''
    cursor = conn.cursor()
    cursor.execute(sql, task)
    conn.commit()


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def delete_task(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def delete_all_tasks(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM tasks'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                priority integer,
                                status_id integer NOT NULL,
                                project_id integer NOT NULL,
                                begin_date text NOT NULL,
                                end_date text NOT NULL,
                                FOREIGN KEY (project_id) REFERENCES projects (id)
                            );"""

conn = create_connection("test.db")
create_table(conn, sql_create_projects_table)
create_table(conn, sql_create_tasks_table)


project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30');
project_id = create_project(conn, project)

# tasks
task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01',
          '2015-01-02')
task_2 = ('Confirm with user about the top requirements', 1, 1, project_id,
          '2015-01-03', '2015-01-05')

# create tasks
# create_task(conn, task_1)
# create_task(conn, task_2)

update_task(conn, (2, '2015-01-04', '2015-01-06', 2))

print("1. Query task by priority:")
select_task_by_priority(conn, 2)

print("2. Query all tasks")
select_all_tasks(conn)

# delete_task(conn, 2); delete by ID
# delete_all_tasks(conn);
