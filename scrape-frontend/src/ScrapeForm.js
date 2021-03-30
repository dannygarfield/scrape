import { useState } from 'react';

function ScrapeForm(props) {
  const [url, setUrl] = useState('')
  const [searchTerm, setSearchTerm] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault();

    if (url === '' || searchTerm === '') {
      return
    }

    console.log(`querying /?search_term=${searchTerm}&url=${url}`);
    fetch(`http://localhost:8000/?search_term=${searchTerm}&url=${url}`)
      .then(response => response.json() )
      .then(responseData => {
        let r = {
          searchTerm,
          url,
          count: responseData.count
        }
        console.log(responseData);
        props.addResult(r);
      })
      .catch(error => {
        console.log('Error fetching and parsing data', error)
      })
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>url to search:</label>
        <input
          name="url"
          type="text"
          value={url}
          onChange={e => setUrl(e.target.value)} />
        <br></br>
        <label>word/phrase to search for:</label>
        <input
          name="search_term"
          type="text"
          value={searchTerm}
          onChange={e => setSearchTerm(e.target.value)} />
        <br />
        <input type="submit" value="Submit" />
      </form>
    </div>
  );
}


export default ScrapeForm;
