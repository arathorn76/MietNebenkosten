"""Module providing stuff for houses."""

import sources.db as db
import sqlite3
import config.settings as settings
import logging


##############################################################################
############################## Class definitions #############################
##############################################################################
class House:
    """Class for modelling houses.
    
    Context: calculating side costs for renters"""
    
    def __init__(self, id = None, name='neues Haus', size = 0, strasse='', zusatz='', plz='', ort='', land='Deutschland'):
        self.id = id
        self.name = name
        self.size = size
        self.strasse = strasse
        self.zusatz = zusatz
        self.plz = plz
        self.ort = ort
        self.land = land

        self.appts = list()

    def db_insert(self):
        verbindung = sqlite3.connect(settings.dbfile)
        zeiger = verbindung.cursor()
        sql_string = "insert into houses values(?, ?, ?, ?, ?, ?, ?, ?)"
        zeiger.execute(sql_string, (
            None,
            self.name,
            self.size,
            self.strasse,
            self.zusatz,
            self.plz,
            self.ort,
            self.land
        ))
        verbindung.commit()
        self.id = zeiger.lastrowid
        verbindung.close()

    def db_update(self):
        verbindung = sqlite3.connect(settings.dbfile)
        zeiger = verbindung.cursor()
        sql_string = """update houses set name=?, size=?, strasse =?, zusatz=?, plz=?, ort=?, land=? where id=?"""
        zeiger.execute(sql_string, (
            self.name,
            self.size,
            self.strasse,
            self.zusatz,
            self.plz,
            self.ort,
            self.land,
            self.id
        ))
        verbindung.commit()
        verbindung.close()

    def db_delete(self):
        verbindung = sqlite3.connect(settings.dbfile)
        zeiger = verbindung.cursor()
        sql_string = "delete from houses where id = ?"
        zeiger.execute(sql_string, (self.id,))
        verbindung.commit()
        verbindung.close()
    


##############################################################################
############################ function definitions ############################
##############################################################################
# Persistenz
def load_houses():
    global houses
    houses.clear()
    for h in db.read_houses():
        houses.append(House(*h))

def get_house_by_id(query_id):
    for h in houses:
        if h.id == query_id:
            logger.debug('Haus mit ID %s gefunden', h.id)
            return h.name

##############################################################################
#################################### coding ##################################
##############################################################################
#Initialisierung des Moduls
logger = logging.getLogger(__name__)

houses = list()
load_houses()