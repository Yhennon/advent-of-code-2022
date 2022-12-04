#coding: utf-8
from pprint import pprint


def main():

    # Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
    with open("input.txt", "r", encoding="utf-8") as file:

        # allElfList is going to contain other lists.
        allElfList = []
        # A single list, containing int values of calories
        singleElfList = []

        # Iterate through the file, line by line. If The line is not an empty new line, add the value to singleElfList. If the line is an empty new line, append the singleElfList to the allElfList, and reset the singleElflist.
        for line in file:
            if line != "\n":
                line = int(line.strip())
                singleElfList.append(line)
            elif line == "\n":
                allElfList.append(singleElfList)
                singleElfList = []

        # I do not add anything to the allElfList in the if branch. Therefore the last time the if branch is triggered, i have to add the latest singleElflist to the allElfList.
        allElfList.append(singleElfList)

        # Iterate through the allElfList, elf by elf. For a single elf, store the sum of the calories they are carrying.
        summedCalories = []

        for elf in allElfList:
            calories = 0

            for food in elf:
                calories += food

            summedCalories.append(calories)

        # Order the summedCalories list by descending order, and take the sum of the first 3 number.
        summedCalories.sort(reverse=True)
        sumTop3 = sum(summedCalories[0:3])

        # This output is your answer for day1-b
        print("Calories: ", sumTop3)


if __name__ == "__main__":
    main()
