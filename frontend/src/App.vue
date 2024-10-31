<template>
    <div class="container">
        <h1 class="text-center mt-4">Ade's Anime Records</h1>
        <ul class="nav nav-tabs">
            <li class="nav-item">
                <a class="nav-link active" data-bs-toggle="tab" href="#anime">Anime</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" href="#characters">Characters</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" href="#appearances" @click="onAppearancesTabClick">Appearances</a>
            </li>
        </ul>
        <div class="tab-content">
            <div class="tab-pane fade show active" id="anime">
                <AnimeList 
                    @anime-updated="refreshAppearances" 
                    ref="animeList" 
                />
            </div>
            <div class="tab-pane fade" id="characters">
                <CharacterList 
                    @character-updated="refreshAppearances" 
                    ref="characterList" 
                />
            </div>
            <div class="tab-pane fade" id="appearances">
                <AppearanceList ref="appearanceList" />
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
    methods: {
        onAppearancesTabClick() {
            if (this.$refs.appearanceList) {
                this.$refs.appearanceList.fetchAppearances();
            }
        },
        refreshAppearances() {
            if (this.$refs.appearanceList) {
                this.$refs.appearanceList.fetchAppearances();
            }
        }
    }
}
</script>

<style scoped>
.container {
    width: 100%;
    margin: 0 auto;
}
</style>
