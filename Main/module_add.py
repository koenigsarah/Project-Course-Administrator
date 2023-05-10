import module_display_persons

t_daten = module_display_persons.t_daten
module_display_persons.display()

def add_person():
    #m = input("Bitte sag mir die Matrikelnummer der Person, die du hinzufügen möchtest: ")
    v = input("Bitte sag mir den Vornamen der Person, die du hinzufügen möchtest: ")
    n = input("Bitte sag mir den Nachnamen der Person, die du hinzufügen möchtest: ")
    s = input("Bitte sag mir die Straße der Person, die du hinzufügen möchtest: ")
    h = input("Bitte sag mir die Hausnummer der Person, die du hinzufügen möchtest: ")
    p = input("Bitte sag mir die Postleitzahl der Person, die du hinzufügen möchtest: ")
    st = input("Bitte sag mir die Stadt der Person, die du hinzufügen möchtest: ")

    for x in t_daten:
        neue_id = len(t_daten["id"]) +1
        t_daten["id"].append(neue_id)
        t_daten["vname"].append(v)
        t_daten["nname"].append(n)
        t_daten["str"].append(s)
        t_daten["nr"].append(h)
        t_daten["plz"].append(p)
        t_daten["ort"].append(st)

add_person()

print(t_daten)

#Problem - werden neue IDs bis inkl. 13 erstellt
#    for x in t_daten:
#         neue_id = len(t_daten["id"]) +1
#         t_daten["id"].append(neue_id)
#         t_daten["vname"].append(v)
#         t_daten["nname"].append(n)
#         t_daten["str"].append(s)
#         t_daten["nr"].append(h)
#         t_daten["plz"].append(p)
#         t_daten["ort"].append(st)
