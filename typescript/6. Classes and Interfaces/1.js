//2. Classes
var MyFirstClass = /** @class */ (function () {
    function MyFirstClass() {
    }
    return MyFirstClass;
}());
var MySecondClass = /** @class */ (function () {
    function class_1() {
    }
    return class_1;
}());
var obj1 = new MyFirstClass();
var obj2 = new MySecondClass();
var Animal = /** @class */ (function () {
    function Animal(specie, weight) {
        this.specie = '';
        this._numberOfKinders = 2;
        this.specie = specie;
        this.weight = weight;
    }
    Animal.prototype.setNumberOfKindneys = function (value) {
        this._numberOfKinders = value;
    };
    Animal.prototype.getNumberOfKindneys = function () {
        return this._numberOfKinders;
    };
    Object.defineProperty(Animal.prototype, "numberOfKidneys", {
        set: function (value) {
            if (value < 0)
                return;
            this._numberOfKinders = value;
        },
        enumerable: false,
        configurable: true
    });
    return Animal;
}());
var koko = new Animal("Goorilla", 200);
// koko.specie = "Chimpanzee"; // cannot change valueoutside of constructor
var whatIsSpecie = koko.specie; //but we can read
var howManyKids = koko.getNumberOfKindneys();
koko.setNumberOfKindneys(3);
koko.weight = 250;
//static members
var MyMathHelper = /** @class */ (function () {
    function MyMathHelper() {
    }
    MyMathHelper.Add = function (x, y) {
        return x + y;
    };
    MyMathHelper.pi = 3.14159;
    return MyMathHelper;
}());
var myBankPassword = MyMathHelper.Add(1, MyMathHelper.pi);
