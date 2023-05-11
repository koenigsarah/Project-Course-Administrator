import module_display_persons

t_daten = module_display_persons.t_daten

def add_person():
    #m = input("Bitte sag mir die Matrikelnummer der Person, die du hinzufügen möchtest: ")
    while True:
        try:
            v = input("Bitte sag mir den Vornamen der Person, die du hinzufügen möchtest: ")
            int(v)
        except ValueError:
            break

    while True:
        try:
            n = input("Nachnamen: ")
            int(n)
        except ValueError:
            break

    while True:
        try:
            s = input("Straße: ")
            len(s) <=100#geht noch nicht
        except ValueError:
            break

    while True:
        try:
            h = input("Hausnummer: ")
            int(h)
        except ValueError:
            break

    while True:
        try:
            p = input("Postleitzahl: ")
            int(p)
        except ValueError:
            break

    while True:
        try:
            st = input("Stadt: ")
            int(st)
        except ValueError:
            break

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
module_display_persons.display()
