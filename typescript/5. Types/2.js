// union type, a variable of many type
var something;
something = [1, 2, 3];
something = "string";
var theLength = something.length;
if (typeof something === "string") {
    something.substr(1, 3);
}
// or cast before doing anything
something.substr(1, 3);
something.substr(1, 3);
