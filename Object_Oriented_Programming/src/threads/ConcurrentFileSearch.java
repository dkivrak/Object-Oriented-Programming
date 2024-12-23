package threads;
import java.io.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ConcurrentFileSearch {

    public static void main(String[] args) {
        String[] files = {"file1.txt", "file2.txt"};
        String keyword = "thread";

        ExecutorService executor = Executors.newFixedThreadPool(files.length);

        for (String file : files) {
            executor.submit(() -> searchInFile(file, keyword));
        }

        executor.shutdown();
    }

    private static void searchInFile(String fileName, String keyword) {
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line;
            int lineNumber = 0;
            while ((line = reader.readLine()) != null) {
                lineNumber++;
                if (line.contains(keyword)) {
                    System.out.println("Keyword \"" + keyword + "\" found in " + fileName + " at line " + lineNumber);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
