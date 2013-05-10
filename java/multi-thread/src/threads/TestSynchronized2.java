package threads;

import java.util.Date;

public class TestSynchronized2 {

	private String value = "!";
	
	private class MyThread extends Thread {
		TestSynchronized2 ts2 ;
		
		public void setParent(TestSynchronized2 ts2) {
			this.ts2 = ts2;
		}
		public void run() {
			synchronized (ts2) {
				value+="thread";
			}
			
		}
	}
	public void loopPrint() {
		int i=0;
		synchronized (this) {
		while (true) {
			
				System.out.println(value);
				System.out.println(new Date());
				i++;
				if (i>=3) {
					break;
				}
			}
		}
	}
	public MyThread myThread  = new MyThread();
	public static void main(String[] args) {
		TestSynchronized2 ts = new TestSynchronized2();
		ts.myThread.setParent(ts);
		ts.myThread.start();
		ts.loopPrint();
	}
}
