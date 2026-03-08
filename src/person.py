class Person:
    """A class to represent a person."""
    
    def __init__(self,
                 name: str | None = None,
                 age: int | None = None,
                 gender: str | None = None):
        """Initialize the person's attributes."""
        self.name = name
        self.age = age
        self.gender = gender
        
    def greet(self) -> None:
        """Do a simple greeting and introduction."""
        print(f'Hello! My name is {self.name}.')
        