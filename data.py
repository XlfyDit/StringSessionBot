from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴛʀɪɴɢ", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("ʙᴏᴛ sᴛᴀᴛᴜs ᴀɴᴅ ᴍᴏʀᴇ ʙᴏᴛs", url="https://t.me/RafaelSupportGrp")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜsᴇ ❔", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("ᴍᴏʀᴇ ᴀᴍᴀᴢɪɴɢ ʙᴏᴛ", url="https://t.me/RafaelSupportGrp")],
    ]

    START = """
Hai {}

{} DIBUAT UNTUK MEMBANTU ANDA MENGAMBIL STRING SESSION TELEGRAM ANDA DENGAN AMAN

Jika Anda tidak mempercayai bot ini,
1) gaush dibaca
2) hapus chat ini terus blok

Manage by : @RapalelWak
    """

    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    ABOUT = """
**About This Bot** 

Telegram Bot to generate Pyrogram and Telethon string session by @RafaelSupportGrp

Source Code : [Click Here](https://github.com/XlfyDit/StringSessionBot)

Framework : [Pyrogram](https://docs.pyrogram.org)

Language : [Python](https://www.python.org)

Developer : @RapalelWak
    """
