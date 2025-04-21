window.onload = () => {
    document.getElementById('analyzeButton').addEventListener('click', async () => {
        const textInput = document.getElementById('textInput');
        const resultDiv = document.getElementById('result');

        const text = textInput.value.trim();

        // ✅ 1. Check if input is empty
        if (!text) {
            resultDiv.textContent = "⚠️ Please enter some text before analyzing!";
            resultDiv.style.color = "orange";
            return;
        }

        try {
            // ✅ 2. Send request to backend
            const response = await fetch('http://127.0.0.1:5000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text }),
            });

            // ✅ 3. Handle errors from the server
            if (!response.ok) {
                throw new Error(`Server error! Status: ${response.status}`);
            }

            const data = await response.json();
            console.log("Backend Response:", data);

            // ✅ 4. Display the prediction in UI
            resultDiv.textContent = `Prediction: ${data.prediction}`;
            resultDiv.style.color = data.prediction === 'Bullying' ? 'red' : 'green';

        } catch (error) {
            console.error('❌ Fetch Error:', error);

            // ✅ 5. Show error messages in the UI instead of alert box
            resultDiv.textContent = `❌ An error occurred: ${error.message}`;
            resultDiv.style.color = "red";
        }
    });
};
