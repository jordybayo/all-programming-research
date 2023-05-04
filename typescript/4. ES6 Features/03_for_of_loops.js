var test_for_of_loop = function () {
    var iterable = [3, 5, 7];
    console.log("for in loop");
    for (var i in iterable) {
        console.log(iterable[i]);
    }
    console.log("for of loop");
    for (var i in iterable) {
        console.log(i);
    }
};
