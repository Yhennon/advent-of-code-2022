import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Scanner;

public class Day1_a {

    public static int sum(int a, int b){
        return a + b;
    }

    public static void main(String[] args) throws FileNotFoundException {

        List<Integer> elf = new ArrayList<>();
        File input = new File("Day1.txt");
        Scanner sc = new Scanner(input);
        int calorie = 0;
        int highest = 0;
        while(sc.hasNextLine()){
            String line = sc.nextLine();

            if (line.isEmpty() || line.trim().equals("") || line.trim().equals("\n")){
                elf.add(calorie);
                calorie = 0;
            }
            else {
                calorie = sum(calorie,Integer.parseInt(line));
            }

        }
        elf.add(calorie);
        sc.close();
        for(int i : elf){
            if (i > highest){
                highest = i;
            }
        }
        System.out.println(highest);
    }
}