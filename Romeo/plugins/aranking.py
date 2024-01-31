from pyrogram import Client, filters
from pyrogram.types import Message
from pymongo import MongoClient
from datetime import datetime, timedelta
from Romeo import app
import congig

# "Write a python code for telegram group message count all users message and  show  leader board top 10 users with command in pyrogram telegram bot and save all messages using mongodb_uri for all chat_id and add daily message count and overall message also should leader board and add a daily and overall button below leaderboard"     



# Replace 'MONGODB_URI' with your MongoDB URI
mongodb_uri = 'MONGO_URL'

# Initialize MongoDB client
mongo_client = MongoClient(mongodb_uri)
db = mongo_client['telegram_bot']
messages_collection = db['group_messages']

# Dictionary to store message counts for each chat_id and user
chat_user_message_count = {}

# Command to display the top 10 leaderboard with daily and overall buttons
@app.on_message(filters.command(["rankings", "r"], ["/", ".", "!"]) & filters.group)
async def show_top10_leaderboard(client: Client, message: Message):
    global chat_user_message_count

    # Get the chat_id
    chat_id = message.chat.id

    # Sort users by overall message count in descending order
    sorted_users_overall = sorted(chat_user_message_count.get(chat_id, {}).items(),
                                  key=lambda x: x[1]['overall'], reverse=True)[:10]

    # Sort users by daily message count in descending order
    sorted_users_daily = sorted(chat_user_message_count.get(chat_id, {}).items(),
                                key=lambda x: x[1]['daily'], reverse=True)[:10]

    # Prepare the leaderboard message
    leaderboard_msg = f"Rankings for {chat_id}:\n\n"
    leaderboard_msg += "Overall Leaderboard:\n"
    leaderboard_msg += format_leaderboard(sorted_users_overall)

    leaderboard_msg += "\nDaily Leaderboard:\n"
    leaderboard_msg += format_leaderboard(sorted_users_daily)

    # Add buttons for daily and overall statistics
    buttons = [
        [{"text": "📆 Daily Stats", "callback_data": "daily_stats"},
         {"text": "📊 Overall Stats", "callback_data": "overall_stats"}]
    ]

    # Send the leaderboard message with buttons
    await message.reply_text(leaderboard_msg, reply_markup={"inline_keyboard": buttons})

# Count messages in the group, save to MongoDB, and update message counts
@app.on_message(filters.group & ~filters.edited)
async def count_messages(client: Client, message: Message):
    global chat_user_message_count

    # Get the chat_id and user_id
    chat_id = message.chat.id
    user_id = message.from_user.id

    # Get or initialize the user's message count for this chat_id
    user_stats = chat_user_message_count.setdefault(chat_id, {}).setdefault(user_id, {
        'daily': 0,
        'overall': 0
    })

    # Increment daily and overall message counts
    user_stats['daily'] += 1
    user_stats['overall'] += 1

    # Save message to MongoDB
    messages_collection.insert_one({
        'user_id': user_id,
        'message_id': message.message_id,
        'text': message.text,
        'date': message.date,
        'chat_id': chat_id,
    })

# Handle button presses for daily and overall statistics
@app.on_callback_query()
async def handle_callback_query(client: Client, callback_query):
    global chat_user_message_count

    # Get the chat_id
    chat_id = callback_query.message.chat.id

    # Get the callback data
    callback_data = callback_query.data

    # Get the user message counts for this chat_id
    user_stats = chat_user_message_count.get(chat_id, {})

    # Prepare statistics message
    stats_msg = f"Stats for {chat_id}:\n\n"

    if callback_data == "daily_stats":
        stats_msg += "📆 Daily Stats:\n"
        stats_msg += format_stats(user_stats, 'daily')

    elif callback_data == "overall_stats":
        stats_msg += "📊 Overall Stats:\n"
        stats_msg += format_stats(user_stats, 'overall')

    # Send the statistics message
    await callback_query.edit_message_text(stats_msg)

def format_stats(user_stats, key):
    """Format statistics for a specific key (daily or overall)."""
    stats_str = ""
    for index, (user_id, stats) in enumerate(sorted(user_stats.items(), key=lambda x: x[1][key], reverse=True)[:10], start=1):
        user = await app.get_users(user_id)
        stats_str += f"{index}. {user.mention} - {stats[key]} messages\n"
    return stats_str

def format_leaderboard(sorted_users):
    """Format leaderboard for a specific sorting (daily or overall)."""
    leaderboard_str = ""
    for index, (user_id, stats) in enumerate(sorted_users, start=1):
        user = await app.get_users(user_id)
        leaderboard_str += f"{index}. {user.mention} - {stats['overall']} messages (Overall), {stats['daily']} messages (Daily)\n"
    return leaderboard_str

  
