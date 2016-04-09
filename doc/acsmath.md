acsmath - math functions
------------------------

### Generic operations on numbers

#### num abs(num x)
Returns the absolute value of `x`.

##### Examples
    abs(2.0) == 2.0;
    abs(-123) == 123;

#### `num min(num a, num b)`
Returns the lesser of `a` and `b`.

##### Examples
    min(3, 5) == 3;
    min(8.0, 7.5) == 7.5;

#### `num max(num a, num b)`
Returns the greater of `a` and `b`.

##### Examples
    max(3, 5) == 5;
    max(8.0, 7.5) == 8.0;


### Trigonometry

Note: `sin` and `cos` are already in ZDoom.

#### `fixed tan(angle x)`
Returns the tangent of `x`.

#### `fixed atan(angle x)`
Returns the arctangent of `x`.