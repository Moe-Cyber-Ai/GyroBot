import discord
from discord.ext import commands
from openai_api import call_openai  # Assuming this is your OpenAI API helper

# Set up intents to read message content
intents = discord.Intents.default()
intents.message_content = True

# Create the bot instance
bot2 = commands.Bot(command_prefix='!', intents=intents)

# Event when the bot is ready


@bot2.event
async def on_ready():
    print(f'Bot 2 (Gyro\'s Spirit) is now online and ready!')

# Event when the bot receives a message


@bot2.event
async def on_message(message):
    # Prevent the bot from replying to itself
    if message.author == bot2.user:
        return

    # Check if the bot was mentioned (Gyro's Spirit)
    if bot2.user in message.mentions:
        # Format the prompt to be sent to OpenAI
        prompt = f"You are a sarcastic but helpful gaming expert who responds to Discord users. " \
            f"Someone just mentioned you: '{message.content}'. Reply in a casual, fun, and slightly roast-y way."

        try:
            # Call OpenAI API and get the response
            reply = await call_openai(prompt)
            # Send the OpenAI response in the channel
            await message.channel.send(reply)
        except Exception as e:
            # If something goes wrong, notify the user
            await message.channel.send("Oops! Something went wrong... 😬")
            print(e)

    # Don't forget to process commands if needed (in case you have other commands)
    await bot2.process_commands(message)

# Example command for testing purposes (optional)


@bot2.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Run the bot with the second token
bot2.run('YOUR_SECOND_BOT_TOKEN')
