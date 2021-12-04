package adventjava;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Day1 {
    public static void main(String[] args) {
        partOne();
    }

    public static void partOne() {
        try {
            File file = new File("./src/day1input.txt");
            FileReader fr = new FileReader(file);
            BufferedReader br = new BufferedReader(fr);
            int answer = br.lines()
                    .map((x) -> Integer.parseInt(x))
                    .reduce(0, (first, second) -> first < second ? 0 : 1); // does not work, need to find a way to keep a running total
            System.out.println("Part 1: " + answer);
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}