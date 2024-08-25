function filter_selection(c) {
    var x = document.getElementsByClassName("column");
    if (c === "all") c = "";
    for (var i = 0; i < x.length; i++) {
        remove_class(x[i], "visible");
        if (x[i].className.indexOf(c) > -1) {
            add_class(x[i], "visible");
        }
    }
}

function add_class(element, name) {
    if (element.className.indexOf(name) === -1) {
        element.className += " " + name;
    }
}

function remove_class(element, name) {
    var classList = element.className.split(" ");
    var newClassList = classList.filter(function(cls) {
        return cls !== name;
    });
    element.className = newClassList.join(" ");
}

document.addEventListener("DOMContentLoaded", function() {
    filter_selection("all");

    var btnContainer = document.getElementById("filter_content");
    if (btnContainer) {
        var btns = btnContainer.getElementsByClassName("btn");
        for (var i = 0; i < btns.length; i++) {
            btns[i].addEventListener("click", function () {
                var current = btnContainer.getElementsByClassName("active");
                // Remove 'active' class from all buttons
                for (var j = 0; j < current.length; j++) {
                    current[j].className = current[j].className.replace(" active", "");
                }
                // Add 'active' class to the clicked button
                this.className += " active";
            });
        }
    }
});
