acszdoom - utilities for ZDoom scripting
========================================


Constants
---------

`int MAX_PLAYERS` - maximum amount of players in Zandronum multiplayer.

Functions
---------

### `bool IsZandronum()`
Returns true if the mod is being played in Zandronum.

Examples:
	
	if (IsZandronum())
		// Use workaronds
	else
		// Use ZDoom 2.7.1 features
		

### `void SetInventory(str item, int amount)`
Sets the amount of inventory items of type `item`
in activator's inventory to be equal to `amount`.

Examples:
	
	SetInventory("Shells", 8); // The player will now have exactly 8 shells.
	SetInventory("IsReloading", 0); // Set the "IsReloading" flag to 0.
	
### `void SetActorInventory(int tid, str item, int amount)`
Sets the amount of inventory items in the given actor's inventory.

**Needs examples**

### `void ClearHudMessage(int id)`
Removes the hud message with the given id.

**Needs examples**

### `str PlayerName(int player)`
Returns the name of the specified player.

Examples:

	for (int i = 0; i < MAX_PLAYERS; i++)
	{
		print(s:"Player ", d:i, "'s name is ", s:PlayerName(i));
	}

### `str ActivatorName()`
If the activator is not a player, returns his DECORATE actor name.

If the activator is a player, returns the player's name.

Examples:

	print(s:"Your name is ", s:ActivatorName());
	
	SetActivator(2); // Some monster.
	PrintBold(s:"This monster's type is ", s:ActivatorName());

### `bool ActivatorIsPlayer()`
Returns true if the activator is a player.