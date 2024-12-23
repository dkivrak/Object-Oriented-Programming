package threads;

public class MatrixMultiplication {

    public static void main(String[] args) {
        int[][] matrixA = {{3, 5}, {5, 4}};
        int[][] matrixB = {{2, 6}, {1, 9}};
        int[][] result = new int[matrixA.length][matrixB.length];

        Thread[][] threads = new Thread[matrixA.length][matrixB.length];
        for (int i = 0; i < matrixA.length; i++) {
            for (int j = 0; j < matrixB[0].length; j++) {
                final int row = i;
                final int col = j;

                threads[i][j] = new Thread(new Runnable() {
                    public void run() {
                        for (int k = 0; k < matrixA[0].length; k++) {
                            result[row][col] += matrixA[row][k] * matrixB[k][col];
                        }
                    }
                });

                threads[i][j].start();
            }
        }

        for (int i = 0; i < threads.length; i++) {
            for (int j = 0; j < threads[i].length; j++) {
                try {
                    threads[i][j].join();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }

        for (int[] row : result) {
            for (int val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
    }
}
