# Linear Search

In this lab you will learn about:

- Linear search
- Computational complexity
- Max Search, a similar algorithm to Linear serach

## What is Linear Search?

There are many important applications of searching algorithms in Computer Science, from looking up a name in an address book to using an internet search engine.

The most basic search algorithm is called **linear search**. This algorithm checks every element in a list, starting at the beginning and incrementing through the list until the desired element is found. In the worst case, this would take *n* steps, where *n* was the number of elements in our list, and in the best case, we would find it in the first step.

If we were looking for the number 50 in an array:

![Linear_Search](https://raw.githubusercontent.com/cs50nestm/cs50labs/2019/linearsearch/linear_search.gif)

{% next %}

The pseudocode might look like this.

```
for each element in array
    if element equals what you're looking for
        return true
return false
```

Note that we only `return false` after the `for` loop has finished, meaning we checked all the values in the array.


## Computational Complexity

When we talk about the complexity of an algorithm, we are talking about the steps an algorithm takes. Since the worst case for **linear search** means having to look at every item in a list of *n* elements, we can notate this as *O(n)*.

We can see that **linear search** is not usually an efficient algorithm, especially for large data sets. In the phone book example, we might have to step through hundreds or thousands of pages to find one name. However, an advantage of linear search is that it does not require sorted data. If we are looking through a short list, and the list is unsorted, it may be more efficient (take fewer steps) to just check each item, than to sort the list first and then search it.

{% next %}

## Your Turn

### Part 1: Linear Search

Practice writing a **linear search** algorithm by completing the function in `linear.c`. The purpose of the program is to determine if a number that is input matches any of the numbers on a particular bingo card.

The function prototype is already defined as:

```c
bool linear_search(int arr[], int n, int size);
```

This tells us that the function has a return type of `bool`, meaning that the function must return `true` or `false`. When the function is called, as it is from the `main()` function, there are three arguments: `arr` the name of the array we are searching through, `n`, the element we are searching for, and `size`, the number of elements in the array.

The function definition is located after the `main()` function closes. Complete this `linear_search()` function to determine if a number that is input is, indeed, on the bingo card.

{% spoiler "Hint" %}

1. Consider using a for loop, to iterate through the array. For instance: `for (int i = 0; i < size; i++)` could work to access each element in the array.
    1. If we find a match  `arr[i] == n` we `return true`
2. When the for loop completes, it means we searched through till the end of the array, and didn't find a match, so `return false`    

{% endspoiler %}

Be sure to test your function by compiling and executing your program. Try a variety of inputs, including some numbers that are in the `bingo_card` array and some numbers that are not.

{% next %}

### Part 2: Max Search

Sometimes we need to find the largest or smallest item in an array of ***unsorted items***. The fact the array is ***unsorted*** is important because if the list is sorted we could infer either the first or last item is the largest. For this example, let's say we don't want to spend the time to sort the list because that would not be worth the effort (take too long to code, isn't necessary in the long term, etc).

How might you do this? Take a minute and think of your pseudocode.

{% spoiler "Hint" %}

How about this:

```
use a variable, max, and set the largest number to the first item in the array.
check each number in the array
    if that number is larger than max
        max equals that number
    else
        continue
```
See what is happeneing? We are changing the value of max as we go through the loop. Give it a try using C below.

{% endspoiler %}

Copy the below code into a file named `maxsearch.c` and complete the `max_search` function to find the largest item in the list.

```c
// complete the max search function

#include <cs50.h>

#define TOTAL 24

// function prototype
int max_search(int arr[], int size);

// Numbers in array
int numbers[] = {7, 14, 400, 9, 6, 26, -22, 24, 201, 28, 40, 3422, 36, 35, 582, 55, 46, -52, 49, 73, 68, -2272, 74, 64};

int main(void)
{  
    printf("The largest number is %d", max_search(numbers, TOTAL));   
}

//This function takes an array and returns the largest integer in the array.
int max_search(int arr[], int size)
{
    
    //TODO

}
````

### Correctness

Check your work with...

```
check50 marinacademycs/cs50labs/2020/linearsearch
```

### Style

Since we want to get into good habits early, check that your indentation, and spacing is correct, by typing:

```
style50 linear.c
style50 maxsearch.c
```

It's good to get into good habits now, so when you start writing longer and more complex programs, you will know how to style your code properly. Code that is properly styled, is much easier to debug!

## How to Submit

To submit your code, execute

```
submit50 marinacademycs/cs50labs/2020/linearsearch
```

Your submission should be graded for corretness and style withing a few minutes on [the me50 course page](https://submit.cs50.io/)
[Download our CS50 Reference sheet on Linear Search](https://cs50.harvard.edu/ap/2020/assets/pdfs/linear_search.pdf)
