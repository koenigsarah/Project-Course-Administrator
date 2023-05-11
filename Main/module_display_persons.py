

t_daten = {"id": [1, 2, 3, 4, 5],
             "rolle": ["Teilnehmer*in"],
             "vname": ["Sarah", "Anna", "Otto", "Ella", "Lia"],
             "nname": ["König", "Huber", "Hofer", "Berger", "Bauer"],
             "str": ["1.A Straße", "Berggasse", "Burggasse", "Hauptstraße", "Blumengasse"],
             "nr": [3, 5, 77, 23, 9],
             "plz": [4425, 1030, 1200, 1230, 1160],
             "ort": ["Waidhofen/Ybbs", "Wien", "Wien", "Wien", "Wien"]}



v_daten = {"id": [1, 2, 3, 4, 5],
             "rolle": ["Lektor*in"],
             "vname": ["Sarah", "Anna", "Otto", "Ella", "Lia"],
             "nname": ["König", "Huber", "Hofer", "Berger", "Bauer"],
             "str": ["1.A Straße", "Berggasse", "Burggasse", "Hauptstraße", "Blumengasse"],
             "nr": [3, 5, 77, 23, 9],
             "plz": [4425, 1030, 1200, 1230, 1160],
             "ort": ["Waidhofen/Ybbs", "Wien", "Wien", "Wien", "Wien"]}


def display():

    for e in t_daten["id"]:
        print("ID:", t_daten["id"][e - 1], "*",
              t_daten["nname"][e - 1], t_daten["vname"][e - 1], "*",
              t_daten["str"][e - 1], t_daten["nr"][e - 1], "*",
              t_daten["plz"][e - 1], t_daten["ort"][e - 1])


# display()


