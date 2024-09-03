import random

def load_challenges(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip()]

def save_challenge(filename, challenge):
    with open(filename, "a") as file:
        file.write(challenge + "\n")

def clear_file(filename):
    with open(filename, "w") as file:
        file.write("")

def list_challenges(challenges):
    if not challenges:
        print("There are currently no challenges")
    else:
        print("The challenges are:")
        for idx, challenge in enumerate(challenges, start=1):
            print(f"[{idx}] {challenge}")

def generate_grid(challenges, export_filename):
    if len(challenges) < 25:
        print("There are not enough challenges to be able to continue\n\n")
    else:
        with open(export_filename, "a") as file:
            file.write("[")
            for _ in range(25):
                challenge = random.choice(challenges)
                file.write(challenge + ", ")
            file.write("]\n")

def main():
    challenges_list = load_challenges("challenges.txt")
    clear_file("export.txt")

    while True:
        action = input(
            "What action do you want to do? (Enter the number in brackets)\n"
            "- List the challenges (1)\n"
            "- Add a challenge (2)\n"
            "- Generate a grid (3)\n"
            "- Exit (0)\n"
        )
        if action == '0':
            break
        elif action == "1":
            list_challenges(challenges_list)
        elif action == "2":
            challenge_to_add = input("What challenge do you want to add?\n")
            save_challenge("challenges.txt", challenge_to_add)
            challenges_list.append(challenge_to_add)
            print("The challenge has been successfully added to the list")
        elif action == "3":
            generate_grid(challenges_list, "export.txt")

if __name__ == "__main__":
    main()