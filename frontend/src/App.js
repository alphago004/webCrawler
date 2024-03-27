import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [url, setUrl] = useState('');
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('https://www.google.com', { url });
      console.log(response.data); // Handle success response
    } catch (error) {
      console.error('Error:', error); // Handle error response
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Enter URL to crawl"
      />
      <button type="submit">Crawl</button>
    </form>
  );
}

export default App;
