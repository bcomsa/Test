package helloworld;

import java.awt.*;
import java.awt.event.*;

public class MousePos extends Frame implements MouseListener, ActionListener{
	TextField tf1 = new TextField(10);
	TextField tf2 = new TextField(10);
	Button btn = new Button("Reset");
	MousePos(String title){
		super(title);
		setLayout(new FlowLayout());
		this.addMouseListener(this);
		btn.addActionListener(this);
		add(tf1);
		add(tf2);
		add(btn);
	}
	
	public void mouseEntered(MouseEvent e) {
	}
	public void mouseExited(MouseEvent e) {
	}
	public void mousePressed(MouseEvent e) {
		tf1.setText(String.valueOf(e.getX()));
		tf2.setText(String.valueOf(e.getY()));
		
	}
	public void mouseReleased(MouseEvent e) {
		
	}
	public void actionPerformed(ActionEvent ae){
		tf1.setText("0");
		tf2.setText("0");
	}
	public static void main(String[] args){
		MousePos test = new MousePos("Test Mouse Position");
		test.setSize(300, 300);
		test.setVisible(true);
	}

	@Override
	public void mouseClicked(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}
}
