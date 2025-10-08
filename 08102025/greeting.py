import argparse

argparser = argparse.ArgumentParser(description="Greet the user.")
argparser.add_argument("name", type=str, help="The name of the user to greet.")
args = argparser.parse_args()
print(f"Hello, {args.name}!, welcome to the program.")
