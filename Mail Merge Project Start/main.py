# Open the template letter file in read mode
with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_content = letter_file.read()

# Open the file containing the list of names in read mode
with open("./Input/Names/invited_names.txt", "r") as names_file:
    for line in names_file:
        # Strip any leading or trailing whitespace from each name
        name = line.strip()

        # Replace the placeholder "[name]" in the template letter with the current name
        personalized_letter = letter_content.replace("[name]", name)

        # Create a new file for each name and write the personalized letter to it
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as output_file:
            output_file.write(personalized_letter)




