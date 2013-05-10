package dynamic_proxy;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Proxy;

public class Client {
	public static void main(String[] args){
		station stationImpl=new TrainStationImpl();
		InvocationHandler handler=new InvocationHandlerImpl(stationImpl);
		ClassLoader loader =handler.getClass().getClassLoader();
		Class<?>[] interfaces=stationImpl.getClass().getInterfaces();
		station station=(station)Proxy.newProxyInstance(loader, interfaces, handler);
		station.SellTickets();
		
	}

}
