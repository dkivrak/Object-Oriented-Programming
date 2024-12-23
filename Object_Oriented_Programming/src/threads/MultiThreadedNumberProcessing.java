package threads;

public class MultiThreadedNumberProcessing {

    public static void main(String[] args) throws InterruptedException {
    	Thread evenSumThread = new Thread(new Runnable() {
    		public void run() {
    	        int evenSum = 0;
    	        for (int i = 1; i <= 1000; i++) {
    	            if (i % 2 == 0) {
    	                evenSum += i;
    	            }
    	        }
    	        System.out.println("Even Sum: " + evenSum);
    	    }
    	});


        Thread oddSumThread = new Thread(() -> {
            int oddSum = 0;
            for (int i = 1; i <= 1000; i++) {
                if (i % 2 != 0) {
                    oddSum += i;
                }
            }
            System.out.println("Odd Sum: " + oddSum);
        });

        evenSumThread.start();
        oddSumThread.start();

        evenSumThread.join();
        oddSumThread.join();
    }
}
