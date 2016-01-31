package helloworld;
import java.io.*;
import java.util.regex.*;
import java.awt.*;
public class TestFile {
	
	public static void main(String[] args) throws IOException{
		System.out.print("Test\n");
		FileWriter stream = new FileWriter("/home/vuquangtam/Desktop/file.txt");
		PrintWriter p = new PrintWriter(stream);
		p.println("okey men");
		p.println("okey men");
		p.close();
		RandomAccessFile fileRead = new RandomAccessFile("/home/vuquangtam/Desktop/file.txt", "r");
		while(true){
			String readFromFile = fileRead.readLine();
			if (readFromFile == null){
				fileRead.close();
				break;
			}
			System.out.println(readFromFile);
		}
		String a = "abc@123";
		System.out.println(a.matches("^[a-zA-Z]*@123"));
	}
}
