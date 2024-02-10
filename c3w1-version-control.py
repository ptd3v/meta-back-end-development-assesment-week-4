#Version Control

#Command Line Command Examples:
cd /Desktop: # Change Directory, changes the current place the cmd is looking
mkdir example # Create a new directory called example in your current location
cd example # Enter the newly created example folder.
touch example.js # Does not work, Linux only?
code example.js # Open the newly created file in VSCode.

#Unix Commands/ Bash commands (Seems the same)
ls # Show the contents of the current working directory
ls -l # Shows the contents of a folder in list order, showing read/write permissions, groups and owners.
ls -a # Shows the contents of a folder, including hidden ones.
pwd # Shows the full path of the current working directory.
cp # Copy command, copies files or folders from one destination to another.
mv # Move command, moves files or folders from one destination to another.

# Flags example
ls #A command
ls -l #Is a command with a flag added '-l', this changes the command to add fununctionality.
man ls #Shows the user manual for the listed command. Great for learning command flags.

#Bash on Windows
ls -la # Show all files and folders in the current directory, hidden and permissions shown.
less example.txt #Open the example.txt file. Press Q to exit.
vim testshell.sh # Creates a new shell file called testshell.

# Create a bash script
#!/bin/bash 
echo "Hello, World" # Print to screen, press Esc to exit.
:wq! # Save and exit the file.
chmod 755 testshell.sh # Change the read/ write permissions of the file to allow execution.
./testshell.sh # Run the file, should print hello world.

# Change Directories, List Contents
pwd #print working directory
cd / #Change current directory to Root
pwd # Will now display /
ls # Will show all the files/ folders in root.
cd etc # Change to the etc folder
ls # List the files/ folders in the current directory.
cd .. # Takes me back up to the parent directory

# Creating and moving directories and files
pwd # print working directory
mkdir example # Create a new directory called 'Example'.
cd example # Change directory. Enter the newly created folder.
ls # Will display nothing as there is nothing in the new folder.
touch example.txt # Creates a file called example.txt. Not windows.
ls -l # Verify that the new files are in the folder.
cd .. # Go back up to root.
mkdir example1 # Creates a second folder.
clear # Clears the screen. Just makes it easier to read.
mv example1 example # Move Command. What do you want to move? To where?

#Pipes
cat example.txt #ConCATentate. Read the contents of the file in the terminal windows.
wc example.txt -w # Will display the total words within the .txt file.
ls | wc -w # The outcome would be two, becuase there are two files in this folder. example.txt and example1.txt.
cat example.txt example1.txt | wc -w # Print the total word count within these two text files.


