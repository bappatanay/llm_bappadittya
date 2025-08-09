import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI
import instructor
import datetime
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='templates')

# Set your API key
url = "https://api.perplexity.ai/chat/completions"
load_dotenv(override=True)
API_KEY = os.getenv("PERPLEXITY_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze_stock():
    data = request.json
    stock_name = data.get("stock_name", "Apple Inc.")
    market = 'NSE'
    dt = datetime.date.today()

    headers = {
    "Authorization": f"Bearer {API_KEY}",  # Replace with your actual API key
    "Content-Type": "application/json"
    }

    system_prompt = '''You are a senior equity research analyst with 20+ years of experience analyzing stock markets. Your task is to produce a detailed analysis of the given stock.'''

    user_prompt = f'''
        Stock to analyze: {stock_name}
        Market: {market}
        Date of analysis: {dt}

        Your analysis should include:
        - Company Overview – Brief description of the company, its sector, and major business segments.
        - Recent Price Performance – 1-month, 6-month, and 1-year price change; compare with sector and market index.
        - Fundamental Analysis
            - Revenue & profit trends (last 4 quarters and last 3 years)
            - Valuation ratios (P/E, P/B, EV/EBITDA, PEG) compared to industry averages
            - Debt levels, cash flow health, and dividend policy
        - Technical Analysis
            - Key support and resistance levels
            - Moving averages (50-day, 200-day)
            - RSI, MACD, and momentum trends
        - News & Sentiment Analysis
            - Summary of the latest 5–10 relevant news articles
            - Overall market sentiment: positive, neutral, or negative
        - Risks & Opportunities
            - Regulatory, competitive, or macroeconomic risks
            - Growth drivers and upcoming catalysts
        - Analyst Consensus – Buy/Hold/Sell rating trends and target price range from credible sources.
        - Final Recommendation – Provide a clear conclusion: Bullish, Neutral, or Bearish, with reasoning.
        - Output format: Present findings in a clear, sectioned report with bullet points where suitable. Include data tables if relevant. All financial figures should include the currency symbol.
    '''
    payload = {
        "model": "sonar-pro",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        }

    response = requests.post(url, headers=headers, json=payload)
    # response.json()["choices"][0]['message']['content']
    # return jsonify({"analysis": response.choices[0].message.content})
    return jsonify({"analysis": response.json()["choices"][0]['message']['content']})


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="127.0.0.1", port=5000, debug=True)