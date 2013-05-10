package threads;

public class TestUncaughtException extends ThreadGroup{
	public TestUncaughtException (String name) {
		super(name);
	}
	public void uncaughtException (Thread t,Throwable e) {
		System.out.println(e.getClass().getName()+"occurs in thread"+ t.getName());
		//e.printStackTrace();
	}
	
	public static void main(String[] args) {
		new Thread(new TestUncaughtException("testuncaughtException"),new Runnable () {
			public void run() {
				System.out.println("Test uncaughtException:1/0");
				int i = 1/0;
				System.out.println("Test uncaughtException ends");
			}
		}).start();
	}
}
