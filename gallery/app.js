const fileInput = document.getElementById('file-input');
const gallery = document.getElementById('gallery');

fileInput.addEventListener('change', (event) => {
    const files = event.target.files;

    for (let i = 0; i < files.length; i++) {
        const file = files[i];

        if (!file.type.startsWith('image/')) {
            continue;
        }

        const reader = new FileReader();

        reader.onload = (e) => {
            const img = document.createElement('img');
            img.src = e.target.result;
            gallery.appendChild(img);
        };

        reader.readAsDataURL(file);
    }
});



fileInput.addEventListener('change', (event) => {
    const files = event.target.files;

    for (let i = 0; i < files.length; i++) {
        const file = files[i];

        if (!file.type.startsWith('image/')) {
            continue;
        }

        const reader = new FileReader();

        reader.onload = (e) => {
            const img = document.createElement('img');
            img.src = e.target.result;
            gallery.appendChild(img);
        };

        reader.readAsDataURL(file);
    }
});
