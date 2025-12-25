document.addEventListener('DOMContentLoaded', () => {
    // Add any necessary interactive logic here
    console.log('Diary loaded successfully!');
    
    // Optional: Add simple animation delay for cards
    const cards = document.querySelectorAll('.diary-card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
    });
});
