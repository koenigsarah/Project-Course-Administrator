personendaten = {"id" : 51802222, "rolle" : "Teilnehmer", "vorname" : "Sarah", "nachname" : "König", "straße" : "1.A Straße", "hausnummer" : "4", "plz" : "4425", "stadt" : "Waidhofen/Ybbs"}


def remove_person(personen):
    person = input("Welche Person willst du löschen? ", personen)
    # liste formatieren: alle vnamen nnamen ids untereinander
    # nur id eingeben? ja, weil doppelte vor- oder nachnamen...
    # nachfragen ob tatsächlich löschen j n dann erst
    # wenn ja -> löschen, wenn nein -> zurück zum hauptmenü (was möchtest du machen?)
