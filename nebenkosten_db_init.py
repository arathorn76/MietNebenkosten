"""Main program for side costs
"""

import sources.db as db

import config.nebenkosten_text_de as texte
import logging

##############################################################################
############################ Function definitions ############################
##############################################################################

##############################################################################
############################## Skript starts here ############################
##############################################################################
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":

    db.create_db()

