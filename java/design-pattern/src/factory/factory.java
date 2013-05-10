package factory;
 interface IProduct{ 

	public void use(String msg);
	
	
}
 class Product1 implements IProduct{

	public void use(String msg){
		System.out.println("product1 use:"+msg);
	}

}

 class Product2 implements IProduct{
	
	public void use(String msg){
		System.out.println("product2 use:"+msg);
	}

}
class simplefactory {
	
	public static IProduct factory(String producttype){
		if(producttype.equals("1"))
			return new Product1();
		else if(producttype.equals("2"))
			return new Product2();
		return null;
	}
		

}
public class factory{
	public static void main(String[] args){
		IProduct product1=simplefactory.factory("1");
		product1.use("something");
		
		IProduct product2=simplefactory.factory("2");
		product2.use("something");
		
	}
	
}
