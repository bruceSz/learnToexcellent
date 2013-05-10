package VirtualProxy;

public class ProxyProcessor extends ideo {
	private RealProcessor realProcessor;
	
	public void generateDocs(String javaFile){
		if(realProcessor==null){
			realProcessor=new RealProcessor();
		}
		realProcessor.generateDocs(javaFile);
	}

}
