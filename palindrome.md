# Input from user {#io}

There will be situations where your program has to interact with the user. For example, you would want to take input from the user and then print some results back. We can achieve this using the `input()` function and `print` function respectively.

Example:

``` python
def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
```

Output:

```{=html}
<pre><code>
Enter text: sir
No, it is not a palindrome

$ python3 io_input.py
Enter text: madam
Yes, it is a palindrome

$ python3 io_input.py
Enter text: racecar
Yes, it is a palindrome
</code></pre>
```
**How It Works**

We use the slicing feature to reverse the text. We've already seen how we can make slices from sequences using the `seq[a:b]` code starting from position `a` to position `b`. We can also provide a third argument that determines the *step* by which the slicing is done. The default step is `1` because of which it returns a continuous part of the text. Giving a negative step, i.e., `-1` will return the text in reverse.

The `input()` function takes a string as argument and displays it to the user. Then it waits for the user to type something and press the return key. Once the user has entered and pressed the return key, the `input()` function will then return that text the user has entered.

We take that text and reverse it. If the original text and reversed text are equal, then the text is a [palindrome](http://en.wiktionary.org/wiki/palindrome).

### Homework exercise

Checking whether a text is a palindrome should also ignore punctuation, spaces and case. For example, "Rise to vote, sir." is also a palindrome but our current program doesn't say it is. Can you improve the above program to recognize this palindrome?

If you need a hint, the idea is that...[^palindrome-1]

[^palindrome-1]: Use a tuple (you can find a list of *all* [punctuation marks here](http://grammar.ccc.commnet.edu/grammar/marks/marks.htm)) to hold all the forbidden characters, then use the membership test to determine whether a character should be removed or not, i.e. forbidden = (`!`, `?`, `.`, ...).
