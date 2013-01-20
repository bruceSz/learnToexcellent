package threads;

public class TestSynchronized {

	public static void main (String[] args) {
		Runnable rb = new Runnable() {
			byte[] bt = new byte[0];
			public void run() {
				synchronized(bt) {
					for (int i=0;i<5;i++) {
						try {
							Thread.sleep(50);
							
						} catch (InterruptedException e) {
							e.printStackTrace();
						}
						bt = new byte[0];
						System.out.println(Thread.currentThread().getName());
						
					}
				}
			}
		};
		for (int i=0;i<5;i++) {
			{
				try {
					Thread.sleep(100);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
				new Thread(rb).start();
			}
		}
	}
}
