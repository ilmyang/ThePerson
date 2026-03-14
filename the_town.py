"""Add yourself as a Person instance here!"""

from src.person import Person

if __name__ == "__main__":
    
    morpheus = Person(
        name="Morpheus",
        gender="male",
        occupation="developer on GitHub"
    )
    morpheus.introduce()
