// appel de la variable hors de la boucle
var test_let_and_const = function () {
    var unchangeableValue = "Tax rate is 36%";
    console.log(unchangeableValue);
    for (var i = 1; i < 4; i++) {
        var inBlockVariable = i;
        console.log(inBlockVariable);
    }
    console.log("out of scope");
    // console.log(inBlockVariable); //marche uniquement avec var
};
