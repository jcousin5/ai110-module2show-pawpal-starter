from datetime import date

from pawpal_system import Owner, Pet, Task, Scheduler


def test_add_task():
    pet = Pet("Buddy", "Dog", 5)

    task = Task(
        "Walk",
        30,
        "Daily",
        "09:00"
    )

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0] == task


def test_sort_by_time():
    owner = Owner("Josh")
    pet = Pet("Buddy", "Dog", 5)

    owner.add_pet(pet)

    task1 = Task(
        "Breakfast",
        10,
        "Daily",
        "09:00"
    )

    task2 = Task(
        "Walk",
        20,
        "Daily",
        "08:00"
    )

    pet.add_task(task1)
    pet.add_task(task2)

    scheduler = Scheduler(owner)

    schedule = scheduler.sort_by_time()

    assert schedule[0][1].description == "Walk"
    assert schedule[1][1].description == "Breakfast"


def test_daily_recurrence():
    owner = Owner("Josh")
    pet = Pet("Buddy", "Dog", 5)

    owner.add_pet(pet)

    task = Task(
        "Feed",
        10,
        "Daily",
        "08:00",
        due_date=date.today()
    )

    pet.add_task(task)

    scheduler = Scheduler(owner)

    scheduler.mark_task_complete(pet, task)

    assert len(pet.tasks) == 2

    new_task = pet.tasks[1]

    assert new_task.completed is False
    assert new_task.due_date == date.today().replace(
        day=date.today().day + 1
    ) or new_task.due_date > task.due_date


def test_conflict_detection():
    owner = Owner("Josh")
    pet = Pet("Buddy", "Dog", 5)

    owner.add_pet(pet)

    task1 = Task(
        "Breakfast",
        10,
        "Daily",
        "09:00"
    )

    task2 = Task(
        "Medicine",
        5,
        "Daily",
        "09:00"
    )

    pet.add_task(task1)
    pet.add_task(task2)

    scheduler = Scheduler(owner)

    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1


def test_filter_by_pet():
    owner = Owner("Josh")

    buddy = Pet("Buddy", "Dog", 5)
    luna = Pet("Luna", "Cat", 2)

    owner.add_pet(buddy)
    owner.add_pet(luna)

    buddy.add_task(
        Task(
            "Walk",
            20,
            "Daily",
            "08:00"
        )
    )

    luna.add_task(
        Task(
            "Feed",
            10,
            "Daily",
            "09:00"
        )
    )

    scheduler = Scheduler(owner)

    buddy_tasks = scheduler.filter_by_pet("Buddy")

    assert len(buddy_tasks) == 1
    assert buddy_tasks[0][0] == "Buddy"