from bot.filetocloud import CloudBot, filters
from pyrogram.types import Message
from bot import START, SOURCE


@CloudBot.on_message(filters.command("start"))
async def start(_, m: Message):
    await m.reply(
        f'Hi {m.from_user.mention(style="md")}, {START}{SOURCE} '
        )
