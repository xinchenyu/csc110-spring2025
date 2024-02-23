# More on Functions

As previously discussed, functions are reusable pieces of programs. They allow you to give a name to a block of statements, allowing you to run that block using the specified name anywhere in your program and any number of times. This is known as *calling* the function.

I'd like to emphasize that the function concept is probably *the* most important building block of any non-trivial software (in any programming language), so we will keep exploring various aspects of functions in this chapter.

If you need a refresher on the basics of functions, go back to the [first functions reading](functions-a.html).

## Function comments

Like we discussed before, comments are very important for documenting your code. Each function should have its function specified in your function comment.

Example:

``` python
def circle_area(radius):
  '''
  This function calculates the area of a circle,
  given a radius.
  Parameters: 
  * radius: integer or float
  It returns a float value representing the area,
  of the circle with the provided radius.
  '''
  # compute the area of a circle
  area = 3.1415 * radius**2
  return area


result = circle_area(radius=4)
print("The area of a circle of radius 4 is", result)
```

Output:

```{=html}
<pre><code>
The area of a circle of radius 4 is 50.264
</code></pre>
```
When you create a string literal right after a function definition, as seen in the example above, that is also called a *docstring*. Docstrings are attributes that can be retrieved using the `__doc__` method as shown in the example below.

Example:

``` python
def circle_area(radius):
  '''
  This function calculates the area of a circle,
  given a radius.
  Parameters: 
  * radius: integer or float
  It returns a float value representing the area,
  of the circle with the provided radius.
  '''
  # compute the area of a circle
  area = 3.1415 * radius**2
  return area


print(circle_area.__doc__)
```

Output:

```{=html}
<pre><code>
  This function calculates the area of a circle,
  given a radius.
  Parameters: 
  * radius: integer or float
  It returns a float value representing the area,
  of the circle with the provided radius.
</code></pre>
```
You can also get docstrings from built-in functions:

Example:

``` python
print(print.__doc__)
```

Output:

```{=html}
<pre><code>
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file:  a file-like object (stream); defaults to the current sys.stdout.
sep:   string inserted between values, default a space.
end:   string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.
</code></pre>
```
## Keyword Arguments

If you have some functions with many parameters and you want to specify only some of them, then you can give values for such parameters by naming them - this is called *keyword arguments* - we use the name (keyword) instead of the position (which we have been using all along) to specify the arguments to the function.

There are two advantages - one, using the function is easier since we do not need to worry about the order of the arguments. Two, we can give values to only those parameters to which we want to, provided that the other parameters have default argument values.

``` python
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)
```

Output:

```{=html}
<pre><code>
a is 3 and b is 7 and c is 10
a is 25 and b is 5 and c is 24
a is 100 and b is 5 and c is 50
</code></pre>
```
**How It Works**

The function named `func` has one parameter without a default argument value, followed by two parameters with default argument values.

In the first usage, `func(3, 7)`, the parameter `a` gets the value `3`, the parameter `b` gets the value `7` and `c` gets the default value of `10`.

In the second usage `func(25, c=24)`, the variable `a` gets the value of 25 due to the position of the argument. Then, the parameter `c` gets the value of `24` due to naming i.e. keyword arguments. The variable `b` gets the default value of `5`.

In the third usage `func(c=50, a=100)`, we use keyword arguments for all specified values. Notice that we are specifying the value for parameter `c` before that for `a` even though `a` is defined before `c` in the function definition.

## Summary

We have seen so many aspects of functions but note that we still haven't covered all aspects of them. However, we have already covered most of what you'll use regarding Python functions on an everyday basis.
