////2. Basic types, part 1 
// number
var n = 17;
n = 0x11; //hex
n = 17; //binary
n = 17; //octal
// boolean
var b = true;
b = false;
b = !!(n); //n == 0 ? false : true
b = !!(null); // false
//string
var s = "Hello Buddy";
s = "Hello buddy";
s = 'my number is ${n}'; //My number is 17
//undefined and null
n = undefined;
b = undefined;
s = undefined; //can be assign to all type of variables
n = null;
b = null;
s = null;
// any
var a;
a = 2;
a = "string";
a = false;
//void
var array = [1, 2, 3];
// array 
var nArray = [1, 2, 3];
var sArray = ['hello', 'hey', 'hello'];
var aArray = [1, 'go'];
// tuple
var t = ["Malcom tur", 63, 20145];
t[1] = 62;
// enum
var Color;
(function (Color) {
    Color[Color["Red"] = 0] = "Red";
    Color[Color["Green"] = 1] = "Green";
    Color[Color["Blue"] = 2] = "Blue";
})(Color || (Color = {}));
var e = Color.Green;
// object
var o = {
    name: "go1"
};
var o2 = {
    name: "go2"
};
