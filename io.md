# Input and Output {#io}

Another common type of input/output (besides using the `input()` function) is dealing with files. The ability to create, read and write files is essential to many programs and we will explore this aspect in this chapter.

You can open and use files for reading or writing by creating an object of the `file` class and using its `read`, `readline` or `write` methods appropriately to read from or write to the file. The ability to read or write to the file depends on the mode you have specified for the file opening. Then finally, when you are finished with the file, you call the `close` method to tell Python that we are done using the file.

Example:

``` python
poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

# Open for 'w'riting
f = open('poem.txt', 'w')
# Write text to file
f.write(poem)
# Close the file
f.close()

# If no mode is specified,
# 'r'ead mode is assumed by default
f = open('poem.txt')
while True:
    line = f.readline()
    # Zero length indicates EOF
    if len(line) == 0:
        break
    # The `line` already has a newline
    # at the end of each line
    # since it is reading from a file.
    print(line, end='')
# close the file
f.close()
```

Output:

```{=html}
<pre><code>
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
</code></pre>
```
**How It Works**

Note that we can create a new file object simply by using the `open` method. We open (or create it if it doesn't already exist) this file by using the built-in `open` function and specifying the name of the file and the mode in which we want to open the file. The mode can be a read mode (`'r'`), write mode (`'w'`) or append mode (`'a'`). We can also specify whether we are reading, writing, or appending in text mode (`'t'`) or binary mode (`'b'`). There are actually many more modes available and `help(open)` will give you more details about them. By default, `open()` considers the file to be a 't'ext file and opens it in 'r'ead mode.

In our example, we first open/create the file in write text mode and use the `write` method of the file object to write our string variable `poem` to the file and then we finally `close` the file.

Next, we open the same file again for reading. We don't need to specify a mode because 'read text file' is the default mode. We read in each line of the file using the `readline` method in a loop. This method returns a complete line including the newline character at the end of the line. When an *empty* string is returned, it means that we have reached the end of the file and we 'break' out of the loop.

In the end, we finally `close` the file.

We can see from our `readline` output that this program has indeed written to and read from our new `poem.txt` file.