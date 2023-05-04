var __spreadArrays = (this && this.__spreadArrays) || function () {
    for (var s = 0, i = 0, il = arguments.length; i < il; i++) s += arguments[i].length;
    for (var r = Array(s), k = 0, i = 0; i < il; i++)
        for (var a = arguments[i], j = 0, jl = a.length; j < jl; j++, k++)
            r[k] = a[j];
    return r;
};
var test_spread_operator = function () {
    var array1 = [1, 2, 3];
    var array2 = __spreadArrays([1], array1, [5]);
    console.log("array2");
    console.log(array2);
    var copyOfArray1 = __spreadArrays(array1);
    console.log(":copy of array1");
    console.log(copyOfArray1);
};
var sum = function (x) {
    var values = [];
    for (var _i = 1; _i < arguments.length; _i++) {
        values[_i - 1] = arguments[_i];
    }
    var result = x;
    for (var _a = 0, values_1 = values; _a < values_1.length; _a++) {
        var value = values_1[_a];
        result += value;
    }
    return result;
};
console.log("sum 1 to 3");
console.log(sum(1, 2, 3));
console.log("sum 1 to 4");
console.log(sum(1, 2, 3, 4));
