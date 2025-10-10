"""This file defines multiple custom enums data types that represent UML conceptual enums data types."""

from enum import StrEnum, auto

# StrEnum unifies the behave of strings and enum types and allows to use the values as strings


class Genere(StrEnum):
    uomo = auto()
    donna = auto()


# The code is going to be executed in this file only
if __name__ == "__main__":

    print(Genere.uomo)

    print(type(Genere.uomo))

    print(Genere.donna.title())

    print(type(Genere.donna))

    try:
        Genere.donna = 5
    
    except AttributeError as e:
        print("Non è possibile riassegnare il valore 'donna' dal tipo Genere")
        print("\t" + str(e))

    if Genere.uomo == Genere.donna:
        print("Uguali")
    
    else:
        print("Diversi\n")




class StatoOrdine(StrEnum):
    in_preparazione = auto()
    inviato = auto()
    da_saldare = auto()
    saldato = auto()

if __name__ == "__main__":

    print(StatoOrdine.in_preparazione)
    print(StatoOrdine.inviato)
    print(StatoOrdine.da_saldare)
    print(StatoOrdine.saldato)

    for stato in StatoOrdine:
        print(f"\nAttualmente l ordine è: {stato.value}")

    try:
        for stato in StatoOrdine:
            stato.StatoOrdine = 5
    except AttributeError as e:
        print()
    