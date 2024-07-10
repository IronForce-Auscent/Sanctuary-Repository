function search() {
    const searchInput = document.getElementById("query-input").value;
    const searchResults = document.getElementById("search-results");

    console.log(searchInput);
    if (!searchInput) {
        searchResults.innerHTML = "Please enter a search result";
    } else {
        searchResults.innerHTML = "No result shown for '" + searchInput + "' .";
    }
    searchResults.style.backgroundColor = "#f4f4f4";
}