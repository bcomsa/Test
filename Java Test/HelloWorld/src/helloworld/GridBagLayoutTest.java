package helloworld;
import java.awt.*;
import java.awt.event.*;

public class GridBagLayoutTest extends Frame implements ActionListener, KeyListener{
	Label topLbl = new Label("Form Test"); 
	Label nameLbl = new Label("Name"); 
	Label listLbl = new Label("List"); 
	TextField txtBox = new TextField();
	Button addBtn = new Button("Add");
	Button cancelBtn = new Button("Cancel");
	TextArea txtArea = new TextArea(5,10);
	GridBagConstraints gbc = new GridBagConstraints();
	GridBagLayout gb = new GridBagLayout();
	public void keyPressed(KeyEvent k){
		
	}
	public void keyTyped(KeyEvent k){

	}
	public void keyReleased(KeyEvent k){
		if (k.getKeyCode() == 10)
			addInform();
		else if (k.getKeyCode() == 27)
			System.exit(0);
	}
	public GridBagLayoutTest(String title){
		super(title);
		this.addWindowListener(new WindowAdapter(){
			public void windowClosing(WindowEvent e){
				System.exit(0);
			}
		});
		txtBox.addKeyListener(this);
		addBtn.addActionListener(this);
		cancelBtn.addActionListener(this);
		setLayout(gb);
		gbc.fill = GridBagConstraints.HORIZONTAL;
		addComponent(topLbl,1,0,1,1);
		gbc.fill = GridBagConstraints.HORIZONTAL;
		addComponent(nameLbl,0,1,1,1);
		gbc.fill = GridBagConstraints.HORIZONTAL;
		addComponent(listLbl,0,3,1,1);
		gbc.fill = GridBagConstraints.HORIZONTAL;
		addComponent(txtBox,1,1,3,1);
		gbc.fill = GridBagConstraints.HORIZONTAL;
		addComponent(addBtn,1,2,1,1);
		gbc.fill = GridBagConstraints.HORIZONTAL;
		addComponent(cancelBtn,2,2,1,1);
		gbc.fill = GridBagConstraints.BOTH;
		addComponent(txtArea,1,3,3,3);
		
	}
	public void addComponent(Component comp, int col, int row, int nrow, int ncol){
		gbc.gridx = col;
		gbc.gridy = row;
		
		gbc.gridwidth = ncol;
		gbc.gridheight = ncol;
		gb.setConstraints(comp,gbc);
		add(comp);
	}
	public void actionPerformed(ActionEvent ae){
		if (ae.getSource()==addBtn){
			addInform();
		}
		if (ae.getSource()==cancelBtn){
			System.exit(0);
		}
	}
	public void addInform(){
		if (txtBox.getText().length() != 0){
			txtArea.setText(txtArea.getText() + txtBox.getText() + "\n");
			txtBox.setText("");
			txtBox.requestFocus();
		}
	}
	public static void main(String[] args){
		GridBagLayoutTest gblt = new GridBagLayoutTest("TEST");
		gblt.setSize(200,200);
		gblt.setVisible(true);
	}
}
