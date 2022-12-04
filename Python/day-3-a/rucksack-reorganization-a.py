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

        # Find the matching item
        for line in file:
            line = line.strip()

            firstHalf = []
            secondHalf = []

            itemCount = len(line)
            half = itemCount//2

            count = 0
            for i in line:
                if count < half:
                    firstHalf.append(i)
                    count += 1
                else:
                    secondHalf.append(i)
                    count += 1

            # Convert them to sets (like a mathetmatical set, where every item is unique, and return the intersection of the two sets.)
            common = list(set(firstHalf) & set(secondHalf))[0]
            print(common)
            commonList.append(priorityDict.get(common))

        # This is the solution
        print("The sum of all the items:", sum(commonList))


        # print(priorityDict.get(common))
if __name__ == "__main__":
    main()
