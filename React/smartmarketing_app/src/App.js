import React, { useState } from 'react';
import './App.css'; // Import your CSS file for styling
import api from './api';
import Header from './Header';

function App() {
  // State variables to manage input and output for the Social Media and Email generators
  const [postInput, setPostInput] = useState({});
  const [emailInput, setEmailInput] = useState({});

  const [postOutput, setPostOutput] = useState();
  const [emailOutput, setEmailOutput] = useState();

  // Function to generate a Social Media post based on the input
  const generatePost = async () => {
    const response = await api.post('/socialmedia', postInput);
    setPostOutput(response.data);
  };

  // Function to generate an Email based on the input
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
                placeholder="What's the Name of your Brand?"
                onChange={(e) => setPostInput({ ...postInput, brand: e.target.value })}
            />
            <input
                className="input-field"
                placeholder="What does your brand do?"
                onChange={(e) => setPostInput({ ...postInput, description: e.target.value })}
            />
            <input
                className="input-field"
                placeholder="Which Industry do you cater?"
                onChange={(e) => setPostInput({ ...postInput, work: e.target.value })}
            />
            <input
                className="input-field"
                placeholder="In which language to want to write the post?"
                onChange={(e) => setPostInput({ ...postInput, posts_language: e.target.value })}
            />
            <input
                className="input-field"
                placeholder="Any new developments, offers or discounts?"
                onChange={(e) => setPostInput({ ...postInput, topics_ideas_prompt_expansion: e.target.value })}
            />
            <input
                className="input-field"
                placeholder="Which Platform do you want to post on?"
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
                placeholder="Style of the Email?"
                onChange={(e) => setEmailInput({ ...emailInput, style: e.target.value })}
            /><input
                className="input-field"
                placeholder="Contents (comma seperated)"
                onChange={(e) => setEmailInput({ ...emailInput, email_contents: e.target.value.split(",") })}
            />
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