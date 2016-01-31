package helloworld;

import java.awt.*;
import java.awt.event.*;
public class setBackgroundTrueVersion extends Frame implements ItemListener{
	Choice color = new Choice();
	setBackgroundTrueVersion(String title){
		super(title);
		setLayout(new FlowLayout());
		color.addItemListener(this);
		color.addItem("White");
		color.addItem("Black");
		color.addItem("Blue");
		color.addItem("Green");
		add(color);
		this.addWindowListener(new WindowAdapter(){
			public void windowClosing(WindowEvent e){
				System.exit(0);
			}
		});
	}
	public void itemStateChanged(ItemEvent e){
		int index = color.getSelectedIndex();
		if (index == 0) this.setBackground(Color.white);
		else if (index == 1) this.setBackground(Color.black);
		else if (index == 2) this.setBackground(Color.blue);
		else if (index == 3) this.setBackground(Color.green);
	}
	public static void main(String args[]){
		setBackgroundTrueVersion t=new setBackgroundTrueVersion("Event handling");
		t.setSize(300,200);
		t.setVisible(true);
	}
}
