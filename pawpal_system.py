from dataclasses import dataclass


@dataclass
class Pet:
    name: str
    species: str
    breed: str
    age: int

    def get_summary(self) -> str:
        pass


@dataclass
class Task:
    name: str
    priority: str
    duration: int
    recurring: bool
    category: str

    def get_summary(self) -> str:
        pass

    def is_high_priority(self) -> bool:
        pass


class Owner:
    def __init__(self, name: str, available_minutes: int, preferences: dict):
        self.name = name
        self.available_minutes = available_minutes
        self.preferences = preferences

    def get_preferences(self) -> dict:
        pass

    def get_summary(self) -> str:
        pass

    def can_fit_task(self, task: Task) -> bool:
        pass


class Scheduler:
    def __init__(self, owner: Owner, pet: Pet):
        self.owner = owner
        self.pet = pet
        self.tasks: list = []
        self.daily_plan = None

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, name: str) -> None:
        pass

    def generate_plan(self):
        pass

    def generate_explanation(self) -> str:
        pass

    def sort_tasks_by_priority(self) -> list:
        pass

    def calc_total_time(self) -> int:
        pass
