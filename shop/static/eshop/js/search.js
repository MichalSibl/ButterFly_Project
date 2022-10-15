// global search timer
var searchTimeout = null;
function search(el) {
    // timer reset
    if (searchTimeout != null) {
        clearTimeout(searchTimeout);
    }
    // Timer for finding
    searchTimeout = setTimeout(() => {
        // obtain value in text input
        let query = el.value;
        // write
        console.log(query);

        fetch(`/api/search?q=${query}`)
            .then((response) => response.json())
            .then((data) => {
                if (data.products.length > 0) {
                    let content = "<ul>";
                    data.products.forEach((product) => {
                        let [id, title] = product;


                        content += `<li><a href="/detail/${id}">${title}</a></li>`;
                    });
                    content += "</ul>";

                    searchresults.innerHTML = content;
                    searchresults.style.display = "block";
                } else {
                    searchresults.innerHTML = "Nothing find it";
                    searchresults.style.display = "block";
                }
            });
    }, 500);
}