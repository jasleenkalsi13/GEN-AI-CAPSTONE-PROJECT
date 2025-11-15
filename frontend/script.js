const BASE_URL = "http://127.0.0.1:8000";

async function uploadResume() {
    let file = document.getElementById("resumeFile").files[0];
    let formData = new FormData();
    formData.append("file", file);

    let res = await fetch(`${BASE_URL}/resume/upload`, {
        method: "POST",
        body: formData
    });

    let data = await res.json();
    document.getElementById("resumeResult").innerText = data.summary || data.error;
}

async function matchJob() {
    let jd = document.getElementById("jobDescription").value;

    let res = await fetch(`${BASE_URL}/jobmatch/match`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ job_description: jd })
    });

    let data = await res.json();
    document.getElementById("jobMatchResult").innerText = data.match_result || data.error;
}

async function sendChat() {
    let message = document.getElementById("chatInput").value;

    let res = await fetch(`${BASE_URL}/chat/query`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question: message })
    });

    let data = await res.json();
    document.getElementById("chatResponse").innerText = data.answer || data.error;
}
