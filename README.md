# RPN Calculator

This is a RPN Calculator written using Django!

![image](https://user-images.githubusercontent.com/35508198/154626416-176ac276-bcd9-4e9e-a7e9-00a2055ce32b.png)

**Reverse Polish Notation (RPN)** provides the quickest way to enter data in a calculator because it eliminates the need for parenthesis. It was made mainstream by HP when they implemented it in their famous programmable calculators. It is also very simple to code into a computer program. This is a simple online RPN calculator for you to try out. It's written in Javascript


**How to use it**

Unlike with a traditional calculator, you enter the parameters first, than the operator.

- For example, to calculate '20+50': type '20' -> Press ↑ -> '50' -> Press '+'
- '↑' is the push button which will push the number to the stack.
- The calculator supports a maximum stack depth of three.
- The displayed output is always a single integer value, unless there is an error.
- The calculator does integer math.
- If user divide an integer by zero, it will have an error.
- If user pushes over three numbers into the calculator, calculator will have "Stack Overflow".
- If user does an operation with only one value stored in the stack, the calculator will have "Stack Underflow".






