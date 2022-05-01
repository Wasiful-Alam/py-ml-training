import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import Connection
import typing as t


DB_FILE_PATH = "data/db/py-sqlite.db"


def create_db(db_file: str) -> None:
    """create a database connection to a SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


create_db(DB_FILE_PATH)


def create_connection(db_file: str) -> t.Union[None, Connection]:
    """create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_table(db_file: str, create_table_str: str) -> None:
    """

    :param db_file:
    :param create_table_str: Ex: CREATE TABLE ...
    :return:
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute(create_table_str)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()


create_project_table_str = """CREATE TABLE IF NOT EXISTS projects (
    project_id   INTEGER PRIMARY KEY,
    name TEXT    NOT NULL,
    begin_date TEXT    NOT NULL,
    end_date TEXT    NOT NULL
);"""

create_task_table_str = """
CREATE TABLE IF NOT EXISTS tasks (
    task_id        INTEGER PRIMARY KEY,
    name      TEXT    NOT NULL,
    completed      INTEGER NOT NULL,
    start_date     TEXT,
    completed_date TEXT,
    project_id     INTEGER NOT NULL,
    FOREIGN KEY (
        project_id
    )
    REFERENCES projects (project_id) ON UPDATE CASCADE
                                     ON DELETE CASCADE
);
"""

create_table(db_file=DB_FILE_PATH, create_table_str="""DROP TABLE IF EXISTS tasks;""")
create_table(db_file=DB_FILE_PATH, create_table_str="""DROP TABLE IF EXISTS projects;""")
create_table(db_file=DB_FILE_PATH, create_table_str=create_project_table_str)
create_table(db_file=DB_FILE_PATH, create_table_str=create_task_table_str)


def create_project(conn: Connection, project: tuple) -> str:
    """
    Create a new project into the projects table
    :param conn:
    :param project: Example: "myproject, 2020-12-01, 2020-12-03"
    :return: project id
    """
    sql = """ INSERT INTO projects(project_name,begin_date,end_date)
              VALUES(?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


PROJECT = ("Cool App with SQLite & Python", "2015-01-01", "2015-01-30")
CONNECTION = create_connection(DB_FILE_PATH)
project_id = create_project(CONNECTION, PROJECT)
print(f"Created project ID is: {project_id}")


def create_task(conn: CONNECTION, task: tuple) -> str:
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = """ INSERT INTO tasks(name,completed,project_id,start_date,completed_date)
              VALUES(?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

    return cur.lastrowid


TASK_1 = ("Analyze the requirements of the app", 0, project_id, "2015-01-01", "")
TASK_2 = (
    "Confirm with user about the top requirements",
    0,
    project_id,
    "2015-01-03",
    "",
)
task_id_1 = create_task(CONNECTION, TASK_1)
print(f"Task created with ID: {task_id_1}")
task_id_2 = create_task(CONNECTION, TASK_2)
print(f"Task created with ID: {task_id_2}")


def update_task(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = """ UPDATE tasks
              SET completed =  ? ,
                  completed_date =  ?
              WHERE task_id =  ?"""
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()


update_task(CONNECTION, (1, "2015-01-03", 2))


def show_task(conn: Connection, task_id: int) -> None:
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task_id:
    :return: project id
    """
    sql = f"SELECT * from tasks WHERE task_id =  {task_id}"
    cur = conn.cursor()
    result = cur.execute(sql)
    print(result.fetchall())


show_task(CONNECTION, task_id=2)


def select_all_tasks(conn: Connection) -> None:
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    result = cur.fetchall()

    for row in result:
        print(row)


select_all_tasks(CONNECTION)


def select_task_by_completed(conn: Connection, completed: int) -> None:
    """
    Query tasks by priority
    :param conn: the Connection object
    :param completed:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE completed= ?", (completed,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


select_task_by_completed(CONNECTION, 1)


def delete_task(conn: Connection, task_id: int) -> None:
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param task_id: id of the task
    :return:
    """
    sql = "DELETE FROM tasks WHERE id= ?"
    cur = conn.cursor()
    cur.execute(sql, (task_id,))
    conn.commit()


delete_task(conn=CONNECTION, task_id=2)


def delete_all_tasks(conn: Connection):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = "DELETE FROM tasks"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


delete_all_tasks(conn=CONNECTION)

CONNECTION.close()
