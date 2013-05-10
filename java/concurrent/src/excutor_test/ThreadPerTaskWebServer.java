package excutor_test;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * @author brucesz
 *
 */
public class ThreadPerTaskWebServer {
	/**
	 * @param args
	 * @throws IOException
	 */
	public static void main (String[] args) throws IOException {
		ServerSocket socket = new ServerSocket(8000);
		while(true) {
			final Socket connection = socket.accept();
			Runnable task = new Runnable() {
				public void run() {
					handleRequest(connection);
				}
			};
			new Thread(task).start();
		}
	}
	/**
	 * @param connection
	 */
	public static void handleRequest(Socket connection) {
		return ;
	}
}
