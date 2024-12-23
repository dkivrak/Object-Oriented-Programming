# Java Multi-threading Project

This project demonstrates various multi-threading concepts in Java by solving six practical problems. Each problem is implemented as a separate class with its own `main` method, making it modular and easy to run independently.

---

## **1. Multi-threaded Number Processing**

### Description
This program creates two threads:
- The first thread calculates the sum of all even numbers from 1 to 1000.
- The second thread calculates the sum of all odd numbers from 1 to 1000.
The results are printed in the `main` thread.

### How to Run
1. Open the `MultiThreadedNumberProcessing` class.
2. Run the program.
3. Observe the sums of even and odd numbers printed in the console.

### Sample Output
```text
Even Sum: 250500
Odd Sum: 250000


# Multi-threaded Number Processing

## Description
This program creates two threads:
- The first thread calculates the sum of all even numbers from 1 to 1000.
- The second thread calculates the sum of all odd numbers from 1 to 1000.
The results are printed in the `main` thread.

## How to Run
1. Open the `MultiThreadedNumberProcessing` class.
2. Run the program.
3. Observe the sums of even and odd numbers printed in the console.

## Sample Output
Thread 1: 1
Thread 2: 2
Thread 1: 3
Thread 2: 4
...
Thread 2: 20


# Matrix Multiplication with Threads

## Description
This program performs matrix multiplication using multiple threads. Each thread calculates one element in the result matrix.

## How to Run
1. Open the `MatrixMultiplication` class.
2. Modify the input matrices (`matrixA` and `matrixB`) if desired.
3. Run the program.
4. Observe the result matrix printed in the console.

## Sample Output
Matrix A:
3 5
5 4

Matrix B:
2 6
1 9

Result:
11 63 
14 66 

# Thread-safe Counter

## Description
This program simulates three threads incrementing a shared counter. The counter is protected using a `ReentrantLock` to ensure thread safety.

## How to Run
1. Open the `ThreadSafeCounter` class.
2. Run the program.
3. Observe the final counter value printed in the console.

## Sample Output
Final Counter Value: 3000

# Concurrent File Search

## Description
This program searches for a keyword in multiple text files concurrently. Each thread is responsible for searching in one file.

## How to Run
1. Open the `ConcurrentFileSearch` class.
2. Add the text files to the project directory.
3. Specify the file names and the keyword to search in the code.
4. Run the program.
5. Observe the results in the console.

## Sample Output
Keyword "thread" found in file1.txt at lines: 2
Keyword "thread" found in file2.txt at lines: 3

# Thread-safe Bank Account System

## Description
This program simulates a bank account accessed by multiple threads. Each thread represents a customer depositing or withdrawing money. The account operations are synchronized to prevent race conditions.

## How to Run
1. Open the `BankAccountSystem` class.
2. Run the program.
3. Observe the deposits, withdrawals, and the final account balance in the console.

## Sample Output
Deposited: 100, Balance: 100
Withdrawn: 50, Balance: 50
Deposited: 100, Balance: 150
...
Final Balance: 500


## General Notes
Each problem is implemented in a separate class with its own main method.
The project requires Java 8 or higher.
All classes can be executed independently.


## How to Setup
Clone or download the project files.
Open the project in your preferred Java IDE 
Build the project to ensure all dependencies are resolved.
Run the desired class to see the results.

## Contribution
Contributions are welcome! Feel free to fork the repository and submit a pull request for any enhancements or bug fixes.