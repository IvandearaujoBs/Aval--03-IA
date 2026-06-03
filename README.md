# 🎬 Plataforma de Recomendação de Filmes

Uma aplicação web interativa para descobrir e buscar filmes por tags, com interface moderna e responsiva.

## 📋 Descrição

A **Plataforma de Recomendação de Filmes** é um exercício de desenvolvimento web que permite aos usuários buscar filmes através de tags (palavras-chave). A aplicação utiliza um algoritmo inteligente que:

- Busca filmes que correspondem às tags inseridas
- Ordena resultados por relevância (quantidade de tags encontradas)
- Utiliza a nota IMDB como critério de desempate
- Exibe informações detalhadas de cada filme (título, rating, tags e descrição)

## 🚀 Recursos

- ✨ **Busca por Tags**: Digite múltiplas tags separadas por vírgulas
- 📊 **Algoritmo Inteligente**: Resultados ordenados por relevância e classificação
- 🎨 **Design Moderno**: Interface dark mode elegante com tema azul
- 📱 **Responsivo**: Funciona em diferentes tamanhos de tela
- ⚡ **Rápido**: Busca instantânea sem necessidade de servidor

## 📁 Estrutura do Projeto

```
movies-tags/
├── index.html           # Arquivo principal (HTML + CSS inline)
├── app.js              # Lógica de recomendação e renderização
├── style.css           # Estilos CSS (opcional, se separado)
└── data/
    └── movies.json     # Base de dados com informações dos filmes
```

## 🛠️ Como Usar

1. **Abra o arquivo `index.html`** em um navegador web
2. **Digite tags** no campo de entrada (ex: "ação, aventura")
3. **Pressione Enter** ou clique em buscar
4. **Veja os resultados** ordenados por relevância

### Exemplos de Tags
- ação
- comédia
- drama
- ficção científica
- aventura
- romance
- terror
- animação

## 📊 Formato dos Dados (movies.json)

Cada filme contém:
```json
{
  "title": "Nome do Filme",
  "rating": 8.5,
  "tags": ["ação", "aventura", "ficção científica"],
  "desc": "Descrição do filme"
}
```

## 💻 Tecnologias Utilizadas

- **HTML5**: Estrutura semântica
- **CSS3**: Estilização moderna com CSS Variables
- **JavaScript**: Lógica de busca e renderização dinâmica
- **JSON**: Armazenamento de dados dos filmes

## 🎯 Funcionalidades Técnicas

### Busca e Filtragem
O algoritmo processa a entrada do usuário:
1. Divide por vírgulas
2. Remove espaços em branco
3. Converte para minúsculas
4. Filtra tags vazias

### Classificação de Resultados
1. **Relevância Primária**: Quantidade de tags encontradas (matchCount)
2. **Relevância Secundária**: Nota IMDB (rating)

## 📝 Exemplo de Uso

**Entrada**: "ação, ficção"
**Resultado**: Filmes que contêm as tags "ação" e/ou "ficção", ordenados primeiro pelos que têm ambas as tags, depois pelos que têm uma, ordenados por rating dentro de cada grupo.

## 🎨 Paleta de Cores

- **Fundo**: #0f1014 (Cinza muito escuro)
- **Superfícies**: #1a1c23 (Cinza escuro)
- **Primária**: #3b82f6 (Azul)
- **Texto Principal**: #f8fafc (Branco frio)
- **Texto Secundário**: #94a3b8 (Cinza claro)

## 📌 Notas

- Este é um projeto educacional de avaliação
- Não requer backend ou servidor externo
- Todos os dados estão armazenados localmente em JSON
- A interface é totalmente responsiva

## 👨‍💻 Autor

Projeto de Avaliação - Exercício de Desenvolvimento Web

---

**Versão**: 1.0  
**Data**: junho de 2026

