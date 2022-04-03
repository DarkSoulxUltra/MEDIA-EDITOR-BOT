from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_MSG = """**Moshi Mosh {}
  
I am a Hitagi Senjougahara, A Media Editor bot...

You can edit/replace the documents,videos,gifs,audios,photos etc… Of Your Channels easily By Using Me**

You should be grateful to me for that

`For More Info On Usage Hit ➟` /help 

"""


HELP_MSG = """
Follow the below steps...

✂️ First Send me A Media That You Need To Edit/Replace with the Old One (New file which you want on your channel instead)

✂️ Now Send The Link Of The Media from channel, That Will Be Replaced/Edited (Copy link of old file from channel, and send it to me)

Note : Both you & I must be an admin in the target Channel where you are doing the replacements.

"""






@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_text(
        text=START_MSG.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text="OWNER SAMA",url = "t.me/yameteee_yamete_kudasai")]]),
        reply_to_message_id=message.message_id,
        parse_mode="combined"
    )    



@Client.on_message(filters.command('help') & filters.private)
async def help(client, message):
    await message.reply_text(
        text=HELP_MSG,
        disable_web_page_preview=True,
        reply_to_message_id=message.message_id
    )    
