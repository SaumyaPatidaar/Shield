# ============================================================
#Group Manager Bot
# Author: LearningBotsOfficial (https://github.com/LearningBotsOfficial) 
# Support: https://t.me/LearningBotsCommunity
# Channel: https://t.me/learning_bots
# YouTube: https://youtube.com/@learning_bots
# License: Open-source (keep credits, no resale)
# ============================================================


from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto
)
from config import BOT_USERNAME, SUPPORT_GROUP, UPDATE_CHANNEL, OWNER_ID
import db

def register_handlers(app: Client):

# ==========================================================
# Start Message
# ==========================================================
    async def send_start_menu(message, user):
    user_mention = f'<a href="tg://user?id={user.id}">{user.first_name}</a>'
    text = f"""

   Hello {user_mention} ✨

I am <a href="https://t.me/{BOT_USERNAME}"><b>𝗔𝗩𝗔𝗦𝗧 - 𝖦𝗋𝗈𝗎𝗉 𝖧𝖾𝗅𝗉𝖾𝗋</b></a>

𝘏𝘦𝘭𝘱𝘪𝘯𝘨 & 𝘔𝘢𝘯𝘢𝘨𝘦𝘮𝘦𝘯𝘵 𝘉𝘰𝘵 𝘪𝘴 𝘥𝘦𝘴𝘪𝘨𝘯𝘦𝘥 𝘵𝘰 𝘴𝘪𝘮𝘱𝘭𝘪𝘧𝘺 𝘛𝘦𝘭𝘦𝘨𝘳𝘢𝘮 𝘨𝘳𝘰𝘶𝘱 𝘮𝘰𝘥𝘦𝘳𝘢𝘵𝘪𝘰𝘯 𝘢𝘯𝘥 𝘢𝘶𝘵𝘰𝘮𝘢𝘵𝘪𝘰𝘯. 𝘑𝘰𝘪𝘯 𝘵𝘩𝘪𝘴 𝘨𝘳𝘰𝘶𝘱 𝘧𝘰𝘳 𝘴𝘶𝘱𝘱𝘰𝘳𝘵, 𝘶𝘴𝘢𝘨𝘦 𝘵𝘪𝘱𝘴, 𝘶𝘱𝘥𝘢𝘵𝘦𝘴, 𝘢𝘯𝘥 𝘢𝘯𝘯𝘰𝘶𝘯𝘤𝘦𝘮𝘦𝘯𝘵𝘴 𝘵𝘰 𝘨𝘦𝘵 𝘵𝘩𝘦 𝘣𝘦𝘴𝘵 𝘦𝘹𝘱𝘦𝘳𝘪𝘦𝘯𝘤𝘦 𝘸𝘩𝘪𝘭𝘦 𝘮𝘢𝘯𝘢𝘨𝘪𝘯𝘨 𝘺𝘰𝘶𝘳 𝘤𝘰𝘮𝘮𝘶𝘯𝘪𝘵𝘺.
─────────────────────────────
❖ 𝘏𝘪𝘨𝘩𝘭𝘪𝘨𝘩𝘵𝘴 :

✦ 𝘚𝘮𝘢𝘳𝘵 𝘈𝘯𝘵𝘪-𝘚𝘱𝘢𝘮 & 𝘓𝘪𝘯𝘬 𝘚𝘩𝘪𝘦𝘭𝘥
✦ 𝘈𝘥𝘢𝘱𝘵𝘪𝘷𝘦 𝘓𝘰𝘤𝘬 𝘚𝘺𝘴𝘵𝘦𝘮 
✦ 𝘜𝘙𝘓𝘴, 𝘔𝘦𝘥𝘪𝘢, 𝘓𝘢𝘯𝘨𝘶𝘢𝘨𝘦 & 𝘮𝘰𝘳𝘦.
✦ 𝘔𝘰𝘥𝘶𝘭𝘢𝘳 & 𝘚𝘤𝘢𝘭𝘢𝘣𝘭𝘦 𝘗𝘳𝘰𝘵𝘦𝘤𝘵𝘪𝘰𝘯
✦ 𝘚𝘭𝘦𝘦𝘬 𝘜𝘐 𝘸𝘪𝘵𝘩 𝘐𝘯𝘭𝘪𝘯𝘦 𝘊𝘰𝘯𝘵𝘳𝘰𝘭𝘴

☘ 𝘋𝘦𝘷𝘦𝘭𝘰𝘱𝘦𝘳 ; @khargyushh
"""

        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("• 𝘼𝙙𝙙 𝙈𝙚 𝙏𝙤 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥 •", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [
                InlineKeyboardButton("• 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 •", url="https://t.me/khargosh_updates"),
                InlineKeyboardButton("• 𝙐𝙥𝙙𝙖𝙩𝙚𝙨 •", url="https://t.me/khargosh_updates"),
            ],
            [
                InlineKeyboardButton("• 𝙊𝙬𝙣𝙚𝙧 •", url=f"tg://user?id=7284147034"),
                InlineKeyboardButton("• 𝙍𝙚𝙥𝙤 •", url="https://github.com/"),
                
            ],
            [InlineKeyboardButton("• 𝙃𝙚𝙡𝙥 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 •", callback_data="help")]
        ])

        # If /start command, send a new photo
        if message.text:
            await message.reply_photo(START_IMAGE, caption=text, reply_markup=buttons)
        else:
            # If callback, edit the same message
            media = InputMediaPhoto(media=START_IMAGE, caption=text)
            await message.edit_media(media=media, reply_markup=buttons)

# ==========================================================
# Start Command
# ==========================================================
    @app.on_message(filters.private & filters.command("start"))
    async def start_command(client, message):
        user = message.from_user
        await db.add_user(user.id, user.first_name)
        await send_start_menu(message, user.first_name)

