package helloworld;
import java.awt.*;
import java.awt.event.*;
import javax.swing.JOptionPane;
public class BorderLayoutTest extends Frame implements ActionListener{
	Label lbl1 = new Label("BorderLayout Test");
	Label lbl2 = new Label("Source");
	Label lbl3 = new Label("Destination");
	Button btn1 = new Button("Copy");
	Button btn2 = new Button("Cancel");
	TextField tf1 = new TextField();
	TextField tf2 = new TextField();
	BorderLayoutTest(String title){
		super(title);
		setLayout(new BorderLayout());
		Panel pn1 = new Panel(new GridLayout(2,2));
		Panel pn2 = new Panel(new GridLayout(1,2));
		btn1.addActionListener(this);
		btn2.addActionListener(this);
		pn1.add(lbl2);
		pn1.add(tf1);
		pn1.add(lbl3);
		pn1.add(tf2);
		pn2.add(btn1);
		pn2.add(btn2);
		add(lbl1, BorderLayout.NORTH);
		add(pn1, BorderLayout.CENTER);
		add(pn2, BorderLayout.SOUTH);
	}
	public void actionPerformed(ActionEvent ae){
		if (ae.getSource() == btn1){
			if(tf1.getText().equals("")){
				JOptionPane.showMessageDialog(this, "Không Được Để Trống", "Báo Lỗi", JOptionPane.WARNING_MESSAGE);
			}
			else
				tf2.setText(tf1.getText());
		}
		if (ae.getSource() == btn2){
			System.exit(0);
		}
	}
	public static void main(String[] args){
		BorderLayoutTest test = new BorderLayoutTest("Copy");
		test.setSize(300,120);
		test.setVisible(true);
	}
}
