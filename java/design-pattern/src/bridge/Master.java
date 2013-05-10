package bridge;

public class Master extends Student{
	public Master(){
		
	}
	public void doMethod(Method method){
		System.out.println("postgraduate");
		method.method();
	}

}
