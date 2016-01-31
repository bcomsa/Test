package helloworld;
import java.awt.*;
public class checkbox extends Frame implements ActionListener{
	Label lbl = new Label("viptam");
	Checkbox chbox1 = new Checkbox("tamver1");
	Checkbox chbox2 = new Checkbox("tamver2");
	Checkbox chbox3 = new Checkbox("tamver3");
	Checkbox chbox4 = new Checkbox("tamver4");
	checkbox(String title){
		super(title);
		setLayout(new GridLayout(6,1));
		chbox1.addItemListener();
		add(lbl );
		add(chbox1);
		add(chbox2);
		add(chbox3);
		add(chbox4);
		}
	checkboxListen(new event.ActionListener()){
		
	}
	
	public static void main(String[] args){
		checkbox a = new checkbox("vip");
		a.setSize(300,200);
		a.show();
	}
}
