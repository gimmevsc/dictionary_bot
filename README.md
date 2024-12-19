# **Dictionary Bot for Telegram**

The bot stores client vocabulary in an SQLite3 database The bot interacts with users on Telegram and processes their requests.

---

## **Setup Instructions**

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
