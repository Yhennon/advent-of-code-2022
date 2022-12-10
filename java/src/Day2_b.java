import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day2_b {
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
                            score += 3;
                            break;
                        case "Y":
                            score += 4;
                            break;
                        case "Z":
                            score += 8;
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
                            score += 2;
                            break;
                        case "Y":
                            score += 6;
                            break;
                        case "Z":
                            score += 7;
                            break;
                    }
                    break;
            }

        }
        System.out.println(score);
    }
}
