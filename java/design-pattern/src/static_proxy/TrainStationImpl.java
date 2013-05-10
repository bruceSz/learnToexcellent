package static_proxy;


interface Station {
	void SellTickets();
	void transport();
}
public class TrainStationImpl implements Station {
	public void SellTickets(){
		System.out.println("TrainStation sell tickets");
	}
	public void transport(){
		System.out.println("TrainStation transport passenger");
	}

}
