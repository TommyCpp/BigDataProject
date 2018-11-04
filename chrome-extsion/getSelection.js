window.onmouseup = function () {
    console.log("mouse up");
    if (window.getSelection()) {
        var selection = window.getSelection();
        if (selection.toString() === "") {
            return;
        }
        var selectText = null;
        selectText = selection.toString();

    }
};

// alert(selectText);