// script.js

// Função para redirecionar para a página de detalhes do filme
function redirectToMovieDetail(movieId) {
    // Redireciona para a URL da página de detalhes do filme
    window.location.href = `/filme/${movieId}/`;
}

// Adiciona um evento de clique para cada item de filme
document.querySelectorAll('.movie-item').forEach(item => {
    // Obtém o ID do filme a partir do atributo 'data-id'
    const movieId = item.getAttribute('data-id');

    // Adiciona um ouvinte de evento para o clique
    item.addEventListener('click', () => {
        redirectToMovieDetail(movieId);
    });
});
