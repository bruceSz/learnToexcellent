package gc;

/**
 * @author brucesz
 *
 */
public class ObjectReborn{
	/**
	 * @param args
	 * @throws Exception
	 */
	public static void main (String[] args) throws Exception {
		A a  = new A(new B("allen",20));
		a = null;
		System.gc();
		Thread.sleep(5000);
		System.out.println(C.a.b);
	}
}

class C {

	static A a;
}
class A  {
	B b;
	public A (B b) {
		this.b = b;
	}
	public void finalize() {
		System.out.println("A finalized");
			C.a = this;
	}
}

class B {
	String name;
	int age;
	public B(String name,int age) {
		this.name = name;
		this.age = age;
	}
	public void finalize() {
		System.out.println("B finalize");
	}
	
	public String toString() {
		return name + " is " + age;
	}
}



