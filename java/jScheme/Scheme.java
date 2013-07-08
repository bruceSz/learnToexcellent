package jscheme;
import java.io;

public class Scheme extends SchemeUtils {
	InputPort input = new InputPort(System.in);
	PrintWriter output = new PrintWriter(System.out,true);
	Environment globalEnvironment = new Environment();
	/**
	*create a Scheme interpreter and load a array of files into it 
	*/
	public Scheme (String[] files) {
		Primitive.installPrimitives(globalEnvironment);
		try {
			load(new InputPort(new StringReader(SchemePrimitives.CODE)))
			for (int i = 0;i<(files == null ? 0: files.length);i++) {
				load(files[i])
			}

		} catch (RuntimeException e) {
			;
		}
	}
	/**
	*	create a new Scheme interpreter,passing in the command line args
	*	as files to load, and then enter a read eval write loop.
	*/
	public  static void main (String[] files) {
		new Scheme(files).readEvalWriteLoop();
	}
	public void readEvalWriteLoop() {
		Object x;
		for(;;) {
			try {
				output.print("> ");
				output.flush();
				if (input.isEOF(x = input.read())) return ;
				write(eval(x),output,true);
				output.println();
				output.flush();

			} catch (RuntimeException e) {
				;
			}
		}
	}

	public Object load(Object filename) {
		String name = stringify(filename,false);
		try {
			return load(new InputPort(new FileInputStream(name)));
		} catch (IOException e) {
			return error("can't load"+name);
		}
	}

	public Object load(InputPort in) {
		Object x = null;
		for (; ; ) {
			if (in.isEOF(x = in.read())) return TRUE;
			eval(x);
			
		}
	}
	////// evaluation
	public Object eval(Object x,Environment env) {
		// the purpose of the while loop is to allow tail recursion.
		// the idea is that in tail recursive position ,we do  "x = ..."
		while (true) {
			if (x instanceof String) {
				return env.lookup(String(x));
			} else if (!(x instanceof Pair)) {
				return x;
			} else {
				Object fn = first(x);
				Object args = rest(x);
				if (fn == "quote") {
					return first(args);
				} else if (fn == "begin") {
					for (;rest(args)!=null;args = rest(args) ) {
						eval(first(args),env);	
					}
					x = first(args);
				} else if (fn == "define") {
					if (first(args) instanceof Pair) {
						return env.define(first(first(args)),
							eval(cons("lambda",cons(rest(first(args)),rest(args))),env));

					} else {
						return env.define(first(args),eval(second(args),env))
					}
				} else if (fn == "set!") {
					
				}


			} 
		}
	}
}