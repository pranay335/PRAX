# PRAX --- Personal AI Execution Agent --- Vision & Project Definition

### PART A — Product Vision (Sections 1-6)

## 1. Project Vision

PRAX is a personal AI execution system designed for students and early-career
professionals who struggle to manage multiple goals, commitments, deadlines,
and routines. Instead of functioning as a passive task manager, PRAX
continuously understands the user's commitments, available time, priorities,
and actual progress to help decide what should happen next, schedule
appropriate actions, follow up when necessary, and adapt the plan when reality
changes. The system is designed to reduce the user's cognitive overhead while
keeping the user in control of consequential decisions and personal data.

The goal is to build a system that can:

-   Remember tasks, commitments, goals, routines, and important dates
    that the user explicitly gives it.
-   Understand the user's daily schedule and available time.
-   Turn goals into practical tasks and schedules.
-   Remind the user at the right time.
-   Follow up on whether a task was completed.
-   Adapt the plan when tasks are skipped, delayed, or priorities
    change.
-   Help the user stay focused on study, projects, DSA, Agentic AI
    learning, aptitude, LinkedIn activity, and other personal goals.
-   Eventually interact through chat and voice.
-   Generate useful outputs such as LinkedIn drafts from things the user
    actually learned.
-   Maintain progress history and provide daily/weekly reviews.
-   Use agentic reasoning, tools, workflows, memory, RAG, multi-agent
    collaboration, and human approval where appropriate.

The project should be developed as a **real usable system**, not as a
collection of disconnected Agentic AI demos.

------------------------------------------------------------------------

## 2. The Core Problem

The user has many things to manage:

-   College
-   Internship/work
-   DSA
-   Agentic AI learning
-   Projects
-   Aptitude preparation
-   LinkedIn activity
-   Assignments
-   Deadlines
-   Calls/messages to make
-   Personal reminders
-   Recurring habits

### Core User Pain

The user's commitments are scattered across conversations, notes,
calendar events, mental reminders, and task lists.

The user must repeatedly answer:

-   What do I need to do?
-   What should I do next?
-   When should I do it?
-   What did I miss?
-   How should I adjust my plan?

PRAX aims to reduce this repeated cognitive work.

The problem is not simply remembering a task.

The larger problem is:

> **Knowing what to do next, doing it on time, staying consistent, and
> adapting when the original plan changes.**

A normal reminder application only says:

> "Do X at 8 PM."

Our system should eventually be able to reason:

> "You planned DSA at 8 PM, but you skipped yesterday and your project
> deadline is approaching. You have 90 minutes available tonight. I
> recommend 45 minutes of project work followed by 45 minutes of DSA. I
> moved the remaining DSA session to tomorrow."

That is the type of behavior we want to learn and implement.

------------------------------------------------------------------------

## 3. Target User & Persona

Primary user: A student or early-career professional with multiple competing
goals who frequently struggles with planning, consistency, and
follow-through.

-   V1 → Student / early professional.
-   V2 → General individual.

Not designing for teams, enterprises, or managers.

------------------------------------------------------------------------

## 4. Product Concept

Working name:

### PRAX --- Personal AI Execution Agent

Possible alternative names can be decided later.

### Core description

> PRAX reduces the cognitive effort required to decide, remember, schedule,
> and follow through on personal commitments.

------------------------------------------------------------------------

## 5. What the User Should Be Able to Say

The system should accept natural language instead of requiring forms for
every action.

Examples:

### Task

> "I need to submit my AI assignment on Friday."

The system should create:

-   Task: AI assignment
-   Deadline: Friday
-   Status: Pending
-   Priority: inferred or requested

### Reminder

> "Remind me tomorrow at 8 PM to solve LeetCode 238."

The system creates a reminder.

### Recurring task

> "Every evening at 9 I want to spend an hour on DSA."

The system creates a recurring activity.

### Memory

> "Remember that I need to call my project guide next week."

The system stores the commitment.

### Schedule

> "I have two hours free tonight. What should I work on?"

The agent checks:

-   Pending tasks
-   Deadlines
-   Goals
-   Priorities
-   Existing schedule
-   Previous progress

