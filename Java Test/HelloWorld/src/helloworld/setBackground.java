package helloworld;
import java.awt.*;
import java.awt.event.*;
class setBackground extends Frame implements ActionListener{
	Label lab=new Label("Enter a number");
	TextField tf1=new TextField(5);
	TextField tf2=new TextField(5);
	Button btnResult=new Button("Double is");
	Button ext=new Button("exit");
	public setBackground(String title){
		super(title);
		setLayout(new FlowLayout());
		btnResult.addActionListener(this);

		ext.addActionListener(this);
		add(lab);
		add(tf1);
		add(btnResult);
		add(tf2);
		add(ext);
	}
public void actionPerformed(ActionEvent ae){
	if (ae.getSource()==btnResult){
		int num=Integer.parseInt(tf1.getText())*2;
		tf2.setText(String.valueOf(num));
	}
	if (ae.getSource()==ext){
		System.exit(0);
	}
}
public static void main(String args[]){
	setBackground t=new setBackground("Event handling");
	t.setSize(300,200);
	t.show();
}
}
