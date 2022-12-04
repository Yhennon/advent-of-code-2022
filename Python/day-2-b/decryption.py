# https://adventofcode.com/2022
from pprint import pprint


def main():

    # X : need to lose
    # Y : need to draw
    # Z : need to win

    # Convert answers first, then calculate score

    with open("input.txt", "r", encoding="utf-8") as file:
        ########## CONVERSION START ###########
        games = []
        choices = []
        for line in file:
            line = line.strip()

            choice1 = line[0]
            choice2 = line[2]

            # Rock and i need to lose = i choose scissors
            if line[0] == "A" and line[2] == "X":
                choice2 = "Z"
            # Paper and i need to lose = i choose rock
            if line[0] == "B" and line[2] == "X":
                choice2 = "X"
            # Scissors and i need to lose = i choose paper
            if line[0] == "C" and line[2] == "X":
                choice2 = "Y"

            # Rock and i need to win = i choose paper
            if line[0] == "A" and line[2] == "Z":
                choice2 = "Y"
            # Paper and i need to win = i choose scissors
            if line[0] == "B" and line[2] == "Z":
                choice2 = "Z"
            # Scissors and i need to win = i choose rock
            if line[0] == "C" and line[2] == "Z":
                choice2 = "X"

            if line[0] == "A" and line[2] == "Y":
                choice2 = "X"
            # Paper and i need to win = i choose scissors
            if line[0] == "B" and line[2] == "Y":
                choice2 = "Y"
            # Scissors and i need to win = i choose rock
            if line[0] == "C" and line[2] == "Y":
                choice2 = "Z"

            choices.append(choice1)
            choices.append(choice2)
            games.append(choices)
            choices = []

        ########## CONVERSION END ###########

        # Now that the conversion is done, the score calculation is the same as in day-2-a.
        myTotalScore = 0

        for game in games:
            # Scenarios when i draw
            score = 0
            # Rock || Rock
            if game[0] == "A" and game[1] == "X":
                score = 3 + 1
            # Paper ||Paper
            if game[0] == "B" and game[1] == "Y":
                score = 3 + 2
            # Scissors || scissors
            if game[0] == "C" and game[1] == "Z":
                score = 3 + 3

            # Scenarios when i win

            # Scissors || rock beats it
            if game[0] == "C" and game[1] == "X":
                score = 6 + 1
            # Rock || paper beats it
            if game[0] == "A" and game[1] == "Y":
                score = 6 + 2
            # Paper || scissors beats it
            if game[0] == "B" and game[1] == "Z":
                score = 6 + 3

            # Scenarios when i lose:

            # Paper || Rock is beaten
            if game[0] == "B" and game[1] == "X":
                score = 0 + 1
            # Scissors || Paper is beaten
            if game[0] == "C" and game[1] == "Y":
                score = 0 + 2
            # Rock || Scissors is beaten
            if game[0] == "A" and game[1] == "Z":
                score = 0 + 3

            myTotalScore += score

            print("first:", game[0], "second:", game[1], "score:", score)

        print("My total score is: ", myTotalScore)


if __name__ == "__main__":
    main()
