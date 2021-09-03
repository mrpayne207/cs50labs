# Hello

## Listing Files

Hello, world! At right, in the *text editor*, is the very first program we wrote in C, in a file called `hello.c`.

Click the folder icon, and you'll see that `hello.c` is the only file that's present at the moment. Click the folder icon again to hide all that.

Next, in the *terminal window* at right, immediately to the right of the dollar sign (`$`), otherwise known as a *prompt*, type precisely the below (in lowercase), then hit Enter:

```
ls
```

You should see just `hello.c`? That's because you've just listed the files in that same folder, this time using a command-line interface (CLI), using just your keyboard, rather than the graphical user interface (GUI) represented by that folder icon. In particular, you *executed* (i.e., ran) a command called `ls`, which is shorthand for "list" (it's such a frequently used command that its authors called it just `ls` to save keystrokes). Make sense?

Here on out, to execute (i.e., run) a command means to type it into a terminal window and then hit Enter. Commands are "case-sensitive," so be sure not to type in uppercase when you mean lowercase or vice versa.

{% next %}

## Compiling Programs

Now, before we can execute the program at right, recall that we must *compile* it with a *compiler* (e.g., `clang` or `make`), translating it from *source code* into *machine code* (i.e., zeroes and ones). Execute the command below to do just that:

```
make helloworld.c
```

And then execute this one again:

```
ls
```

This time, you should see not only `hello.c` but `a.out` listed as well (you can see the same graphically if you click that folder icon again)? That's because `make` has translated the source code in `hello.c` into machine code in `hello`.

Now run the program by executing the below.

```
./helloworld
```

Hello, world, indeed!

{% next %}


## Quick Practice

Now let's make a very small change to this program. Add another line that prints your name. Something like `printf("My name is Keanu Reeves");` Because you changed the program, you'll need to recompile it using `make helloworld`. Got it? Great!


## How to Submit

Now let's practice submitting your work. Labs and problem sets will most often be submitted this way. Execute the code below, logging in with your GitHub username and Github `token` when prompted. 

```
submit50 marinacademycs/labs/2021/x/helloworld
```

You should have received a message that your code was submitted! Follow the link to explore what submitted work looks like.