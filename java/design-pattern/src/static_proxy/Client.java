package static_proxy;

public class Client {
	public static void main(String[] args){
		Station station=new StationProxy();
		station.SellTickets();
	}

}
