# energy-tip-saver-generator
# Overview Of The Project
This is a simple, command line Python application designed to help users save energy at home by providing random, actionable energy-saving tips across different household areas. The program runs in a loop, allowing the user to repeatedly get tips for the same category or switch to a new category.

# Features Categorized Tips:
Provides energy-saving tips for five distinct areas: lighting , heating , kitchen , electronics , and general.
Randomized Output: A different, random tip is generated and displayed from the category's list each time the user requests more tips.
Interactive Menu: Allows the user to repeatedly view tips for the current area or change to a different area.
Input Validation: Handles invalid category inputs by prompting the user to enter a correct area.
Technologies/Tools Used
Language: Python 3
# Core Libraries:
The built-in "random" module is used for selecting tips.
Steps to Install & Run the Project
Requirement: Ensure you have "Python 3" installed on your operating system.
Download the Code: Save the provided source code into a single file named energy_tip_generator.py.
Run the Application: Open your terminal or command prompt, navigate to the directory where you saved the file, and execute the following command: python energy_tip_generator.py
# Instructions for Testing
Since this is a simple console application, testing primarily involves checking the functionality in the terminal.

Start the program as described above.
# Test Valid Inputs: 
Enter each of the following categories when prompted and verify that a unique, relevant tip is displayed:
lighting
heating
kitchen
electronics
general
Test 'More Tips' Loop: After receiving a tip, enter "y" to see another tip for the same area, and then enter "n" to exit the inner loop and proceed to the 'change area' prompt.
Test 'Change Area' Loop: Enter "y" when prompted to change the area and repeat steps 2 & 3. Enter "n"to exit the entire program and verify the "Thank You" message is displayed.
Test Invalid Input: Enter a non-listed category (e.g., "bedroom") and verify the "Enter the correct area." message is displayed.
