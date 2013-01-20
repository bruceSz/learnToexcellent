package threads;

public class TestThreadGroup {

	public static void main (String[] args) {
		ThreadGroup tg = new ThreadGroup("tg-hello");
		new Thread(tg,new Runnable() {
			public void run() {
				
			}
		});
		ThreadGroup tg2 = new ThreadGroup("tg1-hello");
		tg.getParent().list();
	}
}
