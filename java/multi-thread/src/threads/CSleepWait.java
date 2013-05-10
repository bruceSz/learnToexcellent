package threads;

import java.util.logging.Logger;

/**
 * @author brucesz
 *
 */
public class CSleepWait implements Runnable {
	int number = 10;
	static Logger logger = Logger.getLogger("sleepWait.log");
	/**
	 * @throws Exception
	 */
	public void firstMethod() throws Exception {
		synchronized (this) {
			number += 100;
			System.out.println(number);
		}
	}
	
	/**
	 * @throws Exception
	 */
	public void secondMethod() throws Exception {
		synchronized (this) {
			//Thread.sleep(2000);
			this.wait(2000);
			number*=200;
		}
	}
	public void run() {
		try {
			firstMethod();
			
		} catch (Exception e) {
			logger.info(e.getMessage());
		}
	}
	public static void main(String[] args) throws  Exception{
		CSleepWait tt = new CSleepWait();
		Thread thread = new Thread(tt);
		thread.start();
		tt.secondMethod();
		
	}

}
