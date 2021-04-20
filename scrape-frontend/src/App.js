import { useState } from 'react';

import './App.css';
import ScrapeForm from './ScrapeForm';
import ScrapeResults from './ScrapeResults';
import Notes from './Notes';

function App() {
  const [results, setResults] = useState([])

  const handleAddResult = (r) => {
      setResults([r, ...results]);
      console.log("new result:");
      console.log(r);
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>Danny Garfield: YipitData coding challenge</h1>
        <hr></hr>
        <h1>Scrape the web</h1>
        <ScrapeForm addResult={handleAddResult} />
        <ScrapeResults results={results} />
        <Notes />
      </header>
    </div>
  );
}

export default App;
