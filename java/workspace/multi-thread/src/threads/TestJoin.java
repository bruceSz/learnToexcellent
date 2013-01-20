package threads;

public class TestJoin implements Runnable{
	int count = 0;
	public static void main (String[] args) {
		TestJoin tj = new TestJoin();
		for (int i=0;i<5;i++) {
			new Thread(tj,"hello"+i).start();
		}
		
	}
	
	@Override
	public void run(){
		try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
		if (count == 0) {
			count ++;
			Thread thread1 = new Thread(this,"helloSon");
			thread1.start();
			try {
				thread1.join(3000);
			} catch (InterruptedException e ) {
				e.printStackTrace();
			}
		}
		System.out.println(Thread.currentThread().getName());
		while (true) {
			System.out.println("loop");
		}
	}
	
}
