from pprint import pprint


def main():

    # points for shapes chosen:
    # rock: 1 A X
    # paper: 2 B Y
    # scissors: 3 C Z

    # points for game result:
    # lose: 0
    # draw: 3
    # win: 6

    # What would your total score be if everything goes exactly according to your strategy guide?
    with open("input.txt", "r", encoding="utf-8") as file:
        # List of lists
        games = []

        # Make the pairs of choices for each game
        for line in file:
            line = line.strip()
            choices = [line[0], line[2]]
            games.append(choices)
            choices = []

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
