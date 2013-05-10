package static_proxy;

public class StationProxy implements Station{
	Station sta=new TrainStationImpl();
	public void SellTickets(){
		sta.SellTickets();
	}
	public void otherOperate(){
		System.out.println("do some other things");
	}
	public void transport(){
		System.out.println("StationProxy can not transport");
	}

}
