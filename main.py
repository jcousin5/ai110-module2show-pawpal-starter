from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Joshua")

dog = Pet("Buddy", "Dog", 5)
cat = Pet("Luna", "Cat", 3)

dog.add_task(Task("Morning Walk", 30, "Daily"))
dog.add_task(Task("Feed Breakfast", 10, "Daily"))
cat.add_task(Task("Brush Fur", 15, "Weekly"))

owner.add_pet(dog)
owner.add_pet(cat)

scheduler = Scheduler(owner)

print("Today's Schedule")
print("-" * 30)

for pet_name, task in scheduler.generate_schedule():
    print(f"{pet_name}: {task}")
