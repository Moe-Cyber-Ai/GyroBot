import re
import openai
import discord
from discord.ext import commands
from apikey import *
import os
import asyncio
from PIL import Image, ImageDraw
from openai_api import call_openai
import requests
from io import BytesIO

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True
# Required to detect bot's online status

client = commands.Bot(command_prefix="!", intents=intents)
# client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
image_cache = {}
# -------------------------------------------------------------------------------


@client.event
async def on_ready():
    print("--------------------------------")
    print("Your GyroBot is ready for use")
    print("--------------------------------")
# -------------------------------------------------------------------------------


@client.command()
async def logout(ctx):
    await ctx.send("Gyro Bot Logging out. Goodbye!")
    await client.close()


def load_images():
    for filename in os.listdir("."):
        if filename.endswith(".jpg"):
            image_cache[filename[:-4]] = discord.File(filename)


load_images()
# ---------------------------------------------------------------------------------


@client.event
async def on_member_join(member):
    # Constants
    WELCOME_CHANNEL_ID = 1194791585607594004
    WELCOME_IMAGE_PATH = "welcome_image.jpg"
    FULL_ACCESS_CHANNEL_IDS = [
        1159174880969900194,
        1188971689959247982,
        1188972389212627004
    ]

    # Function to create a circular mask for an image
    def create_circle_mask(image):
        mask = Image.new("L", image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + image.size, fill=255)
        return mask

    # Function to resize and crop an image to a circle
    def resize_and_crop_to_circle(image, size):
        image.thumbnail(size, Image.LANCZOS)
        mask = create_circle_mask(image)
        image.putalpha(mask)
        return image

    # Function to add profile picture to welcome image and send the message
    async def welcome_member(member, welcome_channel):
        # Load the welcome image
        welcome_image = Image.open(WELCOME_IMAGE_PATH)
        # Get member's profile picture
        profile_pic_bytes = await member.avatar_url.read()
        profile_pic = Image.open(BytesIO(profile_pic_bytes))
        # Resize and crop profile picture to fit into circle
        profile_pic = resize_and_crop_to_circle(profile_pic, (200, 200))
        # Paste profile picture onto welcome image
        welcome_image.paste(profile_pic, (150, 150), profile_pic)

        # Save the edited image to a BytesIO object
        with BytesIO() as image_binary:
            welcome_image.save(image_binary, 'PNG')
            image_binary.seek(0)
            file = discord.File(fp=image_binary, filename='welcome_image.png')

        # Prepare welcome message
        welcome_message = f"Welcome to the server, {member.mention}!\n"
        welcome_message += "To gain full access to the server, please join the following channels:\n"
        for channel_id in FULL_ACCESS_CHANNEL_IDS:
            channel = member.guild.get_channel(channel_id)
            if channel:
                welcome_message += f"• {channel.mention}\n"

        # Send welcome message with modified welcome image
        await welcome_channel.send(welcome_message, file=file)

    # Get the welcome channel
    welcome_channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
    if welcome_channel:
        await welcome_member(member, welcome_channel)
    else:
        print(f"Welcome channel not found: {WELCOME_CHANNEL_ID}")


# -----------------------------------------------------------------------------------


# Sends back Messages when people use the "!" command
@client.command()
async def Links(ctx):
    await ctx.message.delete()  # Deletes the user's command message
    links = (
        "**MAKE SURE TO FOLLOW AND SUBSCRIBE TO ALL GYRO'S SOCIALS!**\n\n"
        "**TIKTOK:** https://www.tiktok.com/@gyro__codm\n\n"
        "**YOUTUBE:** https://www.youtube.com/@GyroMobile\n\n"
        "**INSTAGRAM:** https://www.instagram.com/gyro_codm\n\n"
    )
    await ctx.send(links)


@client.command()
async def age(ctx):
    await ctx.send("Gyro is 69 years old")
# _______________________________________________
# ___________________________________________


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        msg = await ctx.send(f"❌ {ctx.author.mention} Wrong command! ❌ Please try again or check the #commands channel.")
        await asyncio.sleep(10)
        await msg.delete()
    else:
        raise error