and recommends a plan.

### Rescheduling

> "I can't do DSA tonight."

The agent should consider the remaining workload and reschedule rather
than simply deleting the task.

------------------------------------------------------------------------

## 6. A Normal Tuesday

A timeline showing a realistic day with PRAX:

``` text
07:30  PRAX sends daily plan via message
10:00  No intervention — user is at work
13:00  Optional check-in during user's configured window
20:30  PRAX detects project deadline approaching
21:00  Focus session starts — PRAX notifies
21:50  User reports "blocked"
21:55  PRAX suggests a smaller sub-task
23:00  PRAX sends evening review
23:05  PRAX proposes tomorrow's plan
```

------------------------------------------------------------------------

### PART B — Core Capabilities (Sections 7-13)

## 7. Personal Task Management

Store and manage:

-   Tasks
-   Deadlines
-   Priorities
-   Status
-   Recurring tasks
-   Subtasks
-   Important dates
-   Calls to make
-   Things to remember

Possible statuses:

-   Pending
-   In progress
-   Completed
-   Skipped
-   Deferred
-   Cancelled

------------------------------------------------------------------------

## 8. Task & Commitment Model

Define the spectrum: Idea → Intention → Planned Task → Committed Task →
Hard Deadline.

PRAX should not treat every casual statement as an obligation.

Example: "Maybe I'll study DSA tonight" vs "I will study DSA at 9 PM" vs
"I have to finish DSA before tomorrow."

