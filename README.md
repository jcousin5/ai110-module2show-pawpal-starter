# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

ssbssjosh@Joshuas-MacBook-Air ai110-module2show-pawpal-starter % /usr/local/bin/python3 /Users/ssbssjosh/Downloads/ai110-module2sho
w-pawpal-starter/main.py
/Users/ssbssjosh/Downloads/ai110-module2show-pawpal-starter/pawpal_system.py
Today's Schedule
------------------------------
Buddy: Feed Breakfast (10 min, Daily) [✗]
Luna: Brush Fur (15 min, Weekly) [✗]
Buddy: Morning Walk (30 min, Daily) [✗]

## 🧪 Testing PawPal+
## Testing PawPal+

Run the automated tests with:

```bash
python3 -m pytest
```

The test suite verifies:

- Adding tasks to pets
- Sorting tasks by scheduled time
- Daily recurring task creation
- Conflict detection
- Filtering tasks by pet

Example successful test run:

```text
============================= test session starts =============================
platform darwin -- Python 3.14.6
collected 5 items

tests/test_pawpal.py .....                            [100%]

============================== 5 passed in 0.03s ==============================
```

**Confidence Level:** ⭐⭐⭐⭐⭐ (5/5)

The automated tests cover the core scheduling functionality, including sorting, filtering, recurring tasks, and conflict detection, providing confidence that the system behaves as expected.
## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

## Smarter Scheduling

### Sorting
Implemented in Scheduler.sort_by_time()

### Filtering
Implemented in Scheduler.filter_by_pet() and Scheduler.filter_completed()

### Conflict Detection
Implemented in Scheduler.detect_conflicts()

### Recurring Tasks
Implemented using Task frequency and Scheduler recurring task logic.

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

### Main UI Features

- Add pets
- Create care tasks
- Assign task times
- Generate a daily schedule
- View conflict warnings
- Display scheduled tasks

### Example Workflow

1. Enter an owner name.
2. Add a pet.
3. Create several care tasks.
4. Generate the daily schedule.
5. Review tasks sorted by time.
6. Resolve any conflict warnings displayed by the scheduler.

## Features

- Add multiple pets
- Create daily and weekly care tasks
- Automatically sort tasks by scheduled time
- Filter tasks by pet and completion status
- Detect scheduling conflicts
- Automatically generate recurring daily and weekly tasks
- Display today's schedule in chronological order

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
