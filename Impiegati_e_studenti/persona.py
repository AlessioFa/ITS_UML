from tipi_di_dato_personalizzato import CodiceFiscale, IntGEZ
from datetime import date
from enums import Genere


class Persona:

    _nome: str  # noto alla nascita
    _cognome: str  # noto alla nascita
    _cf: set[CodiceFiscale]  # noto alla nascita, <<immutabile>> {id}
    _nascita: date  # noto alla nascita, <<immutabile>>
    _genere: Genere  # noto alla nascita, <<immutabile>>
    _maternità: IntGEZ  # noto alla nascita
    _posizione_militare: "PosizioneMilitare"  # noto alla nascita, <<immutabile>>

    def __init__(self, nome: str, cognome: str, cf: set[CodiceFiscale], nascita: date, genere: Genere, maternità: IntGEZ | None, posizione_militare: "PosizioneMilitare" | None) -> None:

        if not cf:
            raise ValueError("È obbligatorio avere almeno un codice fiscale.")

        if genere == Genere.uomo and not posizione_militare:
            raise ValueError("Un uomo deve avere una posizione militare.")

        if genere == Genere.donna and maternità is None:
            raise ValueError("Una donna deve avere uno stato di maternità.")

        self.set_nome(nome)
        self.set_cognome(cognome)
        self._cf = set(cf)
        self._nascita = nascita
        self._genere = genere
        self._maternità = maternità
        self._posizione_militare = posizione_militare

    def set_nome(self, nome) -> None:

        self._nome = nome.capitalize()

    def get_nome(self) -> str:

        return self._nome

    def set_cognome(self, cognome) -> None:

        self._cognome = cognome.capitalize()

    def get_cognome(self) -> str:

        return self._cognome

    def add_codice_fiscale(self, cf: CodiceFiscale) -> None:

        self._cf.add(cf)

    def remove_codice_fiscale(self, cf: CodiceFiscale) -> None:
        self._cf.remove(cf)

    def get_codice_fiscale(self) -> frozenset[CodiceFiscale]:

        return frozenset(self._cf)

    def get_nascita(self) -> date:

        return self._nascita

    def get_genere(self) -> Genere:

        return self._genere

    def get_maternità(self) -> IntGEZ:

        return self._maternità

    def get_posizione_militare(self) -> "PosizioneMilitare" | None:

        return self._posizione_militare

    def __str__(self):

        info = (f"Nome: {self.get_nome()} Cognome: {self.get_cognome()}\n"
                f"Codice fiscale: {self.get_codice_fiscale()}\n"
                f"Nascita: {self.get_nascita()}\n")

        if self._genere == Genere.uomo:

            info += f"Posizione Militare: {self.get_posizione_militare()}\n" 

        elif self._genere == Genere.donna:

            info += f"Numero Maternità: {self.get_maternità()}\n"


class PosizioneMilitare:

    _id_posizione: int 
    _tipo_posizione: str

    def __init__(self, id_posizione: int | str, tipo_posizione: str) -> None:

        self._id_posizione = id_posizione
        self._tipo_posizione = tipo_posizione.capitalize()
    
    def get_id(self) -> int:

        return self._id_posizione
    
    def get_tipo_posizione(self) -> str:

        return self._tipo_posizione
    
    def __str__(self) -> str:

        return f"{self.get_tipo_posizione()}, ID: {self.get_id()}"

    def __eq__(self, other) -> bool:

        if not isinstance(other, PosizioneMilitare):
            return False
        
        return self._id_posizione == other._id_posizione
    
    def __hash__(self) -> int:
        
        return hash(self._id_posizione)