# ==========================================================
# Help Menu Message
# ==========================================================
    async def send_help_menu(message):
        text = """
╔══════════════════╗
     Help Menu
╚══════════════════╝

Choose a category below to explore commands:
─────────────────────────────
"""
        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("⌂ Greetings ⌂", callback_data="greetings"),
                InlineKeyboardButton("⌂ Locks ⌂", callback_data="locks"),
            ],
            [
                InlineKeyboardButton("⌂ Moderation ⌂", callback_data="moderation")
            ],
            [InlineKeyboardButton("🔙 Back", callback_data="back_to_start")]
        ])

        media = InputMediaPhoto(media=START_IMAGE, caption=text)
        await message.edit_media(media=media, reply_markup=buttons)

# ==========================================================
# Help Callback_query
# ==========================================================
    @app.on_callback_query(filters.regex("help"))
    async def help_callback(client, callback_query):
        await send_help_menu(callback_query.message)
        await callback_query.answer()

# ==========================================================
# back to start Callback_query
# ==========================================================
    @app.on_callback_query(filters.regex("back_to_start"))
    async def back_to_start_callback(client, callback_query):
        user = callback_query.from_user.first_name
        await send_start_menu(callback_query.message, user)
        await callback_query.answer()

# ==========================================================
# Greetings Callback_query
# ==========================================================
    @app.on_callback_query(filters.regex("greetings"))
    async def greetings_callback(client, callback_query):
        text = """
╔══════════════════╗
    ⚙ Welcome System
╚══════════════════╝

Commands to Manage Welcome Messages:

- /setwelcome <text> : Set a custom welcome message for your group
- /welcome on        : Enable the welcome messages
- /welcome off       : Disable the welcome messages

Supported Placeholders:
- {username} : Telegram username
- {first_name} : User's first name
- {id} : User ID
- {mention} : Mention user in message

Example:
 /setwelcome Hello {first_name}! Welcome to {title}!
"""
        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Back", callback_data="help")]
        ])
        media = InputMediaPhoto(media=START_IMAGE, caption=text)
        await callback_query.message.edit_media(media=media, reply_markup=buttons)
        await callback_query.answer()

# ==========================================================
# Locks callback_query
# ==========================================================
    @app.on_callback_query(filters.regex("locks"))
    async def locks_callback(client, callback_query):
        text = """
╔══════════════════╗
     ⚙ Locks System
╚══════════════════╝

Commands to Manage Locks:

- /lock <type>    : Enable a lock for the group
- /unlock <type>  : Disable a lock for the group
- /locks          : Show currently active locks

Available Lock Types:
- url       : Block links
- sticker   : Block stickers
- media     : Block photos/videos/gifs
- username  : Block messages with @username mentions
- language  : Block non-English messages

Example:
 /lock url       : Blocks any messages containing links
 /unlock sticker : Allows stickers again
"""
        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Back", callback_data="help")]
        ])
        media = InputMediaPhoto(media=START_IMAGE, caption=text)
        await callback_query.message.edit_media(media=media, reply_markup=buttons)
        await callback_query.answer()

# ==========================================================
# Moderation Callback_query
# ==========================================================
    @app.on_callback_query(filters.regex("moderation"))
    async def info_callback(client, callback_query):
        try:
            text = """
╔══════════════════╗
      ⚙️ Moderation System
╚══════════════════╝

Manage your group easily with these tools:

¤ /kick <user> — Remove a user  
¤ /ban <user> — Ban permanently  
¤ /unban <user> — Lift ban  
¤ /mute <user> — Disable messages  
¤ /unmute <user> — Allow messages again  
¤ /warn <user> — Add warning (3 = mute)  
¤ /warns <user> — View warnings  
¤ /resetwarns <user> — Clear all warnings  
¤ /promote <user> — make admin
¤ /demote <user> — remove from admin  

💡 Example:
Reply to a user or type  
<code>/ban @username</code>

"""
            buttons = InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Back", callback_data="help")]
            ])
    
            media = InputMediaPhoto(media=START_IMAGE, caption=text)
            await callback_query.message.edit_media(media=media, reply_markup=buttons)
            await callback_query.answer()
    
        except Exception as e:
            print(f"Error in info_callback: {e}")
            await callback_query.answer("❌ Something went wrong.", show_alert=True)
    

# ==========================================================
# Broadcast Command
# ==========================================================
    @app.on_message(filters.private & filters.command("broadcast"))
    async def broadcast_message(client, message):
        if not message.reply_to_message:
            await message.reply_text("⚠️ Please reply to a message to broadcast it.")
            return

        if message.from_user.id != OWNER_ID:
            await message.reply_text("❌ Only the bot owner can use this command.")
            return

        text_to_send = message.reply_to_message.text or message.reply_to_message.caption
        if not text_to_send:
            await message.reply_text("⚠️ The replied message has no text to send.")
            return

        users = await db.get_all_users()
        sent, failed = 0, 0

        await message.reply_text(f"Broadcasting to {len(users)} users..")

        for user_id in users:
            try:
                await client.send_message(user_id, text_to_send)
                sent += 1
            except Exception:
                failed += 1

        await message.reply_text(f"✅ Broadcast finished!\n\n Sent: {sent}\nFailed: {failed}")

# ==========================================================
# stats Command
# ==========================================================
    @app.on_message(filters.private & filters.command("stats"))
    async def stats_command(client, message):
        if message.from_user.id != OWNER_ID:
            return await message.reply_text("❌ Only the bot owner can use this command")

        users = await db.get_all_users()
        return await message.reply_text(f"💡 Total users: {len(users)}")
