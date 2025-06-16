from typing import Self, Any

class Email:

    SEPARATOR = "@"
    VALID_DOMAINS = [".it", ".com"]

    def __init__(self, identity: str, provider: str, domain: str) -> None:
        if not isinstance(identity, str):
            raise TypeError("Identity must be a string.")

        if not isinstance(provider, str):
            raise TypeError("Provider must be a string.")

        if domain not in self.VALID_DOMAINS:
            raise ValueError(f"Invalid domain: {domain}.")

        self._identity = identity
        self._provider = provider
        self._domain = domain

    def get_separator(self) -> str:
        return self._SEPARATOR

    def get_identity(self) -> str:
        return self._identity

    def get_provider(self) -> str:
        return self._provider

    def get_domain(self) -> str:
        return self._domain

    def __str__(self) -> str:
        return f"{self._identity}{self.SEPARATOR}{self._provider}{self._domain}"

    def __hash__(self) -> int:
        return hash((self.get_identity(), self.get_provider(), self.get_domain()))

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Email):
            return False

        return (self.get_identity() == other.get_identity() and self.get_provider() == other.get_provider() and self.get_domain() == other.get_domain())


class Telefono:

    VALID_PREFIXES: str = ["+39", "+1", "+44", "+33", "+49"]
    MIN_NUM_LENGHT: int = 6

    def __init__(self, prefix: str, number: str) -> None:
        if prefix not in self.VALID_PREFIXES:
            raise ValueError(f"Prefix '{prefix}' is not valid.")

        if not isinstance(number, str) or not number.isdigit():
            raise ValueError("Phone number must contain digits only.")

        if len(number) < self.MIN_NUM_LENGHT or not number.isdigit():
            raise ValueError("Phone number has to be 6 digits long minimum.")

        self._prefix = prefix
        self._number = number

    def get_prefix(self) -> str:
        return self._prefix

    def get_number(self) -> str:
        return self._number

    def __str__(self) -> str:
        return f"{self._prefix}{self._number}"

    def __hash__(self) -> int:
        return hash((self.get_prefix(), self.get_number()))

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Telephone):
            return False

        return self.get_prefix() == other.get_prefix() and self.get_number() == other.get_number()


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
            and self.get_street_number()
    

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
