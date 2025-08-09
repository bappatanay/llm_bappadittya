Stock Analysis Web App
A simple Flask-based web application that allows you to analyze a stock (from NSE) using AI.
Features
* Enter stock name or ticker (NSE listed)
* Get detailed analysis powered by LLMs
* Simple browser interface
* Sample outputs included for reference
Project Structure
??? app.py               # Flask backend
??? templates/
?   ??? index.html       # Frontend UI
??? README.md            # Documentation

Prerequisites
* Python 3.8+ installed
* Flask installed (pip install flask)
? How to Run Locally
1. Clone or download this project
git clone <repo_url>
cd <project_folder>
2. Install dependencies
pip install flask
3. Run the Flask app
python app.py
4. Open your browser and go to:
http://127.0.0.1:5000
5. Enter the stock name or ticker from NSE in the input box.
6. Wait for 15–20 seconds to receive the output.
(Processing time depends on AI model speed and internet connection)
Sample Outputs
You can check the sample_outputs folder for example responses from the app.
Notes
* Ensure internet access if using an AI API.
* Processing time may vary depending on request complexity.
* For NSE tickers, use official symbols (e.g., RELIANCE, TCS, INFY).
