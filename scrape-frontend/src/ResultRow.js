function ResultRow(props) {
  return (
    <tr>
      <td>{props.searchTerm}</td>
      <td>{props.url}</td>
      <td>{props.count}</td>
    </tr>
  );
}

export default ResultRow;