@client.command()
async def birthday(ctx):
    await ctx.send("Born on February 28")


@client.command()
async def ak117(ctx):
    image_name = "ak117"
    if image_name in image_cache:
        await ctx.send(file=image_cache[image_name])
    else:
        await ctx.send("Loadout Not Found, feel free to Tag GYRO and ask him!.")


@client.command()
async def cx9(ctx):
    image_name = "CX9"
    if image_name in image_cache:
        await ctx.send(file=image_cache[image_name])
    else:
        await ctx.send("Loadout Not Found, feel free to Tag GYRO and ask him!.")


@client.command()
async def dlq(ctx):
    image_name = "DLQ"
    if image_name in image_cache:
        await ctx.send(file=image_cache[image_name])
    else:
        await ctx.send("Loadout Not Found, feel free to Tag GYRO and ask him!.")


@client.command()
async def fennec(ctx):
    image_name = "Fennec"
    if image_name in image_cache:
        await ctx.send(file=image_cache[image_name])
    else:
        await ctx.send("Loadout Not Found, feel free to Tag GYRO and ask him!.")


@client.command()
async def krm(ctx):
    image_name = "KRM"
    if image_name in image_cache:
        await ctx.send(file=image_cache[image_name])
    else:
        await ctx.send("Loadout Not Found, feel free to Tag GYRO and ask him!.")


@client.command()
async def mac10(ctx):
    image_name = "MAC10"
    if image_name in image_cache:
        await ctx.send(file=image_cache[image_name])
    else:
        await ctx.send("Loadout Not Found, feel free to Tag GYRO and ask him!.")


@client.command()
async def msmc(ctx):
    image_name = "MSMC"
    if image_name in image_cache:
        await ctx.send(file=image_cache[image_name])
    else:
        await ctx.send("Loadout Not Found, feel free to Tag GYRO and ask him!.")


@client.command()
async def ots(ctx):
    image_messages = {
        "OTS1": "Here's GYRO's (BR) OTs loadout:",
        "OTS2": "Here's GYRO's (MP) OTs loadout:"
    }

    for image_name, message in image_messages.items():
        if image_name in image_cache:
            await ctx.send(f"Hey {ctx.author.mention}! {message}", file=image_cache[image_name])
        else:
            await ctx.send(f"Loadout Not Found, feel free to Tag GYRO and ask him!: {image_name}")


@client.command()
async def qq9(ctx):
    image_messages = {
        "QQ91": "Here's GYRO's BR QQ9 loadout:",
        "QQ92": "Check out this MP QQ9 loadout!:"
    }

    for image_name, message in image_messages.items():
        if image_name in image_cache:
            await ctx.send(f"Hey {ctx.author.mention}! {message}", file=image_cache[image_name])
        else:
            await ctx.send(f"Loadout Not Found, feel free to Tag GYRO and ask him!: {image_name}")


@client.event
async def on_member_remove(member):
    channel = client.get_channel(1159152058889408556)
    await channel.send(f"{member.name} left the server. Goodbye!")


@client.command(pass_context=True)
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        voice_channel = await channel.connect()

        # Do something in the voice channel, if needed

        await ctx.send(f"Connected to {channel.name}")
    else:
        await ctx.send("You must be in a voice channel")


