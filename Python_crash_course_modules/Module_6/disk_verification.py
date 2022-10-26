# Author: Amber Wonnenberg
# Module 6 challenge
# Compiled: Sept. 23, 2022

"""
This program will take the inputted disk title, number and serial number and verify
weather it is a valid game or not.
"""

games = ['pac man world', 'game of life', 'call of duty: big red one', "nhl '99"]
valid_serial_number = [40394, 69302, 76034, 40395, 22490]


# Verify the game title is in a list a valid games
def verify_title(game_title):
    if game_title.lower() in games:
        on_list = True
    else:
        on_list = False

    return on_list


# Verify the disk number is within a given rage
def verify_disk_number(number):
    if number in range(1496833, 5930214):
        disk_number_match = True
    else:
        disk_number_match = False

    return disk_number_match


# Verify serial number is in a list of valid serial numbers
def verify_serial_number(serial_number):
    if serial_number in valid_serial_number:
        serial_number_match = True
    else:
        serial_number_match = False

    return serial_number_match


# If all three (game title, number and serial number) are valid, print statement that the disk is genuine.
def valid_disk():
    if verify_title(disk_name):
        if verify_disk_number(disk_number):
            if verify_serial_number(disk_serial_number):
                print("\nTHIS IS A GENUINE DISK.")
    else:
        print("\nTHIS IS NOT A GENUINE DISK.")


# Welcome screen
print('\n==================================================================',
      "\n\t\t\tPythonCo. Disk Validation Checker",
      "\n==================================================================")

# take in user input to validate
disk_name = input("\nEnter in the name of the disk and press ENTER: ")
disk_number = int(input("Enter in the disk number and press ENTER: "))
disk_serial_number = int(input("Enter in the disk serial number and press ENTER: "))

print("\n\nRESULTS"
      "\n==================================================================")

# Print results
print("On Disk List:".ljust(30), verify_title(disk_name.title()))
print("Disk Number Match:".ljust(30), verify_disk_number(disk_number))
print("Disk Serial Number Match:".ljust(30),verify_serial_number(disk_serial_number))

# print if the disk is genuine or not
valid_disk()


