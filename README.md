### Task

You're given a dictionary `per_cent` with the distribution of interest rates on deposits in various banks, where the ***key*** is the bank's name and the ***value*** is the interest. Write a program that will generate a `deposit` list with accumulated funds for the year of deposit in each of the banks. The amount of `money` that a client plans to deposit at interest is entered into the program input from the keyboard.

`per_cent = {'OP': 2.6, 'Aktia': 1.9, 'Nordea': 2.28, 'S-Bank': 3.0}`

**Example of how the program works**

`money = 100000`

`deposit = [5600, 5900, 4280, 4000]`

Add to the program a search for the maximum value and display it in the format:

`The maximum amount you can earn is deposit[i]`,

where instead of `deposit[i]` the maximum value of the list will be shown.
