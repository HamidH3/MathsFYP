<template>
    <div class="home">
      <h1> Welcome to the Maths Game! </h1>
      <p>🧮 Have fun while learning and improving your math skills! 🚀</p>
  
      <!-- Form to input username -->
      <div class="username-form">
        <input v-model="newUser.username" type="text" placeholder="Enter Username" />
        <button @click="saveUsername" class="btn-saveusername">Save Username</button>
      </div>
  
      <!-- Smaller play game button -->
      <router-link to="/game" class="btn-playgame">🎮 Start Game</router-link>
    </div>
  </template>
  
  <script>
  const baseURL = "http://localhost:8000";
  
  export default {
    name: "HomePage",
    data() {
      return {
        users: [],
        newUser: {
          username: "",
        }
      };
    },
    methods: {
      async saveUsername() {
        if (!this.newUser.username || !this.newUser.username.trim()) {
          alert("Please enter a valid username!");
          return;
        }
        const response = await fetch(`${baseURL}/game/users/create/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            username: this.newUser.username,
          }),
        });
        if (response.ok) {
          const newUser = await response.json();
          this.users.push(newUser);
  
          // Reset users data
          this.newUser = {
            username: '',
          };
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .home {
    text-align: center;
    margin-top: 50px;
    background-color: #B3E5FC;
    padding: 50px 40px; /* Made the padding larger */
    border-radius: 20px;
    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px; /* Space between elements */
  }
  
  h1 {
    color: #FF4081; /* Pink */
    font-family: 'Comic Sans MS', cursive, sans-serif;
    font-size: 36px; /* Increased size */
  }
  
  p {
    color: #51017b; /* Orange */
    font-size: 20px; /* Increased size */
    font-weight: bold;
  }
  
  .username-form {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  
  input[type="text"] {
    padding: 10px;
    font-size: 16px;
    border-radius: 8px;
    border: 1px solid #ddd;
  }
  
  .btn-saveusername {
    display: inline-block;
    background: blue;
    color: white;
    padding: 0.4rem 1.2rem; /* Slightly larger padding */
    font-size: 1rem; /* Larger font size */
    font-weight: bold;
    border-radius: 8px;
    text-decoration: none;
    transition: transform 0.2s, background 0.3s;
  }
  
  .btn-saveusername:hover {
    transform: scale(1.1);
  }
  
  .btn-playgame {
    display: inline-block;
    background: linear-gradient(135deg, #4CAF50, #8BC34A); /* Green gradient */
    color: white;
    padding: 8px 16px; /* Smaller padding */
    font-size: 16px; /* Smaller font size */
    font-weight: bold;
    border-radius: 30px;
    text-decoration: none;
    transition: transform 0.2s, background 0.3s;
  }
  
  .btn-playgame:hover {
    background: linear-gradient(135deg, #43A047, #7CB342); /* Darker green */
    transform: scale(1.1);
  }
  </style>
  