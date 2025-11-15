const BASE_URL = "http://127.0.0.1:8000";

async function uploadResume() {
    let file = document.getElementById("resumeFile").files[0];
    let formData = new FormData();
    formData.append("file", file);

    let res = await fetch(`${BASE_URL}/resume/analyze`, {
        method: "POST",
        body: formData
    });

    let data = await res.json();
    document.getElementById("resumeResult").innerText = data.result || data.error;
}

async function matchJob() {
    let jd = document.getElementById("jobDescription").value;

    let res = await fetch(`${BASE_URL}/jobmatch`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ job_description: jd })
    });

    let data = await res.json();
    document.getElementById("jobMatchResult").innerText = data.match || data.error;
}

async function sendChat() {
    let message = document.getElementById("chatInput").value;

    let res = await fetch(`${BASE_URL}/chat`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ query: message })
    });

    let data = await res.json();
    document.getElementById("chatResponse").innerText = data.response || data.error;
}
