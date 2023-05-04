// appel de la variable hors de la boucle
let test_let_and_const = function(){
    const unchangeableValue = "Tax rate is 36%";
    console.log(unchangeableValue);

    for(let i=1; i<4; i++){
        let inBlockVariable = i;
        console.log(inBlockVariable);
    }

    console.log("out of scope");
    // console.log(inBlockVariable); //marche uniquement avec var
}