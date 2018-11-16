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
    sendData({
        type: "SELECTION",
        value: {
            "text": selection,
            "timestamp": new Date().getTime(),
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