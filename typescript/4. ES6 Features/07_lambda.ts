let test_lambda = function(){
    let function1 = function(){
        console.log("function1 is called");
    }
    function1();

    let function2 = () =>{
        console.log("function2 is called";)
    }
    function2();

    document.getElementById("dynamicContents").innerHTML = '<button id="testBtn">click here!';
    let testBtn = document.getElementById("testBtn");

    let object1 = {
        id : "object 1",
        set: function(){
            testBtn.addEventListener("click", function(){
                console.log("object1 Event Listenner");
                console.log(this.id);
            });
        }
    }
    object1.set();

    let object2 = {
        id : "object 2",
        set : function(){
            testBtn.addEventListener("click", () =>{
                console.log("objects2 event listenner");
                console.log(this.id);
            })
        }
    }
    object2.set();
}