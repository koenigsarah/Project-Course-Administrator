
daten = {"id": [1, 2, 3, 4, 5],
         "rolle": ["Teilnehmer*in", "Vortragende*r"],
         "vname": ["Sarah", "Anna", "Otto", "Ella", "Lia"],
         "nname": ["König", "Huber", "Hofer", "Berger", "Bauer"],
         "str": ["1.A Straße", "Berggasse", "Burggasse", "Hauptstraße", "Blumengasse"],
         "nr": [3, 5, 77, 23, 9],
         "plz": [4425, 1030, 1200, 1230, 1160],
         "ort": ["Waidhofen/Ybbs", "Wien", "Wien", "Wien", "Wien"]}


def display():

    for e in daten["id"]:
        print("ID:", daten["id"][e - 1], "*",
              daten["nname"][e - 1], daten["vname"][e - 1], "*",
              daten["str"][e - 1], daten["nr"][e - 1], "*",
              daten["plz"][e - 1], daten["ort"][e - 1])


