# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
The UML design is feed dog, walk dog, give medicine, groom cat, play fetch. The Owner stores user information and preferences. Each Pet stores its own care tasks. The Task class represents activities such as feeding or walking, including duration and priority. Finally, the Scheduler generates a daily plan based on available time and task priority. Separating these responsibilities makes the application easier to maintain and extend.
- What classes did you include, and what responsibilities did you assign to each?
The classes that I included into the design are Owner, Pet, Task and Schedule. The responsiblities that I assigned to each is: for Owner name, available time, preference, pets; for Pet name, species, age, tasks; for Task title, duration, priority, completed; for Schedule tasks. 

**b. Design changes**

- Did your design change during implementation?
Yes
- If yes, describe at least one change and why you made it.
One change that I made was Scheduler needs more context and so Scheduler now stores an Owner instead of only a task list


---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
The scheduler considers task duration as the main constraint when organizing tasks. It collects tasks from all pets and sorts them by the amount of time each task takes. The priority was decided based on creating an efficient schedule that helps complete shorter tasks first and makes it easier for an owner to manage multiple pet responsibilities.
- How did you decide which constraints mattered most?
Through identifying which would be most usefuk to improve user function with the app

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
One tradeoff the scheduler makes is that it prioritizes shorter tasks over other possible factors, such as urgency or personal preference. This is reasonable for this scenario because completing quick tasks first can help owners manage their time better, but a more advanced scheduler could add priority levels or deadlines in the future. My scheduler only checks for tasks that start at exactly the same time. It does not detect overlapping tasks with different start times. This keeps the algorithm simple while still identifying the most common scheduling conflicts.
- Why is that tradeoff reasonable for this scenario?
This approach keeps the scheduling algorithm simple, easy to understand, and efficient while still identifying the most common scheduling conflicts. For a basic pet care planner, checking for exact time conflicts provides useful feedback without adding unnecessary complexity. More advanced features, such as priority-based scheduling or overlap detection, could be added in a future version.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
I used AI tools to help with debugging, improving code structure, and adding documentation. AI was helpful for identifying issues with imports, explaining test failures, suggesting improvements, and creating clear one-line docstrings for methods. The most helpful prompts were questions about fixing errors, understanding why tests failed, and improving code readability.
- What kinds of prompts or questions were most helpful?
The helpful prompts were the ones that showed errors that were made in the code which allowed it to be easier to fix and improve
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
One moment where I did not accept an AI suggestion immediately was when debugging the module import error. I verified the suggestion by checking my project directory structure, moving to the project root, and running python3 -m pytest. I accepted the solution only after confirming that the tests passed successfully.
- How did you evaluate or verify what the AI suggested?
Checking against other AI and running the code in order to see what the error was and improve it.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
I tested that tasks can be marked as completed and that pets can successfully add tasks to their task list. Specifically, I tested the mark_complete() method and the add_task() method. These tests were important because they verified that the core functionality of the PawPal system worked correctly. They ensured that tasks could be updated and assigned to pets, which are essential features of the application.
- Why were these tests important?
These tests were important because it allowed for me to continuously edit and improve the code until it was at a optimal state in which all cases were passing.
**b. Confidence**

- How confident are you that your scheduler works correctly?
Very confident 
- What edge cases would you test next if you had more time?
N/A

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I was satified with being able to correct and be guided through improving the code and allowing AI to help me create a code and refine it to my personal needs.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
N/A

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
One thing that I learned about designing systems with AI is that there can always be improvements made and not to just settle with the first option just because it functions 