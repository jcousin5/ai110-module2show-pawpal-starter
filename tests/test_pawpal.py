from pawpal_system import Pet, Task


def test_mark_complete():
    task = Task("Feed Buddy", 10, "Daily")
    task.mark_complete()
    assert task.completed is True


def test_add_task():
    pet = Pet("Buddy", "Dog", 5)
    task = Task("Walk", 30, "Daily")

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0] == task

    