const apiUrl = "http://localhost:5000/api/artworks";

const titleInput = document.getElementById('title');
const descriptionInput = document.getElementById('description');
const submitButton = document.getElementById('submit');
const artworksDiv = document.getElementById('artworks');

submitButton.addEventListener('click', () => {
    const title = titleInput.value.trim();
    const description = descriptionInput.value.trim();

    if (!title) {
        alert("Title is required.");
        return;
    }

    fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, description })
    })
    .then(response => response.json())
    .then(() => {
        titleInput.value = '';
        descriptionInput.value = '';
        fetchArtworks();
    });
});

function fetchArtworks() {
    fetch(apiUrl)
        .then(response => response.json())
        .then(artworks => {
            artworksDiv.innerHTML = '';
            artworks.forEach(artwork => {
                const div = document.createElement('div');
                div.className = 'artwork';
                div.innerHTML = `
                    <div class="artwork-title">${artwork.title}</div>
                    <div>${artwork.description || ''}</div>
                    <button onclick="deleteArtwork(${artwork.id})">Delete</button>
                `;
                artworksDiv.appendChild(div);
            });
        });
}

function deleteArtwork(id) {
    fetch(`${apiUrl}/${id}`, { method: 'DELETE' })
        .then(() => fetchArtworks());
}

// Initial fetch
fetchArtworks();
