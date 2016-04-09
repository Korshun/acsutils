ACS Libraries for ZDoom scripting
=================================


This is a collection of various libraries made with the purpose of enhancing your ACS code with easy-to-use functions for common stuff.

Use them how you want as long as you give credit to the authors.

## How to use
Download the libraries from `src/` folder, copy them to your mod and `#include` them. For example:

	#library "myproject"
	#include "zcommon.acs"
	
	#include "acsmath.acs"
	#include "acsstr.acs"
	#include "acsutils.acs"
	
Some libraries can depend on each other or on `zcommon.acs`.
Be sure to include their dependencies before you include them.
Their dependencies are enumerated in the documentation on them.
See the file `src/compile_all.acs` for an include order that makes
all libraries work.


**The easiest way is to simply use ALL libraries** by copying `src/compile_all.acs.

## Included libraries
* `acsmath` - math functions missing from ZDoom
* `acsutils` - utilities for ZDoom scripting
* `acsstr` - common string functions coming from other programming languages


See the `doc/` folder for documentation on each library.

## Authors
* Korshun
* DjSkaarj
