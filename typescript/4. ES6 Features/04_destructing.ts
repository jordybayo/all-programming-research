let $:any;
let test_destructing = function(){
    let theArray = [1, 2, 3];
    let [a, b, c] = theArray;

    console.log('a : ${a}');
    console.log('a : ${b}');
    console.log('a : ${c}');

    let x = 100;
    let y = 200;
    [x, y] = [y, x];
    console.log('x : ${x}');
    console.log('x : ${y}');

    let person = {name: 'Obama', age: 38}
    let {name: v1, age:v2} = person;
    console.log('v1 : ${v1}');
    console.log('v1 : ${v2}');
}