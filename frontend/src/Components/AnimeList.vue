<template>
    <div>
        <h3 class="mt-4">Anime</h3>
        <ul class="list-group">
            <li class="list-group-item d-flex justify-content-between align-items-center" v-for="anime in animes" :key="anime.id">
                <div>
                    <h5>{{ anime.title }}</h5>
                    <p>{{ anime.description }}</p>
                    <p>Release Date: {{ anime.release_date }}</p>
                </div>
                <button class="btn btn-danger btn-sm" @click="deleteAnime(anime.id)">Delete</button>
            </li>
        </ul>
        <button class="btn btn-primary mt-3" data-bs-toggle="modal" data-bs-target="#addAnimeModal">Add Anime</button>

        <!-- Add Anime Modal -->
        <div class="modal fade" id="addAnimeModal" tabindex="-1" aria-labelledby="addAnimeModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="addAnimeModalLabel">Add Anime</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form @submit.prevent="addAnime">
                            <div class="mb-3">
                                <label for="title" class="form-label">Title</label>
                                <input type="text" class="form-control" id="title" v-model="newAnime.title" required>
                            </div>
                            <div class="mb-3">
                                <label for="description" class="form-label">Description</label>
                                <textarea class="form-control" id="description" v-model="newAnime.description" required></textarea>
                            </div>
                            <div class="mb-3">
                                <label for="release_date" class="form-label">Release Date</label>
                                <input type="date" class="form-control" id="release_date" v-model="newAnime.release_date" required>
                            </div>
                            <button type="submit" class="btn btn-primary">Add Anime</button>
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
            animes: [],
            newAnime: { title: '', description: '', release_date: '' }
        }
    },
    async mounted() {
        const response = await fetch('http://localhost:8000/api/anime/');
        this.animes = await response.json();
    },
    methods: {
        async addAnime() {
            const response = await fetch('http://localhost:8000/api/anime/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(this.newAnime)
            });
            const anime = await response.json();
            this.animes.push(anime);
            this.newAnime = { title: '', description: '', release_date: '' };
            const modal = bootstrap.Modal.getInstance(document.getElementById('addAnimeModal'));
            modal.hide();
        },
        async deleteAnime(id) {
            await fetch(`http://localhost:8000/api/anime/`, {
                method: 'DELETE',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ id })
            });
            this.animes = this.animes.filter(anime => anime.id !== id);
        }
    }
}
</script>
