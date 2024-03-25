# Intro to Functions

Functions are reusable pieces of programs. They allow you to give a name to a block of statements, allowing you to run that block using the specified name anywhere in your program and any number of times. This is known as *calling* the function. We have already used many built-in functions such as `len` and `range`.

The function concept is probably *the* most important building block of any non-trivial software (in any programming language), so we will explore various aspects of functions in this chapter.

Functions are defined using the `def` keyword. After this keyword comes an *identifier* name for the function, followed by a pair of parentheses which may enclose some names of variables, and by the final colon that ends the line. Next follows the block of statements that are part of this function. An example will show that this is actually very simple:

Example:

``` python
def say_hello():
    # block belonging to the function
    print('hello world')
# End of function

say_hello()  # call the function
say_hello()  # call the function again
```

Output:

```{=html}
<pre><code>
hello world
hello world
</code></pre>
```
**How It Works**

We define a function called `say_hello` using the syntax as explained above. This function takes no parameters and hence there are no variables declared in the parentheses. Parameters to functions are just input to the function so that we can pass in different values to it and get back corresponding results.

Notice that we can call the same function twice which means we do not have to write the same code again.

## Function Parameters

A function can take parameters, which are values you supply to the function so that the function can *do* something utilizing those values. These parameters are just like variables except that the values of these variables are defined when we call the function and are already assigned values when the function runs.

Parameters are specified within the pair of parentheses in the function definition, separated by commas. When we call the function, we supply the values in the same way. Note the terminology used - the names given in the function definition are called *parameters* whereas the values you supply in the function call are called *arguments*.

Example:

``` python
def print_add_10(value):
    x = value + 10
    print(x)
# End of function

print_add_10(2)  # call the function with integer as a parameter
print_add_10(10)  # call the function again with different parameter
```

Output:

```{=html}
<pre><code>
12
20
</code></pre>
```
**How It Works**

Here, we define a function called `print_add_10` that uses one parameters called `value`. We create a new variable `x` that hold the evaluation of the `value` plus `10` and we printn the value in `x`.

The first time we call the function `print_add_10`, we directly supply `2` as an argument. In the second case, we call the function with the value `10` as an argument.

## Local Variables

When you declare variables inside a function definition, they are not related in any way to other variables with the same names used outside the function - i.e. variable names are *local* to the function. This is called the *scope* of the variable. All variables have the scope of the block they are declared in starting from the point of definition of the name.

Example:

``` python
x = 50

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)


func(x)
print('x is still', x)
```

Output:

```{=html}
<pre><code>
x is 50
Changed local x to 2
x is still 50
</code></pre>
```
**How It Works**

The first time that we print the *value* of the name *x* with the first line in the function's body, Python uses the value of the parameter declared in the main block, above the function definition.

Next, we assign the value `2` to `x`. The name `x` is local to our function. So, when we change the value of `x` in the function, the `x` defined in the main block remains unaffected.

With the last `print` statement, we display the value of `x` as defined in the main block, thereby confirming that it is actually unaffected by the local assignment within the previously called function.

## Default Argument Values {#default-arguments}

For some functions, you may want to make some parameters *optional* and use default values in case the user does not want to provide values for them. This is done with the help of default argument values. You can specify default argument values for parameters by appending to the parameter name in the function definition the assignment operator (`=`) followed by the default value.

Note that the default argument value should be a constant. More precisely, the default argument value should be immutable - this is explained in detail in later chapters. For now, just remember this.

Example:

``` python
def say(message, times=1):
    print(message * times)

say('Hello')
say('World', 5)
```

Output:

```{=html}
<pre><code>
Hello
WorldWorldWorldWorldWorld
</code></pre>
```
**How It Works**

The function named `say` is used to print a string as many times as specified. If we don't supply a value, then by default, the string is printed just once. We achieve this by specifying a default argument value of `1` to the parameter `times`.

In the first usage of `say`, we supply only the string and it prints the string once. In the second usage of `say`, we supply both the string and an argument `5` stating that we want to *say* the string message 5 times.

> *CAUTION*
>
> Only those parameters which are at the end of the parameter list can be given default argument values i.e. you cannot have a parameter with a default argument value preceding a parameter without a default argument value in the function's parameter list.
>
> This is because the values are assigned to the parameters by position. For example,`def func(a, b=5)` is valid, but `def func(a=5, b)` is *not valid*.

## The `return` statement {#return-statement}

The `return` statement is used to *return* from a function i.e. break out of the function. We can optionally *return a value* from the function as well.

Example:

``` python
def add_10(value):
    x = value + 10
    return x
# End of function

result = add_10(5)
print(result)
```

Output:

```{=html}
<pre><code>
15
</code></pre>
```
**How It Works**

The `add_10` function *returns* the parameter value added 10.

Note that a `return` statement without a value is equivalent to `return None`. `None` is a special type in Python that represents nothingness. For example, it is used to indicate that a variable has no value if it has a value of `None`.

Every function implicitly contains a `return None` statement at the end unless you have written your own `return` statement. You can see this by running `print(some_function())` where the function `some_function` does not use the `return` statement such as:

``` python
def some_function():
    pass
```

The `pass` statement is used in Python to indicate an empty block of statements.

## Summary

We have seen so many aspects of functions but note that we still haven't covered all aspects of them.
