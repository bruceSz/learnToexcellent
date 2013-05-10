package Template;

public class MethodBenchmark extends Benchmark {
	public void benchmark(){
		for(int i=0;i<Integer.MAX_VALUE;i++)
		{
			System.out.println("i="+i);
			
		}
	}
	public static void main(String[] args){
		Benchmark operation=new MethodBenchmark();
		long duration=operation.repeat(5);
		System.out.println("the operation took "+duration+"milliseconds");
	}

}
