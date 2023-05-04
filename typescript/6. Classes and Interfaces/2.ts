// 3. Inheritance

class Person{
    public name:string;
    private money: number = 10;

    constructor(name){
        this.name = name;
    }
}



class Employee extends Person{
    public salary : number = 0;

    constructor(name, salary){
        super(name);
        this.salary = salary;
    }
}

let emp1 = new Employee("Bill Gates", 100000);
emp1.name = "Satya";
console.log(' ${emp1.name} ${emp1.salary}') // result "satya 100000"