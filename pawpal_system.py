from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class Task:
    description: str
    duration: int  # minutes
    frequency: str
    scheduled_time: str  # Example: "09:00"
    due_date: date = field(default_factory=date.today)
    completed: bool = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return (
            f"{self.description} "
            f"({self.duration} min, {self.frequency}, {self.scheduled_time}) "
            f"[{status}]"
        )


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
        """Add a pet."""
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

    # -----------------------
    # STEP 2: Sorting
    # -----------------------
    def sort_by_time(self):
        tasks = self.collect_tasks()
        return sorted(tasks, key=lambda item: item[1].scheduled_time)

    # Keep your original method
    def sort_tasks(self):
        tasks = self.collect_tasks()
        return sorted(tasks, key=lambda item: item[1].duration)

    # -----------------------
    # STEP 2: Filtering
    # -----------------------
    def filter_by_pet(self, pet_name):
        return [
            (name, task)
            for name, task in self.collect_tasks()
            if name == pet_name
        ]

    def filter_by_status(self, completed=False):
        return [
            (name, task)
            for name, task in self.collect_tasks()
            if task.completed == completed
        ]

    # -----------------------
    # STEP 3: Recurring Tasks
    # -----------------------
    def create_next_occurrence(self, pet, task):

        if task.frequency == "Daily":
            next_task = Task(
                description=task.description,
                duration=task.duration,
                frequency=task.frequency,
                scheduled_time=task.scheduled_time,
                due_date=task.due_date + timedelta(days=1)
            )
            pet.add_task(next_task)

        elif task.frequency == "Weekly":
            next_task = Task(
                description=task.description,
                duration=task.duration,
                frequency=task.frequency,
                scheduled_time=task.scheduled_time,
                due_date=task.due_date + timedelta(days=7)
            )
            pet.add_task(next_task)

    def mark_task_complete(self, pet, task):
        task.mark_complete()
        self.create_next_occurrence(pet, task)

    # -----------------------
    # STEP 4: Conflict Detection
    # -----------------------
    def detect_conflicts(self):

        warnings = []

        tasks = self.collect_tasks()

        for i in range(len(tasks)):
            for j in range(i + 1, len(tasks)):

                task1 = tasks[i][1]
                task2 = tasks[j][1]

                if task1.scheduled_time == task2.scheduled_time:

                    warnings.append(
                        f"Conflict: "
                        f"{tasks[i][0]}'s '{task1.description}' "
                        f"and "
                        f"{tasks[j][0]}'s '{task2.description}' "
                        f"are both scheduled at "
                        f"{task1.scheduled_time}."
                    )

        return warnings

    def generate_schedule(self):
        return self.sort_by_time()

    def explain_plan(self):
        schedule = self.generate_schedule()

        explanation = "Today's Schedule:\n"

        for pet_name, task in schedule:
            explanation += (
                f"- {pet_name}: "
                f"{task.description} "
                f"at {task.scheduled_time}\n"
            )

        conflicts = self.detect_conflicts()

        if conflicts:
            explanation += "\nWarnings:\n"
            for warning in conflicts:
                explanation += f"- {warning}\n"

        return explanation