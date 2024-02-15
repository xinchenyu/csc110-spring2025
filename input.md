# Input from user {#io}

There will be situations where your program has to interact with the user. For example, you would want to take input from the user and then print some results back. We can achieve this using the `input()` function and `print` function respectively.

Example:

``` python
def say_hi(name):
  print("Hello,", name + "!")
  
name = input("What's your name?\n")
say_hi(name)
```

Output:

```{=html}
<pre><code>
What's your name?
Adriana
Hello, Adriana!
</code></pre>
```
**How It Works**

The `input()` function takes a string as argument and saves it to a variable called `name`. Then it calls the function `say_hi()` with the `name` entered by the user as the argument. The function `say_hi()` prints the `name` argument concatenated with a `Hello` message. 

# Changing types

The `input()` function will always return a string. But many times we will want the user to enter other information, such as a number. 

We can use functions like `int()` to transform a type into an `integer` and `float()` to transform a type into a float number.

Example:

``` python
def calculate_future(years, age):
  print("In", years, "you will be", age + years, "years old.")


age = input("What's your age?\n")
age_int = int(age)
calculate_future(10, age_int)
```

Output:

```{=html}
<pre><code>
What's your age?
41
In 10 you will be 51 years old.
</code></pre>
```

**How It Works**

The `input()` function takes a string as argument and saves it to a variable called `age`. Then it calls the function `int()` to convert the age entered by the user from string to `integer` and saves the value to a variable called `age_int`. The function `calculate_future()` is called with arguments `10` and the age entered by the user converted to integer, it then prints the `age` argument concatenated with a message saying how old the person will be in the number of years passed as argument to the function. 
