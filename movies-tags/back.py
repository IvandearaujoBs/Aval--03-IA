import json
from typing import List, Optional
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Movie Recommendation API")

# --- Configuração de CORS ---
# Permite que o seu front-end (HTML/JS) acesse este back-end sem bloqueios de segurança
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, mude para o domínio do seu front-end
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Carga dos Dados em Memória (Carregamento Rápido) ---
print("Carregando base de dados de filmes...")
try:
    with open("movies.json", "r", encoding="utf-8") as file:
        MOVIES_DB = json.load(file)
    print(f"Sucesso! {len(MOVIES_DB)} filmes carregados na memória.")
except FileNotFoundError:
    print("Erro: O arquivo movies.json não foi encontrado.")
    MOVIES_DB = []


# --- Endpoint de Busca ---
@app.get("/movies")
def get_movies(genres: Optional[List[str]] = Query(None)):
    """
    Retorna os filmes filtrados por gênero (Lógica AND).
    Se nenhum gênero for passado, retorna os 50 mais populares.
    """
    # Se o usuário não selecionou nenhum gênero, retorna os mais populares para não deixar a tela vazia
    if not genres:
        top_movies = sorted(MOVIES_DB, key=lambda x: x.get("popularity", 0), reverse=True)[:50]
        return format_response(top_movies)

    filtered_movies = []
    
    # Transformamos os gêneros buscados em um 'set' para operações matemáticas de conjunto
    # Exemplo recebido: ["Action", "Adventure"] -> {'action', 'adventure'} (em minúsculo para evitar erros)
    selected_genres_set = {g.lower() for g in genres}

    for movie in MOVIES_DB:
        # Normaliza os gêneros do filme atual para minúsculo
        movie_genres_set = {g.lower() for g in movie.get("genres", [])}

        # LÓGICA AND: Verifica se TODOS os gêneros selecionados estão contidos no filme
        # Se selected_genres_set for um subconjunto de movie_genres_set, o filme passa no teste
        if selected_genres_set.issubset(movie_genres_set):
            filtered_movies.append(movie)

    # Ordena os filmes filtrados pela popularidade (avaliação) do maior para o menor
    filtered_movies.sort(key=lambda x: x.get("popularity", 0), reverse=True)

    # Retorna apenas os 50 primeiros resultados para garantir que o front-end carregue instantaneamente
    return format_response(filtered_movies[:50])


def format_response(movies_list: list) -> list:
    """
    Função auxiliar para limpar o payload e retornar apenas o que o front-end pediu:
    Título, capa (poster), gênero e avaliação (popularity).
    """
    return [
        {
            "title": m.get("title"),
            "poster": m.get("poster"),
            "genres": m.get("genres"),
            "evaluation": m.get("popularity")  # Mapeado como a avaliação/popularidade solicitada
        }
        for m in movies_list
    ]