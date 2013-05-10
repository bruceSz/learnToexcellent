package Template;

public abstract class Benchmark {
	
	public abstract void benchmark();
	
	public final long repeat (int count){
		long startTime;
		if(count<=0)
			return 0;
		else{
			startTime=System.currentTimeMillis();
		}
		for(int i=0;i<count;i++)
			benchmark();
		long stopTime=System.currentTimeMillis();
		return stopTime- startTime;
	}

}
