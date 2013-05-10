package threads;

public class TestUncatchedExceptionHandler {
	public static void main (String[] args) {
		Thread.currentThread().setUncaughtExceptionHandler(new Thread.UncaughtExceptionHandler() {
			
			@Override
			public void uncaughtException(Thread t, Throwable e) {
				System.out.println(e.getClass().getName()+"occurs in thread"+ t.getName());
				
				
			}
		});
		int i = 1/0;
	}
}
