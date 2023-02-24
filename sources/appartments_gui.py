import tkinter
from tkinter import ttk
import sources.appartments as appartments
import sources.house as houses
import config.nebenkosten_text_de as texte
import sources.textselector as textsel
import logging


##############################################################################
############################ Function definitions ############################
##############################################################################     
   
def gui_appartments_frame(parent):
    """Aufbau des Wohnungs-Fensters"""
    ##########################################################################
    ############################ nested Functions## ##########################
    ##########################################################################

    def button_next_action():
        """Zeigt nächsten Datensatz an"""
        global apps_index
        if apps_index < len(appartments.appartments) - 1:
            apps_index += 1
        actual = appartments.appartments[apps_index]
        fill_appt_data(actual)
    
    def button_prev_action():
        """Zeigt vorherigen Datensatz an"""
        global apps_index
        if apps_index > 0:
            apps_index -= 1
        actual = appartments.appartments[apps_index]
        fill_appt_data(actual)
     
    
    def button_new_action():
        """Erzeugt neuen Datensatz mit Pseudowerten."""
        global apps_index
        appartments.appartments.append(appartments.Appartment())
        apps_index = len(appartments.appartments) - 1
        actual = appartments.appartments[apps_index]
        actual.db_insert()
        fill_appt_data(actual)
    
    def button_change_action():
        """Übernimmt geänderte Werte in Objekt"""
        global apps_index
        actual = appartments.appartments[apps_index]
        actual.name = name_var.get()
        actual.size = size_var.get()
        actual.house_id = int(housid_var.get())
        actual.roomcount = roomcount_var.get()
        actual.lage = lage_var.get()
        actual.db_update()
        fill_appt_data(actual)
    
    def button_delete_action():
        """Löscht aktuelles Objekt"""
        global apps_index
        appartments.appartments[apps_index].db_delete()
        appartments.appartments.pop(apps_index)
        if len(appartments.appartments) == 0:
            button_new_action()
        elif apps_index == 0:
            pass
        else:
            apps_index -= 1
        actual = appartments.appartments[apps_index]
        fill_appt_data(actual)
    
   
    def button_load_file_action():
        """Lädt Objekte aus Datei"""
        global apps_index
        apps_index = 0
        appartments.load_appartments()
        if len(appartments.appartments) == 0:
            button_new_action()
        else:
            actual = appartments.appartments[apps_index]
            fill_appt_data(actual)
    
    def button_house_choose_action():
        houslist = list()
        for h in houses.houses:
            houslist.append(h.name)
        logger.debug('Hausliste: %s', houslist)
 
        #FIXME per textselector Haus auswählen
        sel = textsel.select_text(houslist)
        new_id = houses.houses[houslist.index(sel)].id
        logger.debug('Auswahlg: %s mit ID %s', sel, new_id)
        #TODO ausgewählte Haus-ID übernehmen und Haus-Name aktualisieren
        pass

    
    def fill_appt_data(actual):
        """Übernimmt Werte des aktuellen Mieter-Objekts in Anzeige"""
        id_var.set(actual.id)
        name_var.set(actual.name)
        housid_var.set(actual.house_id)
        lage_var.set(actual.lage)
        size_var.set(actual.size)
        roomcount_var.set(actual.roomcount)
        if actual.house_id != None:
            house_var.set(houses.get_house_by_id(actual.house_id))
        else:
            house_var.set('')
    
        
    ##########################################################################
    ############################ Coding starts here ##########################
    ##########################################################################
    #Fenster aufbauen
    if parent == None:
        apps_frame = tkinter.Tk()
        apps_frame.title(text=texte.menu_appartments)
    else:
        apps_frame = tkinter.Frame(parent)
        apps_frame.grid(row=1, column=1)
    
    data_frame = tkinter.Frame(apps_frame, relief=tkinter.GROOVE, borderwidth=5, padx=5, pady=5)
    data_frame.grid(row=1, column=1, sticky=tkinter.NW)
    
    #Datendisplay/edit
    id_label = tkinter.Label(data_frame, text=texte.id)
    id_var = tkinter.StringVar(data_frame)
    id_data = tkinter.Entry(data_frame, textvariable=id_var,state=tkinter.DISABLED)
    id_label.grid(row=0, column=1, sticky=tkinter.W)
    id_data.grid(row=0, column=2, sticky=tkinter.W)

    name_label = tkinter.Label(data_frame, text=texte.name)
    name_var = tkinter.StringVar(data_frame)
    name_data = tkinter.Entry(data_frame,textvariable=name_var)
    name_label.grid(row=1, column=1, sticky=tkinter.W)
    name_data.grid(row=1, column=2, sticky=tkinter.W)
    
    housid_label = tkinter.Label(data_frame, text=texte.house)
    housid_var = tkinter.StringVar(data_frame)
    # housid_data = tkinter.Entry(data_frame, textvariable=housid_var)
    housid_data = ttk.Combobox(data_frame, textvariable=housid_var, values=[1,2])
    housid_label.grid(row=2, column=1, sticky=tkinter.W)
    housid_data.grid(row=2, column=2, columnspan=3, sticky=tkinter.W+tkinter.E)

    house_label = tkinter.Label(data_frame, text=texte.house)
    house_var = tkinter.StringVar(data_frame)
    house_data = tkinter.Entry(data_frame, textvariable=house_var,state=tkinter.DISABLED)
    house_label.grid(row=3, column=1, sticky=tkinter.W)
    house_data.grid(row=3, column=2, columnspan=4, sticky=tkinter.W+tkinter.E)
    # house_choose_button = tkinter.Button(data_frame, text=texte.button_house_choose, command=button_house_choose_action)
    # house_choose_button.grid(row=2, column=3)
    housid_data.bind('<<ComboboxSelected>>', house_var.set(houses.get_house_by_id(housid_var.get())))

    lage_label = tkinter.Label(data_frame, text=texte.lage)
    lage_var = tkinter.StringVar(data_frame)
    lage_data = tkinter.Entry(data_frame,textvariable=lage_var)
    lage_label.grid(row=4, column=1, sticky=tkinter.W)
    lage_data.grid(row=4, column=2, sticky=tkinter.W)

    size_label = tkinter.Label(data_frame, text=texte.size)
    size_var = tkinter.StringVar(data_frame)
    size_data = tkinter.Entry(data_frame,textvariable=size_var)
    size_label.grid(row=5, column=1, sticky=tkinter.W)
    size_data.grid(row=5, column=2, sticky=tkinter.W)

    roomcount_label = tkinter.Label(data_frame, text=texte.roomcount)
    roomcount_var = tkinter.StringVar(data_frame)
    roomcount_data = tkinter.Entry(data_frame,textvariable=roomcount_var)
    roomcount_label.grid(row=6, column=1, sticky=tkinter.W)
    roomcount_data.grid(row=6, column=2, sticky=tkinter.W)

   
    #Fenster mit Daten füttern
    if len(appartments.appartments) == 0:
        button_load_file_action()
    apps_index = 0
    actual = appartments.appartments[apps_index]
    fill_appt_data(actual)
    
    #Interaktion
    controls_frame = tkinter.Frame(apps_frame)
    button_prev = tkinter.Button(controls_frame, text=texte.button_prev, command=button_prev_action)
    button_next = tkinter.Button(controls_frame, text=texte.button_next, command=button_next_action)
    button_new = tkinter.Button(controls_frame, text= texte.button_new, command=button_new_action)
    button_change = tkinter.Button(controls_frame, text=texte.button_change, command=button_change_action)
    button_delete = tkinter.Button(controls_frame, text=texte.button_delete, command=button_delete_action)

    
    controls_frame.grid(row=2, column=1)
    button_prev.grid(row=1, column=1)
    button_next.grid(row=1, column=2)
    button_new.grid(row=1, column=3)
    button_change.grid(row=1, column=4)
    button_delete.grid(row=1, column=5)
    
    
    apps_frame.mainloop()

##############################################################################
############################## Skript starts here ############################
##############################################################################
logger = logging.getLogger(__name__)
apps_index = 0


if __name__ == "__main__":
    gui_appartments_frame(None)