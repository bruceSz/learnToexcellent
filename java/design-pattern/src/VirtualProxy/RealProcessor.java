package VirtualProxy;

public class RealProcessor extends ideo{
	javaDocs jdoc;
	public RealProcessor(){
		super();
		jdoc=new javaDocs();
	}
	public void generateDocs(String javaFile){
		jdoc.generateDocs(javaFile);
	}

}
