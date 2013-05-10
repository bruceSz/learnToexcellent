package bridge;

public class Graduate extends Student {
	public Graduate(){
		
	}
	public void doMethod(Method method){
		System.out.println("undergraduate");
		method.method();
	}

}
