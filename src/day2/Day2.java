import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Day2 {
    public static void main(String[] args) {
        partOne();
        partTwo();
    }

    private static void partOne() {
        Submarine sub = new Submarine();
        parseAndExecute(sub);
        sub.printAnswer();
    }

    private static void partTwo() {
        Submarine sub = new Submarine();
        parseAndExecutePartTwo(sub);
        sub.printAnswer();
    }

    private static void parseAndExecute(Submarine sub) {
        try {
            File file = new File("./src/day2input.txt");
            FileReader fr = new FileReader(file);
            BufferedReader br = new BufferedReader(fr);
            br.lines().map(str -> str.split(" ")).forEach((arr) -> {
                if (arr[0].equals("forward")) {
                    sub.moveForward(Integer.parseInt(arr[1]));
                } else if (arr[0].equals("down")) {
                    sub.changeDepth(Integer.parseInt(arr[1]));
                } else if (arr[0].equals("up")) {
                    sub.changeDepth(-Integer.parseInt(arr[1]));
                }
            });
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void parseAndExecutePartTwo(Submarine sub) {
        try {
            File file = new File("./src/day2input.txt");
            FileReader fr = new FileReader(file);
            BufferedReader br = new BufferedReader(fr);
            br.lines().map(str -> str.split(" ")).forEach((arr) -> {
                if (arr[0].equals("forward")) {
                    sub.moveForwardPartTwo(Integer.parseInt(arr[1]));
                } else if (arr[0].equals("down")) {
                    sub.changeAim(Integer.parseInt(arr[1]));
                } else if (arr[0].equals("up")) {
                    sub.changeAim(-Integer.parseInt(arr[1]));
                }
            });
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static class Submarine {
        int depth;
        int distance;
        int aim; // For part 2

        public Submarine() {
            this.depth = 0;
            this.distance = 0;
        }

        public void moveForward(int distance) {
            this.distance = this.distance + distance;
        }

        public void moveForwardPartTwo(int distance) {
            this.distance = this.distance + distance;
            this.depth = this.depth + this.aim * distance;
        }

        public void changeAim(int amount) {
            this.aim = this.aim + amount;
        }

        public void changeDepth(int depth) {
            this.depth = this.depth + depth;
        }

        public void printAnswer() {
            int answer = depth * distance;
            System.out.println(answer);
        }
    }
}
