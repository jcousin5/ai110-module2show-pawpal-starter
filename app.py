import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler


# -----------------------------
# Application Memory
# -----------------------------
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Default Owner")


st.set_page_config(
    page_title="PawPal+",
    page_icon="🐾",
    layout="centered"
)


# -----------------------------
# Title
# -----------------------------
st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to PawPal+!

PawPal+ helps pet owners organize care tasks and create schedules
for their pets.
"""
)


# -----------------------------
# Owner and Pet Section
# -----------------------------
st.divider()

st.subheader("Add Pet")

owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox(
    "Species",
    ["dog", "cat", "other"]
)
age = st.number_input(
    "Pet age",
    min_value=0,
    value=1
)


if st.button("Add Pet"):
    new_pet = Pet(
        name=pet_name,
        species=species,
        age=int(age)
    )

    st.session_state.owner.name = owner_name
    st.session_state.owner.add_pet(new_pet)

    st.success(f"{pet_name} added!")


# -----------------------------
# Display Pets
# -----------------------------
st.subheader("Your Pets")

if st.session_state.owner.pets:
    for pet in st.session_state.owner.pets:
        st.write(
            f"🐾 {pet.name} - {pet.species} ({pet.age} years old)"
        )
else:
    st.info("No pets added yet.")


# -----------------------------
# Add Tasks
# -----------------------------
st.divider()

st.subheader("Add Care Task")


if st.session_state.owner.pets:

    pet_choices = [
        pet.name for pet in st.session_state.owner.pets
    ]

    selected_pet_name = st.selectbox(
        "Choose pet",
        pet_choices
    )

    task_title = st.text_input(
        "Task title",
        value="Morning walk"
    )

    duration = st.number_input(
        "Duration (minutes)",
        min_value=1,
        max_value=240,
        value=20
    )

    frequency = st.selectbox(
        "Frequency",
        ["Daily", "Weekly", "Monthly"]
    )


    if st.button("Add Task"):

        selected_pet = next(
            pet for pet in st.session_state.owner.pets
            if pet.name == selected_pet_name
        )

        new_task = Task(
            description=task_title,
            duration=int(duration),
            frequency=frequency
        )

        selected_pet.add_task(new_task)

        st.success(
            f"Task added for {selected_pet.name}"
        )

else:
    st.info("Add a pet before creating tasks.")


# -----------------------------
# Display Tasks
# -----------------------------
st.divider()

st.subheader("Current Tasks")

all_tasks = st.session_state.owner.get_all_tasks()

if all_tasks:
    for pet_name, task in all_tasks:
        st.write(
            f"🐾 {pet_name}: {task}"
        )
else:
    st.info("No tasks added yet.")


# -----------------------------
# Generate Schedule
# -----------------------------
st.divider()

st.subheader("Build Schedule")


if st.button("Generate Schedule"):

    scheduler = Scheduler(
        st.session_state.owner
    )

    schedule = scheduler.generate_schedule()

    st.success("Schedule created!")

    for pet_name, task in schedule:
        st.write(
            f"📅 {pet_name}: {task.description} "
            f"({task.duration} minutes)"
        )
        