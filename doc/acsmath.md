acsmath - math functions
========================


Implementations of functions missing from Zandronum
---------------------------------------------------

### `int zan_Sqrt(int number)`
[ZDoom Wiki](http://zdoom.org/wiki/Sqrt)


Constants
---------

* `fixed PI` - the number Pi.
* `fixed SQRT_2` - square root of 2
* `int INT_MAX` - maximum possible value of `int`

Generic operations on numbers
-----------------------------

### `num abs(num x)`
Returns the absolute value of `x`.

#### Examples
    abs(2.0) == 2.0;
    abs(-123) == 123;

### `num min(num a, num b)`
Returns the lesser of `a` and `b`.

#### Examples
    min(3, 5) == 3;
    min(8.0, 7.5) == 7.5;

### `num max(num a, num b)`
Returns the greater of `a` and `b`.

#### Examples
    max(3, 5) == 5;
    max(8.0, 7.5) == 8.0;


Trigonometry
------------

Note: `sin` and `cos` are already in ZDoom.

### `fixed tan(angle x)`
Returns the tangent of `x`.

### `fixed atan(angle x)`
Returns the arctangent of `x`.


Vectors
-------

### `fixed length2d(fixed x, fixed y)`
### `fixed length3d(fixed x, fixed y, fixed z)`
Returns the length of the given 2d or 3d vector.

Rounding
--------

### `int round(fixed x)`
Rounds the number and returns it **as an integer**.

#### Examples
	int a = round(123.456); // a = 123
	int a = round(122.678); // a = 123

### `fixed ClearFraction(fixed x)`
Zeroes the fractional part of `x` and returns the result.

This is useful for HudMessages.

#### Examples
	int a = ClearFraction(123.456); // a = 123.0


	int x = ClearFraction(a * sin(x));
	int y = ClearFraction(b * sin(x));
	
	HudMessage(..., x, y, ...);
