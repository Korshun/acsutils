# acsstr
A simplified string library for Zandronum with useful functions.
---------------------------------------------------------------

## Documentation

#### StdAdd(str a, str b)
Joins two strings together and returns result. Simplified variant of StrParam(...).
Examples:
  str a = "hello, ";
  str b = "world!";
  str c = StrAdd(a, b); //*c = "hello, world"*
  
#### StrEquals(str a, str b)
Checks if two strings are equal. Returns 1 if yes, 0 otherwise. Simplified variant of StrCmp(...)
Examples:
  str a = "hello";
  str b = "hello1";
  str c = "hello";
  bool exp1 = StrEquals(a, b); //*exp1 = false*
  bool exp2 = StrEquals(a, c); //*exp2 = true*
