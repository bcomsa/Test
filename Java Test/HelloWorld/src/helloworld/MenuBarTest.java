package helloworld;

import java.awt.*;
import java.awt.event.*;
class MenuBarTest extends Frame implements ActionListener{
	public MenuBarTest(){
		super();
		setTitle("Menu Example");
		setSize(300,200);
		
		MenuBar mbar=new MenuBar();
		setMenuBar(mbar);
		Menu fileMenu=new Menu("File");
		mbar.add(fileMenu);
		fileMenu.addActionListener(this);
		MenuItem openItem=new MenuItem("Open");
		fileMenu.add(openItem);
		MenuItem editItem=new MenuItem("Edit");
		fileMenu.add(editItem);
		MenuItem exitItem=new MenuItem("Exit");
		fileMenu.add(exitItem);
		
		Menu helpMenu=new Menu("Help");
		mbar.add(helpMenu);
		helpMenu.addActionListener(this);
		MenuItem documentationItem=new MenuItem("Documentation");
		helpMenu.add(documentationItem);
		MenuItem aboutItem=new MenuItem("About");
		helpMenu.add(aboutItem);
		MenuItem licenseItem=new MenuItem("License");
		helpMenu.add(licenseItem);
		helpMenu.addSeparator();
		CheckboxMenuItem contentItem=new CheckboxMenuItem("View Content");
		helpMenu.add(contentItem);
		CheckboxMenuItem changeLogItem=new CheckboxMenuItem("Changelog");
		helpMenu.add(changeLogItem);
		Menu versionMenu=new Menu("Version");
		helpMenu.add(versionMenu);
		MenuItem verItem_15=new MenuItem("Version 1.5");
		versionMenu.add(verItem_15);
		MenuItem verItem_16=new MenuItem("Version 1.6");
		versionMenu.add(verItem_16);
		versionMenu.addActionListener(this);
		
	}
	public void actionPerformed(ActionEvent ae){
		if (ae.getActionCommand().equals("Exit")){
			System.exit(0);
		}
		else{
			System.out.print(String.valueOf(ae.getActionCommand()) + " Menu\n");
		}
	}

	public static void main(String[] args)
	{
		MenuBarTest frame=new MenuBarTest();
		frame.setVisible(true);
}
}