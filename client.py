import rpyc
from constCS import *


def main() -> None:
    conn = rpyc.connect(HOST, PORT)

    # Inputs
    first_string = input("Input your first string: ")
    second_string = input("Input your second string: ")
    operation = input("Choose one of the following operations -> Concat, Equal, Distance: ")

    # Operations
    if operation == 'Concat':
        response =  conn.root.concat(first_string, second_string)
        print(f"Concatenated strings: {response}")
    elif operation == 'Distance':
        response =  conn.root.levenshtein_dist(first_string, second_string)
        print(f"Levenshtein Distance: {response}")
    elif operation == 'Equal':
        response =  conn.root.equal(first_string, second_string)
        if response:
            response = "Strings are equal"
        else:
            response = "Strings are not equal"

    else:
        response = "Operation does not exist"


if __name__ == '__main__':
    main()