import argparse
from example_package.example import Example

def main():
    parser = argparse.ArgumentParser(description='Example usage of the Example class.')
    parser.add_argument('message', help='The message to use.')
    parser.add_argument('--ascii', action='store_true', help='Display the message as ASCII art.')
    args = parser.parse_args()

    example_instance = Example(args.message)

    if args.ascii:
        output = example_instance.get_ascii_art()
    else:
        output = example_instance.get_example_message()

    print(output)

if __name__ == '__main__':
    main()
