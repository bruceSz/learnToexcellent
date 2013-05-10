package VirtualProxy;

public abstract class ideo {
	private Compiler cmp;
	private Runtime  rtime;
	
	public void compile(String javaFile){ 
		this.cmp.compile(javaFile);
	}
	public void run(String classFile){
		rtime.run(classFile);
	}
	public abstract void generateDocs(String javaFile);
	public ideo(){
		cmp=new Compiler();
		rtime=new Runtime();
	}

}
