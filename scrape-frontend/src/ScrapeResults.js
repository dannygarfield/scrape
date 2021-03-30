import ResultRow from './ResultRow';

function ScrapeResults(props) {

  const rows = []
  if ( props.results.length === 0 ) {
    return (
      <p>Submit above to view results</p>
    );
  }
  console.log("results:")
  console.log(props.results)
  props.results.forEach((r, index) => {
    console.log("r:", r)
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
      <h2>results</h2>
      <table>
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
