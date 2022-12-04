from pprint import pprint
import string


def main():
    # Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
    with open("input.txt", "r", encoding="utf-8") as file:

        # Pair values to characters from a-Z, starting with 1, incrementing by 1
        priorityDict = {}
        commonList = []

        counter = 1
        for i in string.ascii_letters[0:52]:
            priorityDict.update({i: counter})
            counter += 1

        # Make groups of 3 lines
        # This group of 3 is a list containing lists of 3 lines
        groupOf3 = []

        temp = []
        lineCount = 0

        for line in file:
            line = line.strip()
            temp.append(line)
            if lineCount == 2:
                groupOf3.append(temp)
                lineCount = 0
                temp = []
            else:
                lineCount += 1

        # Take the common character
        entryCount = 0
        for entry in groupOf3:
            common = list(set(groupOf3[entryCount][0]) &
                          set(groupOf3[entryCount][1]) &
                          set(groupOf3[entryCount][2]))[0]
            entryCount += 1
            commonList.append(priorityDict.get(common))

        # A megoldás
        print("The sum of all the items:", sum(commonList))


if __name__ == "__main__":
    main()
