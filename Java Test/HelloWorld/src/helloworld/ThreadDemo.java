package helloworld;

public class ThreadDemo extends Thread{
	private int count;
	ThreadDemo(String name){
		super();
		setName(name);
	}
	void countUpdate(){
		while(true){
			try{
				Thread.sleep(500);
				count++;
				System.out.print("My Name Is : " + getName() + " : " + count + "\n");
			}
			catch (InterruptedException e){}
		}
	}
	public void run(){
		countUpdate();
	}
	public static void main(String[] args){
		ThreadDemo vip = new ThreadDemo("VIP");
		ThreadDemo tam = new ThreadDemo("TAM");
		vip.start();
		tam.start();
	}
}
