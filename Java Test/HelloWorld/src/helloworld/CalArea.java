package helloworld;

public class CalArea {

	public static void main(String[] args){
		Laborer a = new Laborer("viptam",99999,100);
		a.show();
		Manager b = new Manager("viptam",99999,100);
		b.show();
		Scientist c = new Scientist("viptam",99999,100);
		c.show();
	}
}
