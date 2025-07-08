# GyroBot
A custom Discord bot built with Python that automates moderation and enhances engagement in a 5,000+ member gaming server. Integrates OpenAI GPT API for AI-powered contextual responses and features structured command handling and user data logging.
---
## Features

- **Welcome new members** with a custom image featuring their profile picture in a circular frame, along with instructions to join key channels.
- **Loadout image commands** (`!ak117`, `!cx9`, `!dlq`, etc.) to easily share popular Call of Duty Mobile loadouts.
- **Profanity filter** that automatically deletes messages with forbidden words and warns the user.
- **Auto-responses** for greetings, complaints, mentions of the bot, and fun interactions.
- **Voice channel support**: commands to join or disconnect from voice channels.
- **Admin commands** to clear or delete recent messages.
- Welcomes members leaving the server with a goodbye message.
- Responds politely when mentioned.

---

## Commands Overview

| Command     | Description                                   |
|-------------|-----------------------------------------------|
| `!Links`    | Shows Gyro's social media links.              |
| `!age`      | Displays Gyro's age (fun response).           |
| `!birthday` | Shares Gyro's birthday.                        |
| `!ak117`    | Sends the AK117 loadout image.                 |
| `!cx9`      | Sends the CX9 loadout image.                   |
| `!dlq`      | Sends the DLQ loadout image.                    |
| `!fennec`   | Sends the Fennec loadout image.                 |
| `!krm`      | Sends the KRM loadout image.                    |
| `!mac10`    | Sends the MAC10 loadout image.                  |
| `!msmc`     | Sends the MSMC loadout image.                   |
| `!ots`      | Sends two OTS loadout images with messages.    |
| `!qq9`      | Sends two QQ9 loadout images with messages.    |
| `!CLEAR`    | Clears all messages in the channel (admin only).|
| `!delete`   | Deletes last 20 messages in the channel (admin only).|
| `!join`     | Bot joins your voice channel.                   |
| `!disconnect`| Bot disconnects from the voice channel.        |

---

## Requirements

- Python 3.8 or higher
- [discord.py](https://discordpy.readthedocs.io/en/stable/) library
- Pillow (`PIL`) for image manipulation
- `openai` (optional, depending on your extended usage)
- Your Discord bot token (`BOTTOKEN`)

---
## Setup Instructions
1. **Clone or download** the repository.

2. **Install dependencies:**

```bash
pip install discord.py Pillow openai requests
