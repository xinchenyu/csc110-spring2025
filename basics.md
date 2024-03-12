# Constants, variables, and comments

Just printing `hello world` is not enough, is it? You want to do more than that - you want to take some input, manipulate it and get something out of it. We can achieve this in Python using constants and variables, and we'll learn some other concepts as well in this chapter.

## Comments

*Comments* are any text to the right of the `#` symbol and is mainly useful as notes for the reader of the program.

For example:

``` python
print('hello world') # Note that print is a function
```

or:

``` python
# Note that print is a function
print('hello world')
```

Use as many useful comments as you can in your program to:

-   explain assumptions
-   explain important decisions
-   explain important details
-   explain problems you're trying to solve
-   explain problems you're trying to overcome in your program, etc.

[*Code tells you how, comments should tell you why*](https://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/#:~:text=Code%20can%20only%20tell%20you,tell%20you%20why%20it%20works.).

This is useful for readers of your program so that they can easily understand what the program is doing. Remember, that person can be yourself after six months!

## Literal Constants

An example of a literal constant is a number like `5`, `1.23`, or a string like `'This is a string'` or `"It's a string!"`.

It is called a literal because it is *literal* - you use its value literally. The number `2` always represents itself and nothing else - it is a *constant* because its value cannot be changed. Hence, all these are referred to as literal constants.

## Numbers

Numbers are mainly of two types - integers and floats.

An example of an integer is `2` which is just a whole number.

Examples of floating point numbers (or *floats* for short) are `3.23` and `52.3E-4`. The `E` notation indicates powers of 10. In this case, `52.3E-4` means `52.3 * 10^-4^`.

> **Note for Experienced Programmers**
>
> There is no separate `long` type. The `int` type can be an integer of any size.

## Strings

A string is a *sequence* of *characters*. Strings are basically just a bunch of words.

You will be using strings in almost every Python program that you write, so pay attention to the following part.

### Single Quote

You can specify strings using single quotes such as `'Quote me on this'`.

All white space i.e. spaces and tabs, within the quotes, are preserved as-is.

### Double Quotes

Strings in double quotes work exactly the same way as strings in single quotes. An example is `"What's your name?"`.

### Triple Quotes {#triple-quotes}

You can specify multi-line strings using triple quotes - (`"""` or `'''`). You can use single quotes and double quotes freely within the triple quotes. An example is:

``` python
'''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''
```

### Strings Are Immutable

This means that once you have created a string, you cannot change it. Although this might seem like a bad thing, it really isn't. We will see why this is not a limitation in the various programs that we see later on.

> **Note for C/C++ Programmers**
>
> There is no separate `char` data type in Python. There is no real need for it and I am sure you won't miss it.

<!-- -->

> **Note for Perl/PHP Programmers**
>
> Remember that single-quoted strings and double-quoted strings are the same - they do not differ in any way.

### The format method (this is not required for this course, you can skip this part)

Sometimes we may want to construct strings from other information. This is where the `format()` method is useful.

Save the following lines as a file `str_format.py`:

``` python
age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))
```

Output:

```         
$ python str_format.py
Swaroop was 20 years old when he wrote this book
Why is Swaroop playing with that python?
```

**How It Works**

A string can use certain specifications and subsequently, the `format` method can be called to substitute those specifications with corresponding arguments to the `format` method.

Observe the first usage where we use `{0}` and this corresponds to the variable `name` which is the first argument to the format method. Similarly, the second specification is `{1}` corresponding to `age` which is the second argument to the format method. Note that Python starts counting from 0 which means that first position is at index 0, second position is at index 1, and so on.

Notice that we could have achieved the same using string concatenation:

``` python
name + ' is ' + str(age) + ' years old'
```

but that is much uglier and more error-prone. Second, the conversion to string would be done automatically by the `format` method instead of the explicit conversion to strings needed in this case. Third, when using the `format` method, we can change the message without having to deal with the variables used and vice-versa.

Also note that the numbers are optional, so you could have also written as:

``` python
age = 20
name = 'Swaroop'

print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))
```

which will give the same exact output as the previous program.

We can also name the parameters:

``` python
age = 20
name = 'Swaroop'

print('{name} was {age} years old when he wrote this book'.format(name=name, age=age))
print('Why is {name} playing with that python?'.format(name=name))
```

which will give the same exact output as the previous program.

Python 3.6 introduced a shorter way to do named parameters, called "f-strings":

``` python
age = 20
name = 'Swaroop'

print(f'{name} was {age} years old when he wrote this book')  # notice the 'f' before the string
print(f'Why is {name} playing with that python?')  # notice the 'f' before the string
```

which will give the same exact output as the previous program.

What Python does in the `format` method is that it substitutes each argument value into the place of the specification. There can be more detailed specifications such as:

``` python
# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
```

Output:

```         
0.333
___hello___
Swaroop wrote A Byte of Python
```

Since we are discussing formatting, note that `print` always ends with an invisible "new line" character (`\n`) so that repeated calls to `print` will all print on a separate line each. To prevent this newline character from being printed, you can specify that it should `end` with a blank:

``` python
print('a', end='')
print('b', end='')
```

Output is:

```         
ab
```

Or you can `end` with a space:

``` python
print('a', end=' ')
print('b', end=' ')
print('c')
```

Output is:

```         
a b c
```

### Printing Extra Line Breaks

Since the default `end` parameter is set to `\n` it always prints one line break by default.
We can change `end` to `\n\n` to print two line breaks -- that creates an empty line after whatever the `print` statement output.

``` python
print("This is a line", end = "\n\n") 
```

We can also use `print` with no arguments to print just an empty line:

``` python
print() # prints an empty line 
```

### Escape Sequences

Suppose, you want to have a string which contains a single quote (`'`), how will you specify this string? For example, the string is `"What's your name?"`. You cannot specify `'What's your name?'` because Python will be confused as to where the string starts and ends. So, you will have to specify that this single quote does not indicate the end of the string. This can be done with the help of what is called an *escape sequence*. You specify the single quote as `\'` : notice the backslash. Now, you can specify the string as `'What\'s your name?'`.

Another way of specifying this specific string would be `"What's your name?"` i.e. using double quotes. Similarly, you have to use an escape sequence for using a double quote itself in a double quoted string. Also, you have to indicate the backslash itself using the escape sequence `\\`.

What if you wanted to specify a two-line string? One way is to use a triple-quoted string as shown [previously](#triple-quotes) or you can use an escape sequence for the newline character - `\n` to indicate the start of a new line. An example is:

``` python
'This is the first line\nThis is the second line'
```

Another useful escape sequence to know is the tab: `\t`. There are many more escape sequences but I have mentioned only the most useful ones here.

One thing to note is that in a string, a single backslash at the end of the line indicates that the string is continued in the next line, but no newline is added. For example:

``` python
"This is the first sentence. \
This is the second sentence."
```

is equivalent to

``` python
"This is the first sentence. This is the second sentence."
```

### Raw String

If you need to specify some strings where no special processing such as escape sequences are handled, then what you need is to specify a *raw* string by prefixing `r` or `R` to the string. An example is:

``` python
r"Newlines are indicated by \n"
```

> **Note for Regular Expression Users**
>
> Always use raw strings when dealing with regular expressions. Otherwise, a lot of backwhacking may be required. For example, backreferences can be referred to as `'\\1'` or `r'\1'`.

## Variable

Using just literal constants can soon become boring - we need some way of storing any information and manipulate them as well. This is where *variables* come into the picture. Variables are exactly what the name implies - their value can vary, i.e., you can store anything using a variable. Variables are just parts of your computer's memory where you store some information. Unlike literal constants, you need some method of accessing these variables and hence you give them names.

## Identifier Naming

Variables are examples of identifiers. *Identifiers* are names given to identify *something*. There are some rules you have to follow for naming identifiers:

-   The first character of the identifier must be a letter of the alphabet (uppercase ASCII or lowercase ASCII or Unicode character) or an underscore (`_`).
-   The rest of the identifier name can consist of letters (uppercase ASCII or lowercase ASCII or Unicode character), underscores (`_`) or digits (0-9).
-   Identifier names are case-sensitive. For example, `myname` and `myName` are *not* the same. Note the lowercase `n` in the former and the uppercase `N` in the latter.
-   Examples of *valid* identifier names are `i`, `name_2_3`. Examples of *invalid* identifier names are `2things`, `this is spaced out`, `my-name` and `>a1b2_c3`.

## Data Types

Variables can hold values of different types called *data types*. The basic types are numbers and strings, which we have already discussed.

## Object

Remember, Python refers to anything used in a program as an *object*. This is meant in the generic sense. Instead of saying "the *something*"', we say "the *object*".

> **Note for Object Oriented Programming users**:
>
> Python is strongly object-oriented in the sense that everything is an object including numbers, strings and functions.

We will now see how to use variables along with literal constants. Save the following example and run the program.

## Summary

Now that we have gone through many nitty-gritty details, we can move on to more interesting stuff such as functions. Be sure to become comfortable with what you have read in this chapter.
