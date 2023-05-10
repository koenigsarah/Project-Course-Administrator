import module_display_persons

t_daten = module_display_persons.t_daten
module_display_persons.display()

# Try and Error noch überall dazugeben!


def change_person():

    id_ = int(input("Bitte gib die ID der Person ein die du ändern möchtest: "))
    for i in t_daten["id"]:
        if id_ == int(t_daten["id"][i - 1]):
            print("ID:", t_daten["id"][i - 1], "*",
                  t_daten["nname"][i - 1], t_daten["vname"][i - 1], "*",
                  t_daten["str"][i - 1], t_daten["nr"][i - 1], "*",
                  t_daten["plz"][i - 1], t_daten["ort"][i - 1])

    print("Entweder neuen Wert eingeben oder Enter drücken")
    j = 0
    werte = 0
    while j < 1:
        alter_vname = t_daten["vname"][id_ - 1]
        t_daten["vname"][id_ - 1] = input("Neuer Vorname: ")
        if t_daten["vname"][id_ - 1] != "":
            werte += 1
        else:
            t_daten["vname"][id_ - 1] = alter_vname

        alter_nname = t_daten["nname"][id_ - 1]
        t_daten["nname"][id_ - 1] = input("Neuer Nachname: ")
        if t_daten["nname"][id_ - 1] != "":
            werte += 1
        else:
            t_daten["nname"][id_ - 1] = alter_nname

        alte_str = t_daten["str"][id_ - 1]
        t_daten["str"][id_ - 1] = input("Neue Straße: ")
        if t_daten["str"][id_ - 1] != "":
            werte += 1
        else:
            t_daten["str"][id_ - 1] = alte_str

        alte_nr = t_daten["nr"][id_ - 1]
        t_daten["nr"][id_ - 1] = input("Neue Hausnummer: ")
        if t_daten["nr"][id_ - 1] != "":
            werte += 1
        else:
            t_daten["nr"][id_ - 1] = alte_nr

        alte_plz = t_daten["plz"][id_ - 1]
        t_daten["plz"][id_ - 1] = input("Neue Postleitzahl: ")
        if t_daten["plz"][id_ - 1] != "":
            werte += 1
        else:
            t_daten["plz"][id_ - 1] = alte_plz

        alter_ort = t_daten["ort"][id_ - 1]
        t_daten["ort"][id_ - 1] = input("Neuer Ort: ")
        if t_daten["ort"][id_ - 1] != "":
            werte += 1
        else:
            t_daten["ort"][id_ - 1] = alter_ort

        print("ID:", t_daten["id"][id_ - 1], "*",
              t_daten["nname"][id_ - 1], t_daten["vname"][id_ - 1], "*",
              t_daten["str"][id_ - 1], t_daten["nr"][id_ - 1], "*",
              t_daten["plz"][id_ - 1], t_daten["ort"][id_ - 1])
        j = 1
    print(werte, "Werte wurden geändert.")
    module_display_persons.display()


change_person()
