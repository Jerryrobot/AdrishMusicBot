#
# Copyright (C) 2023-2024 by MrAdrish69@Github, < https://github.com/MrAdrish69 >.
#
# This file is part of < https://github.com/MrAdrish69/AdrishMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/MrAdrish69/AdrishMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from strings import get_command, get_string
from AdrishMusic import app
from AdrishMusic.misc import SUDOERS
from AdrishMusic.utils.database import (get_lang, is_maintenance,
                                       maintenance_off,
                                       maintenance_on)
from AdrishMusic.utils.decorators.language import language

# Commands
MAINTENANCE_COMMAND = get_command("MAINTENANCE_COMMAND")


@app.on_message(filters.command(MAINTENANCE_COMMAND) & SUDOERS)
async def maintenance(client, message: Message):
    try:
        language = await get_lang(message.chat.id)
        _ = get_string(language)
    except:
        _ = get_string("en")
    usage = _["maint_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    message.chat.id
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        if await is_maintenance() is False:
            await message.reply_text(
                "Maintenance mode is already enabled"
            )
        else:
            await maintenance_on()
            await message.reply_text(_["maint_2"])
    elif state == "disable":
        if await is_maintenance() is False:
            await maintenance_off()
            await message.reply_text(_["maint_3"])
        else:
            await message.reply_text(
                "Maintenance mode is already disabled"
            )
    else:
        await message.reply_text(usage)
