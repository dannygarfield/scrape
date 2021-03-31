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
        <h1>Danny Garfield: coding challenge</h1>
        <hr></hr>
        <h1>Scrape the web</h1>
        <ScrapeForm addResult={handleAddResult} />
        <ScrapeResults results={results} />

      </header>
    </div>
  );
}

export default App;
