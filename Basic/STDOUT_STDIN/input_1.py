print("Please enter your name:")
name = input()
print(f"Hello, {name}! please enter your birth year:")
age = input()
current_year = 2024
birth_year = current_year - int(age)
print(f"{name}, you were born in {birth_year}. so you are {age} years old.")
print("what is your favorite programming language?")
language = input()
if "," not in language:
    splitted_languages = [lang.strip() for lang in language.split(" ")]
    last_language = splitted_languages[-1]
    splitted_languages=splitted_languages[:-1]
    language = ",".join(splitted_languages)
print(f"{name}, it's great that you like {language} and {last_language}!")
if int(age) < 18:
    print("You are a minor.")
print("Thank you for using the program!")
