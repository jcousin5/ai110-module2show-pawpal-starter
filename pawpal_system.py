from dataclasses import dataclass, field
from typing import Optional

import pawpal_system

print(pawpal_system.__file__)

@dataclass
class Task:

    description: str
    duration: int  # minutes
    frequency: str
    completed: bool = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.description} ({self.duration} min, {self.frequency}) [{status}]"


@dataclass
class Pet:

    name: str
    species: str
    age: int
    tasks: list = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, task: Task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks


class Owner:

    def __init__(self, name: str):
        self.name = name
        self.pets = []

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def remove_pet(self, pet: Pet):
        if pet in self.pets:
            self.pets.remove(pet)

    def get_all_tasks(self):
        tasks = []

        for pet in self.pets:
            for task in pet.tasks:
                tasks.append((pet.name, task))

        return tasks


class Scheduler:

    def __init__(self, owner: Owner):
        self.owner = owner

    def collect_tasks(self):
        return self.owner.get_all_tasks()

    def sort_tasks(self):
        tasks = self.collect_tasks()
        return sorted(tasks, key=lambda item: item[1].duration)

    def generate_schedule(self):
        return self.sort_tasks()

    def explain_plan(self):
        return 