acsmath - math functions
========================
Depends on: nothing

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

Examples:

    abs(2.0) == 2.0;
    abs(-123) == 123;

### `num min(num a, num b)`
Returns the lesser of `a` and `b`.

Examples:

    min(3, 5) == 3;
    min(8.0, 7.5) == 7.5;

### `num max(num a, num b)`
Returns the greater of `a` and `b`.

Examples:

    max(3, 5) == 5;
    max(8.0, 7.5) == 8.0;

### `int sign(num x)`
Returns the sign of `x`. `1` for positive, `-1` for negative, `0` for zero.

### `num clamp(num x, num a, num b)`
Limits `x` to the range [`a`; `b`]. If `x` falls in the range, returns `x`.
If `x` is less than `a`, returns `a`. If `x` is greater than `b`, returns `b`.

Examples:

	clamp(7, 6, 8) == 7;
	clamp(0.1, 0.2, 0.3) == 0.1;

Trigonometry
------------

Note: [`sin`](http://zdoom.org/wiki/Sin) and [`cos`](http://zdoom.org/wiki/Cos) are already in ZDoom.

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

### `fixed, fixed RotateVector(fixed x, fixed y, fixed angle)`
Rotates the vector by the `angle`. Returns the coordinates of the rotated vector.

Examples:

	RotateVector(x, y, angle);
	int newX = r1;
	int newY = r2;
	
### `fixed, fixed RotatePoint(fixed x, fixed y, fixed originX, fixed originY, fixed angle)`
Rotates the point around the the given origin by the `angle`.
Returns the coordinates of the rotated point.

Examples:

	RotatePoint(x, y, 1.0, 2.0, angle);
	int newX = r1;
	int newY = r2;
	
### `angle, angle VectorToAngles(fixed x, fixed y, fixed z)`
Returns a pair of angles (yaw and pitch) that specify the direction equivalent
to that of the given 3D vector.

Examples:
	// Make the player look along the vector
	VectorToAngles(1.0, 2.0, 3.0);
	int angle = r1;
	int pitch = r2;
	SetActorAngle(angle);
	SetActorPitch(pitch);

Note: the `ActorLookAt` function from `acsutils` does exactly this.


Rounding
--------

### `int round(fixed x)`
Rounds the number and returns it **as an integer**.

Examples:

	int a = round(123.456); // a = 123
	int a = round(122.678); // a = 123

### `fixed ClearFraction(fixed x)`
Zeroes the fractional part of `x` and returns the result.

This is useful for HudMessages.

Examples:

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

Examples:

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
	
### `int ipow(int x, int y)`
### `fixed fpow(fixed x, int y)`
Returns `x` raised to the power `y`. `y` must be an integer.

`ipow` is for integer `x`, while `fpow` is for fixeds.