PRAX should understand uncertainty and ask clarifying questions when the
user is vague ("Do you have a fixed deadline, or should I help you choose
one?").

------------------------------------------------------------------------

## 9. Daily Schedule

The agent should understand:

-   Fixed schedule
-   Available/free time
-   Existing events
-   Study sessions
-   Work/internship
-   College
-   Personal commitments

It should generate a practical daily execution plan.

Example:

``` text
07:00  Wake up
08:00  Travel
10:00  Internship
19:00  Leave
20:30  Home
21:00  Dinner
22:00  DSA — 45 min
22:45  Agentic AI — 60 min
23:45  LinkedIn — 20 min
```

The schedule should be adaptable rather than permanently fixed.

------------------------------------------------------------------------

## 10. Accountability

The system should actively follow up.

Example:

``` text
10:00 PM

Agent:
"Your DSA session is starting."

User:
"Not now."

Agent:
"Okay. You have 45 minutes available tomorrow.
Should I move it to tomorrow at 10:30 PM?"
```

After the planned session:

> "Did you complete the session?"

Possible responses:

-   DONE
-   SKIPPED
-   PARTIALLY DONE
-   BLOCKED
-   RESCHEDULE

The response updates the user's state.

### Why did I fail? tracking

PRAX should also ask **why** a task was skipped. Possible failure reasons
include:

-   Too tired
-   No time
-   Task too difficult
-   Forgot
-   Distracted
-   Higher priority appeared

This data feeds into Behavioral Learning over time.

------------------------------------------------------------------------

## 11. Adaptive Planning

This is one of the most important agentic capabilities.

The system should not simply create a plan once.

It should continuously compare:

``` text
PLAN
vs
ACTUAL PROGRESS
```

Example:

``` text
Goal:
Complete 15 DSA problems this week

Current:
8 completed

Remaining:
7

Days:
3
```

The agent can determine whether the current plan is realistic.

If the user falls behind:

``` text
Original plan
      ↓
Progress check
      ↓
Behind schedule
      ↓
Re-plan
      ↓
Updated schedule
```

The agent should explain why it changed the plan.

### Explainability

When PRAX makes a scheduling decision, it must explain why in simple
language.

Example: "Why did you move my DSA session?" → "You had 45 minutes available
tomorrow, your project deadline is earlier, and DSA has no fixed deadline."

------------------------------------------------------------------------

## 12. Scheduling & Conflict Rules

PRAX must distinguish between: Fixed events, Flexible tasks, and Optional
activities.

Conflict resolution policy: When a new commitment conflicts with an existing
one, check if the existing task is flexible. If yes, move it. If no, ask
the user.

PRAX should never silently rearrange important commitments.

Handle uncertainty: "Remind me tomorrow morning" → use the user's
configured morning window or ask.

------------------------------------------------------------------------

## 13. Focus Sessions

The system should support focused work sessions.

Example:

> "Start a 60-minute DSA focus session."

The system records:

-   Task
-   Start time
-   End time
-   Planned duration
-   Actual duration
-   Completion
-   Notes/blockers

At the end:

> "What did you accomplish?"

This creates a history of actual work, not just planned work.

------------------------------------------------------------------------

### PART C — Agent Behavior & Boundaries (Sections 14-21)

## 14. Notification & Interruption Policy

The agent should eventually support:

-   Scheduled reminders
-   Deadline alerts
-   Missed-task follow-ups
-   Daily plan
-   Evening review
-   Weekly review
-   Voice calls
-   Push notifications
-   Email
-   Potentially WhatsApp through an official/appropriate API

Important distinction:

> **The agent decides what should happen; a scheduler/notification
> system executes it at the correct time.**

The LLM should not be responsible for "waiting until 10 PM."

### Formal Policy

Optimize for useful intervention, not maximum intervention.

Multi-stage approach:

-   Single gentle nudge on missed check-in.
-   Secondary follow-up after 4-5 hours, respecting sleep (12 AM - 8 AM
    quiet zone).
-   Task downscaling if user feels lazy or distracted.
-   User can request quiet mode to pause all notifications.
-   PRAX should learn when the user is typically busy and reduce
    interruptions during those windows.

### Proactive Habit Maintenance / Daily Standup

To prevent the user from losing the habit of tracking tasks (the "diary
problem"), the agent proactively reaches out via message or call. It asks
questions like, "Do you have any new plans or tasks to add today?" to
ensure consistent engagement without relying on the user's initial
motivation.

------------------------------------------------------------------------

## 15. Autonomy & Permission Model

The system should not be fully autonomous from the beginning.

We define 4 levels of autonomy:

-   Level 0 — Read: Can inspect tasks and schedule.
-   Level 1 — Suggest: Can recommend changes.
-   Level 2 — Low-risk Action: Can create reminders and tasks.
-   Level 3 — User Approval Required: For sending messages, publishing,
    deleting data, external communication, calls, and other consequential
    actions.

Example:

``` text
Agent wants to publish LinkedIn post
        ↓
Draft generated
        ↓
User approval
        ↓
Publish
```

The user remains in control.

------------------------------------------------------------------------

## 16. Privacy & Data Ownership

Privacy is a core design requirement.

We explicitly decided **not** to build a system that blindly reads a
user's personal WhatsApp conversations and sends everything to an LLM.

WhatsApp conversations can contain:

-   Phone numbers
-   Names
-   Personal conversations
-   Photos
-   Grades
-   Sensitive information
-   Information about other people
-   Completely unrelated content

Therefore, the system should use data minimization.

Preferred approaches:

### MVP

-   User manually enters information
-   User forwards only relevant messages
-   User uploads screenshots
-   User uploads PDFs/notices
-   User forwards relevant emails

### Later

-   Official institutional communication channels
-   Official APIs
-   Local privacy filtering
-   PII detection/redaction before external LLM processing (sensitive data
    boundary concept)

Principle:

> **Only send the minimum information required to perform the task.**

### User Data Ownership

The user has the following rights:

-   Export all data
-   Delete all data
-   Delete individual memories
-   See connected services
-   Disconnect services
-   Know what was sent to external AI providers

------------------------------------------------------------------------

## 17. User-Facing Memory

Memory should be separated into different categories.

### Structured memory

Facts such as:

-   Task
-   Deadline
-   Goal
-   Schedule
-   Habit

Stored in the database.

### Short-term state

Current conversation/session state.

### Long-term semantic memory

Useful historical information that benefits from semantic search.

### RAG knowledge

External or uploaded documents that the user wants the system to
reference.

We should not treat all four as the same thing.

### User-Facing Memory

The user should be able to ask "What do you remember about me?" and say
"Forget that."

Memory operations: View, Edit, Delete, Forget All.

------------------------------------------------------------------------

## 18. Behavioral Learning

The agent learns the user's personal working style over time. If the user
consistently skips 10 PM DSA sessions, it learns to suggest them for 8 AM
instead. It adjusts time estimates based on historical completion times
and remembers what distracts the user.

### Behavioral Learning Principle

PRAX should only learn behavioral patterns necessary to improve
planning, scheduling, or intervention. The user should be able to
inspect, correct, or disable learned patterns.

------------------------------------------------------------------------

## 19. Failure & Recovery Scenarios

-   Wrong date interpretation → User can correct it.
-   Duplicate task detection → PRAX flags possible duplicates.
-   Notification service failure → Record failure and retry.
-   LLM unavailable → Core task CRUD should continue where possible.
-   Conflicting instructions → PRAX recognizes and asks for clarification.

------------------------------------------------------------------------

## 20. Non-Goals

PRAX will NOT:

-   Be a general-purpose chatbot.
-   Read private communications without explicit consent.
-   Make important decisions without user control.
-   Automatically publish content without approval.
-   Replace a calendar, email, or messaging service internally.
-   Use multi-agent architecture just for the sake of being "agentic."
-   Store everything in vector memory.
-   Constantly interrupt the user.
-   Optimize for maximum notifications.
-   Become a surveillance system for the user.

------------------------------------------------------------------------

## 21. Product Boundaries

PRAX manages execution --- it does not own the user's life.

PRAX can:

-   Recommend
-   Schedule
-   Remind
-   Track
-   Adapt
-   Ask

PRAX cannot:

-   Decide user's priorities without context
-   Override fixed commitments
-   Manipulate the user
-   Spam the user
-   Hide decisions
-   Make consequential decisions without approval

------------------------------------------------------------------------

### PART D — Supporting Capabilities (LinkedIn, Voice) (Section 22)

## 22. Supporting Modules

### LinkedIn Activity

The user wants to remain active on LinkedIn while learning.

The agent can maintain a learning-to-content workflow.

Example:

``` text
User learns:
"ReAct Agents"

        ↓

Learning/Activity Agent

        ↓

Generate LinkedIn draft

        ↓

User reviews

        ↓

User approves

        ↓

Publish manually or through an approved integration
```

The system should never invent achievements or claim that the user built
something they did not actually build.

The first version should generate drafts only.

### Voice Interaction

Later, the user should be able to say:

> "Remind me tomorrow at 8 AM to call my project guide."

Pipeline:

``` text
Voice
  ↓
STT
  ↓
Agent
  ↓
create_reminder()
  ↓
Database
```

The agent responds through TTS.

Possible future voice interaction:

> "What do I need to do tonight?"

> "You have three tasks. Your highest-priority task is the AI project
> report, due tomorrow."

------------------------------------------------------------------------

### PART E — Product Philosophy & Success (Sections 23-24)

## 23. Product Philosophy

### Principle 1 --- User first

The system should solve a real problem for the person using it.

### Principle 2 --- Agent, not chatbot

The system should be able to:

-   Decide
-   Use tools
-   Act
-   Observe results
-   Adapt

### Principle 3 --- Automation with boundaries

Not every action should be autonomous.

### Principle 4 --- Privacy by design

Only necessary information should be processed.

### Principle 5 --- Measurable value

Track whether the system actually saves time and improves task
completion.

### Principle 6 --- Build incrementally

Every feature should be added because it solves a real requirement.

### Principle 7 --- Learn through implementation

Agentic AI concepts should be learned by implementing them in this
project rather than studying them only as theory.

### Principle 8 --- Useful intervention, not maximum intervention

Optimize for useful intervention, not maximum intervention.

### Principle 9 --- Explainability

Important decisions made by PRAX should be explainable in simple language.

------------------------------------------------------------------------

## 24. Success Metrics

The project is successful when the user can stop manually managing their
day.

Instead of maintaining separate:

-   Notes
-   To-do lists
-   Reminders
-   Study plans
-   Habit trackers
-   LinkedIn content lists
-   Deadline lists

the user can tell the agent what they need to accomplish.

The agent maintains the state and helps execute the plan.

The system should **reduce cognitive overhead**, not create another
productivity application that requires constant manual maintenance.

Concrete metrics:

-   Task completion rate (before vs after PRAX).
-   Planning accuracy (estimated vs actual duration).
-   Intervention effectiveness (reminder sent → task completed?).
-   Schedule quality (conflicts, reschedules, abandoned tasks).
-   User burden (how much manual work does PRAX itself create?).

Baseline will be established during the first 1-2 weeks of usage
before evaluating PRAX's impact. Example targets:

-   Task completion rate: +15% after 30 days.
-   Planning accuracy: estimated duration within ±30%.
-   User burden: less than 5 minutes/day of manual maintenance.

Final targets will be defined in the SRS.

------------------------------------------------------------------------

### PART F — Engineering Direction (Sections 25-28)

## 25. Agentic Architecture --- Future Engineering Direction

The system should eventually use multiple agentic patterns.

Introduce multiple agents only when a single agent becomes difficult to
maintain, reason about, secure, or evaluate.

These are implementation patterns under consideration, not product
requirements. PRAX's value is measured by whether it can understand
requests, decide what to do, execute safely, and adapt --- not by
which agentic pattern it uses internally.

## Tool Calling

Agents use controlled tools such as:

``` text
create_task()
get_tasks()
update_task()
complete_task()

create_event()
get_schedule()
move_task()

save_memory()
search_memory()

start_focus_session()
get_progress()

create_linkedin_draft()
```

The LLM decides which tool is appropriate; the tool performs the actual
operation.

------------------------------------------------------------------------

## Workflow

Some operations should use deterministic workflows.

Example:

``` text
Collect information
       ↓
Validate
       ↓
Calculate
       ↓
Generate
       ↓
Verify
       ↓
Human approval
       ↓
Execute
```

Workflows are useful when the sequence should be controlled.

------------------------------------------------------------------------

## Router

A router determines what type of request the user has.

``` text
User request
      ↓
Router
 ├── Task
 ├── Schedule
 ├── Study
 ├── Memory
 ├── LinkedIn
 ├── Progress
 └── General conversation
```

------------------------------------------------------------------------

## Supervisor

The supervisor coordinates specialized agents.

``` text
                    Supervisor
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
   Task Agent       Study Agent      Content Agent
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                     Verifier
```

------------------------------------------------------------------------

## Multi-Agent System

Specialized agents can collaborate when a request requires multiple
capabilities.

Example:

> "Plan my preparation for next week's AI exam while keeping my DSA and
> project work on track."

Possible agents:

``` text
Supervisor
    │
    ├── Study Agent
    ├── Planning Agent
    ├── Task Agent
    └── Progress Agent
```

------------------------------------------------------------------------

## ReAct

For tasks that require iterative reasoning:

``` text
Reason
  ↓
Choose tool
  ↓
Execute
  ↓
Observe
  ↓
Reason again
```

Example:

``` text
Check schedule
  ↓
Check deadlines
  ↓
Calculate available time
  ↓
Create plan
  ↓
Check for conflicts
  ↓
Adjust plan
```

------------------------------------------------------------------------

## RAG

RAG should be used for knowledge, not ordinary task storage.

Possible knowledge sources:

-   User's study notes
-   Course material
-   Project documentation
-   Personal learning notes
-   Saved reference documents

Example:

> "What did I learn about Supervisor Agents?"

The system retrieves relevant notes and answers using that information.

------------------------------------------------------------------------

## 26. Data Architecture

We should separate different kinds of information.

## Structured data

Use a relational database for:

``` text
Users
Tasks
Goals
Events
Schedules
Habits
Sessions
Notifications
Progress
Agent runs
```

## Semantic knowledge

Use a vector database for:

``` text
Study notes
Documents
Learning material
Project documentation
Long-form personal knowledge
```

Important distinction:

``` text
PostgreSQL / SQLite
=
What / When / Status / Relationships

Qdrant
=
Semantic knowledge / Meaning / Retrieval
```

------------------------------------------------------------------------

## 27. Recommended Technology Stack

## V1 --- Keep it simple

``` text
Python
FastAPI
SQLite
LLM API
APScheduler
```

Do not start with the entire production stack.

## Later

``` text
Python
FastAPI
LangGraph
PostgreSQL
Qdrant
Redis
React + Vite
Docker
STT
TTS
Notification APIs
```

Possible LLM providers:

-   OpenRouter
-   Gemini
-   OpenAI
-   Other compatible APIs

The LLM interface should be designed so the provider can be changed
without rewriting the application.

------------------------------------------------------------------------

## 28. Product vs Engineering vs Learning

Clarify the three goals of the project:

-   **Product:** What PRAX should do for the user.
-   **Engineering:** How we will build it (technology choices).
-   **Learning:** What Agentic AI concepts we expect to learn.

Principle: We should not add a feature only because we want to learn a
technology.

------------------------------------------------------------------------

### PART G — Development Roadmap (Sections 29-31)

## 29. Development Roadmap

## Phase 1 --- Agent with Task Tools

``` text
User
 ↓
Agent
 ↓
Tool
 ↓
Database
```

Implement:

``` text
create_task()
get_tasks()
update_task()
complete_task()
```

Learn:

-   LLM API
-   Prompting
-   Structured output
-   Tool calling
-   Function schemas
-   Tool execution
-   Error handling
```

------------------------------------------------------------------------

## Phase 2 --- Scheduler

``` text
Agent
 ↓
create_reminder()
 ↓
Scheduler
 ↓
Notification
```

Learn:

-   Scheduled jobs
-   Background execution
-   Time handling
-   Recurring tasks

------------------------------------------------------------------------

## Phase 3 --- Memory

Add:

-   User profile
-   Goals
-   Preferences
-   Task history
-   Progress

Learn the difference between state, database memory, and semantic
memory.

------------------------------------------------------------------------

## Phase 4 --- Planning

Build:

``` text
Goal
 ↓
Break into tasks
 ↓
Estimate effort
 ↓
Prioritize
 ↓
Schedule
```

------------------------------------------------------------------------

## Phase 5 --- Adaptive Planning

``` text
Plan
 ↓
Actual progress
 ↓
Detect deviation
 ↓
Re-plan
```

This is a major step toward a genuinely agentic system.

------------------------------------------------------------------------

## Phase 6 --- RAG

Add:

``` text
Study notes
Project notes
Documents
 ↓
Embeddings
 ↓
Qdrant
 ↓
Retriever
 ↓
Agent
```

------------------------------------------------------------------------

## Phase 7 --- Specialized Agents

Introduce:

``` text
Supervisor
 ├── Task Agent
 ├── Study Agent
 ├── Planning Agent
 ├── Content Agent
 └── Progress Agent
```

------------------------------------------------------------------------

## Phase 8 --- Verification

Add:

``` text
Agent output
 ↓
Verifier
 ↓
PASS / FAIL
 ↓
Re-plan if necessary
```

------------------------------------------------------------------------

## Phase 9 --- Voice

``` text
Microphone
 ↓
STT
 ↓
Agent
 ↓
Tool
 ↓
TTS
```

------------------------------------------------------------------------

## Phase 10 --- React Dashboard

Build:

-   Today's schedule
-   Tasks
-   Goals
-   Progress
-   Focus sessions
-   Upcoming deadlines
-   Agent activity
-   Weekly reports

------------------------------------------------------------------------

## Phase 11 --- Production Architecture

Potentially add:

``` text
PostgreSQL
Redis
Qdrant
Docker
Background workers
Authentication
Logging
Monitoring
Deployment
```

------------------------------------------------------------------------

## 30. First MVP

The first version should NOT contain:

-   Multi-agent architecture
-   Voice
-   WhatsApp
-   Complex RAG
-   React dashboard
-   Redis
-   PostgreSQL
-   Autonomous actions

The first working milestone should be:

> **"Remind me tomorrow at 8 PM to solve LeetCode 238."**

The system should:

``` text
Understand request
       ↓
Extract task/time
       ↓
Call create_task()
       ↓
Save task
       ↓
Schedule reminder
       ↓
At 8 PM
       ↓
Send notification
```

Then:

> **"I finished it."**

The system updates:

``` text
Task → Completed
```

That gives us the first complete agentic loop.

------------------------------------------------------------------------

## 31. Long-Term Vision

Eventually the system should operate like:

``` text
                         USER
                           │
                Chat / Voice / UI
                           │
                           ▼
                    ┌────────────┐
                    │ SUPERVISOR │
                    └─────┬──────┘
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
    Task Agent       Study Agent       Content Agent
        │                 │                 │
        ▼                 ▼                 ▼
    Task Tools          RAG             LinkedIn
        │                 │                 │
        └─────────────────┼─────────────────┘
                          ▼
                       Planner
                          │
                          ▼
                    Schedule/State
                          │
                          ▼
                       Verifier
                          │
                          ▼
                  Notifications/Voice
                          │
                          ▼
                         USER
                          │
                          ▼
                    Actual Progress
                          │
                          ▼
                    Re-planning
```

The ultimate loop is:

``` text
GOALS
  ↓
PLAN
  ↓
EXECUTE
  ↓
TRACK
  ↓
EVALUATE
  ↓
ADAPT
  ↓
EXECUTE AGAIN
```

------------------------------------------------------------------------

### PART H — Future Enhancements (Section 32)

## 32. Future Enhancements

Based on further discussion, the following advanced capabilities are
targeted for later phases to reduce cognitive overhead and make the
agent truly proactive:

1.  **Context-Aware Energy Scheduling**: Instead of just scheduling
    based on available time, the agent schedules based on cognitive
    load. For example, suggesting light reading after a heavy 4-hour
    coding session, rather than complex DSA tasks.

2.  **Proactive RAG & Deep Integrations**: Instead of the user manually
    searching for notes, the agent proactively provides context. By
    connecting to external sources (Google Drive, college websites, or a
    user-provided map of where things are stored), the agent
    automatically retrieves relevant links and documents.

3.  **Frictionless Brain Dump Inbox**: A feature to send messy,
    unstructured thoughts or voice notes. The agent automatically parses
    this into separate categorized tasks and schedules them during the
    next review.

4.  **Habit Stacking & Routines**: Managing flows instead of isolated
    tasks. If the user finishes a DSA problem, the agent guides them to
    the next micro-habit (e.g., spending 5 minutes adding the solution
    to notes).

5.  **Focus Mode Environment Control**: During a Focus Session, the
    agent interacts with the OS or integrations to block distractions
    like distracting websites or muting notifications.

6.  **Motivation & Gamification Tracking**: The agent actively tracks
    streaks and visualizes consistency, offering encouragement based on
    historical procrastination patterns. (Note: Secondary priority)

7.  **Execution Layer vs. Control Center Layer**: Moving away from a
    dashboard-only model. The Dashboard acts as a Control Center for
    weekly reviews. Daily execution happens via low-friction Push
    notifications (Telegram, Discord, or PWA) to interrupt the user
    when needed without requiring them to open an app.

------------------------------------------------------------------------

### PART I — Current Scope (Section 33)

## 33. Current Scope

The following is our current understanding and should be treated as a
**draft vision**, not a final specification.

### We are trying to build:

**A personal AI execution agent that:**

1.  Remembers user-provided tasks and commitments.
2.  Understands the user's schedule.
3.  Manages goals and deadlines.
4.  Creates daily/weekly plans.
5.  Sends timely reminders.
6.  Follows up on task completion.
7.  Re-plans when the user falls behind.
8.  Tracks study/productivity progress.
9.  Helps maintain LinkedIn activity based on actual learning.
10. Eventually supports voice interaction.
11. Uses tools to perform actions.
12. Uses RAG for personal knowledge.
13. Uses specialized agents when useful.
14. Uses a supervisor to coordinate agents.
15. Uses verification and human approval for important actions.
16. Maintains privacy and minimizes unnecessary data exposure.
17. Serves the primary persona of a student/early professional.
18. Operates with explicit non-goals (e.g., will not constantly interrupt).
19. Follows a tiered autonomy model.

This document is now **frozen at v0.3**. The next step is requirements
engineering (SRS_PRAX_v0.1.md).
