# n8n AI Builder Prompts for PRAX

Use these prompts in **n8n's AI workflow builder** (the "Describe what you want" input box).
Copy-paste the prompt that matches what you want to build.

---

## 🟢 Prompt 1 — Core PRAX Agent (Start Here)

> Copy everything inside the code block below and paste into n8n AI builder:

```
Build a Telegram chatbot workflow that acts as a personal AI task management agent called "PRAX".

The workflow should:

1. Start with a Telegram Trigger node that listens for incoming messages.

2. Use a Code node to extract the chat ID, user name, message text, and timestamp from the Telegram message.

3. Send the user's message to an AI model (use Gemini or OpenAI) to classify the intent into one of these categories:
   - "create_task" (user wants to add a task, e.g. "I need to submit my AI assignment on Friday")
   - "create_reminder" (user wants a reminder, e.g. "Remind me at 8 PM to call mom")
   - "set_schedule" (user wants a recurring activity, e.g. "Every evening at 9 I want DSA practice")
   - "save_memory" (user wants you to remember something)
   - "check_status" (user asks about pending tasks or schedule)
   - "complete_task" (user says they finished something)
   - "reschedule" (user wants to skip or postpone something)
   - "general" (greetings, chitchat, anything else)
   
   The AI should return only a JSON with intent and confidence.

4. Use a Switch node to route based on the classified intent.

5. For each intent branch, use a Code node to build a tailored prompt. The system prompt should say: "You are PRAX, a personal AI execution agent for students. You help manage tasks, schedules, deadlines, and goals. You are friendly, concise, and action-oriented."

6. Send the tailored prompt to the AI model to generate a natural language response.

7. Use a Telegram Send Message node to reply to the user with the AI-generated response. Use Markdown parse mode.

8. Add an Activity Log code node that logs the intent, message, and timestamp for debugging.

Connect Telegram input and output. All Switch outputs should merge into the prompt builder.
```

---

## 🟡 Prompt 2 — Add Google Sheets Task Storage

> Use this AFTER Prompt 1 is working. Paste into n8n AI builder:

```
Extend my existing PRAX Telegram bot workflow to store tasks in Google Sheets.

Add the following:

1. Create a Google Sheets spreadsheet connection with columns: TaskID, TaskName, Deadline, Priority, Status, Category, CreatedAt, CompletedAt, Notes.

2. When the intent is "create_task":
   - After the AI extracts task details from the user message, use a Code node to parse the AI response and extract: task name, deadline, and priority.
   - Write a new row to Google Sheets with Status = "Pending" and CreatedAt = current timestamp.
   - Then send the confirmation to the user via Telegram.

3. When the intent is "check_status":
   - Read all rows from Google Sheets where Status is "Pending" or "In Progress".
   - Format them into a readable list.
   - Send the list to the user via Telegram.

4. When the intent is "complete_task":
   - Search Google Sheets for the matching task.
   - Update its Status to "Completed" and set CompletedAt to current timestamp.
   - Confirm completion to the user.

Keep the existing Telegram trigger and AI classification nodes unchanged.
```

---

## 🟡 Prompt 3 — Scheduled Daily Plan & Reminders

> Use this to add proactive scheduled messages. Paste into n8n AI builder:

```
Create a separate n8n workflow for scheduled PRAX reminders via Telegram.

This workflow should:

1. Use a Cron/Schedule Trigger that runs every day at 7:30 AM IST (2:00 AM UTC).

2. Read all pending tasks from Google Sheets (or a connected database) that have today's date as deadline or are high priority.

3. Send the list to the AI model with this prompt: "You are PRAX. Generate a friendly morning briefing for the user. List their tasks for today ordered by priority. Include deadlines. Keep it concise and motivating. Use emoji."

4. Send the AI-generated daily plan to the user's Telegram chat using a Telegram Send Message node.

5. Add a second Schedule Trigger at 11:00 PM IST (5:30 PM UTC) that:
   - Reads today's tasks from Google Sheets.
   - Checks which are still "Pending".
   - Asks the AI to generate an evening review: what was done, what was missed, and a suggestion for tomorrow.
   - Sends it via Telegram.

Use the same Telegram bot credentials as my main PRAX workflow.
```

---

## 🔵 Prompt 4 — Accountability Follow-Up

> Adds follow-up messages when tasks are missed:

