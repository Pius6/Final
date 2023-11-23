import asyncio, re, ast, time, math, logging, random, pyrogram, shutil, psutil 

# Pyrogram Functions
from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto
from pyrogram import Client, filters, enums 
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid

# Helper Function
from Script import script
from utils import get_size, is_subscribed, get_poster, search_gagala, temp, get_settings, save_group_settings, get_time, humanbytes, send_all 

# Database Function 
from database.connections_mdb import active_connection, all_connections, delete_connection, if_active, make_active, make_inactive
from database.ia_filterdb import Media, get_file_details, get_search_results
from database.filters_mdb import del_all, find_filter, get_filters
from database.users_chats_db import db

# Configuration
from info import ADMINS, AUTH_CHANNEL, AUTH_USERS, CUSTOM_FILE_CAPTION, AUTH_GROUPS, P_TTI_SHOW_OFF, PICS, IMDB, PM_IMDB, SINGLE_BUTTON, PROTECT_CONTENT, \
    SPELL_CHECK_REPLY, IMDB_TEMPLATE, IMDB_DELET_TIME, START_MESSAGE, PMFILTER, BUTTON_LOCK, BUTTON_LOCK_TEXT

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)



@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "close_data":
        await query.message.delete()
        
    elif query.data == "delallconfirm":
        userid = query.from_user.id
        chat_type = query.message.chat.type
        if chat_type == enums.ChatType.PRIVATE:
            grpid = await active_connection(str(userid))
            if grpid is not None:
                grp_id = grpid
                try:
                    chat = await client.get_chat(grpid)
                    title = chat.title
                except:
                    return await query.message.edit_text("Make Sure I'm Present In Your Group!!", quote=True)
            else:
                return await query.message.edit_text("I'm Not Connected To Any Groups!\ncheck /Connections Or Connect To Any Groups", quote=True)
        elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            grp_id = query.message.chat.id
            title = query.message.chat.title
        else: return
        st = await client.get_chat_member(grp_id, userid)
        if (st.status == enums.ChatMemberStatus.OWNER) or (str(userid) in ADMINS): await del_all(query.message, grp_id, title)
        else: await query.answer("You Need To Be Group Owner Or An Auth User To Do That!", show_alert=True)
        
    elif query.data == "delallcancel":
        userid = query.from_user.id
        chat_type = query.message.chat.type
        if chat_type == enums.ChatType.PRIVATE:
            await query.message.reply_to_message.delete()
            await query.message.delete()
        elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            grp_id = query.message.chat.id
            st = await client.get_chat_member(grp_id, userid)
            if (st.status == enums.ChatMemberStatus.OWNER) or (str(userid) in ADMINS):
                await query.message.delete()
                try: await query.message.reply_to_message.delete()
                except: pass
            else: await query.answer("Buddy Don't Touch people's Property 😁", show_alert=True)
            
    elif "groupcb" in query.data:
        group_id = query.data.split(":")[1]
        act = query.data.split(":")[2]
        hr = await client.get_chat(int(group_id))
        title = hr.title
        user_id = query.from_user.id
        if act == "":
            stat = "Connect"
            cb = "connectcb"
        else:
            stat = "Disconnect"
            cb = "disconnect"
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton(f"{stat}", callback_data=f"{cb}:{group_id}"),
            InlineKeyboardButton("Delete", callback_data=f"deletecb:{group_id}")
            ],[
            InlineKeyboardButton("Back", callback_data="backcb")]
        ])
        await query.message.edit_text(f"Group Name:- **{title}**\nGroup Id:- `{group_id}`", reply_markup=keyboard, parse_mode=enums.ParseMode.MARKDOWN)
      
    elif "connectcb" in query.data:
        group_id = query.data.split(":")[1]
        hr = await client.get_chat(int(group_id))
        title = hr.title
        user_id = query.from_user.id
        mkact = await make_active(str(user_id), str(group_id))
        if mkact: await query.message.edit_text(f"Connected To: **{title}**", parse_mode=enums.ParseMode.MARKDOWN,)
        else: await query.message.edit_text('Some Error Occurred!!', parse_mode="md")
       
    elif "disconnect" in query.data:
        group_id = query.data.split(":")[1]
        hr = await client.get_chat(int(group_id))
        title = hr.title
        user_id = query.from_user.id
        mkinact = await make_inactive(str(user_id))
        if mkinact: await query.message.edit_text(f"Disconnected From **{title}**", parse_mode=enums.ParseMode.MARKDOWN)
        else: await query.message.edit_text(f"Some Error Occurred!!", parse_mode=enums.ParseMode.MARKDOWN)
      
    elif "deletecb" in query.data:
        user_id = query.from_user.id
        group_id = query.data.split(":")[1]
        delcon = await delete_connection(str(user_id), str(group_id))
        if delcon: await query.message.edit_text("Successfully Deleted Connection")
        else: await query.message.edit_text(f"Some Error Occurred!!", parse_mode=enums.ParseMode.MARKDOWN)
       
    elif query.data == "backcb":
        userid = query.from_user.id
        groupids = await all_connections(str(userid))
        if groupids is None:
            return await query.message.edit_text("There Are No Active Connections!! Connect To Some Groups First.")
        buttons = []
        for groupid in groupids:
            try:
                ttl = await client.get_chat(int(groupid))
                title = ttl.title
                active = await if_active(str(userid), str(groupid))
                act = " - ACTIVE" if active else ""
                buttons.append([InlineKeyboardButton(f"{title}{act}", callback_data=f"groupcb:{groupid}:{act}")])
            except: pass
        if buttons: await query.message.edit_text("Your Connected Group Details ;\n\n", reply_markup=InlineKeyboardMarkup(buttons))
            
    elif "alertmessage" in query.data:
        grp_id = query.message.chat.id
        i = query.data.split(":")[1]
        keyword = query.data.split(":")[2]        
        reply_text, btn, alerts, fileid = await find_filter(grp_id, keyword)       
        if alerts is not None:
            alerts = ast.literal_eval(alerts)
            alert = alerts[int(i)]
            alert = alert.replace("\\n", "\n").replace("\\t", "\t")
            await query.answer(alert, show_alert=True)
            
    if query.data.startswith("pmfile"):
        ident, file_id = query.data.split("#")
        files_ = await get_file_details(file_id)
        if not files_: return await query.answer('No Such File Exist.')
        files = files_[0]
        title = files.file_name
        size = get_size(files.file_size)
        f_caption = f_caption = f"{title}"
        if CUSTOM_FILE_CAPTION:
            try: f_caption = CUSTOM_FILE_CAPTION.format(mention=query.from_user.mention, file_name='' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)                                                                                                      
            except Exception as e: logger.exception(e)
        try:                  
            if AUTH_CHANNEL and not await is_subscribed(client, query):
                return await query.answer(url=f"https://t.me/{temp.U_NAME}?start={ident}_{file_id}")
            else:
                await client.send_cached_media(chat_id=query.from_user.id, file_id=file_id, caption=f_caption, protect_content=True if ident == "pmfilep" else False)                       
        except Exception as e:
            await query.answer(f"⚠️ Eʀʀᴏʀ {e}", show_alert=True)
        
    if query.data.startswith("file"):        
        ident, req, file_id = query.data.split("#")
        if BUTTON_LOCK:
            if int(req) not in [query.from_user.id, 0]:
                return await query.answer(BUTTON_LOCK_TEXT.format(query=query.from_user.first_name), show_alert=True)
        files_ = await get_file_details(file_id)
        if not files_: return await query.answer('No Such File Exist.')
        files = files_[0]
        title = files.file_name
        size = get_size(files.file_size)
        f_caption = f_caption = f"{title}"
        settings = await get_settings(query.message.chat.id)
        if CUSTOM_FILE_CAPTION:
            try: f_caption = CUSTOM_FILE_CAPTION.format(mention=query.from_user.mention, file_name='' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)                               
            except Exception as e: logger.exception(e)
        try:
            if AUTH_CHANNEL and not await is_subscribed(client, query):
                return await query.answer(url=f"https://t.me/{temp.U_NAME}?start={ident}_{file_id}")
            elif settings['botpm']:
                return await query.answer(url=f"https://t.me/{temp.U_NAME}?start={ident}_{file_id}")
            else:
                await client.send_cached_media(chat_id=query.from_user.id, file_id=file_id, caption=f_caption, protect_content=True if ident == "filep" else False)
                await query.answer('Cʜᴇᴄᴋ YOUR PM, I Hᴀᴠᴇ Sᴇɴᴛ THE Fɪʟᴇs THERE', show_alert=False)
        except UserIsBlocked:
            await query.answer('unblock the bot! (Go to your settings and check privacy settings and then check your blocked users and unblock the bot there!', show_alert=True)
        except PeerIdInvalid:
            await query.answer(url=f"https://t.me/{temp.U_NAME}?start={ident}_{file_id}")
        except Exception as e:
            await query.answer(url=f"https://t.me/{temp.U_NAME}?start={ident}_{file_id}")
     
    elif query.data.startswith("checksub"):
        if AUTH_CHANNEL and not await is_subscribed(client, query):
            return await query.answer("𝖨 𝖫𝗂𝗄𝖾 𝖸𝗈𝗎𝗋 𝖲𝗆𝖺𝗋𝗍𝗇𝖾𝗌𝗌, 𝖡𝗎𝗍 𝖣𝗈𝗇'𝗍 𝖡𝖾 𝖮𝗏𝖾𝗋𝗌𝗆𝖺𝗋𝗍 😒 \n𝖩𝗈𝗂𝗇 the 𝖴𝗉𝖽𝖺𝗍𝖾 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖿𝗂𝗋𝗌𝗍", show_alert=True)
        ident, file_id = query.data.split("#")
        files_ = await get_file_details(file_id)
        if not files_: return await query.answer('NO SUCH FILE EXIST....')
        files = files_[0]
        title = files.file_name
        size = get_size(files.file_size)
        f_caption = f_caption = f"{title}"
        if CUSTOM_FILE_CAPTION:
            try: f_caption = CUSTOM_FILE_CAPTION.format(mention=query.from_user.mention, file_name='' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)  
            except Exception as e: logger.exception(e)
        await client.send_cached_media(chat_id=query.from_user.id, file_id=file_id, caption=f_caption, protect_content=True if ident == 'checksubp' else False)
    elif query.data == "pages":
        await query.answer("What are you looking for? 😁", show_alert=True)
    
    elif query.data.startswith("send_all"):
        _, req, key, pre = query.data.split("#")
        if int(req) not in [query.from_user.id, 0]:
            return await query.answer("This is Not your Request, Request for Yours!!" , show_alert=True)
            except Exception as e:
        await query.answer(url=f"https://t.me/{temp.U_NAME}?start=all_{key}_{pre}")

    elif query.data == 'info':
        await query.answer("𝗥𝗲𝗾𝘂𝗲𝘀𝘁𝘀 𝗙𝗼𝗿𝗺𝗮𝘁𝘀\n\n• moana 2016\n• 𝖣𝗁𝗈𝗈𝗆 3 𝖧𝗂𝗇𝖽𝗂\n• 𝖪𝗎𝗋𝗎𝗉 𝖪𝖺𝗇𝗇𝖺𝖽𝖺\n• 𝖣𝖺𝗋𝗄 S01\n• 𝖲𝗁𝖾 𝖧𝗎𝗅𝗄 S01E01\n• 𝖥𝗋𝗂𝖾𝗇𝖽𝗌 𝗌03 1080𝗉\n\n‼️𝗗𝗼𝗻𝘁 𝗮𝗱𝗱 𝘄𝗼𝗿𝗱𝘀 & 𝘀𝘆𝗺𝗯𝗼𝗹𝘀  , . - / : 𝗲𝘁𝗰‼️", True)
    
    elif query.data == 'tips':
        await query.answer("𝖳𝗁𝗂𝗌 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖶𝗂𝗅𝗅 𝖡𝖾 𝖣𝖾𝗅𝖾𝗍𝖾𝖽 𝖠𝖿𝗍𝖾𝗋 5 𝖬𝗂𝗇𝗎𝗍𝖾𝗌 𝗍𝗈 𝖯𝗋𝖾𝗏𝖾𝗇𝗍 𝖢𝗈𝗉𝗒𝗋𝗂𝗀𝗁𝗍 !\n\n𝖳𝗁𝖺𝗇𝗄 𝖸𝗈𝗎 𝖥𝗈𝗋 𝖴𝗌𝗂𝗇𝗀 𝖬𝖾 😊", True)
    
    elif query.data == "start":                        
        buttons = [[
            InlineKeyboardButton("⚚ ΛᎠᎠ MΞ ϮԾ YԾUᏒ GᏒԾUᎮ ⚚", url=f'http://t.me/{temp.U_NAME}?startgroup=true')
            ],[
            InlineKeyboardButton("🔍 𝚂𝚎𝚊𝚛𝚌𝚑", switch_inline_query_current_chat=''),
            InlineKeyboardButton("🍿 UᎮDΛTΞS 🍿", url="https://t.me/Lordshiptv")
            ],[
            InlineKeyboardButton("♻️ HΞLᎮ ♻️", callback_data="help"),
            InlineKeyboardButton("💫 ΛBOUT 💫", callback_data="about")
         ]]
        await query.message.edit_text(text=script.START_MESSAGE.format(user=query.from_user.mention, bot=client.mention), enums.ParseMode.HTML), reply_markup=InlineKeyboardMarkup(buttons))
       
    elif query.data == "help":
        buttons = [[
            InlineKeyboardButton('⚙️ Aᴅᴍɪɴ Pᴀɴᴇʟ ⚙️', 'admin')            
            ],[
            InlineKeyboardButton('Fɪʟᴛᴇʀꜱ', 'openfilter'),
            InlineKeyboardButton('Cᴏɴɴᴇᴄᴛ', 'coct')
            ],[                       
            InlineKeyboardButton('Exᴛʀᴀ Mᴏᴅᴇ', 'extmod')
            ],[           
            InlineKeyboardButton('Gʀᴏᴜᴩ Mᴀɴᴀɢᴇʀ', 'gpmanager'), 
            InlineKeyboardButton('Bᴏᴛ Sᴛᴀᴛᴜꜱ 🔮', 'stats')
            ],[
            InlineKeyboardButton('✘ Cʟᴏꜱᴇ', 'close_data'),
            InlineKeyboardButton('« Bᴀᴄᴋ', 'start')           
        ]]
        await query.message.edit_text(text=script.HELP_TXT.format(query.from_user.mention), enums.ParseMode.HTML), reply_markup=InlineKeyboardMarkup(buttons))     
        
    elif query.data == "about":
        buttons= [[
            InlineKeyboardButton('✘ Cʟᴏꜱᴇ', 'close_data'),
            InlineKeyboardButton('« Bᴀᴄᴋ', 'start')          
        ]]
        await query.message.edit_text(text=script.ABOUT_TXT.format(temp.B_NAME), enums.ParseMode.HTML), reply_markup=InlineKeyboardMarkup(buttons))
        
    elif query.data == "admin":
        buttons = [[
            InlineKeyboardButton('✘ Cʟᴏꜱᴇ', 'close_data'),
            InlineKeyboardButton('« Bᴀᴄᴋ', 'help')           
        ]]
        if query.from_user.id not in ADMINS:
            return await query.answer("Sᴏʀʀʏ Tʜɪs Mᴇɴᴜ Oɴʟʏ Fᴏʀ Mʏ Aᴅᴍɪɴs ⚒️", show_alert=True)
        await query.message.edit("Pʀᴏᴄᴇꜱꜱɪɴɢ Wᴀɪᴛ Fᴏʀ 15 ꜱᴇᴄ...")
        total, used, free = shutil.disk_usage(".")
        stats = script.SERVER_STATS.format(get_time(time.time() - client.uptime), psutil.cpu_percent(), psutil.virtual_memory().percent, humanbytes(total), humanbytes(used), psutil.disk_usage('/').percent, humanbytes(free))            
        stats_pic = await make_carbon(stats, True)
        await query.message.edit_text(text=script.ADMIN_TXT, enums.ParseMode.HTML), reply_markup=InlineKeyboardMarkup(buttons))
        
    elif query.data == "openfilter":
        buttons = [[
            InlineKeyboardButton('AᴜᴛᴏFɪʟᴛᴇʀ', 'autofilter'),
            InlineKeyboardButton('MᴀɴᴜᴀʟFɪʟᴛᴇʀ', 'manuelfilter')
            ],[
            InlineKeyboardButton('✘ Cʟᴏꜱᴇ', 'cse_data'),
            InlineKeyboardButton('« Bᴀᴄᴋ', 'help')           
        ]]
        await query.message.edit_text(text=script.FILTER_TXT, enums.ParseMode.HTML), reply_markup=InlineKeyboardMarkup(buttons))
        
    elif query.data == "autofilter":
        buttons = [[
            InlineKeyboardButton('✘ Cʟᴏꜱᴇ', 'close_data'),
            InlineKeyboardButton('« Bᴀᴄᴋ', 'openfilter')           
        ]]
        await query.message.edit_text(text=script.AUTOFILTER_TXT, enums.ParseMode.HTML), reply_markup=InlineKeyboardMarkup(buttons))
        
    elif query.data == "manuelfilter":
        buttons = [[
            InlineKeyboardButton('Bᴜᴛᴛᴏɴ Fᴏʀᴍᴀᴛ', 'button')
            ],[
            InlineKeyboardButton('✘ Cʟᴏꜱᴇ', 'close_data'),
            InlineKeyboardButton('« Bᴀᴄᴋ', 'openfilter')           
        ]]
        await query.message.edit_text(text=script.MANUELFILTER_TXT, enums.ParseMode.HTML), reply_markup=InlineKeyboardMarkup(buttons))
    
    elif query.data.startswith("button"):
        buttons = [[
            InlineKeyboardButton('✘ Cʟᴏꜱᴇ', 'close_data'),
            InlineKeyboardButton('« Bᴀᴄᴋ', 'manuelfilter')           
        ]]
        await query.message.edit_text(text=script.BUTTON_TXT, enums.ParseMode.HTML), reply_markup=InlineKeyboardMarkup(buttons))
   
    elif query.data == "coct":
        buttons = [[
            InlineKeyboardButton('✘ Cʟᴏꜱᴇ', 'close_data'),
            InlineKeyboardButton('« Bᴀᴄᴋ', 'help')           
        ]]
        await query.message.edit_text(text=script.CONNECTION_TXT, enums.ParseMode.HTML), reply_markup=InlineKeyboardMarkup(buttons))
         
    elif query.data == "newdata":
        buttons = [[
            InlineKeyboardButton('✘ Cʟᴏꜱᴇ', 'close_data'),
            InlineKeyboardButton('« Bᴀᴄᴋ', 'help')           
        ]]
        await query.message.edit_text(text=script.FILE_TXT, enums.ParseMode.HTML), reply_markup=InlineKeyboardMarkup(buttons))
        
    elif query.data == "extmod":
        buttons = [[
            InlineKeyboardButton('✘ Cʟᴏꜱᴇ', 'close_data'),
            InlineKeyboardButton('« Bᴀᴄᴋ', 'help')           
        ]]
        await query.message.edit_text(text=script.EXTRAMOD_TXT, enums.ParseMode.HTML),             reply_markup=InlineKeyboardMarkup(buttons))
        
    elif query.data == "gpmanager":
        buttons = [[
            InlineKeyboardButton('✘ Cʟᴏꜱᴇ', 'close_data'),
            InlineKeyboardButton('« Bᴀᴄᴋ', 'help')           
        ]]
        await query.message.edit_text(text=script.GROUPMANAGER_TXT, enums.ParseMode.HTML), reply_markup=InlineKeyboardMarkup(buttons))           
        
    elif query.data == "stats":
        buttons = [[
            InlineKeyboardButton('♻️ Rᴇꜰʀᴇꜱʜ', 'stats'),
            InlineKeyboardButton('« Bᴀᴄᴋ', 'help')           
        ]]
        total = await Media.count_documents()
        users = await db.total_users_count()
        chats = await db.total_chat_count()
        monsize = await db.get_db_size()
        free = 536870912 - monsize
        monsize = get_size(monsize)
        free = get_size(free)
        await query.message.edit('ʟᴏᴀᴅɪɴɢ....')
        await query.message.edit_text(text=script.STATUS_TXT.format(total, users, chats, monsize, free), enums.ParseMode.HTML), reply_markup=InlineKeyboardMarkup(buttons))
    
    elif query.data.startswith("setgs"):
        ident, set_type, status, grp_id = query.data.split("#")
        grpid = await active_connection(str(query.from_user.id))
        if str(grp_id) != str(grpid):
            return await query.message.edit("Yᴏᴜʀ Aᴄᴛɪᴠᴇ Cᴏɴɴᴇᴄᴛɪᴏɴ Hᴀs Bᴇᴇɴ Cʜᴀɴɢᴇᴅ. Gᴏ Tᴏ /settings")
        if status == "True": await save_group_settings(grpid, set_type, False)
        else: await save_group_settings(grpid, set_type, True)
        settings = await get_settings(grpid)
        if settings is not None:
            buttons = [[
                InlineKeyboardButton(f"ꜰɪʟᴛᴇʀ ʙᴜᴛᴛᴏɴ : {'sɪɴɢʟᴇ' if settings['button'] else 'ᴅᴏᴜʙʟᴇ'}", f'setgs#button#{settings["button"]}#{str(grp_id)}')
                ],[
                InlineKeyboardButton(f"ꜰɪʟᴇ ɪɴ ᴩᴍ ꜱᴛᴀʀᴛ: {'ᴏɴ' if settings['botpm'] else 'ᴏꜰꜰ'}", f'setgs#botpm#{settings["botpm"]}#{str(grp_id)}')
                ],[                
                InlineKeyboardButton(f"ʀᴇꜱᴛʀɪᴄᴛ ᴄᴏɴᴛᴇɴᴛ : {'ᴏɴ' if settings['file_secure'] else 'ᴏꜰꜰ'}", f'setgs#file_secure#{settings["file_secure"]}#{str(grp_id)}')
                ],[
                InlineKeyboardButton(f"ɪᴍᴅʙ ɪɴ ꜰɪʟᴛᴇʀ : {'ᴏɴ' if settings['imdb'] else 'ᴏꜰꜰ'}", f'setgs#imdb#{settings["imdb"]}#{str(grp_id)}')
                ],[
                InlineKeyboardButton(f"ꜱᴩᴇʟʟɪɴɢ ᴄʜᴇᴄᴋ : {'ᴏɴ' if settings['spell_check'] else 'ᴏꜰꜰ'}", f'setgs#spell_check#{settings["spell_check"]}#{str(grp_id)}')
                ],[
                InlineKeyboardButton(f"ᴡᴇʟᴄᴏᴍᴇ ᴍᴇꜱꜱᴀɢᴇ : {'ᴏɴ' if settings['welcome'] else 'ᴏꜰꜰ'}", f'setgs#welcome#{settings["welcome"]}#{str(grp_id)}')
            ]]
            await query.message.edit_reply_markup(InlineKeyboardMarkup(buttons))







