from typing import TextIO
from datetime import datetime


class Person:
    """A class to represent a person."""

    def __init__(
        self,
        name: str | None = None,
        age: int | None = None,
        gender: str | None = None,
        height: float | None = None,
        nationality: str | None = None,
        occupation: str | None = None,
        birthday_date: datetime | None = None,
        married_date: datetime | None = None,
        graduation_date: datetime | None = None,
        death_date: datetime | None = None,
    ) -> None:
        """Initialize the person's attributes."""
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.nationality = nationality
        self.occupation = occupation
        self.birthday_date = birthday_date
        self.married_date = married_date
        self.graduation_date = graduation_date
        self.death_date = death_date

    def greet(self) -> None:
        """Do a simple greeting and introduction."""
        self.say(f"Hello! My name is {self.name}.")

    @staticmethod
    def say(*args: object,
            sep: str | None = " ",
            end: str | None = "\n",
            file: TextIO | None = None,
            flush: bool = False) -> None:
        """Say a word, phrase, sentence or paragraph."""
        print(*args, sep=sep, end=end, file=file, flush=flush)

    def introduce(self) -> None:
        """Print a full self-introduction using the person's attributes."""
        intro = f"Hi, my name is {self.name}."
        if self.age is not None:
            intro += f" I am {self.age} years old."
        if self.gender is not None:
            intro += f" I identify as {self.gender}."
        self.say(intro)

    def celebrate(
        self,
        day: str = "birthday",
        check_date: bool = True,
        message: str | None = None,
    ) -> None:
        """Celebrate a special day for the person.

        Args:
            day: The name of the celebration (e.g. 'birthday', 'married').
                 Must match an existing attribute like 'birthday_date'.
            check_date: If True, checks whether today's date matches the
                        celebration date before printing the message.
            message: A custom message to print. If None, a default message
                     is used.

        Raises:
            AttributeError: If the celebration day attribute does not exist.
        """
        attr = f"{day}_date"
        if not hasattr(self, attr):
            raise AttributeError(
                f"'{day}' is not a recognised celebration. "
                f"Expected an attribute named '{attr}'."
            )

        celebration_date: datetime | None = getattr(self, attr)
        today = datetime.today()

        default_message = message or f"Happy {day.capitalize()}, {self.name}! 🎉"
        not_today_message = (
            f"Today is not {self.name}'s {day} yet, but it's coming soon!"
        )

        if check_date:
            if (
                celebration_date is not None
                and today.month == celebration_date.month
                and today.day == celebration_date.day
            ):
                self.say(default_message)
            else:
                self.say(not_today_message)
        else:
            self.say(default_message)