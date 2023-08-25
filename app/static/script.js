document.addEventListener("DOMContentLoaded", function () {
    const itemList = document.getElementById("item-list");
    const sortSelect = document.getElementById("sort");
    const filterSelect = document.getElementById("filter");

    let items = []; // Store the loaded items

    // Load data from the JSON file (assuming it's on the same domain)
    fetch("/app/static/data.jsonl")
    .then(response => response.text())
    .then(data => {
        const lines = data.split("\n");
        items = lines.map(line => JSON.parse(line.trim()));
        renderItems();
    });

    sortSelect.addEventListener("change", renderItems);
    filterSelect.addEventListener("change", renderItems);

    function renderItems() {
        const sortValue = sortSelect.value;
        const filterValue = filterSelect.value;

        // Apply sorting and filtering
        const filteredItems = items.filter(item =>
            filterValue === "" || item.source === filterValue
        );

        if (sortValue === "asc") {
            filteredItems.sort((a, b) => {
                const priceA = parseFloat(a.price.replace(/[$,]/g, ''));
                const priceB = parseFloat(b.price.replace(/[$,]/g, ''));
                return priceA - priceB; // Sort in ascending order
            });

        } else if (sortValue === "desc") {
            filteredItems.sort((a, b) => {
                const priceA = parseFloat(a.price.replace(/[$,]/g, ''));
                const priceB = parseFloat(b.price.replace(/[$,]/g, ''));
                return priceB - priceA; // Sort in descending order
            });
        }

        // Clear existing items
        itemList.innerHTML = "";

        // Render filtered and sorted items
        filteredItems.forEach(item => {
            const li = document.createElement("li");
            //li.innerHTML = `<div><img src="${item.image_url}" alt="${item.title}" width="100"></div><div>${item.title} - Price: ${item.price} - Source: ${item.source}</div>`;
            li.innerHTML = `
                <h2>${item.title }</h2>
                <img src="${item.image_url}" alt="Image">
                <p>Price: ${item.price}</p>
                <p>Delivery: ${item.shipping}</p>
                <p>Source: ${item.source}</p>
                <p>
                    <a href="${item.listing_url}" target="_blank" class="styled-link">Link</a>
                </p>
            `;
            itemList.appendChild(li);
        });
    }
});
