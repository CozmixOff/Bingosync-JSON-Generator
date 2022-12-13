import random

challenges_list = []
value = 0
challenges_to_export = []

challenges_file = open("challenges.txt", "r")
challenges_file_content = challenges_file.read()
challenges_count = challenges_file_content.count('\n')
challenges_lines = challenges_file_content.split('\n')
for i in range(0, challenges_count + 1):
    defi_to_append = challenges_lines[i]
    if defi_to_append =='' or defi_to_append =='\n':
        pass
    else:
        challenges_list.append(defi_to_append)
challenges_file.close()
challenges_export = open("export.txt", "w")
challenges_export.write("")
challenges_export.close()
challenges_count = challenges_file_content.count('\n')

while True:
    action = input(
        "What action do you want to do? (Enter the number in brackets)\n- List the challenges (1)\n- Add a challenge (2)\n- Generate a grid (3)\n- Exit (0)\n")
    if action == '0':
        break
    if action == "1":
        if len(challenges_list) == 0:
            print("There are currently no challenges")
        else:
            print("The challenges are:")
            for j in range(0, len(challenges_list)):
                print("[" + str(j + 1) + "] " + challenges_list[j])
    if action == "2":
        defi_to_add = input("What challenge do you want to add?\n")
        challenges_add = open("challenges.txt", "a")
        challenges_add.write(defi_to_add+"\n")
        challenges_add.close()
        print("The challenge has been successfully added to the list")
    if action == "3":
        if len(challenges_list) < 25:
            print("There are not enough challenges to be able to continue\n\n")
        else:
            challenges_export = open("export.txt", "a")
            challenges_export.write("[")
            for k in range(0, 25):
                challenges_update = random.choice(challenges_list)
                challenges_list.remove(challenges_update)
                challenges_export.write('{"name":"' + challenges_update + '"}')
                if k != 24:
                    challenges_export.write(',')
            challenges_export.write("]")
            challenges_export.close()
            print('The list has been successfully exported\n\n')
    else:
        print('\n')

print("You left the application")
