package helloworld;

public class Manager extends Employee {
	protected double business_amount;
	Manager(String _name , double _salary , double _b_a){
		super(_name,_salary);
		business_amount = _b_a;
	}
	protected double calculatepay(){
		double commission;
		if (business_amount > 50000){
			commission = 10;
		}
		else commission = 5;
		double total_pay = salary + salary*commission/100;
		return total_pay;
	}
	protected void show(){
		System.out.print("\n\nManager\n");
		System.out.print("\nName : "+name);
		System.out.print("\nSalary : "+salary);
		System.out.print("\nBusiness Amount : " + business_amount);
		System.out.print("\nTotal Pay : " + calculatepay());
	}
}
