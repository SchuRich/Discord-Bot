
# Get Game Info Command
async def get_game_info(ctx):
    await ctx.send(
        "**__Developer__** --> Early Morning Studio\n"
        "**__Publisher__** --> Early Morning Studio\n"
        "**__Platforms__** --> Android / Apple\n"
        "**__Release date__** --> September 8, 2018\n"
        "**__Genre__** --> RPG\n"
        "**__Mode__** --> Singleplayer (Offline) , Multiplayer\n\n"
        "__Android__ - 97 MB Storage space / Android 4.1+\n"
        "__Apple__ - 468.9 MB Storage space / Requires iOS 10.0+ / Compatible with iPhone, iPad, and iPod touch.")


async def get_update(ctx):
    await ctx.send("__**Update 1.1.2**__\n"
                   "- NG+\n"
                   "- Stun in PvP now reduces focus instead of properly stunning in combo turns\n"
                   "- Item Augmentation\n"
                   "- Raised level cap to 75\n"
                   "- Ability to remove bloodstones from items\n"
                   "- Creature Lure potions available in stores\n"
                   "- Removed Armor Cap\n"
                   "- Less effect from bloodstones for stun, block chance, crit. dmg and crit. hit\n"
                   "- Displaying PvP-resilience values in PvP-menu\n"
                   "- Added  shield block resilience in PvP\n"
                   "- General bug fixes")