```
Extend my PRAX workflow to add accountability follow-ups.

After a task's scheduled time passes:

1. Add a Schedule Trigger that checks every 30 minutes between 8 AM and 11 PM IST.

2. Read tasks from Google Sheets that have a scheduled time that has passed but Status is still "Pending".

3. For each overdue task, send a gentle Telegram nudge using the AI model. The prompt should be: "You are PRAX. The user was supposed to do [TASK] at [TIME] but hasn't marked it done. Send a single gentle nudge. Don't be pushy. Offer to reschedule. Keep it to 2-3 sentences."

4. Track that a nudge was sent by updating a "NudgeCount" column in Google Sheets. Don't send more than 2 nudges per task per day.

5. If the user replies with "done", "finished", "completed", or "skip", update the task status accordingly.
```

---

## 🔵 Prompt 5 — LinkedIn Draft Generator

> Creates a content generation side-workflow:

```
Create a new n8n workflow for PRAX LinkedIn content generation via Telegram.

1. Telegram Trigger listens for messages starting with "/linkedin" or "generate linkedin post".

2. Extract the topic from the user's message (everything after the command).

3. Send to AI model with this prompt: "You are PRAX's content assistant. The user is a student learning AI and tech. They want a LinkedIn post about what they learned today. Topic: [USER_TOPIC]. Write a genuine, first-person LinkedIn post (150-250 words). Don't exaggerate or claim false achievements. Use a conversational tone. Include 3-5 relevant hashtags at the end."

4. Send the draft to the user via Telegram with a message: "Here's your LinkedIn draft. Reply with 'approve' to finalize or tell me what to change."

5. If the user replies "approve", send a final confirmation. If they reply with feedback, regenerate with the feedback included.

Keep this as a separate workflow from the main PRAX task management workflow.
```

---

## 🟣 Prompt 6 — Full Agent with Memory (Advanced)

> For when you're ready to build the complete agent:

```
Build an advanced PRAX AI agent workflow with Telegram and persistent memory.

Architecture:
- Telegram Trigger receives user messages
- AI Agent node (use n8n's built-in AI Agent) with these tools:
  1. "create_task" tool: Writes to Google Sheets with columns TaskID, Name, Deadline, Priority, Status, CreatedAt
  2. "get_tasks" tool: Reads from Google Sheets, filters by status
  3. "complete_task" tool: Updates task status to Completed in Google Sheets
  4. "save_memory" tool: Writes to a separate "Memories" Google Sheet with Key, Value, CreatedAt
  5. "search_memory" tool: Searches the Memories sheet for relevant entries
  6. "get_schedule" tool: Returns today's planned tasks sorted by time

- The AI Agent's system prompt should be:
  "You are PRAX, a personal AI execution agent for students and early-career professionals. You help manage tasks, schedules, deadlines, goals, and habits. You are friendly, concise, and action-oriented. You remember what the user tells you. You proactively suggest what to work on based on deadlines and priorities. You follow up on incomplete tasks. You never make decisions without the user's approval. You explain your reasoning when you reschedule or reprioritize."

- Use Window Buffer Memory with a session window of 10 messages, keyed by Telegram chat ID.

- Send the agent's response back via Telegram with Markdown formatting.

This should be a single workflow using n8n's AI Agent node with tool calling.
```

---

## 💡 Tips for Using These Prompts

1. **Start with Prompt 1** — get the basic bot working first
2. **Add storage with Prompt 2** — so tasks persist
3. **Add scheduling with Prompt 3** — for proactive daily plans
4. **Layer on Prompts 4-6** as you need more features
5. After the AI generates the workflow, you'll still need to:
   - Add your **Telegram Bot Token** credential
   - Add your **LLM API Key** (Gemini/OpenAI)
   - Add **Google Sheets** credential (if using storage prompts)
   - Test each node individually before activating

---

## 🗺️ How These Map to PRAX Vision Phases

| Prompt | PRAX Phase | Vision Sections |
|--------|-----------|-----------------|
| Prompt 1 | Phase 1 — Agent with Task Tools | §5, §7, §25 |
| Prompt 2 | Phase 1 + Storage | §7, §26 |
| Prompt 3 | Phase 2 — Scheduler | §6, §9, §14 |
| Prompt 4 | Phase 2 + Accountability | §10, §11 |
| Prompt 5 | Supporting Module | §22 (LinkedIn) |
| Prompt 6 | Phase 3 — Memory + Advanced | §17, §25, §29 |
     