@client.command()
async def disconnect(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Disconnected from the voice channel")
    else:
        await ctx.send("I'm not currently in a voice channel")


@client.event
async def on_voice_state_update(member, before, after):
    if before.channel and not after.channel:
        # User left a voice channel
        voice_channel = member.guild.voice_client
        if voice_channel:
            await voice_channel.disconnect()

# Detects certain words in Discord Chat


@client.event
async def on_message(message):
    watch_list = ["Loadout", "Build", "Loadouts",
                  "builds", "gunsmith", "gunsmiths"]
    mentioned_words = [
        word for word in watch_list if word.lower() in message.content.lower()]
    forbidden_pattern = re.compile(
        r'\b[fu]+[ck]+[ed]*[c]*[k]*\b|\b[fu]+[ck]+[ing]*\b', re.IGNORECASE)

    en_friends = ["Otraps", "otraps", "Venouz",
                  "venouz", "Tanone", "tanone", "7ki", ]
    en_greeting_list = ["hey", "hello", "hi"]
    gyro_bot = ["gyro bot", "discord bot", "chat bot", "gyrobot", "chatbot"]
    ar_greeting_list = ["سلام", "اهلين", "هلا"]
    trash_gamer = ["I keep dying", "he kept killing me", "I am bad", "I am trash",
                   "I suck", "it's too hard", "im trash", "im bad", "its too hard", "It's too hard", "Its too hard"]
    salam_greeting = ["سلام عليكم"]
    kiss_user = ["Kiss me", "kiss", "kiss me", "mwah"]
    complain_list = ["campers", "camping", "camp", "corner camping", "corner"]

    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Check if the forbidden pattern is present in the message
    if forbidden_pattern.search(message.content):
        # Delete the message
        await message.delete()
        await message.channel.send(f"{message.author.mention}, Let's not CURSE, BRUVV! 🚫")

    if mentioned_words:
        # If any watched words are mentioned, send a message mentioning the user
        response = response = f"Hey {
            message.author.mention}! Check <#1159153288663543808> for Loadouts!"

        await message.channel.send(response)

    # Check if the message content matches any of the greetings
    if message.content.lower() in en_greeting_list:
        reply = f"Hey {message.author.mention}! How are you?"
        await message.channel.send(reply)

    if message.content.lower() in complain_list:
        reply = f"Bruh look at this dude {message.author.mention}! Stop complaining and get better"
        await message.channel.send(reply)

    if message.content.lower() in salam_greeting:
        reply = f" وعليكم السلام يا غالي {message.author.mention}"
        await message.channel.send(reply)

    if message.content.lower() in gyro_bot:
        reply = f"Keep my name out of your filthy mouth or I will 1v1 you!!{message.author.mention}"
        await message.channel.send(reply)
    if message.content.lower() in ar_greeting_list:
        reply = f" اهلين كيف حالك؟؟ {message.author.mention}"
        await message.channel.send(reply)

    if message.content.lower() in en_friends:
        reply = f" YEH HE'S GAY {message.author.mention}"
        await message.channel.send(reply)

    if message.content.lower() in kiss_user:
        reply = f" MWAAAAH U ARE SEXY!! {message.author.mention}"
        await message.channel.send(reply)

    if message.content.lower() in trash_gamer:
        reply = f" Skill issue, but alright… {message.author.mention}"
        await message.channel.send(reply)

    await client.process_commands(message)

    if client.user in message.mentions:
        response_texts = [
            f"Yo {message.author.mention}, you called Gyro? 😎",
            f"GYRO IS HERE {message.author.mention}! What's up?",
            f"I'm listening, {message.author.mention}. How can I help?",
            f"Tagged and ready! Need something, {message.author.mention}?"
        ]
        import random
        response = random.choice(response_texts)
        await message.channel.send(response)

    await client.process_commands(message)


@client.command()
async def CLEAR(ctx):
    admin_role_name = "ADMIN"  # Replace this with the exact name of your admin role
    if any(role.name == admin_role_name for role in ctx.author.roles):
        await ctx.channel.purge()  # Clears all messages in the channel
        confirmation = await ctx.send("✅ All messages have been cleared!")
        await asyncio.sleep(5)  # Wait 5 seconds
        await confirmation.delete()  # Delete the confirmation message
    else:
        await ctx.send("❌ You do not have permission to use this command.")


@client.command()
async def delete(ctx):
    admin_role_name = "ADMIN"  # Replace with your admin role name
    if any(role.name == admin_role_name for role in ctx.author.roles):
        # Fetch the last 20 messages
        messages_to_delete = [msg async for msg in ctx.channel.history(limit=20)]
        for message in messages_to_delete:
            await message.delete()
            await asyncio.sleep(0.5)  # Add a delay to avoid rate limits
        confirmation = await ctx.send("✅ The last 20 messages have been deleted!")
        # Wait 5 seconds before deleting the confirmation message
        await asyncio.sleep(5)
        await confirmation.delete()
    else:
        await ctx.send("❌ You do not have permission to use this command.")


client.run(BOTTOKEN)
