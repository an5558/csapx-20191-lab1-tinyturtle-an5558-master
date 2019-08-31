import turtle as tt
"""
CSAPX Lab 1: Tiny Turtle

A program that takes an enhanced TT program, expands it into basic TT commands,
and then does turtle drawing from it.

author: Ayane Naito
"""
def evaluate(input_cmd):
    

def main() -> None:
    """
    The main function prompts the user to enter a TT program.  It then expands
    that program to the basic TT commands and then executes them.
    :return: None
    """
    user_cmd = input("Enter a string containing basic TT commands: ")
    evaluate(user_cmd)
    tt.mainloop()
if __name__ == '__main__':
    main()