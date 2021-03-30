import { useState } from 'react';

import './App.css';
import ScrapeForm from './ScrapeForm';
import ScrapeResults from './ScrapeResults';

function App() {
  const [results, setResults] = useState([])

  const handleAddResult = (r) => {
      setResults([r, ...results]);
      console.log("new results:");
      console.log(results);
  }

  return (
    <div className="App">
      <header className="App-header">
        <p>this is my scraper</p>
        <ScrapeForm addResult={handleAddResult} />
        <ScrapeResults results={results} />
      </header>
    </div>
  );
}

export default App;
