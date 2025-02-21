<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <router-link to="/" class="nav-link">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/leaderboard" class="nav-link">Leaderboard</router-link>
          </li>
        </ul>
      </div>
    </nav>

    <!-- Add margin-top to prevent content from hiding behind the navbar -->
    <div class="container mt-5">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: "App"
};
</script>

<style scoped>

.navbar {
  width: 100%; 
  left: 0; 
  z-index: 1000;
}

body, html {
  padding-top: 56px; 
  min-height: 100vh;
  font-family: 'Arial', sans-serif;
}
</style>
