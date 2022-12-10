import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Day1_b {
    public static int sum(int a, int b){
        return a + b;
    }

    public static void main(String[] args) throws FileNotFoundException {

        List<Integer> elf = new ArrayList<>();
        File input = new File("Day1.txt");
        Scanner sc = new Scanner(input);
        int calorie = 0;
        int sum = 0;
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
        Collections.sort(elf);
        System.out.println(elf);

        for (int i = elf.size()-1; i > elf.size()-4 ; i--) {
            sum += elf.get(i);
        }
        System.out.println(sum);
    }
}

