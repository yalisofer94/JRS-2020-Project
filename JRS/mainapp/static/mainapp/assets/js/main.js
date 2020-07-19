window.onload = function () {

    var userCollTogg = false;

    userBoxToggler = function () {
        var collapse = document.getElementsByClassName("userCollapse");
        if (userCollTogg == false) {
            collapse[0].style.display = "block";
            collapse[1].style.display = "block";
            userCollTogg = true;
        }
        else {
            collapse[0].style.display = "none";
            collapse[1].style.display = "none";
            userCollTogg = false;
        }

    };

    delButton = function (todel) {
        var result = confirm("Are you sure you want to delete?")   
        if(result){
            todel.href = "delJob/" + todel.name;
        }
    };
};
