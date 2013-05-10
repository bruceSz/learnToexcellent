package adapter;

public class Adapter2 implements ITarget{
	private Animal animal;
	public Adapter2(Animal animal){
		this.animal=animal;
	}
	public void fly(){
		System.out.println("fly");
	}
	public void run(){
		this.animal.run();
	}

}
