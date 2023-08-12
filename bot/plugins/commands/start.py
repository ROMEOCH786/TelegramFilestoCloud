from bot.filetocloud import CloudBot, filters
from bot import START, SOURCE


@CloudBot.on_message(filters.command("start"))
async def start_message(client, message):
    await m.reply(
        f'Hi {m.from_user.mention(style="md")}, {START}{SOURCE} '
        )
