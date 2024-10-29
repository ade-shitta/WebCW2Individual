<template>
    <div>
        <ul class="nav nav-tabs">
            <li class="nav-item">
                <a class="nav-link active" data-bs-toggle="tab" href="#anime">Anime</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" href="#characters">Characters</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" href="#appearances">Appearances</a>
            </li>
        </ul>
        <div class="tab-content">
            <div class="tab-pane fade show active" id="anime">
                <AnimeList 
                    :animes="animeList"
                    @add-anime="addAnime"
                    @delete-anime="deleteAnime"
                />
            </div>
            <div class="tab-pane fade" id="characters">
                <CharacterList 
                    :characters="characterList"
                    @add-character="addCharacter"
                    @delete-character="deleteCharacter"
                />
            </div>
            <div class="tab-pane fade" id="appearances">
                <AppearanceList 
                    :appearances="appearanceList"
                    :animeList="animeList"
                    :characterList="characterList"
                    @add-appearance="addAppearance"
                    @delete-appearance="deleteAppearance"
                />
            </div>
        </div>
    </div>
</template>

<script>
import AnimeList from './Components/AnimeList.vue';
import CharacterList from './Components/CharacterList.vue';
import AppearanceList from './Components/AppearanceList.vue';

export default {
    components: {
        AnimeList,
        CharacterList,
        AppearanceList
    },
    data() {
        return {
            animeList: [],
            characterList: [],
            appearanceList: []
        };
    },
    async mounted() {
        await this.fetchData();
    },
    methods: {
        async fetchData() {
            // Fetch anime data
            const animeResponse = await fetch('http://localhost:8000/api/anime/');
            this.animeList = await animeResponse.json();

            // Fetch character data
            const characterResponse = await fetch('http://localhost:8000/api/characters/');
            this.characterList = await characterResponse.json();

            // Fetch appearance data
            const appearanceResponse = await fetch('http://localhost:8000/api/appearances/');
            this.appearanceList = await appearanceResponse.json();
        },
        async addAnime(anime) {
            const response = await fetch('http://localhost:8000/api/anime/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(anime)
            });
            const newAnime = await response.json();
            // Update the anime list reactively
            this.animeList.push(newAnime);
        },
        async deleteAnime(id) {
            await fetch('http://localhost:8000/api/anime/', {
                method: 'DELETE',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ id })
            });
            this.animeList = this.animeList.filter(anime => anime.id !== id);
        },
        async addCharacter(character) {
            const response = await fetch('http://localhost:8000/api/characters/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(character)
            });
            const newCharacter = await response.json();
            // Update the character list reactively
            this.characterList.push(newCharacter);
        },
        async deleteCharacter(id) {
            await fetch('http://localhost:8000/api/characters/', {
                method: 'DELETE',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ id })
            });
            this.characterList = this.characterList.filter(character => character.id !== id);
        },
        async addAppearance(appearance) {
            const response = await fetch('http://localhost:8000/api/appearances/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(appearance)
            });
            const newAppearance = await response.json();
            // Update the appearance list reactively
            this.appearanceList.push(newAppearance);
        },
        async deleteAppearance(id) {
            await fetch('http://localhost:8000/api/appearances/', {
                method: 'DELETE',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ id })
            });
            this.appearanceList = this.appearanceList.filter(appearance => appearance.id !== id);
        }
    }
}
</script>
