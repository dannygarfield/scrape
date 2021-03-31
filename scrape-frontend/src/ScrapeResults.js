import ResultRow from './ResultRow';

function ScrapeResults(props) {

  const rows = []
  if ( props.results.length === 0 ) {
    return (
      <p className="no-results">Submit above to view results</p>
    );
  }
  props.results.forEach((r, index) => {
    rows.push(
      <ResultRow
        key={index}
        url={r.url}
        searchTerm={r.searchTerm}
        count={r.count} />
    )
  });

  return (
    <div>
      <h2>Results</h2>
      <table className="results">
        <thead>
          <tr>
            <th>search term</th>
            <th>url</th>
            <th>count</th>
          </tr>
        </thead>
        <tbody>
          {rows}
        </tbody>
      </table>
      <p>*A count of -1 indicates a bad URL was given. Please check that your URL begins with "http://" or "https://".</p>
    </div>
  );
}

export default ScrapeResults;
