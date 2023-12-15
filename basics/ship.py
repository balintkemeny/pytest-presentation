from dataclasses import dataclass, field

@dataclass
class Ship:
    name: str = field(default="", compare=False)
    speed: int = 0
    size: int = 0
