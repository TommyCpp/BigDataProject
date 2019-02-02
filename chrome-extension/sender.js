function sendData(data) {
    /**
     * input: Data object
     * output: null
     * Send data to back-end
     * */
    console.log("Sended!")//todo:send
}

function sendSelection(selection) {
    /**
     * input: string
     * output: null
     * Send selection string
     * */
    chrome.storage.sync.get(['JITR-username', 'JITR-id'], function (result) {
        var id = result["JITR-id"];
        var username = result["JITR-username"];
        if(id !== null && username !== null){
            sendData({
                error: "",
                id: id,
                type: "SELECTION",
                value: {
                    "text": selection,
                    "timestamp": new Date().getTime(),
                    "type": "SELECTION",
                    "username": username,
                }
            });
        }
    });

}

function sendLocation(location) {
    sendData({
        type: "LOCATION",
        values: {
            "text": location,
            "timestamp": new Date().getTime()
        }
    })
}