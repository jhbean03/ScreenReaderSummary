// Listen for when HTML content fully loads
document.addEventListener("DOMContentLoaded", () => {
    // Obtain summary from Chrome local storage
    chrome.storage.local.get("summary", (data) => {
        console.log("Retrieved from storage:", data);

        // Ensure summary is available
        if (data.summary) {
            document.getElementById("summary").textContent = data.summary;
        } else {
            document.getElementById("summary").textContent = "No summary available.";
        }
    });
});