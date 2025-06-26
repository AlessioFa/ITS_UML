from tipi_di_dato_personalizzato import Telefono, RealGZ, Indirizzo
from datetime import date
from typing import Self

"""
A breve aggiungerò la ristrutturazione dell' associazione 'direzione'. Integrerò delle docstring per ciascuna classe e commenti per alcune funzioni, dove necessario.
"""


class Impiegato:

    _nome: str  # noto alla nascita
    _cognome: str  # noto alla nascita
    _nascita: date  # <<immutabile>>, noto alla nascita
    _stipendio: RealGZ  # noto alla nascita
    _coinvolgimenti: set["Coinvolto._link_imp_prog"]  # non noto alla nascita
    _afferenza: None  # non noto alla nascita 

    def __init__(self, nome: str, cognome: str, nascita: date, stipendio: RealGZ) -> None:

        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)
        self._coinvolgimenti = set()
        self._afferenza = None 

    def set_nome(self, nome: str) -> None:
        
        self._nome = nome.capitalize()

    def get_nome(self) -> str:
        
        return self._nome

    def set_cognome(self, cognome: str) -> None:
        
        self._cognome = cognome.capitalize()

    def get_cognome(self) -> str:
        
        return self._cognome

    def get_nascita(self) -> date:
        
        return self._nascita

    def set_stipendio(self, stipendio: RealGZ) -> None:
        
        self._stipendio = stipendio

    def get_stipendio(self) -> RealGZ:
        
        return self._stipendio

    def add_link_coinvolto(self, link_imp_prog) -> None:

        self._coinvolgimenti.add(link_imp_prog)

    def get_coinvolgimenti(self):

        return self._coinvolgimenti

    def remove_link_coinvolto(self, link_imp_prog) -> None:

        self._coinvolgimenti.remove(link_imp_prog)
    
    def get_nome_dipartimento(self) -> str:

        if self._afferenza is None:
            return "Nessun dipartimento associato."
        
        return self._afferenza.get_nome_dipartimento()

    def set_afferenza(self, afferenza: "Afferenza") -> None:

        if self._afferenza is not None:
            raise ValueError(f"L'impiegato {self.get_nome()} è già associato a un dipartimento.")

        self._afferenza = afferenza
    
    def get_afferenza(self) -> str:

        if self._afferenza is None:
            return f"L' impiegato {self.get_nome()} non afferisce a nessun dipartimento."

        return self._afferenza.get_nome_dipartimento()

    def __str__(self) -> str:
        return f"Impiegato: {self.get_nome()} {self.get_cognome()} \nNascita: {self._nascita}\nStipendio : {self.get_stipendio()}"

    def __eq__(self, other: object) -> bool:

        if not isinstance(other, Impiegato):
            return False

        return (self._nome, self._cognome, self._nascita) == (other._nome, other._cognome, other._nascita)

    def __hash__(self) -> int:
        return hash((self._nome, self._cognome, self._nascita))


class Progetto:

    _nome: str  # noto alla nascita  
    _budget: RealGZ  # noto alla nascita ???
    _coinvolgimenti: set["Coinvolto._link"]  # non noto alla nascita

    def __init__(self, nome: str, budget: RealGZ) -> None:

        self.set_nome(nome)
        self.set_budget(budget)
        self._coinvolgimenti = set()

    def set_nome(self, nome: str) -> None:

        self._nome = nome.capitalize()

    def get_nome(self) -> str:

        return self._nome

    def set_budget(self, budget: RealGZ) -> None:

        self._budget = budget

    def get_budget(self) -> RealGZ:

        return self._budget

    def add_link_coinvolto(self, link_imp_prog) -> None:

        self._coinvolgimenti.add(link_imp_prog)

    def get_coinvolgimenti(self) -> set["Coinvolto._link"]:

        return self._coinvolgimenti

    def remove_link_coinvolto(self, link_imp_prog) -> None:

        self._coinvolgimenti.remove(link_imp_prog)

    def __str__(self) -> str:

        return f"Progetto: {self.get_nome()} Budget: {self.get_budget()}"


class Dipartimento:

    _nome: str  # noto alla nascita
    _telefono: set[Telefono]  # noto alla nascita [1..*]
    _indirizzo: Indirizzo | None   # possibilmente non noto alla nascita
    _afferenze: "afferenze"

    def __init__(self, nome: str, telefono: Telefono, indirizzo: None | Indirizzo) -> None:

        self.set_nome(nome)

        if not isinstance(telefono, Telefono) or telefono is None:
            raise ValueError("Deve esserci almeno un numero di telefono valido.")

        self._telefono = {telefono}

        self._indirizzo = indirizzo

    def set_nome(self, nome) -> None:

        self._nome = nome.capitalize()

    def get_nome(self) -> str:

        return self._nome

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

    def remove_indirizzo(self) -> Indirizzo | None:

        if self._indirizzo:
            self._indirizzo = None
    
    def add_afferenza(self, afferenza: "Afferenza") -> None:
        
        self._afferenze.add(afferenza)
    
    def get_afferenze(self) -> set:
        
        return self._afferenze

    def __str__(self) -> str:

        telefoni_str: str = ", ".join(str(tel) for tel in self._telefono)

        indirizzo_str = str(self._indirizzo) if self._indirizzo else "Nessun indirizzo inserito."

        return f"Nome dipartimento: {self.get_nome()}, Telefono : {telefoni_str}, Indirizzo: {indirizzo_str}"


