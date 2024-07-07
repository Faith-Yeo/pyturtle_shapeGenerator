function generateShape() {
    const shape = document.getElementById('shape').value;
    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({shape: shape})
    }).then(response => {
        if (response.ok) {
            console.log('Shape generation request sent.');
        } else {
            console.log('Shape generation request failed.');
        }
    });
}