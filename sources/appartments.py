import sources.db as db
import sqlite3
import config.settings as settings

##############################################################################
############################## Class definitions #############################
##############################################################################
class Appartment:
    """Class for modelling appartments.
    
    Context: calculating side costs for renters"""
    
    def __init__(self, id = None, name='neue Wohnung', house_id = None, lage = None, size = 0, roomcount = 0):
        self.id = id
        self.name = name
        self.house_id = house_id
        self.lage = lage
        self.size = size
        self.roomcount = roomcount

    def db_insert(self):
        verbindung = sqlite3.connect(settings.dbfile)
        zeiger = verbindung.cursor()
        sql_string = "insert into appartments values(?, ?, ?, ?, ?, ?)"
        zeiger.execute(sql_string, (
            None,
            self.name,
            self.house_id,
            self.lage,
            self.size,
            self.roomcount
        ))


        verbindung.commit()
        self.id = zeiger.lastrowid
        verbindung.close()

    def db_update(self):
        verbindung = sqlite3.connect(settings.dbfile)
        zeiger = verbindung.cursor()
        sql_string = """update appartments set name=?, house_id=?,  lage=?, size=?, roomcount=? where id=?"""
        zeiger.execute(sql_string, (
            self.name,
            self.house_id,
            self.lage,
            self.size,
            self.roomcount,
            self.id
        ))
        verbindung.commit()
        verbindung.close()

    def db_delete(self):
        verbindung = sqlite3.connect(settings.dbfile)
        zeiger = verbindung.cursor()
        sql_string = "delete from appartments where id = ?"
        zeiger.execute(sql_string, (self.id,))
        verbindung.commit()
        verbindung.close()

# Persistenz
def load_appartments():
    apps = list()
    for a in db.read_appartments():
        apps.append(Appartment(*a))
    return apps

def get_appts_by_house_id(house_id):
    appts = list()
    for a in appartments:
        if a.house_id == house_id:
            appt = { 'id': a.id,
                     'name': a.name}
            # appt.append(a.id)
            # appt.append(a.name)
            appts.append(appt)
    return appts

#Initialisierung des Moduls
appartments = list()
appartments = load_appartments()