package excutor_test;

import java.util.concurrent.Executor;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;

/**
 * @author brucesz
 *
 */
public class ExecutorTest {
	/**
	 * @param args
	 */
	public static void main (String[] args) {
		Executor exec = Executors.newFixedThreadPool(20);
		Executor execCachedPool = Executors.newCachedThreadPool();
		Executor singleTaskPool = Executors.newSingleThreadExecutor();
		ScheduledExecutorService shceduledPool = Executors.newScheduledThreadPool(20);
		
		singleTaskPool.execute(new Runnable() {
			public void run() {
				System.out.println("this is a task!");
			}
			
		});
		//exec.equals(obj);
	}
}
