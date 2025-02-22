/* Set up a listener that checks for HTML from the webpage user is 
viewing */
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    // Once the HTML is obtained, send to Python script
    if (message.action === "sendHTML") {
        // Send the html to the Python script
        fetch("http://127.0.0.1:5000/summarize", {
            method: "POST",
            headers: { "Content-Type": "application/json"},
            body: JSON.stringify({ html: message.html })
        })

        // Obtain the response from Python and convert to JSON
        .then(response => response.json())

        // Output confirmation and store summary
        .then(data => {
            console.log("Received summary:", data.summary);
            chrome.storage.local.set({ summary: data.summary }, () => {
                console.log("Summary saved to local storage");
            });
            sendResponse({ status: "Summary saved", summary: data.summary });
        })

        // If HTML couldn't be sent to Python script, output error
        .catch(error => {
            console.error("Error communicating with Python:", error);
            sendResponse({ status: "Error", error: error.message });
        });

        return true;
    }
});