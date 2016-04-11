acsstr - string functions
=========================


### `str StdAdd(str a, str b)`
Joins two strings together and returns the result. Simplified variant of `StrParam(...)`.

Examples:

	str a = "hello, ";
	str b = "world!";
	str c = StrAdd(a, b); // c = "hello, world!"
  
### `str StrEquals(str a, str b)`
Checks if two strings are equal. Returns `true` if yes, `false` otherwise. Simplified variant of `StrCmp(...)`.

Examples:

	str a = "hello";
	str b = "hello1";
	str c = "hello";
	bool exp1 = StrEquals(a, b); // exp1 = false
	bool exp2 = StrEquals(a, c); // exp2 = true

### `int StrSub(str a, str b)`
Looks for the substring **b** in the string **a**. If the string was found, the function will return the position of the beginning of the first detected substring. If impossible or there's no matching substring, -1 will be returned.

Examples:

	str a = "aaabcdddd";
	str b = "aaaaaaaaa";
	str sub = "abc";
	int as = StrSub(a, sub); // as = 2
				 // a a **a b c** d d d d
				 // 0 1 **2 3 4** 5 6 7 8

	int bs = StrSub(b, sub); // bs = -1, the substring wasn't found.

### `str StrSubCut(str a, str b)`
Cuts the substring **b** from the string **a** and returns the resulting string.

Examples:

	str a = "000abc111";
	str b = "abc";
	str c = StrCut(a, b); // c = "000111"

### `str StrCut(str s, int l, int r)`
Removes the substring `s[l..r]` from the string **s** and returns the result.

Examples:

	str s = "abcdef";
	str res = StrCut(s, 2, 4); // res = "abf", symbols s[2] (c), s[3] (d), s[4] (e) were removed.

### `str StrSlice(str s, int l, int r)`
Copies the substring `s[l..r]` from the string **s** and returns it.

Examples:

	str s = "abcdef";
	str res = StrSlice(s, 2, 4); // res = "cde", symbols s[2], s[3], s[4] are returned.

### `bool IsAscii(str s)`
Checks if string **s** contains only ASCII symbols. Returns `true` if yes, returns `false` if it contains non-ASCII symbols.

Examples:

	str a = "Hello 88005553535 boom"; // ASCII string
	str b = "Ïðèâåò, äðóã!"; // contains Cyrillic letters
	bool exp1 = IsAscii(a); // a = true
	bool exp2 = IsAscii(b); // b = false

### `bool StrHasColorCodes(str s)`
Checks if string **s** has color codes (like /ca, /cb, /cg etc.). Returns `true` if yes, `false` otherwise. This is mostly used for player names.

Examples:

	str name1 = PlayerName(0); // The name of the first player, for example: \cgThe_\cjPlayer (contains \cX color codes)
	str name2 = PlayerName(1); // The name of the second player, for example: The_Player (no color codes)
	bool exp1 = StrHasColorCodes(name1); // exp1 = true
	bool exp2 = StrHasColorCodes(name2); // exp2 = false

### `str StrStripColorCodes(str s)`
Removes the color codes from the given string **s**. 

Examples:
	
	str name = PlayerName(0); // For example, name = "\cgThe_\cjPlayer"
	str nameclean = StrStripColorCodes(name); // nameclean = "The_Player"
	

