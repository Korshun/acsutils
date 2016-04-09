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

### `fixed sec(angle x)`
Returns the secant of `x`.

### `fixed cosec(angle x)`
returns the cosecant of `x`.


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


Other
-----

### `fixed lerp(fixed a, fixed b, fixed alpha)`
Performs [linear interpolation](https://en.wikipedia.org/wiki/Linear_interpolation)
between two numbers `a` and `b` using factor `alpha` and returns the result.

In other words, "mixes" the values `a` and `b` using `alpha` to determine
how close the resulting value will be to either `a` or `b`.

#### Examples
	lerp(a, b, 0.0) == a;
	lerp(a, b, 1.0) == b;
	lerp(a, b, 0.5) == (a + b) / 2; // Average of a and b.

	// Simple animation.
	for (int time = 0; time < 1.0; time += 0.05)
	{
		int x = lerp(x1, x2, time); 
		int y = lerp(y1, y2, time);
		DrawSomething(x, y);
		Delay(1);
	}