package threads;

/**
 * @author brucesz
 *
 */
public class RunnableTest implements Runnable{
	public void run() {
		System.out.println("i'm running!");
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		RunnableTest rt = new RunnableTest();
		Thread t = new Thread(rt);
		t.start();
	}

}
