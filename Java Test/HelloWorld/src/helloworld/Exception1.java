package helloworld;
import java.awt.*;
import java.awt.event.*;

public class Exception1 extends Frame implements ActionListener{
	Label lbl1 = new Label("lbl1");
	Label lbl2 = new Label("lbl2");
	TextField txt1 = new TextField(10);
	TextField txt2 = new TextField(10);
	TextField txt3 = new TextField(10);

	Exception1(String title){
		super(title);
		setLayout(new GridLayout(3,3));
		txt1.addActionListener(this);
		add(lbl1);
		add(lbl2);
		add(txt1);
		add(txt2);
		add(txt3);
	}
	public void actionPerformed(ActionEvent ae){
		try{
			
			int num = Integer.parseInt(ae.getActionCommand());
			int result = num * num;
			txt2.setText(String.format("%s",result));
			txt3.setText("");
		}
		catch(NumberFormatException e){
			txt3.setText("Lỗi Rồi");
		}
			
	}

	public static void main(String[] args){
		Exception1 ex1 = new Exception1("Exception1");
		ex1.setSize(500,500);
		ex1.setVisible(true);
	}
}
