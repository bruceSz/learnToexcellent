package threads;

import java.io.IOException;
import java.util.Timer;
import java.util.logging.Logger;

/**
 * @author brucesz
 *
 */
public class TimerTest {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Timer timer = new Timer();
		Logger logger = Logger.getLogger("timer.log");
		timer.schedule(new MyTask(),1000,2000);
		while (true) {
			try {
				int ch = System.in.read();
				if (ch-'c'==0) {
					System.out.println("now end My Task!");
					timer.cancel();
					break;
				}
			} catch (IOException e) {
				logger.info("error occured when get input from in");
			}
		}
	}
}
