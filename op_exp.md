# More Operators and Expressions {#op-exp}

Here is a quick overview of more operators:

-   `<` (less than)
    -   Returns whether x is less than y. All comparison operators return `True` or `False`. Note the capitalization of these names.
    -   `5 < 3` gives `False` and `3 < 5` gives `True`.
    -   Comparisons can be chained arbitrarily: `3 < 5 < 7` gives `True`.
-   `>` (greater than)
    -   Returns whether x is greater than y
    -   `5 > 3` returns `True`. If both operands are numbers, they are first converted to a common type. Otherwise, it always returns `False`.
-   `<=` (less than or equal to)
    -   Returns whether x is less than or equal to y
    -   `x = 3; y = 6; x <= y` returns `True`
-   `>=` (greater than or equal to)
    -   Returns whether x is greater than or equal to y
    -   `x = 4; y = 3; x >= 3` returns `True`
-   `==` (equal to)
    -   Compares if the objects are equal
    -   `x = 2; y = 2; x == y` returns `True`
    -   `x = 'str'; y = 'stR'; x == y` returns `False`
    -   `x = 'str'; y = 'str'; x == y` returns `True`
-   `!=` (not equal to)
    -   Compares if the objects are not equal
    -   `x = 2; y = 3; x != y` returns `True`
-   `not` (boolean NOT)
    -   If x is `True`, it returns `False`. If x is `False`, it returns `True`.
    -   `x = True; not x` returns `False`.
-   `and` (boolean AND)
    -   `x and y` returns `False` if x is `False`, else it returns evaluation of y
    -   `x = False; y = True; x and y` returns `False` since x is False. In this case, Python will not evaluate y since it knows that the left hand side of the 'and' expression is `False` which implies that the whole expression will be `False` irrespective of the other values. This is called short-circuit evaluation.
-   `or` (boolean OR)
    -   If x is `True`, it returns True, else it returns evaluation of y
    -   `x = True; y = False; x or y` returns `True`. Short-circuit evaluation applies here as well.

## Evaluation Order

Here's the updated table with the evaluation order, from the highest precedence to the lowest precedence. This means that in a given expression, Python will first evaluate the operators and expressions first in the table before the ones listed last in the table. It is far better to use parentheses to group operators and operands appropriately in order to explicitly specify the precedence. This makes the program more readable.

-   `(expressions...)`
-   `**` : Exponentiation
-   `*, /, //, %` : Multiplication, Division, Floor Division and Remainder
-   `+, -` : Addition and subtraction
-   `<, <=, >, >=, !=, ==` : Comparisons, including membership tests and identity tests
-   `not x` : Boolean NOT
-   `and` : Boolean AND
-   `or` : Boolean OR

The operators which we have not already come across will be explained in later chapters.

Operators with the *same precedence* are listed in the same row in the above table. For example, `+` and `-` have the same precedence.

## Expressions

Example:

``` python
def is_larger(x, y):
  '''
  Given two values, it returns a bool indicating whether
  x is larger than y.
  Parameters: x and y can be any type
  It returns a bool
  '''
  return x > y

a = 10
b = 15
result = is_larger(a, b)
print("Is", a, "larger than", str(b) + "?", result)
```

Output:

```{=html}
<pre><code>
Is 10 larger than 15? False
</code></pre>
```
**How It Works**

Two integers are first stored as global variables as `a` and `b`. The function `is_larger()` is called with `a` and `b` as arguments. The function returns `False` because `10` is not larger than `15`. The returned value, `False`, is stored in a global variable called `result`. We then print it using the `print` function.

Also, notice how Python *pretty-prints* the output, with spaces between `Is` and `10` and `larger than`. We don't want a space after `15` and `?`, so `+` concatenation is used instead -- then the integer stored in `b` needs to be converted to a `string` type, which is done with the `str()` function.

## Summary

We have seen how to use operators, operands and expressions - these are the basic building blocks of any program. Next, we will see how to make use of these in our programs using statements.
