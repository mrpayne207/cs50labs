# Bugs and Debugging

In this lab you will learn about:

- The differences between syntax errors and logic errors
- Various ways to debug your code

## What are Syntax vs. Logic Errors?

Most of us encounter **syntax errors** at some point when creating a new program. Syntax errors prevent a program from successfully compiling and could include misspelled keywords, missing or misplaced curly braces, semicolon, parentheses, etc.

If the compiler error message is hard to understand, we can prepend `help50` to `make hello` to get a bit more guidance on how to correct our error:

```
help50 make hello
```
help50 still has it's shortcomings because it is dependant on the information that the comiler gives it. Remember a single missing comma likely throws errors for most of the code that comes after that. That could be fine though, it's just a missing comma that came before that.

On the other hand, when we encounter a **logical error**, our program usually compiles and runs, but gives us an incorrect result.

<img src="https://raw.githubusercontent.com/cs50nestm/cs50labs/2019/debugging/error.gif" width="400px">

{% next %}

## Debugging Methods

### Printf

Since our program executes so fast, it can be hard to know exactly what is wrong with our program just by running it. One technique that can help is to add extra `printf()` statements to examine the value of our variables at different points in our program. We can remove these once our program works correctly:

```c
printf("The value of a: %i\n", a);
```

Sometimes we're not sure if a block of code is even running. To know for sure if an `if` statement or `while` loop for example executes, we can add a temporary line of code inside our loop:

```c
printf("Executing while loop\n");
```

### Commenting out code

Another technique is to comment out sections of code that we know work correctly, to be able to focus only on any sections of code we need to debug. Of course we would need to make sure not to comment out code that declares or initializes variables that we will need for our testing.

To comment out blocks of code quickly, highlight multiple lines of code and press:

* `ctrl + /` (On Windows and Linux)
* `command ⌘ + /` (On Mac)

This will toggle comments on and off.


### Test using inputs that you think should work, and ***inputs you expect will fail.***

It is easy to expect the users of our programs to always enter proper inputs and behave correctly when using our programs. This is not always (or perhaps usually) the case. Test your programs using inputs to help confirm your program works like you wanted it to. Also, **test using incorrect values to make sure it fails when it is supposed to!** This is really important. Just like `get_int` doesn't accept strings, you programs should handle misbehaving users who enter incorrect information or otherwise try to get your programs to break.


### Rubber Duck Debugging

Yes, this is actually a thing! The idea is to explain your code, line-by-line, to a rubber duck, or another inanimate object. In describing what our code is supposed to do, and observing what it actually does, our error can become apparent. Forcing ourselves to explain code line-by-line can provide a deeper understanding as well.


### Compile and test code frequently

In general, it's a good idea to compile and run our code frequently to get immediate feedback. This way when we do have a bug, we can be fairly certain it is contained in the new segment of code we just finished writing.


{% next %}

## Your Turn

The program on the right is supposed to convert binary numbers to decimal (base ten) numbers. It compiles, so the syntax is probably correct, but the output is wrong!

{% spoiler "How does the program work?" %}

1. The `main`function starts by prompting for a binary number and storing this in the variable `binary`
2. Main then calls `check_binary(binary)` which returns `true` or `false` if the input is valid or invalid
    1. If the input is invalid, the program ends with `return 1`
3. The function `bin_to_dec(binary)` which does the actual conversion.
4. `bin_to_dec(binary)` works by isolating each digit in `binary` and multiplying the 0 or 1 by the appropriate value.
5. The result is saved in `decimal`.
6. The result is output via `printf`

{% endspoiler %}

Try using some of the debugging techniques above to see if you can find the logical error and correct it.

You can declare additional variables if you want to and use functions in any of the libraries included on top of the program.

{% spoiler "Debugging hints" %}
Try adding a `printf` inside of the `bin_to_dec(binary)` function to see if the calculation is working correctly.
{% endspoiler %}

### Correctness

Check your work with...

```
check50 marinacademycs/cs50labs/2020/debugging
```

### Style

Since we want to get into good habits early, check that your indentation, and spacing is correct, by typing:

```
style50 buggy.c
```

It's good to get into good habits now, so when you start writing longer and more complex programs, you will know how to style your code properly. Code that is properly styled, is much easier to debug!

## How to Submit

To submit your code, execute

```
submit50 marinacademycs/cs50labs/2020/debugging
```

Your submission should be graded for corretness and style withing a few minutes on [the me50 course page](https://submit.cs50.io/)


## More Info

[For more info, download the CS50 Bugs and Debugging Reference Sheet](https://cs50.harvard.edu/ap/2020/assets/pdfs/bugs_and_debugging.pdf)
