import mysql.connector
import core

class Database:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

        self.conn = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
        )

    def save(self, obj):
        c = self.conn.cursor()

        if not self.table_exists(obj.table_name):
            self.create_table(obj)

        else:
            if obj.id:
                c.execute(f"UPDATE {obj.table_name} SET {obj.get_update_clause()} WHERE id=%s",
                          obj.get_values() + (obj.id,))
            else:
                c.execute(f"INSERT INTO {obj.table_name} {obj.get_insert_clause()} VALUES {obj.get_placeholder_clause()}",
                          obj.get_values())

                # Update the object with the assigned ID
                obj.id = c.lastrowid

            self.conn.commit()

    def load(self, obj_cls, id):
        c = self.conn.cursor()
        c.execute(f"SELECT * FROM {obj_cls.table_name} WHERE id=%s", (id,))
        row = c.fetchone()
        if not row:
            return None
        obj = obj_cls(*row[1:])  # pass all columns except the first one (id)
        return obj

    def create_table(self, obj_cls):
        c = self.conn.cursor()

        c.execute(f"CREATE TABLE IF NOT EXISTS {obj_cls.table_name} ({obj_cls.get_schema()})")

        self.conn.commit()

    def create_instance(self, obj_cls, *args):
        obj = obj_cls(*args)
        self.create_table(obj_cls)
        self.save(obj)
        return obj

    def table_exists(self, table_name):
        c = self.conn.cursor()
        c.execute("SHOW TABLES")
        tables = [row[0] for row in c.fetchall()]
        return table_name in tables