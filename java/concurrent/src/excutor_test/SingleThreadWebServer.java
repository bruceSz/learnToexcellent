package excutor_test;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * @author brucesz
 *
 */
public class SingleThreadWebServer {
	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main (String[] args) throws IOException {
		ServerSocket socket = new ServerSocket(8000);
		while(true) {
			Socket connection = socket.accept();
			handleRequest(connection);
		}
				
	}
	
	private static void handleRequest(Socket connection) {
		// ToDo:
		return;
	}
}
