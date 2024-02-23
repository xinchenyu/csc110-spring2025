# Operators and Expressions {#op-exp}

Most statements (logical lines) that you write will contain *expressions*. A simple example of an expression is `2 + 3`. An expression can be broken down into operators and operands.

*Operators* are functionality that do something and can be represented by symbols such as `+` or by special keywords. Operators require some data to operate on and such data is called *operands*. In this case, `2` and `3` are the operands.

## Operators

We will briefly take a look at the operators and their usage.

Note that you can evaluate the expressions given in the examples using the interpreter interactively. For example, to test the expression `2 + 3`, use the interactive Python interpreter prompt:

``` python
>>> 2 + 3
5
>>> 3 * 5
15
>>>
```

Here is a quick overview of the available operators:

-   `+` (plus)
    -   Adds two objects
    -   `3 + 5` gives `8`. `'a' + 'b'` gives `'ab'`.
-   `-` (minus)
    -   Gives the subtraction of one number from the other; if the first operand is absent it is assumed to be zero.
    -   `-5.2` gives a negative number and `50 - 24` gives `26`.
-   `*` (multiply)
    -   Gives the multiplication of the two numbers or returns the string repeated that many times.
    -   `2 * 3` gives `6`. `'la' * 3` gives `'lalala'`.
-   `**` (power)
    -   Returns x to the power of y
    -   `3 ** 4` gives `81` (i.e. `3 * 3 * 3 * 3`)
-   `/` (divide)
    -   Divide x by y
    -   `13 / 3` gives `4.333333333333333`
-   `//` (divide and floor)
    -   Divide x by y and round the answer *down* to the nearest integer value. Note that if one of the values is a float, you'll get back a float.
    -   `13 // 3` gives `4`
    -   `-13 // 3` gives `-5`
    -   `9//1.81` gives `4.0`
-   `%` (modulo)
    -   Returns the remainder of the division
    -   `13 % 3` gives `1`. `-25.5 % 2.25` gives `1.5`.

## Evaluation Order

If you had an expression such as `2 + 3 * 4`, is the addition done first or the multiplication? Our high school maths tells us that the multiplication should be done first. This means that the multiplication operator has higher precedence than the addition operator.

The following table gives the precedence table for Python, from the highest precedence to the lowest precedence. This means that in a given expression, Python will first evaluate the operators and expressions first in the table before the ones listed last in the table. It is far better to use parentheses to group operators and operands appropriately in order to explicitly specify the precedence. This makes the program more readable.

-   `(expressions...)`
-   `**` : Exponentiation
-   `*, /, //, %` : Multiplication, Division, Floor Division and Remainder
-   `+, -` : Addition and subtraction

Operators with the *same precedence* are listed in the same row in the above table. For example, `+` and `-` have the same precedence.

## Changing the Order Of Evaluation {#changing-order-of-evaluation}

To make the expressions more readable, we can use parentheses. For example, `2 + (3 * 4)` is definitely easier to understand than `2 + 3 * 4` which requires knowledge of the operator precedences. As with everything else, the parentheses should be used reasonably (do not overdo it) and should not be redundant, as in `(2 + (3 * 4))`.

There is an additional advantage to using parentheses - it helps us to change the order of evaluation. For example, if you want addition to be evaluated before multiplication in an expression, then you can write something like `(2 + 3) * 4`.

## Associativity

Operators are usually associated from left to right. This means that operators with the same precedence are evaluated in a left to right manner. For example, `2 + 3 + 4` is evaluated as `(2 + 3) + 4`.

## Expressions

Example:

``` python
length = 5
breadth = 2

area = length * breadth
print('Area is', area)
print('Perimeter is', 2 * (length + breadth))
```

Output:

```         
Area is 10
Perimeter is 14
```

**How It Works**

The length and breadth of the rectangle are stored in variables by the same name. We use these to calculate the area and perimeter of the rectangle with the help of expressions. We store the result of the expression `length * breadth` in the variable `area` and then print it using the `print` function. In the second case, we directly use the value of the expression `2 * (length + breadth)` in the print function.

Also, notice how Python *pretty-prints* the output. Even though we have not specified a space between `'Area is'` and the variable `area`, Python puts it for us so that we get a clean nice output and the program is much more readable this way (since we don't need to worry about spacing in the strings we use for output). This is an example of how Python makes life easy for the programmer.

## Round built-in function

The built-in python function `round` returns an integer if `ndigits` (number of digits) is omitted. Otherwise the return value has the same type as the number provided as argument (if the number is an integer, `round` returns an integer, if the number is a float, `round` returns a float). This function is useful to return a float number rounded to the decimal places provided as the second argument when calling it. The syntax is `round(number, ndigits)`

``` python
round(50.5555, 2)
```

The call above returns `50.56`

Python uses the IEEE 754 standard for rounding, called the banker’s rounding. So python rounds to the nearest even number if the fractional component of the number is halfway between two integers. The idea is that 50% of the numbers are rounded up and 50% down. 


``` python
>>> round(50.5)
50
>>> round(51.5)
52
```

Note that decimal fractions often cannot be represented exactly as a binary floating-point number, so the return value of `round` is not always what you'd expect (not a bug).

``` python
>>> round(4.675, 2)
4.67
>>> round(4.665, 2)
4.67
```

If you are curious, you can read more about [floating point arithmetic](https://docs.python.org/3/tutorial/floatingpoint.html).

## Summary

We have seen how to use operators, operands and expressions - these are the basic building blocks of any program. Next, we will see how to make use of these in our programs using statements.
