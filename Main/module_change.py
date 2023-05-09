import module_display_persons

daten = module_display_persons.daten
module_display_persons.display()


def change_person():

    id_ = input("Bitte gib die ID der Person ein die du ändern möchtest")
    for i in daten["id"]:
        if int(id_) == int(daten["id"][i-1]):
            print("ID:", daten["id"][i-1], "*",
                  daten["nname"][i-1], daten["vname"][i-1], "*",
                  daten["str"][i-1], daten["nr"][i-1], "*",
                  daten["plz"][i-1], daten["ort"][i-1])
            daten["nname"][i-1] = "Vivaldi"

    module_display_persons.display()


change_person()
