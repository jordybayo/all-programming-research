var test_lambda = function () {
    var function1 = function () {
        console.log("function1 is called");
    };
    function1();
    var function2 = function () {
        console.log("function2 is called");
    };
    function2();
    document.getElementById("dynamicContents").innerHTML = '<button id="testBtn">click here!';
    var testBtn = document.getElementById("testBtn");
    var object1 = {
        id: "object 1",
        set: function () {
            testBtn.addEventListener("click", function () {
                console.log("object1 Event Listenner");
                console.log(this.id);
            });
        }
    };
    object1.set();
    var object2 = {
        id: "object 2",
        set: function () {
            var _this = this;
            testBtn.addEventListener("click", function () {
                console.log("objects2 event listenner");
                console.log(_this.id);
            });
        }
    };
    object2.set();
};
