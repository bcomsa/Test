package helloworld;
import java.util.*;
import java.awt.*;
import java.awt.event.*;
public class PressButtonGUI extends Frame implements ActionListener{
	int count = 1;
	TextField tf = new TextField(10);
	ArrayList<Button> btn_list = new ArrayList<Button>();
	public PressButtonGUI(String title, int numOfButton) {
		super(title);
		setLayout(new FlowLayout());
		while (count < numOfButton){
			Button btn = new Button(String.valueOf(count));
			btn_list.add(btn);
			add(btn);
			btn.addActionListener(this);
			count++;
		}
		add(tf);	
	}
	
	public void actionPerformed(ActionEvent ae){
		tf.setText(ae.getActionCommand());
	}
	public static void main(String[] args){
		PressButtonGUI test = new PressButtonGUI("VIPTAM", 50);
		test.setSize(500,200);
		test.setVisible(true);
	}
}
