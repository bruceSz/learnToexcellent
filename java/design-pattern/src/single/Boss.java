package single;

public class Boss {
	private static Boss boss;
	
	private Boss(){
		
	}
	public static Boss getInstance(){
		if(boss==null){
			boss=new Boss();
		}
		return boss;
	}
	public void speak(){
		System.out.println("i am estany , my No is 222"+boss.hashCode());
	}

}
