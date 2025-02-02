import React, { useState, useEffect } from "react";
import axios from "axios";
import "../styles.css"; 
const FAQList = () => {
  const [faqs, setFaqs] = useState([]);
  const [language, setLanguage] = useState("en");

  useEffect(() => {
    fetchFAQs();
  }, [language]);

  const fetchFAQs = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/faqs/?lang=${language}`);
      setFaqs(response.data);
    } catch (error) {
      console.error("Error fetching FAQs:", error);
    }
  };

  return (
    <div className="container">
      <h1>Frequently Asked Questions</h1>

      {/* Language Selector */}
      <label>Select Language:</label>
      <select value={language} onChange={(e) => setLanguage(e.target.value)}>
        <option value="en">English</option>
        <option value="hi">Hindi</option>
        <option value="bn">Bengali</option>
      </select>

      {/* FAQ List */}
      {faqs.length === 0 ? (
        <p>No FAQs available.</p>
      ) : (
        faqs.map((faq, index) => (
          <div key={index} className="faq-item">
            <h3>{faq.question}</h3>
            <p dangerouslySetInnerHTML={{ __html: faq.answer }} />
          </div>
        ))
      )}
    </div>
  );
};

export default FAQList;
