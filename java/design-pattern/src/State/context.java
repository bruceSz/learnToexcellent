package State;

public class context {
	public static final int STATE_ONE=0;
	public static final int STATE_TWO=1;
	
	private state currentState=new ConcreteState1();
	public void request(){
		currentState.handle();
	}
	
	public void changeState(int state){
		switch(state){
		case STATE_ONE:
			currentState=new ConcreteState1();
			break;
		case STATE_TWO:
			currentState=new ConcreteState2();
			break;
		}
	}

}
