package single;

public class Client {
	public static void main(String[] args){
		Boss boss1=Boss.getInstance();
		Boss boss2=Boss.getInstance();
		
		boss1.speak();
		boss2.speak();
	}

}
