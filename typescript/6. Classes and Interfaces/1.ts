//2. Classes
class MyFirstClass{
    property: "value";
}

let MySecondClass = class{
    property: "value";
}

var obj1 = new MyFirstClass();
var obj2 = new MySecondClass();

class Animal{
    readonly specie: string = '';
    private _numberOfKinders = 2;
    public weight: number;

    constructor(specie, weight){
        this.specie = specie;
        this.weight = weight;
    }

    public setNumberOfKindneys(value){
        this._numberOfKinders = value;
    }

    public getNumberOfKindneys(){
        return this._numberOfKinders;
    }

    set numberOfKidneys(value){
        if (value < 0) return;
        this._numberOfKinders = value;
    }
}

let koko = new Animal("Goorilla", 200);
// koko.specie = "Chimpanzee"; // cannot change valueoutside of constructor
let whatIsSpecie = koko.specie; //but we can read
var howManyKids = koko.getNumberOfKindneys();
koko.setNumberOfKindneys(3);
koko.weight = 250;


//static members
class MyMathHelper{
    public static pi : number = 3.14159;
    public static Add(x:number, y: number):number{
        return x+y;
    }
}

let myBankPassword = MyMathHelper.Add(1, MyMathHelper.pi);