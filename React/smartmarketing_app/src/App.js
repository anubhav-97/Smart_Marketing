import React, { useState } from 'react';
import './App.css'; // Import your CSS file for styling
import api from './api';
import Header from './Header';

function App() {
  const [postInput, setPostInput] = useState({});
  const [emailInput, setEmailInput] = useState({ email_contents: [] });

  const [postOutput, setPostOutput] = useState();
  const [emailOutput, setEmailOutput] = useState();

  const generatePost = async () => {
    const response = await api.post('/socialmedia', postInput);
    setPostOutput(response.data);
  };

  const generateEmail = async () => {
    const response = await api.post('/emailgenerator', emailInput);
    setEmailOutput(response.data);
  };

  return (
    <div className="app">
      <nav className="navbar">
        <h1 className="header-main">Smart Marketer</h1>
      </nav>
      <div className="app-container">
        <div className="generator-container">
            <h1 className="header">Social Media Marketer</h1>
            <div className="input-container">
            <input
                className="input-field"
                placeholder="Brand"
                onChange={(e) => setPostInput({ ...postInput, brand: e.target.value })}
            />
            <input
                className="input-field"
                placeholder="Description"
                onChange={(e) => setPostInput({ ...postInput, description: e.target.value })}
            />
            <input
                className="input-field"
                placeholder="Work"
                onChange={(e) => setPostInput({ ...postInput, work: e.target.value })}
            />
            <input
                className="input-field"
                placeholder="Language"
                onChange={(e) => setPostInput({ ...postInput, posts_language: e.target.value })}
            />
            <input
                className="input-field"
                placeholder="Expansion"
                onChange={(e) => setPostInput({ ...postInput, topics_ideas_prompt_expansion: e.target.value })}
            />
            <input
                className="input-field"
                placeholder="Platform"
                onChange={(e) => setPostInput({ ...postInput, platforms: e.target.value })}
            />
            </div>
            <button className="generate-button" onClick={generatePost}>
            Generate Post
            </button>
            {postOutput && <div className="output">{JSON.stringify(postOutput)}</div>}
        </div>

        <div className="generator-container">
            <h1 className="header">Email Marketer</h1>
            <div className="input-container">
            <input
                className="input-field"
                placeholder="Sender"
                onChange={(e) => setEmailInput({ ...emailInput, sender: e.target.value })}
            />
            <input
                className="input-field"
                placeholder="Recipient"
                onChange={(e) => setEmailInput({ ...emailInput, recipient: e.target.value })}
            />
            <input
                className="input-field"
                placeholder="Style"
                onChange={(e) => setEmailInput({ ...emailInput, style: e.target.value })}
            />
            <input
                className="input-field"
                placeholder="Contents"
                onChange={(e) => setEmailInput({ ...emailInput, email_contents: e.target.value })}
            />
            {/* Add similar inputs for other fields */}
            </div>
            <button className="generate-button" onClick={generateEmail}>
            Generate Email
            </button>
            {emailOutput && <div className="output">{JSON.stringify(emailOutput)}</div>}
        </div>
      </div>
    </div>
  );
}

export default App;
