acsstr - string functions
=========================
Depends on: `zcommon.acs`

### `str StdAdd(str a, str b)`
Joins two strings together and returns the result. Simplified variant of `StrParam(...)`.

#### Examples
	str a = "hello, ";
	str b = "world!";
	str c = StrAdd(a, b); // c = "hello, world"
  
### `str StrEquals(str a, str b)`
Checks if two strings are equal. Returns `true` if yes, `false` otherwise. Simplified variant of `StrCmp(...)`.

#### Examples
	str a = "hello";
	str b = "hello1";
	str c = "hello";
	bool exp1 = StrEquals(a, b); // exp1 = false
	bool exp2 = StrEquals(a, c); // exp2 = true

### `int SubStr(str a, str b)`
Looks for the substring **b** in the string **a**. **needs more info**

#### Examples
	str a = "aaabcdddd";
	str b = "aaaaaaaaa";
	str sub = "abc";
	int as = StrSub(a, sub); // as = 2
				 // a a *A B C* d d d d
				 // 0 1 *2 3 4* 5 6 7 8

	int bs = StrSub(b, sub); // bs = -1, the substring wasn't found.

### `str StrSubCut(str a, str b)`
Cuts the substring **b** from the string **a** and returns the resulting string.

#### Examples
	str a = "000abc111";
	str b = "abc";
	str c = StrCut(a, b); // c = "000111"

### `str StrSlice(str s, int l, int r)`
**No description yet**

### `str StrSlice(str s, int l, int r)`
**No description yet**

### `bool IsAscii(str s)`
Checks if string contain only ASCII symbols. Returns `true` if yes, returns `false` if it contains non-ASCII symbols.

#### Examples
	str a = "Hello 88005553535 boom"; // ASCII string
	str b = "Ïðèâåò, äðóã!"; // contains Cyrillic letters
	bool exp1 = IsAscii(a); // a = true
	bool exp2 = IsAscii(b); // b = false

### `bool StrHasColorCodes(str s)`
**No description yet**

### `str StrStripColorCodes(str s)`
**No description yet**

