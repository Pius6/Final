class script(object):  
    START_TXT = """<b>✨ Hᴇʟʟᴏ {user}.

Mʏ Nᴀᴍᴇ Is {bot}.

I Cᴀɴ Pʀᴏᴠɪᴅᴇ Mᴏᴠɪᴇ Fᴏʀ Yᴏᴜ... 𝖳𝗎𝗍𝗈𝗋𝗂𝖺𝗅 𝖦𝗎𝗂𝖽𝖾 @mcrequestbot</b>""" 
    
    HELP_TXT = "Hᴇʏ {}\nHᴇʀᴇ Iꜱ Mʏ Hᴇʟᴩ"

    ABOUT_TXT = """<b>✯ Mʏ ɴᴀᴍᴇ: {}
✯ Dᴇᴠᴇʟᴏᴩᴇʀ: <a href=https://t.me/Manlikerex>Manlikerex</a>
✯ Cᴏᴅᴇᴅ Oɴ: ᴩʏᴛʜᴏɴ/ᴩʏʀᴏɢʀᴀᴍ
✯ Mʏ DᴀᴛᴀBᴀꜱᴇ: ᴍᴏɴɢᴏ-ᴅʙ
✯ Mʏ Sᴇʀᴠᴇʀ: ᴀɴʏᴡʜᴇʀᴇ
✯ Mʏ Vᴇʀꜱɪᴏɴ: V1.0</b>"""
   
    FILTER_TXT = "Sᴇʟᴇᴄᴛ Wʜɪᴄʜ Oɴᴇ Yᴏᴜ Wᴀɴᴛ...✨"

    MANUELFILTER_TXT = """<b>Hᴇʟᴘ Fᴏʀ Fɪʟᴛᴇʀs</b>

<i>Fɪʟᴛᴇʀ Is Tʜᴇ Fᴇᴀᴛᴜʀᴇ Wᴇʀᴇ Usᴇʀs Cᴀɴ Sᴇᴛ Aᴜᴛᴏᴍᴀᴛᴇᴅ Rᴇᴘʟɪᴇs Fᴏʀ A Pᴀʀᴛɪᴄᴜʟᴀʀ Kᴇʏᴡᴏʀᴅ Aɴᴅ Bᴏᴛ  Wɪʟʟ Rᴇsᴘᴏɴᴅ Wʜᴇɴᴇᴠᴇʀ A Kᴇʏᴡᴏʀᴅ Is Fᴏᴜɴᴅ Tʜᴇ Mᴇssᴀɢᴇ</i>

<b>Nᴏᴛᴇ:</b>
𝟷. Tʜɪs Bᴏᴛ Sʜᴏᴜʟᴅ Hᴀᴠᴇ Aᴅᴍɪɴ Pʀɪᴠɪʟʟᴀɢᴇ.
𝟸. Oɴʟʏ Aᴅᴍɪɴs Cᴀɴ Aᴅᴅ Fɪʟᴛᴇʀs Iɴ A Cʜᴀᴛ.
𝟹. Aʟᴇʀᴛ Bᴜᴛᴛᴏɴs Hᴀᴠᴇ A Lɪᴍɪᴛ Oғ 𝟼𝟺 Cʜᴀʀᴀᴄᴛᴇʀs.

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b>
• /filter - Aᴅᴅ A Fɪʟᴛᴇʀ Iɴ Cʜᴀᴛ
• /filters - Lɪsᴛ Aʟʟ Tʜᴇ Fɪʟᴛᴇʀs Oғ A Cʜᴀᴛ
• /del - Dᴇʟᴇᴛᴇ A Sᴘᴇᴄɪғɪᴄ Fɪʟᴛᴇʀ Iɴ Cʜᴀᴛ
• /delall - Dᴇʟᴇᴛᴇ Tʜᴇ Wʜᴏʟᴇ Fɪʟᴛᴇʀs Iɴ A Cʜᴀᴛ (Cʜᴀᴛ Oᴡɴᴇʀ Oɴʟʏ)"""

    BUTTON_TXT = """<b>Hᴇʟᴘ Fᴏʀ Bᴜᴛᴛᴏɴs</b>

<i>Tʜɪs Bᴏᴛ Sᴜᴘᴘᴏʀᴛs Bᴏᴛʜ Uʀʟ Aɴᴅ Aʟᴇʀᴛ Iɴʟɪɴᴇ Bᴜᴛᴛᴏɴs.</i>

<b>Nᴏᴛᴇ:</b>
𝟷. Tᴇʟᴇɢʀᴀᴍ Wɪʟʟ Nᴏᴛ Aʟʟᴏᴡs Yᴏᴜ Tᴏ Sᴇɴᴅ Bᴜᴛᴛᴏɴs Wɪᴛʜᴏᴜᴛ Aɴʏ Cᴏɴᴛᴇɴᴛ, Sᴏ Cᴏɴᴛᴇɴᴛ Is Mᴀɴᴅᴀᴛᴏʀʏ.
𝟸. Tʜɪs Bᴏᴛ Sᴜᴘᴘᴏʀᴛs Bᴜᴛᴛᴏɴs Wɪᴛʜ Aɴʏ Tᴇʟᴇɢʀᴀᴍ Mᴇᴅɪᴀ Tʏᴘᴇ.
𝟹. Bᴜᴛᴛᴏɴs Sʜᴏᴜʟᴅ Bᴇ Pʀᴏᴘᴇʀʟʏ Pᴀʀsᴇᴅ As Mᴀʀᴋᴅᴏᴡɴ Fᴏʀᴍᴀᴛ

<b>Uʀʟ Bᴜᴛᴛᴏɴs:</b>
[Bᴜᴛᴛᴏɴ Tᴇxᴛ](buttonurl:xxxxxxxxxxxx)

<b>Aʟᴇʀᴛ Bᴜᴛᴛᴏɴs:</b>
[Bᴜᴛᴛᴏɴ Tᴇxᴛ](buttonalert:Tʜɪs Is Aɴ Aʟᴇʀᴛ Mᴇssᴀɢᴇ)"""

    AUTOFILTER_TXT = """<b>Hᴇʟᴘ Fᴏʀ AᴜᴛᴏFɪʟᴛᴇʀ</b>

<Ai>Aᴜᴛᴏ Fɪʟᴛᴇʀ Is Tʜᴇ Fᴇᴀᴛᴜʀᴇ Tᴏ Fɪʟᴛᴇʀ & Sᴀᴠᴇ Tʜᴇ Fɪʟᴇs Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ Fʀᴏᴍ Cᴜᴀɴɴᴇʟ Tᴏ Gʀᴏᴜᴘ. Yᴏᴜ Cᴀɴ Usᴇ Tʜᴇ Fᴏʟʟᴏᴡɪɴɢ Cᴏᴍᴍᴀɴᴅ Tᴏ ᴏɴ/ᴏғғ Tʜᴇ AᴜᴛᴏFɪʟᴛᴇʀ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ</i>

• /autofilter on - ᴀᴜᴛᴏғɪʟᴛᴇʀ ᴇɴᴀʙʟᴇ ɪɴ ʏᴏʀ ᴄʜᴀᴛ
• /autofilter off - ᴀᴜᴛᴏғɪʟᴛᴇʀ ᴅɪsᴀʙʟᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ

<Ob>Oᴛʜᴇʀ Cᴏᴍᴍᴀɴᴅs:</b>
• /set_template - Sᴇᴛ Iᴍᴅʙ Tᴇᴍᴘʟᴀᴛᴇ Fᴏʀ Yᴏᴜʀ Gʀᴏᴜᴘ 
• /get_template - Gᴇᴛ Cᴜʀʀᴇɴᴛ Iᴍᴅʙ Tᴇᴍᴘʟᴀᴛᴇ Fᴏʀ Yᴏᴜʀ Gʀᴏᴜᴘ"""

    CONNECTION_TXT = """<b>Hᴇʟᴘ Fᴏʀ Cᴏɴɴᴇᴄᴛɪᴏɴs</b>

<i> Usᴇᴅ Tᴏ Cᴏɴɴᴇᴄᴛ Bᴏᴛ Tᴏ Pᴍ Fᴏʀ Mᴀɴᴀɢɪɴɢ Fɪʟᴛᴇʀs. Iᴛ Hᴇʟᴘs Tᴏ Aᴠᴏɪᴅ Sᴘᴀᴍᴍɪɴɢ Iɴ Gʀᴏᴜᴘs</i>

<b>Nᴏᴛᴇ:</b>
• Oɴʟʏ Aᴅᴍɪɴs Cᴀɴ Aᴅᴅ A Cᴏɴɴᴇᴄᴛɪᴏɴ.
• Sᴇɴᴅ /connect Fᴏʀ Cᴏɴɴᴇᴄᴛɪɴɢ Mᴇ Tᴏ Uʀ Pᴍ

<Cb>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b>
• /connect - Cᴏɴɴᴇᴄᴛ A Pᴀʀᴛɪᴄᴜʟᴀʀ Cʜᴀᴛ Tᴏ Yᴏᴜʀ Pᴍ
• /disconnect - Dɪsᴄᴏɴɴᴇᴄᴛ Fʀᴏᴍ A Cʜᴀᴛ
• /connections - Lɪsᴛ Aʟʟ Yᴏᴜʀ Cᴏɴɴᴇᴄᴛɪᴏɴs"""

    ADMIN_TXT = """<b>Hᴇʟᴩ Fᴏʀ Aᴅᴍɪɴꜱ</b>
    
<i>Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs</i>

<b>Cᴏᴍᴍᴀɴᴅ & Uꜱᴀɢᴇ</b>
• /logs - Tᴏ Gᴇᴛ Tʜᴇ Rᴇᴄᴇɴᴛ Eʀʀᴏʀꜱ
• /delete - Tᴏ Dᴇʟᴇᴛᴇ A Sᴘᴇᴄɪꜰɪᴄ Fɪʟᴇ Fʀᴏᴍ DB
• /deleteall - Tᴏ Dᴇʟᴇᴛᴇ Aʟʟ Fɪʟᴇs Fʀᴏᴍ DB
• /users - Tᴏ Gᴇᴛ Lɪꜱᴛ Oꜰ Mʏ Uꜱᴇʀꜱ Aɴᴅ Iᴅꜱ
• /chats - Tᴏ Gᴇᴛ Lɪꜱᴛ Oꜰ Mʏ Cʜᴀᴛꜱ Aɴᴅ Iᴅꜱ
• /channel - Tᴏ Gᴇᴛ Lɪꜱᴛ Oꜰ Tᴏᴛᴀʟ Cᴏɴɴᴇᴄᴛᴇᴅ Cʜᴀɴɴᴇʟꜱ
• /broadcast - Tᴏ Bʀᴏᴀᴅᴄᴀꜱᴛ A Mᴇꜱꜱᴀɢᴇ Tᴏ Aʟʟ Uꜱᴇʀꜱ
• /group_broadcast - Tᴏ Bʀᴏᴀᴅᴄᴀsᴛ A Mᴇssᴀɢᴇ Tᴏ Aʟʟ Cᴏɴɴᴇᴄᴛᴇᴅ Gʀᴏᴜᴘs
• /leave  - Wɪᴛʜ Cʜᴀᴛ Iᴅ Tᴏ Lᴇᴀᴠᴇ Fʀᴏᴍ A Cʜᴀᴛ
• /disable  - Wɪᴛʜ Cʜᴀᴛ Iᴅ Tᴏ Dɪꜱᴀʙʟᴇ A Cʜᴀᴛ
• /invite - Wɪᴛʜ Cʜᴀᴛ Iᴅ Tᴏ Gᴇᴛ Tʜᴇ Iɴᴠɪᴛᴇ Lɪɴᴋ Oғ Aɴʏ Cʜᴀᴛ Wʜᴇʀᴇ Tʜᴇ Bᴏᴛ Is Aᴅᴍɪɴ
• /ban_user  - Wɪᴛʜ Iᴅ Tᴏ Bᴀɴ A Uꜱᴇʀ
• /unban_user  - Wɪᴛʜ Iᴅ Tᴏ Uɴʙᴀɴ A Uꜱᴇʀ
• /restart - Tᴏ Rᴇsᴛᴀʀᴛ Tʜᴇ Bᴏᴛ
• /clear_junk - Cʟᴇᴀʀ Aʟʟ Dᴇʟᴇᴛᴇ Aᴄᴄᴏᴜɴᴛ & Bʟᴏᴄᴋᴇᴅ Aᴄᴄᴏᴜɴᴛ Iɴ Dᴀᴛᴀʙᴀsᴇ
• /clear_junk_group - Cʟᴇᴀʀ Aᴅᴅ Rᴇᴍᴏᴠᴇᴅ Gʀᴏᴜᴘ Oʀ Dᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ Gʀᴏᴜᴘs Oɴ Dʙ"""


    STATUS_TXT = """<b>◉ ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ: <code>{}</code>
◉ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: <code>{}</code>  
◉ ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ: <code>{}</code>
◉ ᴜꜱᴇᴅ ᴅʙ ꜱɪᴢᴇ: <code>{}</code>
◉ ꜰᴇᴇᴇ ᴅʙ ꜱɪᴢᴇ: <code>{}</code></b>"""

    LOG_TEXT_G = """<b>#ɴᴇᴡ_ɢʀᴏᴜᴩ

◉ ɢʀᴏᴜᴩ: {a}
◉ ɢ-ɪᴅ: <code>{b}</code>
◉ ʟɪɴᴋ: @{c}
◉ ᴍᴇᴍʙᴇʀꜱ: <code>{d}</code>
◉ ᴀᴅᴅᴇᴅ ʙʏ: {e}

◉ ʙʏ: @{f}</b>"""
  
    LOG_TEXT_P = """#ɴᴇᴡ_ᴜꜱᴇʀ
    
◉ ᴜꜱᴇʀ-ɪᴅ: <code>{}</code>
◉ ᴀᴄᴄ-ɴᴀᴍᴇ: {}
◉ ᴜꜱᴇʀɴᴀᴍᴇ: @{}

◉ ʙʏ: @{}</b>"""

    EXTRAMOD_TXT = """<b>Hᴇʟᴩ Fᴏʀ Exᴛʀᴀ Mᴏᴅᴜʟᴇ</b>

<i>Jᴜꜱᴛ Sᴇɴᴅ Aɴʏ Iᴍᴀɢᴇ Tᴏ Eᴅɪᴛ Iᴍᴀɢᴇ ✨</i>

<b>Cᴏᴍᴍᴀɴᴅꜱ & Uꜱᴀɢᴇ:</b>
• /id - Gᴇᴛ Iᴅ Oғ A Sᴘᴇᴄɪғᴇᴅ Usᴇʀ
• /info  - Gᴇᴛ Iɴғᴏʀᴍᴀᴛɪᴏɴ Aʙᴏᴜᴛ A Usᴇʀ
• /imdb  - Gᴇᴛ Tʜᴇ Fɪʟᴍ Iɴғᴏʀᴍᴀᴛɪᴏɴ Fʀᴏᴍ Iᴍᴅʙ Sᴏᴜʀᴄᴇ
• /json - Rᴇᴩʟʏ Wɪᴛʜ Aɴʏ Mᴇꜱꜱᴀɢᴇ Tᴏ Gᴇᴛ Mᴇꜱꜱᴀɢᴇ Iɴꜰᴏ (ᴜꜱᴇꜰᴜʟʟ ꜰᴏʀ ɢʀᴏᴜᴩ)"""    
    
    CREATOR_REQUIRED = "❗<b>Yᴏᴜ Hᴀᴠᴇ To Bᴇ Tʜᴇ Gʀᴏᴜᴩ Cʀᴇᴀᴛᴏʀ Tᴏ Dᴏ Tʜᴀᴛ</b>"
      
    INPUT_REQUIRED = "❗ **Aʀɢᴜᴍᴇɴ Rqᴜɪʀᴇᴅ**"
      
    KICKED = "✔️ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ Kɪᴄᴋᴇᴅ {} Mᴇᴍʙᴇʀꜱ Acᴄᴏʀᴅɪɴɢ To Tʜᴇ Aʀɢᴜᴍᴇɴᴛꜱ Prᴏᴠɪᴅᴇᴅ"
      
    START_KICK = "Rᴇᴍᴏᴠɪɴɢ Iɴᴀᴄᴛɪᴠᴇ Mᴇᴍʙᴇʀs Tʜɪs Mᴀʏ Tᴀᴋᴇ A Wʜɪʟᴇ"
      
    ADMIN_REQUIRED = "❗<b>Iᴀᴍ Nᴏᴛ Aᴅᴍɪɴ Iɴ Tʜɪꜱ Cʜᴀᴛ Sᴏ Pʟᴇᴀꜱᴇ Aᴅᴅ Mᴇ Aɢᴀɪɴ Wɪᴛʜ Aʟʟ Pᴅᴍɪɴ Pᴇʀᴍɪꜱꜱɪᴏɴ</b>"
      
    DKICK = "✔️ Kɪᴄᴋᴇᴅ {} Dᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛꜱ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ"
      
    FETCHING_INFO = "<b>Wᴀɪᴛ I Wɪʟʟ Tᴀᴋᴇ Tʜᴇ Aʟʟ Iɴꜰᴏ</b>"
   
    SERVER_STATS = """Sᴇʀᴠᴇʀ Sᴛᴀᴛꜱ:
 
Uᴩᴛɪᴍᴇ: {}
CPU Uꜱᴀɢᴇ: {}%
RAM Uꜱᴀɢᴇ: {}%
Tᴏᴛᴀʟ Dɪꜱᴋ: {}
Uꜱᴇᴅ Dɪꜱᴋ: {} ({}%)
Fʀᴇᴇ Dɪꜱᴋ: {}"""
    
    BUTTON_LOCK_TEXT = "Hᴇʏ {query}\nTʜɪꜱ Iꜱ Nᴏᴛ Fᴏʀ Yᴏᴜ. Sᴇᴀʀᴄʜ For Yᴏᴜʀ Sᴇʟꜰ"
   
    FORCE_SUB_TEXT = "Pʟᴇᴀsᴇ Cʟɪᴄᴋ THE Jᴏɪɴ Bᴜᴛᴛᴏɴ Tᴏ Jᴏɪɴ Mʏ Cʜᴀɴɴᴇʟ Aɴᴅ Tʀʏ Aɢᴀɪɴ"
   
    WELCOM_TEXT = """Hᴇʏ {user} 💞

Wᴇʟᴄᴏᴍᴇ ᴛᴏ {chat}.

ꜱʜᴀʀᴇ & ꜱᴜᴩᴩᴏʀᴛ"""

