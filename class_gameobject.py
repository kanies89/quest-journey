class GameObject:
    table_name = None  # set in subclass
    fields = []  # set in subclass

    def __init__(self, *args):
        self.id = None  # assigned by database on save
        for i, field in enumerate(self.fields):
            setattr(self, field[0], args[i])

    def get_insert_clause(self):
        return f"({', '.join([field[0] for field in self.fields])})"

    def get_placeholder_clause(self):
        return f"({', '.join(['%s' for _ in self.fields])})"

    def get_values(self):
        return tuple(getattr(self, field[0]) for field in self.fields)

    def get_update_clause(self):
        return ', '.join([f"{field[0]}=%s" for field in self.fields])

    def save(self, db):
        db.save(self)

    def get_values_tuple(self):
        return tuple(getattr(self, field[0]) for field in self.fields if field[0] != 'id')

    @classmethod
    def load(cls, db, id):
        return db.load(cls, id)

    @classmethod
    def create_table(cls, db):
        db.create_table(cls)

    @classmethod
    def create_instance(cls, db, *args):
        return db.create_instance(cls, *args)
