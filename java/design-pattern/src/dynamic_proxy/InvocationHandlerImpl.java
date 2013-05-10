package dynamic_proxy;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;

public class InvocationHandlerImpl implements InvocationHandler{
	Object proxyobj;
	public InvocationHandlerImpl(Object object){
		this.proxyobj=object;
	}
	public Object invoke(Object obj,Method method,Object[] args)
	throws Throwable{
		System.out.print("start doing ...");
		method.invoke(proxyobj, args);
		System.out.println("stop doing ...");
		return null;
	}

}