<u>𝗥𝗲𝗾𝘂𝗲𝘀𝘁𝘀 𝗙𝗼𝗿𝗺𝗮𝘁𝘀</u>

• 𝖲𝗈𝗅𝗈 2017
• 𝖣𝗁𝗈𝗈𝗆 3 𝖧𝗂𝗇𝖽𝗂
• 𝖪𝗎𝗋𝗎𝗉 𝖪𝖺𝗇
• 𝖣𝖺𝗋𝗄 𝗌01
• 𝖲𝗁𝖾 𝖧𝗎𝗅𝗄 720𝗉
• 𝖥𝗋𝗂𝖾𝗇𝖽𝗌 𝗌03 1080𝗉

‼️𝗗𝗼𝗻𝘁 𝗮𝗱𝗱 𝘄𝗼𝗿𝗱𝘀 & 𝘀𝘆𝗺𝗯𝗼𝗹𝘀 𝗹𝗶𝗸𝗲 , . - / 𝗲𝘁𝗰‼️"""

  
    IMDB_TEMPLATE = """<b>Qᴜᴇʀʏ: {query}</b>

🏷 Tɪᴛʟᴇ: <a href={url}>{title}</a>
🎭 Gᴇɴʀᴇꜱ: {genres}
📆 Yᴇᴀʀ: <a href={url}/releaseinfo>{year}</a>
🌟 Rᴀᴛɪɴɢ: <a href={url}/ratings>{rating}</a>/10"""
   
  
 


   
  
 


