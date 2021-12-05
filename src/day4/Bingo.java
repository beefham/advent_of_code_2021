import java.util.ArrayList;
import java.util.HashMap;

/**
 * This class functions as a Bingo card for Day 4's problem
 */
class Bingo {
    public static int SIZE = 5;

    private boolean[][] marked;

    private HashMap<Integer, Coords> card;

    public int finalScore = -1; // -1 means the board has not won yet. Once a board wins its final score is
                                // calculated and will overwrite this value.

    Bingo(ArrayList<Integer> numbers) {
        this.marked = new boolean[SIZE][SIZE];
        this.card = new HashMap<>();
        for (int i = 0; i < SIZE; i++) { // rows
            for (int j = 0; j < SIZE; j++) { // columns
                int number = numbers.get(SIZE * i + j);
                Coords position = new Coords(i, j);
                card.put(number, position);
            }
        }
    }

    public void mark(int number) {
        if (this.card.containsKey(number)) {
            Coords position = this.card.get(number);
            int row = position.getRow();
            int col = position.getCol();
            marked[row][col] = true;
        }
    }

    public boolean isWinningBoard() {
        boolean isWin = false;
        for (int i = 0; i < SIZE; i++) {
            isWin = isWin || isRowAllTrue(i) || isColumnAllTrue(i);
            if (isWin) {
                return isWin;
            }
        }
        return isWin;
    }

    private boolean isRowAllTrue(int rowIndex) {
        if (rowIndex >= SIZE || rowIndex < 0) {
            throw new IllegalArgumentException("Index out of bounds");
        }
        boolean[] row = marked[rowIndex];
        boolean id = true;
        for (int i = 0; i < SIZE; i++) {
            id = id && row[i];
        }
        return id;
    }

    private boolean isColumnAllTrue(int colIndex) {
        if (colIndex >= SIZE || colIndex < 0) {
            throw new IllegalArgumentException("Index out of bounds");
        }
        boolean id = true;
        for (int i = 0; i < SIZE; i++) {
            id = id && marked[i][colIndex];
        }
        return id;
    }

    public int getScore(int lastNumber) {
        if (this.finalScore != -1) { // used for part 2
            return this.finalScore;
        }
        int unmarkedSum = 0;
        for (int num : card.keySet()) {
            Coords pos = card.get(num);
            if (!marked[pos.getRow()][pos.getCol()]) {
                unmarkedSum += num;
            }
        }
        this.finalScore = unmarkedSum * lastNumber;
        return (unmarkedSum * lastNumber);
    }

    @Override
    public String toString() {
        StringBuilder s = new StringBuilder();
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                char mark = marked[i][j] ? 'X' : 'O';
                s.append(mark);
            }
            s.append("\n");
        }
        return s.toString();
    }

    private class Coords {
        int row;
        int col;

        Coords(int row, int col) {
            this.row = row;
            this.col = col;
        }

        public int getRow() {
            return row;
        }

        public int getCol() {
            return col;
        }

    }

    // For testing
    public static void main(String[] args) {
        ArrayList<Integer> numbers = new ArrayList<>();
        for (int i = 0; i < 25; i++) {
            numbers.add(i);
        }
        Bingo bingo = new Bingo(numbers);
        System.out.println(bingo);
        for (int i = 2; i < 25; i = i + 5) {
            bingo.mark(i);
        }
        System.out.println(bingo);
        System.out.println(bingo.isWinningBoard());
    }
}