import turtle
"""
CSAPX Lab 1: Tiny Turtle

A program that takes an enhanced TT program, expands it into basic TT commands,
and then does turtle drawing from it.

author: Ayane Naito
"""
def evaluate(input_cmd):
    """
    Interprets basic TT commands submitted by the user into turtle commands.
    Returns a message when program is done drawing shape.
    :param input_cmd: Basic TT command string inputted by user
    :return: None
    """
    command_q = input_cmd.split()
    for cmd in command_q:
        if cmd[0] == 'F':
            turtle.forward(int(cmd[1::]))
        elif cmd[0] == 'L':
            turtle.left(int(cmd[1::]))
        elif cmd[0] == 'R':
            turtle.right(int(cmd[1::]))
        elif cmd[0] == 'U':
            turtle.up()
        elif cmd[0] == 'D':
            turtle.down()
        elif cmd[0] == 'B':
            turtle.backward(int(cmd[1::]))
        else:
            turtle.circle(int(cmd[1::]))
    print("Shape drawn. Close graphics window when done.")

def main() -> None:
    """
    The main function prompts the user to enter a TT program.  It then expands
    that program to the basic TT commands and then executes them.
    :return: None
    """
    user_cmd = input("Enter a string containing basic TT commands: ")
    evaluate(user_cmd)
    turtle.mainloop()
if __name__ == '__main__':
    main()