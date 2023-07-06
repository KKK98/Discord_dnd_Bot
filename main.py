import discord
from discord.ext import commands
import os
import openai


# 设置 OpenAI API 密钥
openai.api_key = os.getenv('OPENAI_API_KEY')

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    if message.content.startswith('$hello'):
        await message.channel.send('hello!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$chat'):
        # 提取用户输入的消息内容
        user_input = message.content.removeprefix('$chat').strip()

        # 使用 OpenAI API 进行聊天
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        # 提取 OpenAI 返回的回复内容
        bot_reply = response.choices[0].message.content.strip()

        # 将回复发送到 Discord
        await message.channel.send(bot_reply)

client.run(os.getenv('DISCORD_TOKEN'))
