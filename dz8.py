import sys
import colorama
from colorama import Fore
from fractions import Fraction

# Initialize colorama
colorama.init(autoreset=True)

def calculator_decorator(func):
    def wrapper(expression):
        try:
            # Replace fractions like '1/2' with 'Fraction(1, 2)'
            parsed_expression = ''
            tokens = expression.split(' ')
            for token in tokens:
                if '/' in token and token.replace('/', '').isdigit():
                    num, denom = token.split('/')
                    parsed_expression += f'Fraction({num}, {denom}) '
                else:
                    parsed_expression += token + ' '
            result = func(parsed_expression.strip())
            print(f"{Fore.GREEN}Result: {result}")
            return result
        except ZeroDivisionError:
            print(f"{Fore.RED}Error: Division by zero is not allowed.")
        except SyntaxError:
            print(f"{Fore.RED}Error: Invalid syntax.")
        except Exception as e:
            print(f"{Fore.RED}Error: {str(e)}")
    return wrapper

@calculator_decorator
def calculate(expression):
    return eval(expression)

def main():
    # User Manual
    print(Fore.GREEN + "Welcome to the RoмкаР Python Calculator!")
    print("  Supported operations: +, -, *, /, ** (exponentiation), // (integer division), % (modulus)")
    print("  You can also work with fractions and floating-point numbers.")
    print(Fore.GREEN + "  Examples:")
    print("    5 + 5")
    print("    10 / 2")
    print("    1/2 + 3/4")
    print(Fore.YELLOW + "Python version required: 3.7 or higher " + Fore.GREEN + f"(recommended 3.13.0 or higher)")
    print(Fore.CYAN + f"Current Python version: {sys.version}")
    print("Enter a mathematical expression (or type 'exit' to quit):")

    while True:
        expression = input(": ")
        if expression.lower() == 'exit':
            break
        calculate(expression)

if __name__ == '__main__':
    main()
