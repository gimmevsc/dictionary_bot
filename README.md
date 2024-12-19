# **Dictionary Bot for Telegram**

This project is a **Telegram bot** designed to provide dictionary functionalities such as word definitions, synonyms, and more. The bot interacts with users on Telegram and processes their requests.

---

## **Features**
- Fetch word definitions
- Provide synonyms and antonyms
- User-friendly interaction through Telegram
- Configurable environment setup

---

## **Setup Instructions**

Follow these steps to set up and run the bot:

---

### **1. Prerequisites**

Ensure you have the following installed:
- **Python 3.8+**
- **Telegram Bot Token** (create one via [BotFather](https://core.telegram.org/bots#botfather))

---
### **2. Setup Instructions**

#### 1. Clone the Repository

```bash
git clone https://github.com/gimmevsc/dictionary_bot.git
cd <your-repository-folder>
```

#### 2. Create and Activate a Virtual Environment
##### For Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
##### For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
#### 3. Install Dependencies
##### Install the required Python libraries:
```bash
pip install -r requirements.txt
```

#### 4. Set Up Environment Variables
##### Create a .env file in the project root and add the following:

TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN

#### 5. Run the Bot
##### Start the bot by running the following command:
```bash
python main.py
```

The bot will now start and listen for messages on Telegram