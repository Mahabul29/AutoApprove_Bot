import random
from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from Script import text
from config import ADMIN, PICS

@Client.on_callback_query()
async def callback_query_handler(client, query: CallbackQuery):
    if query.data == "start":
        await query.message.edit_media(
            InputMediaPhoto(
                media=random.choice(PICS),
                caption=text.START.format(query.from_user.mention)
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('⇆ 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 ⇆', url="https://telegram.me/AutoApproval_Bot?startgroup=true&admin=invite_users")],
                [InlineKeyboardButton('𝖠𝖻𝗈𝗎𝗍', callback_data='about'),
                 InlineKeyboardButton('𝖧𝖾𝗅𝗉', callback_data='help')],
                [InlineKeyboardButton('⇆ 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 ⇆', url="https://telegram.me/AutoApproval_Bot?startchannel=true&admin=invite_users")]
            ])
        )

    elif query.data == "help":
        await query.message.edit_media(
            InputMediaPhoto(
                media=random.choice(PICS),
                caption=text.HELP.format(query.from_user.mention)
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('ᴜᴘᴅᴀᴛᴇs', url='https://telegram.me/EvaLinks'),
                 InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', url='https://telegram.me/EvaLinks')],
                [InlineKeyboardButton('ʙᴀᴄᴋ', callback_data="start"),
                 InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data="close")]
            ])
        )

    elif query.data == "about":
        await query.message.edit_media(
            InputMediaPhoto(
                media=random.choice(PICS),
                caption=text.ABOUT
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('ᴅᴇᴠᴇʟᴏᴘᴇʀ', user_id=int(ADMIN))],
                [InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="start"),
                 InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")]
            ])
        )

    elif query.data == "close":
        await query.message.delete()
