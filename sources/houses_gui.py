# import imp
import tkinter
from tkinter import ttk
import sources.house as house
import config.nebenkosten_text_de as texte
import sources.appartments as appartments
import sources.textselector as textselector
import logging



##############################################################################
############################ Function definitions ############################
##############################################################################     
   
def gui_houses_frame(parent):
    """Aufbau des Häuser-Fensters"""
    ##########################################################################
    ############################ nested Functions## ##########################
    ##########################################################################

    def button_next_action():
        """Zeigt nächsten Datensatz an"""
        global houses_index
        if houses_index < len(house.houses) - 1:
            houses_index += 1
        actual = house.houses[houses_index]
        fill_house_data(actual)
    
    def button_prev_action():
        """Zeigt vorherigen Datensatz an"""
        global houses_index
        if houses_index > 0:
            houses_index -= 1
        actual = house.houses[houses_index]
        fill_house_data(actual)
     
    
    def button_new_action():
        """Erzeugt neuen Datensatz mit Pseudowerten."""
        global houses_index
        house.houses.append(house.House())
        houses_index = len(house.houses) - 1
        actual = house.houses[houses_index]
        actual.db_insert()
        fill_house_data(actual)
    
    def button_change_action():
        """Übernimmt geänderte Werte in Objekt"""
        global houses_index
        actual = house.houses[houses_index]
        actual.name = name_var.get()
        actual.size = size_var.get()
        actual.strasse = strasse_var.get()
        actual.zusatz= zusatz_var.get()
        actual.plz = plz_var.get()
        actual.ort = ort_var.get()
        actual.land = land_var.get()
        actual.db_update()
        fill_house_data(actual)
    
    def button_delete_action():
        """Löscht aktuelles Objekt"""
        global houses_index
        house.houses[houses_index].db_delete()
        house.houses.pop(houses_index)
        if len(house.houses) == 0:
            button_new_action()
        elif houses_index == 0:
            pass
        else:
            houses_index -= 1
        actual = house.houses[houses_index]
        fill_house_data(actual)
    
   
    def button_load_file_action():
        """Lädt Objekte aus Datei"""
        global houses_index
        houses_index = 0
        house.load_houses()
        if len(house.houses) == 0:
            button_new_action()
        else:
            actual = house.houses[houses_index]
            fill_house_data(actual)
    
   
    def fill_house_data(actual):
        """Übernimmt Werte des aktuellen Mieter-Objekts in Anzeige"""
        nonlocal appts_frame

        id_var.set(actual.id)
        name_var.set(actual.name)
        size_var.set(actual.size)
        strasse_var.set(actual.strasse)
        zusatz_var.set(actual.zusatz)
        plz_var.set(actual.plz)
        ort_var.set(actual.ort)
        land_var.set(actual.land)
        logger.debug('filled')
        actual.appts = appartments.get_appts_by_house_id(actual.id)
        print(actual.appts)
        appt_table.delete(*appt_table.get_children())
        for a in actual.appts:
            # logger.debug('appartment %s',a.id)
            print(a)
            appt_table.insert("", "end", values=(a['id'], a['name']))
    

        
    ##########################################################################
    ############################ Coding starts here ##########################
    ##########################################################################
    #Fenster aufbauen
    if parent == None:
        houses_frame = tkinter.Tk()
        houses_frame.title("Hausdaten")
    else:
        houses_frame = tkinter.Frame(parent)
        houses_frame.grid(row=1, column=1)
    
    data_frame = tkinter.Frame(houses_frame, relief=tkinter.GROOVE, borderwidth=5, padx=5, pady=5)
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
    
    size_label = tkinter.Label(data_frame, text=texte.size)
    size_var = tkinter.StringVar(data_frame)
    size_data = tkinter.Entry(data_frame,textvariable=size_var)
    size_label.grid(row=2, column=1, sticky=tkinter.W)
    size_data.grid(row=2, column=2, sticky=tkinter.W)

    strasse_label = tkinter.Label(data_frame, text=texte.strasse)
    strasse_var = tkinter.StringVar(data_frame)
    strasse_data = tkinter.Entry(data_frame, textvariable=strasse_var)
    strasse_label.grid(row=3, column=1, sticky=tkinter.W)
    strasse_data.grid(row=3, column=2, columnspan=3, sticky=tkinter.W+tkinter.E)

    zusatz_label = tkinter.Label(data_frame, text=texte.zusatz)
    zusatz_var = tkinter.StringVar(data_frame)
    zusatz_data = tkinter.Entry(data_frame, textvariable=zusatz_var)
    zusatz_label.grid(row=4, column=1, sticky=tkinter.W)
    zusatz_data.grid(row=4, column=2, columnspan=4, sticky=tkinter.W+tkinter.E)
   
    plz_label = tkinter.Label(data_frame, text=texte.plz)
    plz_var = tkinter.StringVar(data_frame)
    plz_data = tkinter.Entry(data_frame, textvariable=plz_var)
    plz_label.grid(row=5, column=1, sticky=tkinter.W)
    plz_data.grid(row=5, column=2, columnspan=4, sticky=tkinter.W+tkinter.E)

    ort_label = tkinter.Label(data_frame, text=texte.ort)
    ort_var = tkinter.StringVar(data_frame)
    ort_data = tkinter.Entry(data_frame, textvariable=ort_var)
    ort_label.grid(row=6, column=1, sticky=tkinter.W)
    ort_data.grid(row=6, column=2, columnspan=4, sticky=tkinter.W+tkinter.E)

    land_label = tkinter.Label(data_frame, text=texte.land)
    land_var = tkinter.StringVar(data_frame)
    land_data = tkinter.Entry(data_frame, textvariable=land_var)
    land_label.grid(row=7, column=1, sticky=tkinter.W)
    land_data.grid(row=7, column=2, columnspan=4, sticky=tkinter.W+tkinter.E)

    
    #Interaktion
    controls_frame = tkinter.Frame(houses_frame)
    button_prev = tkinter.Button(controls_frame, text=texte.button_prev, command=button_prev_action)
    button_next = tkinter.Button(controls_frame, text=texte.button_next, command=button_next_action)
    button_new = tkinter.Button(controls_frame, text= texte.button_new, command=button_new_action)
    button_change = tkinter.Button(controls_frame, text=texte.button_change, command=button_change_action)
    button_delete = tkinter.Button(controls_frame, text=texte.button_delete, command=button_delete_action)

    
    controls_frame.grid(row=2, column=1)
    button_prev.grid(row=2, column=1)
    button_next.grid(row=2, column=2)
    button_new.grid(row=2, column=3)
    button_change.grid(row=2, column=4)
    button_delete.grid(row=2, column=5)
    
    #appartments associated with this house
    appts_frame = tkinter.Frame(houses_frame)
    appts_frame.grid(row=3, column=1)
    appt_table = ttk.Treeview(appts_frame, columns=('apptID','Name'),  show='headings') 
    appt_table.column('apptID', anchor=tkinter.CENTER, width=40)
    appt_table.heading('apptID', text="ID")
    appt_table.heading('Name', text="Name")
    appt_table.grid(row = 1, column=1)


    #Fenster mit Daten füttern
    if len(house.houses) == 0:
        button_load_file_action()
    houses_index = 0
    actual = house.houses[houses_index]
    fill_house_data(actual)


    houses_frame.mainloop()

##############################################################################
############################## Skript starts here ############################
##############################################################################
logger = logging.getLogger(__name__)

houses_index = 0

if __name__ == "__main__":
    gui_houses_frame(None)