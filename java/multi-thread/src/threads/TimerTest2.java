package threads;
import java.io.IOException;
import java.util.Timer;
import java.util.logging.Logger;



/**
 * @author brucesz
 *
 */
public class TimerTest2 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Logger logger = Logger.getLogger("timer-test2.log");
		Timer timer = new Timer();
		MyTask2 myTask1 = new MyTask2();
		MyTask2 myTask2 = new MyTask2();
		
		myTask2.setInfo("mytask2-2");
		timer.schedule(myTask1, 1000,2000);
		timer.scheduleAtFixedRate(myTask2, 2000, 3000);
		while(true) {
			try {
				byte[] info = new byte[1024];
				int len = System.in.read(info);
				String strInfo = new String(info,0,len,"GBK");
				if (strInfo.charAt(strInfo.length()-1)==' ') {
					strInfo = strInfo.substring(0, strInfo.length()-2);
				}
				if (strInfo.startsWith("Cancel-1")) {
					myTask1.cancel();
				} else if (strInfo.startsWith("Cancel-2")) {
					myTask2.cancel();
				} else if (strInfo.startsWith("Cancel-All")) {
					timer.cancel();
					break;
				} else {
					System.out.println("Cancel nothing!");
					
				}
			} catch (IOException e) {
				logger.info("error occured when getting from in");
			}
		}
	}
}
