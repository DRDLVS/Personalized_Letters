# Personalized Letters

## Description

The **Personalized Letters** script automates the creation of personalized letters using a template and a list of names. The script reads a template letter and a list of names from specified input files, generates a customized letter for each name by replacing a placeholder in the template, and then saves each personalized letter as a separate file in the output directory.

## How It Works

1. **Read Template Letter**: The script opens and reads the content of a template letter from `starting_letter.txt`.
2. **Process Names**: It reads a list of names from `invited_names.txt`, processes each name to remove any extra whitespace, and replaces a placeholder `[name]` in the template letter with the actual name.
3. **Generate and Save Letters**: For each name, it creates a new file in the `ReadyToSend` directory with the personalized letter content.

## File Structure

- `Input/Letters/starting_letter.txt`: The template letter file with a placeholder `[name]`.
- `Input/Names/invited_names.txt`: A text file containing names, one per line.
- `Output/ReadyToSend/`: Directory where the personalized letters are saved.
