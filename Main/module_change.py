import module_display_persons

daten = module_display_persons.daten
module_display_persons.display()

# Try and Error noch überall dazugeben!


def change_person():

    id_ = int(input("Bitte gib die ID der Person ein die du ändern möchtest: "))
    for i in daten["id"]:
        if id_ == int(daten["id"][i-1]):
            print("ID:", daten["id"][i-1], "*",
                  daten["nname"][i-1], daten["vname"][i-1], "*",
                  daten["str"][i-1], daten["nr"][i-1], "*",
                  daten["plz"][i-1], daten["ort"][i-1])

    print("Entweder neuen Wert eingeben oder Enter drücken")
    j = 0
    werte = 0
    while j < 1:
        alter_vname = daten["vname"][id_-1]
        daten["vname"][id_-1] = input("Neuer Vorname: ")
        if daten["vname"][id_ - 1] != "":
            werte += 1
        else:
            daten["vname"][id_-1] = alter_vname

        alter_nname = daten["nname"][id_-1]
        daten["nname"][id_-1] = input("Neuer Nachname: ")
        if daten["nname"][id_ - 1] != "":
            werte += 1
        else:
            daten["nname"][id_-1] = alter_nname

        alte_str = daten["str"][id_-1]
        daten["str"][id_-1] = input("Neue Straße: ")
        if daten["str"][id_-1] != "":
            werte += 1
        else:
            daten["str"][id_-1] = alte_str

        alte_nr = daten["nr"][id_-1]
        daten["nr"][id_-1] = input("Neue Hausnummer: ")
        if daten["nr"][id_-1] != "":
            werte += 1
        else:
            daten["nr"][id_-1] = alte_nr

        alte_plz = daten["plz"][id_-1]
        daten["plz"][id_-1] = input("Neue Postleitzahl: ")
        if daten["plz"][id_-1] != "":
            werte += 1
        else:
            daten["plz"][id_-1] = alte_plz

        alter_ort = daten["ort"][id_-1]
        daten["ort"][id_-1] = input("Neuer Ort: ")
        if daten["ort"][id_-1] != "":
            werte += 1
        else:
            daten["ort"][id_-1] = alter_ort

        print("ID:", daten["id"][id_-1], "*",
              daten["nname"][id_-1], daten["vname"][id_-1], "*",
              daten["str"][id_-1], daten["nr"][id_-1], "*",
              daten["plz"][id_-1], daten["ort"][id_-1])
        j = 1
    print(werte, "Werte wurden geändert.")
    module_display_persons.display()


change_person()
