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
