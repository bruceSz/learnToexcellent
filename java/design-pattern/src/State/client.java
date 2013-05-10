package State;

public class client {
	public static void main(String[] args){
		context ctx=new context();
		ctx.request();
		ctx.changeState(context.STATE_TWO);
		ctx.request();
	}

}
