import argparse

argparser = argparse.ArgumentParser(description="Greet the user.")
argparser.add_argument("name", type=str, help="The name of the user to greet.")
argparser.add_argument("age",type=int, help="Enter the age")
args = argparser.parse_args()
print(f"Hello, {args.name}!, welcome to the program.\nyour age is {args.age}")
