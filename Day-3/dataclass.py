from dataclasses import dataclass

@dataclass
class person:
    name: str
    age: int
    profession: str

Person = person("krish", 17, "SE")
Person