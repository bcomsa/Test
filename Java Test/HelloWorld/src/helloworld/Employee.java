package helloworld;

public abstract class Employee {
	protected String name;
	protected double salary;
	protected abstract double calculatepay();
	Employee(String _name, double _salary){
		name = _name;
		salary = _salary;
	}
}
