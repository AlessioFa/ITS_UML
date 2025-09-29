from datetime import datetime
"""Partendo dal diagramma delle classi ristrutturato, implementare in Python le seguenti classi con i relativi tipi di dato e link:

    Utente
    UtentePrivato
    Bid
    Asta
    asta_bid
    bid_ut
"""

"""
Utente

username: str <<imm>> {id}
registrazione: datetime <<imm>>

poi due operazioni 

popolarità(i: DataOra): Popolarità
affidabilità(i: DataOra): RealZO

"""

class Utente:

    _username: str  # noto alla nascita <<imm>> {id}
    _registrazione: datetime  # noto alla nascita <<imm>>

    def __init__(self, username: str, registrazione: datetime) -> None:
        
        if not username:
            raise ValueError("Username non può essere vuoto.")
        
        if not registrazione:
            raise ValueError("La registrazione non può essere vuota.")
        
        self._username = username
        self._registrazione = registrazione

    def get_username(self) -> str:

        return self._username
    
    def get_registrazione(self) -> datetime:

        return self._registrazione
    
    def __eq__(self, other):

        if not isinstance(other, Utente):
            
            return False
        
        return self._username == other._username
    
    def __hash__(self) -> int:

        return self._username 

        



        