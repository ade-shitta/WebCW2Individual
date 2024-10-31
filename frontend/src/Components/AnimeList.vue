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
                        <button class="btn btn-primary btn-sm me-2" @click="editAnime(anime)" data-bs-toggle="modal" data-bs-target="#editAnimeModal">
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
                            <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Add Anime</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>

        <!-- Edit Anime Modal -->
        <div class="modal fade" id="editAnimeModal" tabindex="-1" aria-labelledby="editAnimeModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="editAnimeModalLabel">Edit Anime</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form @submit.prevent="updateAnime">
                            <div class="mb-3">
                                <label for="edit_title" class="form-label">Title</label>
                                <input type="text" class="form-control" id="edit_title" v-model="editingAnime.title" required>
                            </div>
                            <div class="mb-3">
                                <label for="edit_description" class="form-label">Description</label>
                                <textarea class="form-control" id="edit_description" v-model="editingAnime.description" required></textarea>
                            </div>
                            <div class="mb-3">
                                <label for="edit_release_date" class="form-label">Release Date</label>
                                <input type="date" class="form-control" id="edit_release_date" v-model="editingAnime.release_date" required>
                            </div>
                            <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Update Anime</button>
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
            newAnime: { title: '', description: '', release_date: '' },
            editingAnime: { id: null, title: '', description: '', release_date: '' }
        }
    },
    async mounted() {
        const response = await fetch('http://localhost:8000/api/anime/');
        this.animes = await response.json();
    },
    methods: {
        async addAnime() {
            try {
                const response = await fetch('http://localhost:8000/api/anime/', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(this.newAnime)
                });
                const data = await response.json();
                this.animes.push(data);
                this.newAnime = { title: '', description: '', release_date: '' };
                const modal = document.getElementById('addAnimeModal');
                const modalInstance = bootstrap.Modal.getInstance(modal);
                modalInstance.hide();
                
                this.$emit('anime-updated');
            } catch (error) {
                console.error('Error adding anime:', error);
            }
        },
        async deleteAnime(id) {
            await fetch(`http://localhost:8000/api/anime/`, {
                method: 'DELETE',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ id })
            });
            this.animes = this.animes.filter(anime => anime.id !== id);
            this.$emit('anime-updated');
        },
        editAnime(anime) {
            this.editingAnime = { ...anime };
        },
        async updateAnime() {
            const response = await fetch('http://localhost:8000/api/anime/', {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(this.editingAnime)
            });
            const updatedAnime = await response.json();
            const index = this.animes.findIndex(a => a.id === updatedAnime.id);
            this.animes[index] = updatedAnime;
            const modal = document.getElementById('editAnimeModal');
            const modalInstance = bootstrap.Modal.getInstance(modal);
            modalInstance.hide();
            this.$emit('anime-updated');
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
