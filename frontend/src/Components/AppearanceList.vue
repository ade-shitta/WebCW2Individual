<template>
    <div>
        <h3 class="mt-4">Appearances</h3>
        <ul class="list-group">
            <li class="list-group-item d-flex justify-content-between align-items-center" v-for="appearance in appearances" :key="appearance.id">
                <div>
                    <p>Anime: {{ appearance.anime__title }} - Character: {{ appearance.character__name }}</p>
                    <p>Role: {{ appearance.role }} - Main Character: {{ appearance.is_main_character }}</p>
                </div>
                <button class="btn btn-danger btn-sm" @click="deleteAppearance(appearance.id)">Delete</button>
            </li>
        </ul>
        <button class="btn btn-primary mt-3" data-bs-toggle="modal" data-bs-target="#addAppearanceModal">Add Appearance</button>

        <!-- Add Appearance Modal -->
        <div class="modal fade" id="addAppearanceModal" tabindex="-1" aria-labelledby="addAppearanceModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="addAppearanceModalLabel">Add Appearance</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form @submit.prevent="addAppearance">
                            <div class="mb-3">
                                <label for="anime_id" class="form-label">Anime</label>
                                <select v-model="newAppearance.anime_id" class="form-select" required>
                                    <option v-for="anime in animeList" :key="anime.id" :value="anime.id">{{ anime.title }}</option>
                                </select>
                            </div>
                            <div class="mb-3">
                                <label for="character_id" class="form-label">Character</label>
                                <select v-model="newAppearance.character_id" class="form-select" required>
                                    <option v-for="character in characterList" :key="character.id" :value="character.id">{{ character.name }}</option>
                                </select>
                            </div>
                            <div class="mb-3">
                                <label for="role" class="form-label">Role</label>
                                <input type="text" class="form-control" id="role" v-model="newAppearance.role" required>
                            </div>
                            <div class="form-check mb-3">
                                <input type="checkbox" class="form-check-input" id="is_main_character" v-model="newAppearance.is_main_character">
                                <label class="form-check-label" for="is_main_character">Main Character</label>
                            </div>
                            <button type="submit" class="btn btn-primary">Add Appearance</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            appearances: [],
            animeList: [],
            characterList: [],
            newAppearance: { anime_id: '', character_id: '', role: '', is_main_character: false }
        }
    },
    async mounted() {
        const appearanceResponse = await fetch('http://localhost:8000/api/appearances/');
        this.appearances = await appearanceResponse.json();

        const animeResponse = await fetch('http://localhost:8000/api/anime/');
        this.animeList = await animeResponse.json();

        const characterResponse = await fetch('http://localhost:8000/api/characters/');
        this.characterList = await characterResponse.json();
    },
    methods: {
        async addAppearance() {
            const response = await fetch('http://localhost:8000/api/appearances/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(this.newAppearance)
            });
            const appearance = await response.json();
            this.appearances.push(appearance);
            this.newAppearance = { anime_id: '', character_id: '', role: '', is_main_character: false };
            const modal = bootstrap.Modal.getInstance(document.getElementById('addAppearanceModal'));
            modal.hide();
        },
        async deleteAppearance(id) {
            await fetch(`http://localhost:8000/api/appearances/`, {
                method: 'DELETE',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ id })
            });
            this.appearances = this.appearances.filter(appearance => appearance.id !== id);
        }
    }
}
</script>
