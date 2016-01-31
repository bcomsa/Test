package helloworld;
import java.awt.*;
import java.awt.event.*;

public class FormTest extends Frame implements ActionListener{
	Label lbl1 = new Label("Form Test");
	Label lbl2 = new Label("1 nè");
	Label lbl3 = new Label("2 nè");
	Label lbl4 = new Label("3 nè nè");
	Button btn = new Button("Button nè");
	TextField tf1 = new TextField(15);
	TextField tf2 = new TextField(15);
	TextField tf3 = new TextField(15);
	GridBagLayout gb = new GridBagLayout();
	GridBagConstraints gbc = new GridBagConstraints();
	public FormTest(String title){
		super(title);
		this.addWindowListener(new WindowAdapter(){
			public void windowClosing(WindowEvent e){
				System.exit(0);
			}
		});
		setLayout(gb);
		tf3.setEnabled(false);
		btn.addActionListener(this);
		Panel btnLayout = new Panel(new FlowLayout(FlowLayout.CENTER));
		btnLayout.add(btn);
		Panel lbl2Layout = new Panel(new FlowLayout(FlowLayout.RIGHT));
		lbl2Layout.add(lbl2);
		Panel lbl3Layout = new Panel(new FlowLayout(FlowLayout.RIGHT));
		lbl3Layout.add(lbl3);
		Panel lbl4Layout = new Panel(new FlowLayout(FlowLayout.RIGHT));
		lbl4Layout.add(lbl4);
		
		gbc.fill = GridBagConstraints.HORIZONTAL;
		addComponent(lbl1,1,0,1,1);
		gbc.fill = GridBagConstraints.HORIZONTAL;
		addComponent(lbl2Layout,0,1,1,1);
		gbc.fill = GridBagConstraints.HORIZONTAL;
		addComponent(lbl3Layout,0,2,1,1);
		gbc.fill = GridBagConstraints.HORIZONTAL;
		addComponent(lbl4Layout,0,3,1,1);
		gbc.fill = GridBagConstraints.HORIZONTAL;
		addComponent(tf1,1,1,1,1);
		gbc.fill = GridBagConstraints.HORIZONTAL;
		addComponent(tf2,1,2,1,1);
		gbc.fill = GridBagConstraints.HORIZONTAL;
		addComponent(tf3,1,3,1,1);
		gbc.fill = GridBagConstraints.BOTH;
		addComponent(btnLayout,0,4,1,2);
		
	}
	public void addComponent(Component comp, int col, int row, int nrow, int ncol){
		gbc.gridx = col;
		gbc.gridy = row;
		
		gbc.gridwidth = ncol;
		gbc.gridheight = ncol;
		gb.setConstraints(comp,gbc);
		add(comp);
	}
	
	@Override
	public void actionPerformed(ActionEvent ae) {
		double rate = 2.34;
		try
		{
			String rateStr = tf2.getText();
			if(!rateStr.equals(""))
				rate = Double.parseDouble(rateStr);
			double basic = Double.parseDouble(tf1.getText());
			tf3.setText(String.valueOf(rate*basic));
		}
		catch (NumberFormatException e){
			tf3.setText("Nhập số đi bạn");
			return;
		}
	}
	
	public static void main(String[] args){
		FormTest gblt = new FormTest("TEST");
		gblt.setSize(250,200);
		gblt.setVisible(true);
	}
	
	
}
