# Exceptions

Exceptions occur when *exceptional* situations occur in your program. For example, what if you are going to read a file and the file does not exist? Or what if you accidentally deleted it when the program was running? Such situations are handled using **exceptions**.

Similarly, what if your program had some invalid statements? This is handled by Python which **raises** its hands and tells you there is an **error**.

## Errors

Consider a simple `print` function call. What if we misspelt `print` as `Print`? Note the capitalization. In this case, Python *raises* a syntax error.

``` python
>>> Print("Hello World")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Print' is not defined
>>> print("Hello World")
Hello World
```

Observe that a `NameError` is raised and also the location where the error was detected is printed. This is what an **error handler** for this error does.

## Exceptions

We will **try** to read input from the user. Enter the first line below and hit the `Enter` key. When your computer prompts you for input, instead press `[ctrl-d]` on a Mac or `[ctrl-z]` with Windows and see what happens. (If you're using Windows and neither option works, you can try `[ctrl-c]` in the Command Prompt to generate a KeyboardInterrupt error instead).

``` python
>>> s = input('Enter something --> ')
Enter something --> Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
EOFError
```

Python raises an error called `EOFError` which basically means it found an *end of file* symbol (which is represented by `ctrl-d`) when it did not expect to see it.

## Handling Exceptions

We can handle exceptions using the `try..except` statement. We basically put our usual statements within the try-block and put all our error handlers in the except-block.

Example (save as `exceptions_handle.py`):

Example:

``` python
try:
    text = input('Enter something --> ')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered', text)
```

Output:

```{=html}
<pre><code>
# Press ctrl + d
$ python exceptions_handle.py
Enter something --> Why did you do an EOF on me?

# Press ctrl + c
$ python exceptions_handle.py
Enter something --> ^CYou cancelled the operation.

$ python exceptions_handle.py
Enter something --> No exceptions
You entered No exceptions
</code></pre>
```

**How It Works**

We put all the statements that might raise exceptions/errors inside the `try` block and then put handlers for the appropriate errors/exceptions in the `except` clause/block. The `except` clause can handle a single specified error or exception, or a parenthesized list of errors/exceptions. If no names of errors or exceptions are supplied, it will handle *all* errors and exceptions.

Note that there has to be at least one `except` clause associated with every `try` clause. Otherwise, what's the point of having a try block?

If any error or exception is not handled, then the default Python handler is called which just stops the execution of the program and prints an error message. We have already seen this in action above.

You can also have an `else` clause associated with a `try..except` block. The `else` clause is executed if no exception occurs.

In the next example, we will also see how to get the exception object so that we can retrieve additional information.


## The with statement {#with}

Acquiring a resource in the `try` block and subsequently releasing the resource in the `finally` block is a common pattern. Hence, there is also a `with` statement that enables this to be done in a clean manner:

``` python
with open("poem.txt") as f:
    for line in f:
        print(line, end='')
```

**How It Works**

We are using here the `open` function with the `with` statement - we leave the closing of the file to be done automatically by `with open`.

What happens behind the scenes is that there is a protocol used by the `with` statement. It fetches the object returned by the `open` statement, let's call it "thefile" in this case.
