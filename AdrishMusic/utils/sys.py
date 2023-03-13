#
# Copyright (C) 2023-2024 by MrAdrish69@Github, < https://github.com/MrAdrish69 >.
#
# This file is part of < https://github.com/MrAdrish69/AdrishMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/MrAdrish69/AdrishMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import time

import psutil

from AdrishMusic.misc import _boot_

from .formatters import get_readable_time


async def bot_sys_stats():
    bot_uptime = int(time.time() - _boot_)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    UP = f"{get_readable_time((bot_uptime))}"
    CPU = f"{cpu}%"
    RAM = f"{mem}%"
    DISK = f"{disk}%"
    return UP, CPU, RAM, DISK
