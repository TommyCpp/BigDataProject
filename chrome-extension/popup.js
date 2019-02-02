chrome.storage.sync.get(['JITR-username', 'JITR-id'], function (result) {
    document.getElementById("username").value = result["JITR-username"];
    document.getElementById("id").value = result["JITR-id"];
    document.getElementById("username").setAttribute("disabled", true);
    document.getElementById("id").setAttribute("disabled", true);
});
document.getElementById("submit").onclick = function () {
    var username = document.getElementById("username").value;
    var id = document.getElementById("id").value;
    chrome.storage.sync.set({"JITR-username": username.toString()}, function () {
        console.log('Value is set to ' + username.toString());
    });
    chrome.storage.sync.set({"JITR-id": id.toString()}, function () {
        console.log('Value is set to ' + id.toString());
    });
};
document.getElementById("reset").onclick = function () {
    var username = document.getElementById("username").value;
    var id = document.getElementById("id").value;
    chrome.storage.sync.set({"JITR-username": username.toString()}, function () {
        console.log('Value is set to ' + username.toString());
    });
    chrome.storage.sync.set({"JITR-id": id.toString()}, function () {
        console.log('Value is set to ' + id.toString());
    });
};