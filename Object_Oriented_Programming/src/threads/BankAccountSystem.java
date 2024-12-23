package threads;

public class BankAccountSystem {

    public static class BankAccount {
        private int balance = 0;

        public synchronized void deposit(int amount) {
            balance += amount;
            System.out.println("Deposited: " + amount + ", Balance: " + balance);
        }

        public synchronized void withdraw(int amount) {
            if (balance >= amount) {
                balance -= amount;
                System.out.println("Withdrawn: " + amount + ", Balance: " + balance);
            } else {
                System.out.println("You do not have enough amount ");
            }
        }

        public synchronized int getBalance() {
            return balance;
        }
    }

    public static void main(String[] args) {
        BankAccount account = new BankAccount();

        Thread t1 = new Thread(new Runnable(){
        	public void run() {
            for (int i = 0; i < 10; i++) {
                account.deposit(100);
            }
        }});

        Thread t2 = new Thread(new Runnable(){
        	public void run() {
            for (int i = 0; i < 5; i++) {
                account.withdraw(50);
            }
        }});

        t1.start();
        t2.start();
    }
}
