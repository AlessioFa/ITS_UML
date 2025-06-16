from tipi_di_dato_personalizzato import *
from typing import Self, Any
from datetime import *

    
class Impiegato:

    _nome: str
    _cognome: str
    _nascita: date # immutabile
    _stipendio: RealGZ

    def __init__(self, nome: str, cognome: str, nascita: date, stipendio: RealGZ):

        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome.capitalize()

    def get_nome(self) -> str:
        return self._nome
    
    def set_cognome(self, cognome: str) -> str:
        self._cognome = cognome.capitalize()
    
    def get_cognome(self) -> str:
        return self._cognome
    
    def get_nascita(self) -> date:
        return self._nascita
    
    def set_stipendio(self, stipendio: RealGZ) -> None:
        self._stipendio = stipendio

    def __str__(self) -> str:
        return f"Impiegato: {self.get_nome()} {self.get_cognome()}"
    
    def __eq__(self, other: object) -> bool:
        
        if not isinstance(other, Impiegato):
            return False
        
        return (self._nome, self._cognome, self._nascita) == (other._nome, other._cognome, other._nascita)
    
    def __hash__(self) -> int:
        return hash((self._nome, self._cognome, self._nascita))
    
    
class Progetto:

    _nome: str
    _budget: RealGZ
    _impiegati: set[Impiegato]

    def __init__(self, nome: str, budget: RealGZ) -> None:

        self.set_nome(nome)
        self.set_budget(budget)
        self.impiegati = set()

    def set_nome(self, nome: str) -> None:

        self._nome = nome.capitalize()

    def get_nome(self) -> str:
        
        return self._nome
        
    def set_budget(self, budget: RealGZ) -> None:

        self._budget = budget
        
    def get_budget(self) -> RealGZ:
            
        return self._budget
    
    def add_impiegato(self, impiegato: Impiegato) -> None | str:
        
        if impiegato in self._impiegati:
            raise ValueError("Impiegato già assegnato al progetto.")
        
        else:
            self._impiegati.add(impiegato)
            
    
    def is_coinvolto(self, impiegato: Impiegato) -> str:
        
        if impiegato in self._impiegati:
            return f"L' impiegato {impiegato} si trova nel progetto {self.get_nome()}."
        
        return f"L impiegato non si trova nel progetto {self.get_nome()}."

    
    def __str__(self):
        
        return f"Progetto: {self.get_nome()} Budget: {self.get_budget()}"
    

class Dipartimento: 

    _nome: str
    _telefono: set[Telefono]
    _indirizzo: Indirizzo | None

    def __init__(self, nome: str, telefono: Telefono, indirizzo: Indirizzo) -> None:

        self.set_nome(nome)
        self._telefono = {telefono}
        self.indirizzo = indirizzo

    def set_nome(self, nome) -> None:

        self.nome = nome.capitalize()
    
    def get_nome(self) -> str:

        return self.nome
    
    def get_telefono(self) -> frozenset[Telefono]:

        return frozenset(self._telefono)
    
    def add_telefono(self, telefono: Telefono) -> None:

        self._telefono.add(telefono)

    def remove_telefono(self, telefono: Telefono) -> None:

        if len(self._telefono) >= 2:
            self._telefono.remove(telefono)
        else:
            raise RuntimeError("Il dipartimento deve avere almeno un numero di telefono.")
    
    def set_indirizzo(self, indirizzo: Indirizzo) -> None:
        
        self._indirizzo = indirizzo
    
    def get_indirizzo(self) -> Indirizzo:
        
        return self._indirizzo
  
    def remove_indirizzo(self) -> Indirizzo |None:
        
        if self._indirizzo: 
            self._indirizzo = None
    
    def __str__(self) -> str:

        telefoni_str: str = ", ".join(str(t) for t in self._telefono)

        indirizzo_str = str(self._indirizzo) if self._indirizzo else "Nessun indirizzo inserito."

        return f"Nome: {self.get_nome()}, Telefono: {telefoni_str}, Indirizzo: {indirizzo_str}"
    

class Afferenza:
    _data_afferenza: date # immutabile

    def __init__(self, data_afferenza: date) -> None:

        self._data_afferenza = data_afferenza
    
    def get_data_afferenza

if __name__ == "__main__":
    alice: Impiegato = Impiegato(nome="Alice", cognome="Alberelli",
                                 nascita=date.today() - timedelta(weeks=52*25),
                                 stipendio = RealGZ(45_000))
    print(alice)