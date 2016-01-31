package helloworld;

public class Laborer extends Employee{
	public int hrsworked;
	Laborer(String _name, double _salary, int _hrsworked){
		super(_name,_salary);
		hrsworked = _hrsworked;
	}
	protected double calculatepay(){
		double commission;
		if (hrsworked > 50){
			commission = 15;
		}
		else commission = 8;
		double total_pay = salary + salary*commission/100;
		return total_pay;
	}
	protected void show(){
		System.out.print("\n\nLaborer\n");
		System.out.print("\nName : "+name);
		System.out.print("\nSalary : "+salary);
		System.out.print("\nHrsworked : " + hrsworked);
	}
}
