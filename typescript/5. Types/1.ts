////2. Basic types, part 1 

// number
let n : number = 17;
n = 0x11; //hex
n = 0b10001//binary
n = 0o21 //octal

// boolean
let b : boolean = true;
b = false;
b = !!(n); //n == 0 ? false : true
b = !!(null); // false


//string
let s : string = "Hello Buddy";
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
let a:any;
a = 2;
a = "string";
a = false;


//void
let array :number [] = [1,2,3]

// array 
let nArray:number[] = [1, 2, 3];
let sArray:Array<string> = ['hello', 'hey', 'hello'];
let aArray:any[] = [1, 'go'];

// tuple
let t:[string, number, number] = ["Malcom tur", 63, 20145];
t[1] = 62 ;

// enum
enum Color {Red, Green, Blue}
let e:Color = Color.Green;


// object
let o: object = {
    name : "go1"
};

let o2: {name:string} = {
    name : "go2"
};