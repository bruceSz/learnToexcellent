class Base
{
    String name = "base";

    public Base() {
	print();
	tell();
    }
    public void print() {
	System.out.println("Base print "+name);
    }
    public void tell() {
	System.out.println("Base tell"+name);
    }
}

public class Derived extends Base {
    String name = "derived";

    public Derived() {
	print();
	tell();
    } 
    public void print() {
	System.out.println("Derived print"+name);
    }
    public void tell() {
	System.out.println("Derived tell"+name);
    }
    public static void main(String[] args) {
	new Derived();
    }
}
