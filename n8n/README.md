# PRAX — n8n Workflows

This folder contains n8n workflow JSON files that implement the **PRAX Personal AI Execution Agent** vision using n8n as the orchestration layer, with **Telegram** as the primary input/output interface.

---

## 📁 Files

| File | Description |
|------|-------------|
| `PRAX — Personal AI Execution Agent- V1.json` | V1 — Reactive agent. Telegram chat → AI Agent with task/memory tools → reply. |
| `PRAX — Personal AI Execution Agent- V2.json` | **V2 — Proactive agent.** Upgraded main agent + scheduled morning briefing, reminder checker, and evening review. |
| `n8n_ai_builder_prompt.md` | Prompts for n8n's AI builder to generate PRAX workflows interactively. |
| `README.md` | This file — setup guide and architecture overview. |

---

## 🆕 V1 → V2 Changelog

| Feature | V1 | V2 |
|---------|----|----|
| Task CRUD | Create, Read, Complete | + **Update** (edit deadline/priority/status) + **Delete** (cancel) |
| Reminders | ❌ Stored as tasks only | ✅ **Separate Reminders table** with `remind_at` datetime |
| Reminder delivery | ❌ Never sends at scheduled time | ✅ **Cron checks every 15 min**, sends via Telegram |
| Morning briefing | ❌ | ✅ **Daily at 7:30 AM IST** — prioritized task plan |
| Evening review | ❌ | ✅ **Daily at 11:00 PM IST** — summary of completed/pending |
| Task statuses | Pending, Completed | + In Progress, Skipped, Deferred, Cancelled |
| System prompt | Basic | **Enhanced** — certainty detection, skip-reason tracking, overwhelm handling |
| Proactive behavior | ❌ Fully reactive | ✅ **3 cron-triggered workflows** reach out to you |

---

## 🏗️ V2 Architecture Overview

```
┌─────────────────────────────────────────────────────┐
│              MAIN AGENT PATH (reactive)             │
│                                                     │
│  User ──► Telegram ──► PRAX Agent ──► Telegram      │
│              Trigger      │           Reply          │
│                           │                          │
│           ┌───────────────┼───────────────┐          │
│           │  create_task   get_tasks       │          │
│           │  complete_task update_task     │          │
│           │  delete_task   create_reminder │          │
│           │  save_memory   search_memory   │          │
│           │  get_schedule  Date & Time     │          │
│           │  Chat Memory (10-msg window)   │          │
│           └───────────────────────────────┘          │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│           PROACTIVE CRON PATHS (V2 new)             │
│                                                     │
│  ☀️ 7:30 AM ──► Morning Agent ──► Telegram Send     │
│                   └── reads pending tasks            │
│                                                     │
│  ⏰ */15 min ──► Reminder Agent ──► IF due ──► Send  │
│                   └── checks remind_at vs now        │
│                                                     │
│  🌙 11:00 PM ──► Evening Agent ──► Telegram Send    │
│                   └── reads all tasks for summary    │
└─────────────────────────────────────────────────────┘
```

---

## 🚀 V2 Setup Instructions

### Prerequisites

1. **n8n** installed locally or running on a server
   - Local: `npx n8n` or `npm install -g n8n && n8n start`
   - Docker: `docker run -it --rm -p 5678:5678 n8nio/n8n`

2. **Telegram Bot** created via [@BotFather](https://t.me/BotFather)
   - Create a new bot: `/newbot`
   - Save the **Bot Token**
   - Get your **Chat ID**: send a message to your bot, then visit `https://api.telegram.org/bot<TOKEN>/getUpdates`

3. **OpenRouter API Key** → https://openrouter.ai/keys

### Step 1: Create the Reminders Data Table

Before importing V2, create a new Data Table in n8n:

1. Go to **Data** → **Create Data Table**
2. Name it: `PRAX Reminders`
3. Add these columns:

| Column | Type |
|--------|------|
| `reminder_id` | Text |
| `chat_id` | Text |
| `reminder_text` | Text |
| `remind_at` | DateTime |
| `status` | Text |
| `created_at` | DateTime |

4. **Copy the table ID** from the URL when viewing the table

### Step 2: Import & Configure

1. Go to **Workflows** → **Import from File** → select `PRAX — Personal AI Execution Agent- V2.json`
2. **Find & Replace** these placeholders (use n8n's node editor or a text editor):
   - `REPLACE_REMINDERS_TABLE_ID` → the ID of your new Reminders data table
   - `REPLACE_YOUR_CHAT_ID` → your Telegram chat ID (a number like `123456789`)
3. Configure credentials:
   - **Telegram API**: Add/verify your Bot Token on all Telegram nodes
   - **OpenRouter**: Add/verify your API Key on all OpenRouter nodes
4. **Activate** the workflow

### Step 3: Verify Cron Times

The cron schedules use **UTC** times by default. Adjust if your n8n server uses a different timezone:

| Feature | IST Time | UTC Cron Expression |
|---------|----------|-------------------|
| Morning Briefing | 7:30 AM | `0 2 * * *` |
| Reminder Check | Every 15 min | `*/15 * * * *` |
| Evening Review | 11:00 PM | `30 17 * * *` |

> **Tip:** If your n8n server timezone is already IST, change the crons to: `30 7 * * *` (morning) and `0 23 * * *` (evening).

---

## 🧠 PRAX Vision Coverage

| Vision Section | V1 | V2 |
|----------------|----|----|
| §7 Task Management | ✅ Basic CRUD | ✅ Full CRUD + update/delete/statuses |
| §8 Commitment Model | 🔶 Partial | ✅ Certainty detection in prompt |
| §9 Daily Schedule | ✅ On-demand | ✅ + Proactive morning plan |
| §10 Accountability | 🔶 Manual check | ✅ Skip-reason tracking |
| §11 Adaptive Planning | ⬜ | 🔶 Evening review suggests tomorrow |
| §13 Focus Sessions | ⬜ | ⬜ Planned for V3 |
| §14 Notifications | 🔶 Reply only | ✅ Scheduled reminders + briefings |
| §22 LinkedIn | ⬜ | ⬜ Planned for V3 |
| §22 Voice | ⬜ | ⬜ Planned for V3 |

---

## 🔧 Customization

### Changing Cron Times

Edit the Schedule Trigger nodes to adjust when PRAX reaches out:
- `Schedule — Morning Briefing`: change the cron expression
- `Schedule — Reminder Check`: change the interval (default: every 15 min)
- `Schedule — Evening Review`: change the cron expression

### Changing the LLM Model

All agents use OpenRouter. To change the model, edit the OpenRouter nodes. V2 uses 4 separate LLM instances:
- **Main agent**: maxTokens=2000, temp=0.4 (most flexible)
- **Morning/Evening agents**: maxTokens=1000, temp=0.3 (focused)
- **Reminder checker**: maxTokens=500, temp=0.1 (deterministic)

### Reminder Check Precision

The reminder checker runs every 15 minutes by default. For tighter precision, change `*/15 * * * *` to `*/5 * * * *` (every 5 min) — note this uses more LLM API calls.

---

## 📌 Notes

- **V2 is imported as inactive** — activate it only after completing setup
- The workflow has a **yellow sticky note** on the canvas with setup reminders
- All data stays within your n8n instance — no external data sharing beyond LLM API calls
- The V1 workflow can remain imported as a backup
- Refer to `docs/PRAX_Agent_Vision.md` for the full product vision
