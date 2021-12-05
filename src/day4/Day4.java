import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

class Day4 {
    public static void main(String[] args) {
        partOne();
        partTwo();
    }

    public static ArrayList<Integer> parseDraws(String numbers) {
        ArrayList<Integer> drawnInts = new ArrayList<>();
        String[] splitNumbers = numbers.split(",");
        for (String s : splitNumbers) {
            drawnInts.add(Integer.parseInt(s));
        }
        return drawnInts;
    }

    public static ArrayList<Bingo> parseBingoCards(ArrayList<String> numbers) {
        ArrayList<Bingo> cards = new ArrayList<>();
        for (int i = 0; i < numbers.size() / Bingo.SIZE; i++) {
            ArrayList<Integer> parsedLine = new ArrayList<>();
            for (int j = 0; j < Bingo.SIZE; j++) {
                String[] line = numbers.get(5 * i + j).trim().split("\\s+");
                for (String num : line) {
                    parsedLine.add(Integer.parseInt(num.trim()));
                }
            }
            Bingo bingo = new Bingo(parsedLine);
            cards.add(bingo);
        }
        return cards;
    }

    public static int simulatePartOne(ArrayList<Integer> draws, ArrayList<Bingo> cards) {
        boolean isFirst = true;
        int answer = 0;
        for (int draw : draws) {
            for (Bingo card : cards) {
                card.mark(draw);
                if (card.isWinningBoard() && isFirst) {
                    answer = card.getScore(draw);
                    isFirst = false;
                    break;
                }
            }
        }
        return answer;
    }

    public static int simulatePartTwo(ArrayList<Integer> draws, ArrayList<Bingo> cards) {
        int answer = 0;
        for (int draw : draws) {
            for (Bingo card : cards) {
                card.mark(draw);
                if (card.isWinningBoard() && card.finalScore == -1) {
                    answer = card.getScore(draw);
                }
            }
        }
        return answer;
    }

    private static void partOne() {
        try {
            File file = new File("./day4input.txt");
            FileReader fr = new FileReader(file);
            BufferedReader br = new BufferedReader(fr);
            String drawnNumbers = br.readLine();
            ArrayList<Integer> ints = parseDraws(drawnNumbers);
            String currentLine = null;
            ArrayList<String> cardNumbers = new ArrayList<>();
            while ((currentLine = br.readLine()) != null) {
                if (!currentLine.isBlank()) {
                    cardNumbers.add(currentLine);
                }
            }
            ArrayList<Bingo> cards = parseBingoCards(cardNumbers);
            int partOneAnswer = simulatePartOne(ints, cards);
            System.out.println("Part one: " + partOneAnswer);
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void partTwo() {
        try {
            File file = new File("./day4input.txt");
            FileReader fr = new FileReader(file);
            BufferedReader br = new BufferedReader(fr);
            String drawnNumbers = br.readLine();
            ArrayList<Integer> ints = parseDraws(drawnNumbers);
            String currentLine = null;
            ArrayList<String> cardNumbers = new ArrayList<>();
            while ((currentLine = br.readLine()) != null) {
                if (!currentLine.isBlank()) {
                    cardNumbers.add(currentLine);
                }
            }
            ArrayList<Bingo> cards = parseBingoCards(cardNumbers);
            int partTwoAnswer = simulatePartTwo(ints, cards);
            System.out.println("Part two: " + partTwoAnswer);
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}