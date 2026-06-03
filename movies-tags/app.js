const kaggleMovieData = 

        function recommendMovies() {
            const input = document.getElementById('tagInput').value;
            const resultsContainer = document.getElementById('results');
            resultsContainer.innerHTML = '';

            // Tratamento da entrada do usuário: divide por vírgulas, remove espaços e passa para minúsculas
            const searchTags = input.split(',')
                .map(tag => tag.trim().toLowerCase())
                .filter(tag => tag !== '');

            if (searchTags.length === 0) {
                resultsContainer.innerHTML = '<p class="no-results">Por favor, digite alguma tag para buscar.</p>';
                return;
            }

            // Algoritmo de recomendação
            const recommendations = kaggleMovieData.map(movie => {
                // Calcula quantas tags batem com a busca
                const matchCount = movie.tags.reduce((count, tag) => {
                    return searchTags.includes(tag.toLowerCase()) ? count + 1 : count;
                }, 0);
                
                return { ...movie, matchCount };
            })
            // Filtra apenas os que tiveram pelo menos 1 match
            .filter(movie => movie.matchCount > 0)
            // Ordena primeiro pela relevância (matchCount) e, em caso de empate, pela nota do IMDB
            .sort((a, b) => b.matchCount - a.matchCount || b.rating - a.rating);

            // Renderização no DOM
            if (recommendations.length === 0) {
                resultsContainer.innerHTML = '<p class="no-results">Nenhum filme encontrado com essas tags. Tente outras!</p>';
                return;
            }

            recommendations.forEach(movie => {
                const card = document.createElement('div');
                card.className = 'movie-card';
                card.innerHTML = `
                    <h3 class="movie-title">
                        ${movie.title} 
                        <span class="movie-rating">★ ${movie.rating}</span>
                    </h3>
                    <p class="movie-tags"><strong>Tags:</strong> ${movie.tags.join(', ')}</p>
                    <p class="movie-desc">${movie.desc}</p>
                `;
                resultsContainer.appendChild(card);
            });
        }

        // Permite buscar apertando "Enter"
        function handleKeyPress(event) {
            if (event.key === 'Enter') {
                recommendMovies();
            }
        }