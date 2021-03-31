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
    </div>
  );
}

export default ScrapeResults;
