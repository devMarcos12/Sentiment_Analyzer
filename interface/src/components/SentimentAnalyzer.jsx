import React, { useState } from "react";
import axios from "axios";
import "../styles.css";
import { FaLinkedin } from "react-icons/fa";
import aiIcon from "../components/ai_icon.png";

export default function SentimentAnalyzer() {
    const [text, setText] = useState("");
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const analyzeSentiment = async () => {
        if (!text.trim()) {
            setError("Please enter a text to analyze.");
            return;
        }

        setLoading(true);
        setError(null);
        setResult(null);

        try {
            const response = await axios.post("https://web-production-e0eb.up.railway.app/predict/", { text });
            setResult(response.data.sentiment);
        } catch (err) {
            setError("Failed to analyze sentiment. Try again later.");
        }
        setLoading(false);
    };

    return (
        <div className="page-container">
            <header className="title-container">
                <div className="text-title">
                    <h3>Hi, I'm</h3>
                    <h1>Sentiment Analyzer - AI </h1>
                </div>
                <img src={aiIcon} alt="AI Icon" className="ai-icon" />
            </header>
            <div className="content">
                <div className="container">
                    <textarea
                        placeholder="Type your text here! (pt-br)"
                        value={text}
                        onChange={(e) => setText(e.target.value)}
                        className="text-area"
                    ></textarea>
                    <button onClick={analyzeSentiment} disabled={loading}>
                        {loading ? "Analyzing..." : "Analyze"}
                    </button>
                    {error && <p className="error">{error}</p>}
                    {result && <p className="result">Sentiment: {result}</p>}
                </div>
            </div>
            <footer className="footer">
                <p>Made by Marcos Junior</p>
                <a href="https://www.linkedin.com/in/marcos-junior-b367b91b3" target="_blank" rel="noopener noreferrer">
                    <FaLinkedin className="linkedin-icon" />
                </a>
            </footer>
        </div>
    );
}