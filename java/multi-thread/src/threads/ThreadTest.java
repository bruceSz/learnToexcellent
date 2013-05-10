package threads;

/**
 * @author brucesz
 *
 */
public class ThreadTest extends Thread{
	public void run() {
		System.out.println("i am running");
		
	}
	/**
	 * @param times
	 */
	public void run(int times) {
		System.out.println("i am running (overload)");
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		ThreadTest tt = new ThreadTest();
		tt.start();
	}

}
