import sqlite3

from Database.IDatabase import *


class SQLDatabase(IDatabase):
    def __init__(self, database_name="employees.db"):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def backup_database(self):
        self.execute_sql("""select * from employee""")
        get_data = self.cursor.fetchall()
        data = []
        for d in get_data:
            data.append(d)
        return data

    def execute_sql(self, sql):
        self.cursor.execute(sql)

    def close_connection(self):
        self.connection.close()

    def commit(self):
        self.connection.commit()

    def setup(self):
        data = [("e01","m","20","20","Normal","200","12-06-17"), ("e02","f","21","21","Underweight","201","12-07-17"), ("e03","m","22","22","Obesity","202","12-08-17")]
        self.execute_sql("""drop table if exists employee""")
        sql = """
        CREATE TABLE employee ( 
        EMPID char(3),
        Gender char(1),
        Age int,
        Sales int,
        BMI varchar(200),
        Salary int,
        Birthday date
        );
        
        """
        self.execute_sql(sql)
        self.commit()
        for d in data:
            format_str = """INSERT INTO employee (EMPID, Gender, Age, Sales, BMI, Salary, Birthday) 
            VALUES ("{empid}","{gender}","{age}","{sales}","{BMI}","{salary}","{birthday}"); """
            sql_command = format_str.format(empid=d[0], gender=d[1], age=d[2], sales=d[3], BMI=d[4], salary=d[5],birthday=d[6])
            self.execute_sql(sql_command)

        self.commit()

    def reset(self):
        self.execute_sql("""drop table if exists employee""")
        self.setup()
