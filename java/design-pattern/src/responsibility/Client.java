package responsibility;

public class Client {
	public static void main(String[] args){
		Macro macro=new Macro();
		macro.bindSkill(new IceBloodFast());
		macro.bindSkill(new IceArrow());
		macro.castSkill();
		
	}

}
