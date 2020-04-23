## 1.1.3 Write a program that takes three integer command-line arguments and prints equal if all three are equal, and not equal otherwise.
def Solution():
    inputs = []
    for i in range(3):
        var = input('Please enter integer ' + str(i+1))
        while not isinstance(var, int):
            var = input('Input type wrong. Please enter INTEGER ' + str(i+1))
            if var=='q':
                break
            inputs.append(var)
    
    print('You entered integers ' + str(inputs[0]) + ', ' + str(inputs[1]) + ' and ' + str(inputs[2]) + 'These values are:' )
    if inputs[0]==inputs[1] and inputs[1]==inputs[2]:
        print('equal')
    else:
        print('not equal')


## 1.1.5 Write a code fragment that prints true if the double variables x and y are both strictly between 0 and 1 and false otherwise.





## 1.1.9 Write a code fragment that puts the binary representation of a positive integer N into a String s.




## 1.1.11 Write a code fragment that prints the contents of a two-dimensional boolean
array, using * to represent true and a space to represent false. Include row and column
numbers.



## 1.1.13 Write a code fragment to print the transposition (rows and columns changed)
of a two-dimensional array with M rows and N columns.




1.1.14 Write a static method lg() that takes an int value N as argument and returns
the largest int not larger than the base-2 logarithm of N. Do not use Math.
1.1.15 Write a static method histogram() that takes an array a[] of int values and
an integer M as arguments and returns an array of length M whose ith entry is the number
of times the integer i appeared in the argument array. If the values in a[] are all
between 0 and M–1, the sum of the values in the returned array should be equal to
a.length.



1.1.20 Write a recursive static method that computes the value of ln (N !)
1.1.21 Write a program that reads in lines from standard input with each line containing
a name and two integers and then uses printf() to print a table with a column of
the names, the integers, and the result of dividing the first by the second, accurate to
three decimal places. You could use a program like this to tabulate batting averages for
baseball players or grades for students.
1.1.22 Write a version of BinarySearch that uses the recursive rank() given on page
25 and traces the method calls. Each time the recursive method is called, print the argument
values lo and hi, indented by the depth of the recursion. Hint: Add an argument
to the recursive method that keeps track of the depth.
1.1.23 Add to the BinarySearch test client the ability to respond to a second argument:
+ to print numbers from standard input that are not in the whitelist, - to print
numbers that are in the whitelist.
1.1.24 Give the sequence of values of p and q that are computed when Euclid’s algorithm
is used to compute the greatest common divisor of 105 and 24. Extend the code
given on page 4 to develop a program Euclid that takes two integers from the command
line and computes their greatest common divisor, printing out the two arguments for
each call on the recursive method. Use your program to compute the greatest common
divisor or 1111111 and 1234567.
1.1.25 Use mathematical induction to prove that Euclid’s algorithm computes the
greatest common divisor of any pair of nonnegative integers p and q.