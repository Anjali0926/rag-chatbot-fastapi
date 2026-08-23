import { useState } from "react";

function UploadPDF() {
    const [file, setFile] = useState(null);
    const [status, setStatus] = useState("");

    const uploadPDF = async () => {
        if (!file) {
            setStatus("Please select a PDF.");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        try {
            setStatus("Uploading...");

            const response = await fetch("http://127.0.0.1:8000/upload", {
                method: "POST",
                body: formData,
            });

            const data = await response.json();

            if (response.ok) {
                setStatus(`✅ ${data.message}`);
            } else {
                setStatus("❌ Upload failed");
            }
        } catch (error) {
            console.error(error);
            setStatus("❌ Server error");
        }
    };

    return (
        <div className="upload-container">
            <input
                type="file"
                accept=".pdf"
                onChange={(e) => setFile(e.target.files[0])}
            />

            <button onClick={uploadPDF}>
                Upload PDF
            </button>

            <p>{status}</p>
        </div>
    );
}

export default UploadPDF;