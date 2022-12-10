import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day2_a {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("Day2.txt");
        Scanner sc = new Scanner(file);
        int score =0;
        while (sc.hasNextLine()){
            Scanner line = new Scanner(sc.nextLine());
            String first = line.next();
            String second = line.next();
            switch (first){
                case "A":
                    switch (second){
                        case "X":
                            score += 4;
                            break;
                        case "Y":
                            score += 8;
                            break;
                        case "Z":
                            score += 3;
                            break;
                    }
                    break;
                case "B":
                    switch (second){
                        case "X":
                            score += 1;
                            break;
                        case "Y":
                            score += 5;
                            break;
                        case "Z":
                            score += 9;
                            break;
                    }
                    break;
                case "C":
                    switch (second){
                        case "X":
                            score += 7;
                            break;
                        case "Y":
                            score += 2;
                            break;
                        case "Z":
                            score +=6;
                            break;
                    }
                    break;
            }

        }
        System.out.println(score);
    }
}
