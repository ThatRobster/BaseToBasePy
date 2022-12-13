This is a very simple python program that will convert a number from any base system into any other base system

To use it, simply open the file, add the numbers that you use to the library of numbers at the bottom (By default numbers 1-F, corresponding to 1-16 are added),
or if you dont need a higher base than 16, just leave it as is, and run the program!

How does it work?

There are a few steps to switch a base of a number [I came up with this method myself but I am certain many people came up with this before me]

1 - We convert the number to a base10 integer, to make it easier to work with.
    
    To do this, we simply get out the characters each individualy and get their corresponding base10 value, so for example 1 -> 1, A -> 10 and F -> 15
    Then we just multiply this number by the current base of the system, 
    to the power of the number of digit we're on (The number of digit starting from the back, starting at 0).
    Now we do this for all the characters and add them up, thats the number in base10!
    
2 - We get the amount of digits we'll need in the new number
    To get the amount of digits we'll need, we have to loop through a number i, increasing it each time it loops.
    If the base we want to the power of i is greater than the base10 number we just calculated, then that number must be i*
    *This only works if the base that we want to the power of (i-1) is smaller than base10, but since were cancelling the loop right after this that wont matter
    Now we know the amount of digits we will need.

3 - Now we can calculate the number in the new base
    To do this, simply loop down from i, the number of digits, calculated in the last step, and keep a running total that starts at the original number in base10,
    calculated at step 1. Loop for as long as the digit we're checking in the loop > -1.
    The minimum value the digit could hold, if we filled in a 1 is the base to the power of the number of the digit were on. 
    So if the current running total is less than that, the digit must be a 0
    If not though, we have to do a bit more math.
    The number the digit we're checking will hold is the amount of times that the running total is bigger 
    than the minimum value of the digit (the base of the number ^ the number of the digit), floored.
    This means that we can calculate it by just dividing the running total by the base of the number to the power of the number of the digit, floored.
    After this we just remove the number of this digit we just calculated multiplied by the minimum value of that digit, 
    the base of the number to the power of the digit number, from the running total.
    Repeat this for every digit, and add the digits' numbers to a string, and boom you've got yourself a number in a new base :)


I know its nothing crazy to do this but I thought it was cool that I figured it out by myself, and I hope this can help anyone thats having a hard time figuring it out!
I also hope I didnt make any mistakes, that would be embarrasing :P
