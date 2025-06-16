from typing import Self, Any
from datetime import *
import re


class Facolta:
    _nome: str
    _tipo: str
    _corsi: List["Corso"]

    def __init__(self, nome: str, tipo: str):
        self._nome = nome
        self._tipo = tipo
        self._corsi = []

    def nome(self) -> str:
        return self._nome

    def tipo(self) -> str:
        return self._tipo

    def corsi(self) -> List["Corso"]:
        return self._corsi

    def aggiungi_corso(self, corso: "Corso") -> None:
        if corso not in self._corsi:
            self._corsi.append(corso)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Facolta) and self._nome == other._nome and self._tipo == other._tipo

    def __hash__(self) -> int:
        return hash((self._nome, self._tipo))

    def __repr__(self) -> str:
        return f"{self._nome} ({self._tipo})"


class Nazione:
    def __init__(self, nome: str):
        self._nome = nome
        self._regioni: List["Regione"] = []

    def add_regione(self, regione: "Regione") -> None:
        if regione not in self._regioni:
            self._regioni.append(regione)

    def remove_regione(self, regione: "Regione") -> None:
        if regione in self._regioni:
            self._regioni.remove(regione)

    def nome(self) -> str:
        return self._nome

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Nazione) and self._nome == other._nome

    def __hash__(self) -> int:
        return hash(self._nome)

    def __repr__(self) -> str:
        return f"Nazione('{self._nome}')"


class Regione:
    def __init__(self, nome: str, nazione: Nazione):
        self._nome = nome
        self._città: List["Città"] = []
        self._nazione = nazione
        nazione.add_regione(self)

    def add_città(self, città: "Città") -> None:
        if any(c.nome() == città.nome() for c in self._città):
            raise ValueError("Esiste già una città con questo nome in questa regione.")
        self._città.append(città)

    def remove_città(self, città: "Città") -> None:
        if città in self._città:
            self._città.remove(città)

    def nome(self) -> str:
        return self._nome

    def città(self) -> List["Città"]:
        return self._città

    def nazione(self) -> Nazione:
        return self._nazione

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Regione) and self._nome == other._nome and self._nazione == other._nazione

    def __hash__(self) -> int:
        return hash((self._nome, self._nazione))

    def __repr__(self) -> str:
        return f"Regione('{self._nome}', {repr(self._nazione)})"


class Città:
    def __init__(self, nome: str, regione: Regione):
        self._nome = nome
        self._regione = regione
        regione.add_città(self)

    def nome(self) -> str:
        return self._nome

    def regione(self) -> Regione:
        return self._regione

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Città) and self._nome == other._nome and self._regione == other._regione

    def __hash__(self) -> int:
        return hash((self._nome, self._regione))

    def __repr__(self) -> str:
        return f"Città('{self._nome}', {repr(self._regione)})"
            



    



