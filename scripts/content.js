console.log("Content script loaded!");

// Extract the entire HTML from the given webpage
const pageHTML = document.documentElement.outerHTML
console.log("Extracted HTML:", pageHTML.substring(0, 100));

// Send the HTML to the background script
chrome.runtime.sendMessage({ action: "sendHTML", html: pageHTML }, (response) => {
    if (chrome.runtime.lastError) {
        console.error("Error sending message:", chrome.runtime.lastError);
    } else {
        console.log("Message sent successfully", response);
    }
});