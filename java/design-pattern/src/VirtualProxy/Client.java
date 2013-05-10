package VirtualProxy;

public class Client {
	public static void main(String[] args){
		ideo ide=new ProxyProcessor();
		ide.compile("test.java");
		ide.run("test.class");
		ide.generateDocs("test.java");
	}

}
