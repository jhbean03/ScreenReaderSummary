// Extract the entire HTML from the given webpage
const pageHTML = document.documentElement.outerHTML

// Send the HTML to the background script
chrome.runtime.sendMessage({
    action: "sendHTML",
    html: pageHTML
});