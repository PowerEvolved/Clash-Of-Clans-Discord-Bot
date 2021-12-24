# Called when the bot joins a guild

import discord

from Data.Const_variables.import_const import Ids
from Script.Clients.top_gg_client import Dbl_client
from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def guild_join(self, guild):
    await Dbl_client.post_guild_count(len(self.guilds))
    users = 0
    bots = 0
    for member in guild.members:
        if member.bot:
            bots += 1
        else:
            users += 1
    log = self.get_channel(Ids["Log_bot_channel"])
    await log.send(f"The bot has JOINED the server {guild.name},\n owned by {guild.owner},\n with {len(guild.members)} members ({users} users and {bots} bots)")
    if guild.me.guild_permissions.manage_channels:
        channel_found = False
        for channel in guild.text_channels:
            if "clash-info-news" in channel.name:
                channel_found = True
                break
        if not channel_found:
            overwrite = {guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=False), guild.me: discord.PermissionOverwrite(add_reactions=True, embed_links=True, external_emojis=True, read_message_history=True, send_messages=True, view_channel=True)}
            channel = await guild.create_text_channel("clash-info-news", overwrites=overwrite)
        embed = create_embed("Thank you for using this bot on your server !", f"Hello\nIf you want to receive the list of the features for the bot, please check the reaction {Emojis['News']} bellow. If you want to delete this channel, please check the reaction {Emojis['Delete']} bellow. You can join the Clash INFO support server here : https://discord.gg/KQmstPw\n\nPlease grant the permissions `Use External Emoji` to `@everyone`, or the bot slash commands won't show emojis !", 0x00ffff, "", guild.me.avatar_url)
        msg = await channel.send(embed=embed)
        await msg.add_reaction(Emojis["News"])
        await msg.add_reaction(Emojis["Delete"])
        await channel.send("ses")
    return
