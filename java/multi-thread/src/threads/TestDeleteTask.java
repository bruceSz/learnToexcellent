package threads;

import java.util.Timer;

public class TestDeleteTask {
	
	public class TimerTask extends java.util.TimerTask {
		
		Timer myTimer = null;
		public void run() {
			System.out.println("thread is running!");
		}
	}

	/*public void finalize() {
		timer.cancel();
	}*/
	private TimerTask tt = null;
	
	public void createTimerTask() {
		Timer timer = new Timer();
		tt = new TimerTask();
		tt.myTimer = timer;
		timer.scheduleAtFixedRate(tt, 1, 2);
	}
	public void clearThread() {
		tt.myTimer.cancel();
	}
	public static void main(String[] args) {
		
		TestDeleteTask tdt = new TestDeleteTask();
		tdt.createTimerTask();
		try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		tdt.clearThread();
		//tdt=null;
		//tdt.clearThread();
		System.gc();
		
		//tdt.timer=null;
		//tdt.timer.cancel();
		
	}
}
