from app.mod_tables.serverside.serverside_table import ServerSideTable
from app.mod_tables.serverside import table_schemas
from app import db

DATA_SAMPLE = [
    {'A': 'Hello!', 'B': 'How is it going?', 'C': 3, 'D': 4},
    {'A': 'These are sample texts', 'B': 0, 'C': 5, 'D': 6},
    {'A': 'Mmmm', 'B': 'I do not know what to say', 'C': 7, 'D': 16},
    {'A': 'Is it enough?', 'B': 'Okay', 'C': 8, 'D': 9},
    {'A': 'Just one more', 'B': '...', 'C': 10, 'D': 11},
    {'A': 'Thanks!', 'B': 'Goodbye.', 'C': 12, 'D': 13}
]

class SomeTable(db.Model):
    __tablename__ = 'some_table'
    cola = db.Column('A', db.String(2))
    colb = db.Column('B', db.String(2))
    colc = db.Column('C', db.Integer, primary_key=True)
    cold = db.Column('D', db.Integer)

    def __init__(self, cola, colb, colc, cold):
        self.cola = cola
        self.colb = colb
        self.colc = colc
        self.cold = cold

    @property
    def serialize(self):
        return {
             'A': self.cola,
             'B': self.colb,
             'C': self.colc,
             'D': self.cold
        }


def add_some_random_db_entries():
    letters = 'arstarstarstarstaars'
    for i in range(10):
        item = SomeTable(letters[i], letters[i + 1: i + 3], i, i + 1)
        db.session.add(item)
    db.session.commit()


def make_data_sample_from_db():
    newlist = []
    for row in SomeTable.query.all():
        newlist.append(row.serialize)
    return newlist


class TableBuilder(object):

    def collect_data_clientside(self):
        return {'data': DATA_SAMPLE}

    def collect_data_serverside(self, request):
        columns = table_schemas.SERVERSIDE_TABLE_COLUMNS
        data = make_data_sample_from_db()
        return ServerSideTable(request, data, columns).output_result()
