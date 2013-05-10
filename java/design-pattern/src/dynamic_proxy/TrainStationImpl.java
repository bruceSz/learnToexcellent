package dynamic_proxy;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

interface station{
	void SellTickets();
}
public class TrainStationImpl implements station{
	public void SellTickets(){
		System.out.print("TrainStation sell tickets");
	}

}
