ACS Libraries for ZDoom scripting
=================================


This is a collection of useful ACS functions to make ACS scripting easier.

Use it how you want as long as you give credit to the authors.

## How to use
Download the libraries from the `src/` folder,
copy them to your mod and `#include "acsutils.acs"`. For example:

	#library "myproject"
	#include "zcommon.acs"
	#include "acsutils.acs"
	
	// Your code follows.

## Included libraries
* `acsretval` - multiple return values for ACS functions
* `acsmath` - additional math functions coming from other programming languages
* `acsstr` - common string functions coming from other programming languages
* `acszdoom` - utilities for ZDoom and Zandronum scripting

See the `doc/` folder for documentation on each library.

## Authors
* Korshun
* DjSkaarj

**Contributions are welcome!**