// Dark / Light mode toggle
function toggleMode() {
    document.body.classList.toggle('dark');

    // Tanlovni saqlash
    if (document.body.classList.contains('dark')) {
        localStorage.setItem('theme', 'dark');
    } else {
        localStorage.setItem('theme', 'light');
    }
}

// Sahifa yuklanganda oldingi tanlovni tiklash
window.onload = function () {
    const theme = localStorage.getItem('theme');
    if (theme === 'dark') {
        document.body.classList.add('dark');
    } else {
        document.body.classList.remove('dark');
    }
}

function filterCards() {
    let input = document.getElementById('search').value.toLowerCase();
    let cards = document.getElementById('cardList').getElementsByClassName('card');

    for (let i = 0; i < cards.length; i++) {
        let card = cards[i];
        let tags = card.dataset.tags.toLowerCase();
        let title = card.querySelector('h3').textContent.toLowerCase();
        let shortText = card.querySelector('p').textContent.toLowerCase();

        if (tags.includes(input) || title.includes(input) || shortText.includes(input)) {
            card.style.display = '';
        } else {
            card.style.display = 'none';
        }
    }
}

function filterByTag(tag) {
    document.getElementById('search').value = tag;
    filterCards();
}