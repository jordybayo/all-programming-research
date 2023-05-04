// 3. Inheritance
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var Person = /** @class */ (function () {
    function Person(name) {
        this.money = 10;
        this.name = name;
    }
    return Person;
}());
var Employee = /** @class */ (function (_super) {
    __extends(Employee, _super);
    function Employee(name, salary) {
        var _this = _super.call(this, name) || this;
        _this.salary = 0;
        _this.salary = salary;
        return _this;
    }
    return Employee;
}(Person));
var emp1 = new Employee("Bill Gates", 100000);
emp1.name = "Satya";
console.log(' ${emp1.name} ${emp1.salary}'); // result "satya 100000"
