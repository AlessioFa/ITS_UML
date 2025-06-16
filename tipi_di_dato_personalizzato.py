from typing import Self, Any



class Indirizzo:
    VALID_TYPES = ["Via", "Piazza", "Viale", "Corso"]
    MIN_CAP_LENGHT = 5

    def __init__(self, address_type: str, name: str, street_number: int, cap: str) -> None:
        if address_type not in self.VALID_TYPES:
            raise ValueError(f"Type: '{type}' is not valid.")
        
        if not isinstance(street_number, int):
            raise ValueError("Street number must contain digits only.")

        if len(cap) < self.MIN_CAP_LENGHT or not cap.isdigit():
            raise ValueError("The cap number has to be 5 digits long minimum.")

        self._address_type = address_type
        self._name = name
        self. _street_number = street_number
        self._cap = cap

    def get_address_type(self) -> str:
        return self._address_type

    def get_name(self) -> str:
        return self._name

    def get_street_number(self) -> int:
        return self._street_number

    def get_cap(self) -> str:
        return self._cap

    def __str__(self) -> str:
        return f"{self._address_type} {self._name} {self.street_number} {self._cap}"

    def __hash__(self):
        return hash((self.get_address_type(), self.get_name(), self. get_street_number(), self.get_cap()))

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Address):
            return False

        return self.get_address_type() == other.get_address_type() and self.get_name() == other.get_name() \
            and self.get_street_number() == other.get_street_number() and self.get_cap() == other.get_cap()


class CodiceFiscale:
    LENGHT = 16

    def __init__(self, codice_fiscale: str) -> None:
        if len(codice_fiscale) != self.LENGHT:
            raise ValueError("The codice fiscale must be 16 character long.")

        if not codice_fiscale.isalnum():
            raise ValueError("The codice fiscale must contain letters and digits only.")

        self._codice_fiscale = codice_fiscale.upper()

    def get_codice_fiscale(self) -> str:
        return self._codice_fiscale

    def __str__(self) -> str:
        return f"{self._codice_fiscale}"

    def __hash__(self):
        return hash(self.get_codice_fiscale())

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CodiceFiscale):
            return False

        return self.get_codice_fiscale() == other.get_codice_fiscale


class IntGEZ(int):
    # Tipo di dato specializzato Intero >= 0

    def __new__(cls, v: Self | int | float | str | bool) -> Self:

        value: int = super().__new__(cls, v)

        if value < 0:
            raise ValueError(f"The value {v} must be greater than or equal to zero")
        return value


class IntGZ(int):
    # Tipo di dato specializzato Intero > 0
     
    def __new__(cls, v: Self | int | float | str | bool) -> Self:
        value: int  = super().__new__(cls, v)
        if value <= 0:
            raise ValueError(f"The value {v} must be greater than zero")
        return value
    

class RealGZ(int):
    # Tipo di dato specializzato Intero > 0

    def __new__(cls, v: Self | int | float | str | bool) -> Self:

        value: int = super().__new__(cls, v)
        
        if value <= 0:
            raise ValueError(f"The value {v} must be greater than zero")
        return value
