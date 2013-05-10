package bridge;

public class Client {
	public static void main(String[] args){
		Student s=new Master();
		s.doMethod(new Method1());
	}

}
