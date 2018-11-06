window.onmouseup = function (event) {
    console.log("mouse up");
    if (window.getSelection() != null && window.getSelection().toString() !== "") {
        //if we get selection
        var selection = window.getSelection();
        if (selection.toString() === "") {
            return;
        }
        var selectText = null;
        selectText = selection.toString();
        // show icon
        var icon = document.createElement("img");
        icon.setAttribute("src", "data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==");//todo: change icon
        //todo: find position of mouse
        // language=CSS
        icon.setAttribute("style", `top: ${event.clientX + 1} px !important; left: ${event.clientY + 1}px !important; position:absolute;`);
        icon.setAttribute("id", "user-behavior-icon");
        document.getElementsByTagName("body")[0].appendChild(icon);
    } else {
        if (document.getElementById("user-behavior-icon") != null){
            document.getElementById("user-behavior-icon").remove();
        }
    }
};

// alert(selectText);