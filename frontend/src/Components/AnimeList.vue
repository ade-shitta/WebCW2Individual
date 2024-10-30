<template>
    <div>
        <h3 class="mt-4">Anime List</h3>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Title</th>
                    <th>Description</th>
                    <th>Release Date</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(anime, index) in animes" :key="anime.id">
                    <td>{{ index + 1 }}</td>
                    <td>{{ anime.title }}</td>
                    <td>{{ anime.description }}</td>
                    <td>{{ anime.release_date }}</td>
                    <td>
                        <button class="btn btn-primary btn-sm me-2">
                            <i class="bi bi-pencil-square"></i>
                        </button>
                        <button class="btn btn-danger btn-sm" @click="deleteAnime(anime.id)">
                            <i class="bi bi-trash"></i>
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
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

<style scoped>
.table {
    width: 100%;
    margin-top: 1rem;
}
.btn i {
    margin-right: 0.25rem;
}
</style>
