<template>
  <div>
      <h3 class="mt-4">Character List</h3>
      <ul class="list-group">
          <li class="list-group-item d-flex justify-content-between align-items-center" v-for="character in characters" :key="character.id">
              <div>
                  <h5>{{ character.name }}</h5>
                  <p>{{ character.bio }}</p>
              </div>
              <button class="btn btn-danger btn-sm" @click="deleteCharacter(character.id)">Delete</button>
          </li>
      </ul>
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
  props: ['characters'],
  data() {
      return {
          newCharacter: { name: '', bio: '' }
      }
  },
  methods: {
      addCharacter() {
          this.$emit('add-character', this.newCharacter);
          this.newCharacter = { name: '', bio: '' };
          const modal = bootstrap.Modal.getInstance(document.getElementById('addCharacterModal'));
          modal.hide();
      },
      deleteCharacter(id) {
          this.$emit('delete-character', id);
      }
  }
}
</script>
