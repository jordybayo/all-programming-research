let test_for_of_loop = function(){
    let iterable = [3,5,7];

    console.log("for in loop")
    for (let i in iterable){
        console.log(iterable[i]);
    }

    console.log("for of loop")
    for(let i in iterable){
        console.log(i)
    }
}