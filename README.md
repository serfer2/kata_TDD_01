# Fizzbuzz - kata

## Instructions

In this very basic kata you will have to create a function that returns the same numbers that is given as a parameter, with the following exceptions:

 - If input value is not int or float - raises TypeError.

 - If number divides evenly with 3 - returns string "fizz".

 - If number divides evenly with 5 - returns string "buzz".

 - If number divides evenly with 3 and 5 - returns string "fizz buzz".

### Examples:

```python
fizzbuzz(1) == 1
fizzbuzz(9) == "fizz"
fizzbuzz(25) == "buzz"
fizzbuzz(37) == 37
fizzbuzz(45) == "fizz buzz"
```

Launch in console:

```bash
python -m test.test_fizz_buzz
```

Source: [codewars](https://www.codewars.com/kata/your-basic-fizzbuzz-kata/python)


# String Adder - kata

## Instructions

Try to solve these steps, in order, as simply as possible. Remember to refactor after each passing test.

 1. Create a simple String calculator with a method signature: `int Add(string numbers)`.  
 The method can take up to two numbers, separated by commas, and will return their sum.  
 For example `""` or `"1"` or `"1,2"` as inputs.  
 For an empty string it will return `0`.

 2. Allow the Add method to handle an unknown amount of numbers.

 3. Allow the Add method to handle new lines between numbers (instead of commas).

    - The following input is ok: `"1\n2,3"` (will equal 6).

    - The following input is NOT ok: `"1,\n"` (not need to prove it - just clarifying).

 4. Support different delimiters.

    - To change a delimiter, the beginning of the string will contain a separate line that looks like this: `"//[delimiter]\n[numbers…]"` for example `"//;\n1;2"` should return `3` where the default delimiter is `';'`.

    - The first line is optional. All existing scenarios should still be supported.

 5. Calling Add with a negative number will throw an exception `"negatives not allowed"` - and the negative that was passed.  
 If there are multiple negatives, show all of them in the exception message.

 6. Numbers bigger than 1000 should be ignored, so adding `2 + 1001 = 2`.

 7. Delimiters can be of any length with the following format: `"//[delimiter]\n"` for example: `"//[***]\n1***2***3"` should return `6`.

 8. Allow multiple delimiters like this: `"//[delim1][delim2]\n"` for example `"//[*][%]\n1*2%3"` should return `6`.

 9. Make sure you can also handle multiple delimiters with length longer than one char.

Source: [https://osherove.com/tdd-kata-1](https://osherove.com/tdd-kata-1)
