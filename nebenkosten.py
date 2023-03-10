"""Main program for side costs
"""

#from pip import main
import sources.db as db
import sources.houses_gui as houses_gui
import sources.renter_gui as renter_gui
import sources.appartments_gui as apps
import tkinter
import config.nebenkosten_text_de as texte
import logging

##############################################################################
############################ Function definitions ############################
##############################################################################
def button_houses_action(): 
    global main_frame
    main_frame.destroy()
    main_frame = tkinter.Frame(top_window)
    main_frame.grid(row=1, column=2)
    houses_gui.gui_houses_frame(main_frame)

def button_renters_action():
    global main_frame
    main_frame.destroy()
    main_frame = tkinter.Frame(top_window)
    main_frame.grid(row=1, column=2)
    renter_gui.gui_renter_frame(main_frame)

def button_appartments_action():
    global main_frame
    main_frame.destroy()
    main_frame = tkinter.Frame(top_window)
    main_frame.grid(row=1, column=2)
    apps.gui_appartments_frame(main_frame)

def display_window():
    top_window.title(texte.title)
    top_window.minsize(width=600, height=400)

    #Main Menu
    main_menu = tkinter.Frame(top_window, relief=tkinter.GROOVE, borderwidth=5, padx=5, pady=5, bg="#99f")
    main_menu.grid(row=0, column=0, rowspan=99, sticky=tkinter.N+tkinter.S)

    button_houses = tkinter.Button(main_menu, text=texte.menu_houses, command=button_houses_action)
    button_appartments = tkinter.Button(main_menu, text=texte.menu_appartments, command=button_appartments_action)
    button_renters = tkinter.Button(main_menu, text=texte.menu_renters, command=button_renters_action)
    menu_spacer = tkinter.Label(main_menu, text=" ", bg="#99f", fg="#99f")
    button_exit = tkinter.Button(main_menu, text=texte.menu_exit, command=top_window.destroy)

    button_houses.grid(row=1, column=1, sticky=tkinter.W+tkinter.E, pady=2)
    button_appartments.grid(row=3, column=1, sticky=tkinter.W+tkinter.E, pady=2)
    button_renters.grid(row=4, column=1, sticky=tkinter.W+tkinter.E, pady=2)
    menu_spacer.grid(row=10, column=1)
    button_exit.grid(row=15, column=1, sticky=tkinter.W+tkinter.E, pady= 10)

    #Main Frame
    main_frame.grid(row=1, column=2)


    top_window.mainloop()


##############################################################################
############################## Skript starts here ############################
##############################################################################
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(levelname)s:%(name)s:line_%(lineno)d:%(funcName)s:%(message)s', level=logging.DEBUG)
# logging.basicConfig(format='%(levelname)s:%(name)s:line_%(lineno)d:%(funcName)s:%(message)s', level=logging.WARNING)
# logger.setLevel(logging.DEBUG)

if __name__ == "__main__":

    top_window = tkinter.Tk()
    main_frame = tkinter.Frame(top_window)

    display_window()
