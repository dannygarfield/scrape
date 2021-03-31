function Notes() {
  return (
    <div className="notes">
      <h2>Notes</h2>
      <ul>
        <li>This page will display results only from the current session. A new session begins each time the page is refreshed.</li>
        <li>A count of -1 indicates a bad URL was given. Please check that your URL begins with "http://" or "https://".</li>
      </ul>
    </div>
  );
}

export default Notes;
