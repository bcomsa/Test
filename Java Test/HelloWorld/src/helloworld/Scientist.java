package helloworld;

public class Scientist extends Employee{
	protected int publication;
	Scientist(String _name, double _salary, int _publication){
		super(_name, _salary);
		publication = _publication;
	}
	protected double calculatepay(){
		double commission;
		if (publication > 25){
			commission = 20;
		}
		else commission = 10;
		double total_pay = salary + salary*commission/100;
		return total_pay;
	}
	protected void show(){
		System.out.print("\n\nScientist\n");
		System.out.print("\nName : "+name);
		System.out.print("\nSalary : "+salary);
		System.out.print("\nPublication : " + publication);
	}
}
