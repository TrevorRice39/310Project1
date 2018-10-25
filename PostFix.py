from Array_Stack import ArrayStack


def do_op(n2, n1, op):  # function that returns the value to (n2) op (n1) where op = ['+', '*', '-', '/]
    return {'+': (n1 + n2), '*': (n1 * n2), '-': (n1 - n2), '/': (n1 / n2)}.get(op)


def evaluate_postfix(e):  # evaluates a postfix notated expression
    nums = ArrayStack()  # stack for processing integers in the expression
    for i in range(len(e)):  # scans the input string
        #  if  e[i] is an operator, two values are popped from the stack and
        #  are evaluated along with the operator (e[i]) in the function do_op()
        #  otherwise, if e[i] is a number it is pushed onto the stack
        nums.push(int(e[i]) if e[i].isdigit() else do_op(nums.pop(), nums.pop(), e[i]))
    return nums.pop()  # returns the value of the expression


exp = '52+83-*4/'

print(exp + " = " + str(evaluate_postfix(exp)))
