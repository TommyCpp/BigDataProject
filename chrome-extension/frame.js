document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('#close').addEventListener('click', close);
    main();
});


function close() {
    document.getElementsByTagName("html")[0].setAttribute("style", "display:none;");
}

function main() {
    var selectedText = null;
    var url = window.location.search.substring(1); //get rid of "?" in querystring
    var qArray = url.split('&'); //get key-value pairs
    for (var i = 0; i < qArray.length; i++) {
        var pArr = qArray[i].split('='); //split key and value
        if (pArr[0] === "text")
            selectedText = pArr[1];
    }
    selectedText = selectedText.toLowerCase();
    selectedText = selectedText.trim();
    switch (selectedText) {
        case "constructor":
            document.getElementById("constructor").classList.remove("hidden-content");
            break;
        case "stream":
            document.getElementById("stream").classList.remove("hidden-content");
            break;
        case "use%20strict":
            document.getElementById("use-strict").classList.remove("hidden-content");
            break;
    }
    // document.getElementById("text").textContent = "About " + selectedText + " , We find following may interest you";
}
