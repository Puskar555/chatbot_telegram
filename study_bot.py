from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random

# Sample subjects for a data science student
subjects = ["Machine Learning", "Statistics", "Programming", "Data Analysis"]

# Function to generate a study schedule
def generate_schedule():
    # Divide 8 hours of study time into 4 blocks
    blocks = ["9:00 AM - 11:00 AM", "11:30 AM - 1:30 PM", "3:00 PM - 5:00 PM", "6:00 PM - 8:00 PM"]
    selected_subjects = random.sample(subjects, 2)
    schedule = []
    for i, time_block in enumerate(blocks):
        schedule.append(f"{time_block}: {selected_subjects[i % 2]}")
    return schedule

# Command to get a schedule
def get_schedule(update: Update, context: CallbackContext) -> None:
    """
    :param update:
    :param context:
    """
    routine = generate_schedule()
    message = (
        "📚 Here's your study schedule for today:\n"
        f"5 Hours of School: 8:00 AM - 1:00 PM\n\n"
        "Study Time:\n" +
        "\n".join(routine) +
        "\n\nRemember to take breaks and stay hydrated! 😊"
    )
    update.message.reply_text(message)

def main():
    # Replace 'YOUR_TOKEN_HERE' with your bot token
    updater = Updater("YOUR_TOKEN_HERE")

    dispatcher = updater.dispatcher

    # Command handler for /schedule
    dispatcher.add_handler(CommandHandler("schedule", get_schedule))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
