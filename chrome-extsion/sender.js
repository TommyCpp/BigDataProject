function sendData(data) {
    /**
     * input: Data object
     * output: null
     * Send data to back-end
     * */
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