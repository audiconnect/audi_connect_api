"""Vehicle class"""

@dataclass
class Vehicle:
    id: str = None
    name: str = None
    model: str = None
    registration_date: str = None
    year: int = None
    VIN: str = None