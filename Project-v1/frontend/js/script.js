const messageTextarea = document.getElementById("message");
const inputFile = document.getElementById("input");
const submitButton = document.getElementById("button");
const resultTextarea = document.getElementById("result");
const baseURL = "http://localhost:8000";

async function readFileContent(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = async (e) => {
      const arrayBuffer = e.target.result;
      try {
        let fileContent = "";
        if (file.name.endsWith(".txt")) {
          const decoder = new TextDecoder("utf-8");
          fileContent = decoder.decode(arrayBuffer);
        } else if (file.name.endsWith(".pdf")) {
          const typedArray = new Uint8Array(arrayBuffer);
          const pdf = await pdfjsLib.getDocument(typedArray).promise;
          for (let pageNum = 1; pageNum <= pdf.numPages; pageNum++) {
            const page = await pdf.getPage(pageNum);
            const pageText = await page.getTextContent();
            pageText.items.forEach((item) => {
              fileContent += item.str;
            });
          }
        } else {
          const mammothResult = await mammoth.extractRawText({ arrayBuffer });
          const lines = mammothResult.value.split("\n");
          fileContent = lines.filter((line) => line.trim() !== "").join("\n");
        }
        resolve(fileContent);
      } catch (error) {
        reject(error);
      }
    };
    reader.onerror = (err) => {
      reject(err);
    };
    reader.readAsArrayBuffer(file);
  });
}

inputFile.addEventListener("change", async (e) => {
  const file = e.target.files[0];
  if (file) {
    try {
      const fileContent = await readFileContent(file);
      messageTextarea.value = fileContent;
    } catch (error) {
      console.error("An error occurred while reading the file:", error);
    }
  }
});

submitButton.addEventListener("click", async (e) => {
  e.preventDefault();
  const message = messageTextarea.value;
  const file = inputFile.files[0];

  if (!message && !file) {
    console.error("No message or file selected.");
    return;
  }
  try {
    const requestData = file ? { message: await readFileContent(file) } : { message };
    await sendJSONRequest(requestData);
  } catch (error) {
    console.error("An error occurred while sending JSON request:", error);
  } finally {
    inputFile.value = ""; // Reset the file input
  }
});

async function sendJSONRequest(data) {
  try {
    const response = await fetch(`${baseURL}/generate_json/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const responseData = await response.json();
    console.log("API response:", responseData);
    const jsonResponse = JSON.parse(responseData.json_output);
    resultTextarea.value = JSON.stringify(jsonResponse, null, 2);
  } catch (error) {
    console.error("Error:", error);
  }
}

const downloadButton = document.getElementById("downloadButton");

downloadButton.addEventListener("click", () => {
  if (!resultTextarea.value) {
    console.error("No content to download.");
    return;
  }
  const jsonContent = resultTextarea.value;
  const blob = new Blob([jsonContent], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "result.json";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
});
