<template>
  <div>
      <h3 class="mt-4">Character List</h3>
      <table class="table table-striped">
          <thead>
              <tr>
                  <th>#</th>
                  <th>Character</th>
                  <th>Description</th>
                  <th>Actions</th>
              </tr>
          </thead>
          <tbody>
              <tr v-for="(character, index) in characters" :key="character.id">
                  <td>{{ index + 1 }}</td>
                  <td>{{ character.name }}</td>
                  <td>{{ character.bio }}</td>
                  <td>
                      <button class="btn btn-primary btn-sm me-2">
                          <i class="bi bi-pencil-square"></i>
                      </button>
                      <button class="btn btn-danger btn-sm" @click="deleteCharacter(character.id)">
                          <i class="bi bi-trash"></i>
                      </button>
                  </td>
              </tr>
          </tbody>
      </table>
      <button class="btn btn-primary mt-3" data-bs-toggle="modal" data-bs-target="#addCharacterModal">Add Character</button>

      <!-- Add Character Modal -->
      <div class="modal fade" id="addCharacterModal" tabindex="-1" aria-labelledby="addCharacterModalLabel" aria-hidden="true">
          <div class="modal-dialog">
              <div class="modal-content">
                  <div class="modal-header">
                      <h5 class="modal-title" id="addCharacterModalLabel">Add Character</h5>
                      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                      <form @submit.prevent="addCharacter">
                          <div class="mb-3">
                              <label for="name" class="form-label">Name</label>
                              <input type="text" class="form-control" id="name" v-model="newCharacter.name" required>
                          </div>
                          <div class="mb-3">
                              <label for="bio" class="form-label">Bio</label>
                              <textarea class="form-control" id="bio" v-model="newCharacter.bio" required></textarea>
                          </div>
                          <button type="submit" class="btn btn-primary">Add Character</button>
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
          characters: [],
          newCharacter: { name: '', bio: '' }
      }
  },
  async mounted() {
      const response = await fetch('http://localhost:8000/api/characters/');
      this.characters = await response.json();
  },
  methods: {
      async addCharacter() {
          const response = await fetch('http://localhost:8000/api/characters/', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(this.newCharacter)
          });
          const character = await response.json();
          this.characters.push(character);
          this.newCharacter = { name: '', bio: '' };
          const modal = bootstrap.Modal.getInstance(document.getElementById('addCharacterModal'));
          modal.hide();
      },
      async deleteCharacter(id) {
          await fetch(`http://localhost:8000/api/characters/`, {
              method: 'DELETE',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ id })
          });
          this.characters = this.characters.filter(character => character.id !== id);
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
