package threads;

/**
 * @author brucesz
 *
 */
public class MyTask2 extends java.util.TimerTask{
	
	private String info = "haha";
	 public void run() {
		 System.out.println(info);
	 }
	 
	 /**
	 * @return info.
	 */
	public String getInfo () {
		 return info;
	 }
	 /**
	 * @param info
	 */
	public void setInfo (String info) {
		 this.info = info;
	 }
	 
}
