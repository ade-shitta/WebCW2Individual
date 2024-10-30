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
                <a class="nav-link" data-bs-toggle="tab" href="#appearances">Appearances</a>
            </li>
        </ul>
        <div class="tab-content">
            <div class="tab-pane fade show active" id="anime">
                <AnimeList />
            </div>
            <div class="tab-pane fade" id="characters">
                <CharacterList />
            </div>
            <div class="tab-pane fade" id="appearances">
                <AppearanceList />
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
    }
}
</script>

<style scoped>
.container {
    max-width: 800px;
    margin: 0 auto;
}
</style>
