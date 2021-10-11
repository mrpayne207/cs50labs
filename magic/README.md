# Magic Numbers

In this lab you will learn:

- What we mean by magic numbers
- Why magic numbers are considered poor design

## What are Magic Numbers?

In the variable lab, we replaced a hard-coded number representing age with a variable. This was a far better design than having to change the program each time we run it to hard-code another value.

```c
// My age next year
printf("Next year I'll be %i years old.\n", 17 + 1);

// My age in 10 years
printf("In 10 years, I'll be %i!\n", 17 + 10);

// My age in 50 years!
printf("In 50 years, I'll be %i! Wow!\n", 17 + 50);
```

However, there are still other numbers directly written into the program, even after replacing 17 with the variable `age`. We still have a 1, 10 and 50. If we didn't have comments, would we know what these numbers represent? While this is a simple program and it may be easy to understand what each calculation is doing, in more complex programs the meaning of hard-coded numbers may not be as obvious.

Numbers that are directly written into our code in this way are sometimes referred to as **magic numbers**.

{% next %}

## Using Constants Instead!

When we have a need to use a number in a program whose value is never going to change, it's considered good design to use a constant.

Let's take an example. What if we wrote a program that uses the number 3.14. Some people might recognize this as Pi, but others may not be sure what this number represents.

To improve the readability of our code, we could define Pi as a constant.

A program with Pi defined as a constant could look like this:

```c
#include <cs50.h>
#include <stdio.h>

#define PI 3.14

int main(void)
{
    float radius = get_float("Radius in inches: ");
    float area = PI * radius * radius;
    printf("Your area is %.1f square inches.\n", area);
}
```

Notice the syntax for creating the constant Pi, is the keyword `#define` then the name of the constant, `PI`, followed by the replacement value, 3.14. We write `#define` statements before the `main` function. The name of the constant is, by convention, all caps.

The general syntax to create constants is:

```
#define NAME <replacement value>
```

By defining these values once, at the top of our program, it becomes easier to change these universal values when necessary. Say for instance, we need a program above to calculate more accurately with `PI`, we can easily change 3.14 to 3.14159265. If we had multiple occurrences of `PI` in our program, each of these would reflect the more accurate value.

{% next %}

## Your Turn

### Part 1: Replace magic numbers with constants
Modify the program on the right (the same program as in the variables lab) and change each of the **magic numbers** to **constants**. The first of these is already done for you.


Be sure to compile your program by typing:

```
make magic
```

and then test it several times by executing:

```
./magic
```

Once complete, let's move on!

{% next %}

### Part 2: Add another constant, C (the speed of light)

Modify this program to compute `e` in the famous `e=mc^2`. 

1. Ask the user to input a value for mass, `m`. 
2. Create a constant `c` for the speed of light (you will need to look up the value). You may need to also look up the correct data type!
3. Computer `e` using `m` and `c`

Be sure to compile your program by typing:

```
make magic
```

and then test it several times by executing:

```
./magic
```

One more problem to go!

{% next %}

### Part 3: Redo Cash

1. Go back and find the cod eyou submitted for the cash problem. The fastest way is to find it on the [submit50 page](https://submit.cs50.io)
2. Copy that code into a new file in this lab called cash.c.
3. Create constants for all the times you ran an operation using one of the money values. In other words, create a constant for quarter, dime, nickel and penny. 
4. Then replace the appropriate areas in your code with these constants.

Finally when all seems good, check your style with:

```
style50 magic.c
```

### Part 4: Submitting your code and Additional Information

Once you completed parts 1-3, you can submit your code using the link further down. After submitting your work, please read the folling PDF on good design principles.

`submit50 marinacademycs/cs50labs/2020/magic`

[For more info, download the CS50 Principles of Good Design Reference Sheet](https://cs50.harvard.edu/ap/2020/assets/pdfs/principles_of_good_design.pdf)
