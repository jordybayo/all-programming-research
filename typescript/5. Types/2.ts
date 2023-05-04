// union type, a variable of many type

let something  : (Array<any> | string);

something = [1, 2, 3];
something = "string";

let theLength = something.length;

if (typeof something  === "string"){
    something.substr(1, 3);
}

// or cast before doing anything
(something as string).substr(1, 3);
(<string>something).substr(1, 3);