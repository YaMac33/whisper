/* static/script.js */
/* 音声ファイルをアップロードし、Whisper APIで文字起こしを実行するJS */

document.addEventListener("DOMContentLoaded", () => {
    const uploadForm = document.getElementById("uploadForm");
    const audioInput = document.getElementById("audioFile");
    const resultDiv = document.getElementById("result");

    uploadForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        const formData = new FormData();
        const audioFile = audioInput.files[0];

        if (!audioFile) {
            alert("音声ファイルを選択してください。");
            return;
        }

        formData.append("audio", audioFile);
        resultDiv.textContent = "処理中...";

        try {
            const response = await fetch("/transcribe", {
                method: "POST",
                body: formData
            });
            const data = await response.json();

            if (data.error) {
                resultDiv.textContent = "エラー: " + data.error;
            } else {
                resultDiv.textContent = data.text;
            }
        } catch (err) {
            resultDiv.textContent = "通信エラーが発生しました: " + err.message;
        }
    });
});