class Afferenza:
    _data_afferenza: date  # <<immutabile>>, noto alla nascita
    _impiegato: Impiegato  # <<immutabile>>, noto alla nascita
    _dipartimento: Dipartimento  # <<immutabile>>, noto alla nascita

    def __init__(self, data_afferenza: date, impiegato: Impiegato, dipartimento: Dipartimento) -> None:

        self._data_afferenza = data_afferenza
        self._impiegato = impiegato
        self._dipartimento = dipartimento

    def get_data_afferenza(self) -> date:

        return self._data_afferenza

    def get_impiegato(self) -> Impiegato:

        return self._impiegato

    def get_dipartimento(self) -> Dipartimento:

        return self._dipartimento
    
    def get_nome_dipartimento(self) -> str:

        return self._dipartimento.get_nome()

    def __eq__(self, other) -> bool:

        if not isinstance(other, Afferenza):
            return False

        return (self._data_afferenza, self._impiegato, self._dipartimento) == (other._data_afferenza, other._impiegato, other._dipartimento)


class Coinvolto:
    # È una classe 'factory': non ha oggetti suoi,
    # serve solo a creare oggetti di un'altra classe (in questo caso, di _link)
    @classmethod
    def add(cls, impiegato: Impiegato, progetto: Progetto) -> "_link_imp_prog":

        link_imp_prog = cls._link_imp_prog(impiegato, progetto)

        impiegato.add_link_coinvolto(link_imp_prog) # deve essere un metodo in Impiegato che registra il link nell'impiegato

        progetto.add_link_coinvolto(link_imp_prog) # deve essere un metodo in Progetto che registra il link nel Progetto

        return link_imp_prog

    @classmethod
    def remove(cls, link_imp_prog: "_link_imp_prog") -> None:

        link_imp_prog.impiegato().remove_link_coinvolto(link_imp_prog)

        link_imp_prog.progetto().remove_link_coinvolto(link_imp_prog)

        del link_imp_prog

    class _link_imp_prog:
        # ogni oggetto di questa class rappresenta un link
        # dell'associazione 'coinvolto', cioè una coppia
        #  (Impiegato, Progetto)
        _impiegato: Impiegato   # immutabile
        _progetto: Progetto     # immutabile

        def __init__(self, impiegato: Impiegato, progetto: Progetto) -> None:
            self._impiegato = impiegato
            self._progetto = progetto

        def impiegato(self) -> Impiegato:

            return self._impiegato

        def progetto(self) -> Progetto:

            return self._progetto


if __name__ == "__main__":
    print("=== CREAZIONE IMPIEGATI ===")
    alice = Impiegato("alice", "rossi", date(1990, 5, 17), RealGZ("3000.00"))
    biagio = Impiegato("biagio", "verdi", date(1985, 9, 12), RealGZ("3500.00"))
    print(alice)
    print(biagio)

    print("\n=== CREAZIONE TELEFONI ===")
    tel_hr = Telefono("06", "2025389")
    tel_it = Telefono("06", "2123119")
    print(tel_hr)
    print(tel_it)

    print("\n=== CREAZIONE DIPARTIMENTI ===")
    hr = Dipartimento("Risorse Umane", tel_hr, "Via Roma 10")
    it = Dipartimento("Informatica", tel_it, "Via Milano 20")
    print(hr)
    print(it)

    print("\n=== CREAZIONE AFFERENZE ===")
    aff1 = Afferenza(date(2020, 1, 15), alice, hr)
    aff2 = Afferenza(date(2021, 6, 30), biagio, it)
    print(f"Afferenza di {aff1.get_impiegato().get_nome()} al dipartimento {aff1.get_dipartimento().get_nome()} dal {aff1.get_data_afferenza()}")
    print(f"Afferenza di {aff2.get_impiegato().get_nome()} al dipartimento {aff2.get_dipartimento().get_nome()} dal {aff2.get_data_afferenza()}")

    print("\n=== TEST COINVOLTO ===")
pegaso = Progetto("pegaso", RealGZ("100000.00"))
andromeda = Progetto("andromeda", RealGZ("75000.00"))
print(pegaso)
print(andromeda)

# Aggiungo coinvolgimenti
link1 = Coinvolto.add(alice, pegaso)
link2 = Coinvolto.add(biagio, pegaso)
link3 = Coinvolto.add(alice, andromeda)

print(f"\nCoinvolgimenti di {alice.get_nome()}:")
for c in alice.get_coinvolgimenti():
    print(f"- {c.progetto().get_nome()}")

print(f"\nCoinvolgimenti di {biagio.get_nome()}:")
for c in biagio.get_coinvolgimenti():
    print(f"- {c.progetto().get_nome()}")

print(f"\nCoinvolgimenti su {pegaso.get_nome()}:")
for c in pegaso.get_coinvolgimenti():
    print(f"- {c.impiegato().get_nome()}")

print(f"\nCoinvolgimenti su {andromeda.get_nome()}:")
for c in andromeda.get_coinvolgimenti():
    print(f"- {c.impiegato().get_nome()}")

# Rimuovo un coinvolgimento
Coinvolto.remove(link3)
print(f"\nRimosso coinvolgimento tra {alice.get_nome()} e {andromeda.get_nome()}")

print(f"\nCoinvolgimenti aggiornati di {alice.get_nome()}:")
for c in alice.get_coinvolgimenti():
    print(f"- {c.progetto().get_nome()}")

print(f"\nCoinvolgimenti aggiornati su {andromeda.get_nome()}:")
for c in andromeda.get_coinvolgimenti():
    print(f"- {c.impiegato().get_nome()}")
