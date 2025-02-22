<template>
    <div>
      <h1>Real-Time Game Stream</h1>
      <canvas ref="gameCanvas" width="800" height="600"></canvas>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        socket: null,
      };
    },
    mounted() {
      this.setupWebSocket();
    },
    methods: {
      setupWebSocket() {
        this.socket = new WebSocket("ws://localhost:8000/ws/game/");
  
        this.socket.onopen = () => {
          console.log("WebSocket connection established");
        };
  
        this.socket.onmessage = (event) => {
          console.log("Received frame data", event.data);
          this.updateCanvas(event.data);
        };
  
        this.socket.onerror = (error) => {
          console.error("WebSocket error:", error);
        };
  
        this.socket.onclose = () => {
          console.log("WebSocket connection closed");
        };
      },
      updateCanvas(frameData) {
        const img = new Image();
        img.onload = () => {
          const canvas = this.$refs.gameCanvas;
          const ctx = canvas.getContext("2d");
  
          // Clear the previous frame
          ctx.clearRect(0, 0, canvas.width, canvas.height);
          
          // Draw new frame
          ctx.drawImage(img, 0, 0);
        };
        img.src = `data:image/png;base64,${frameData}`;
      },
    },
    beforeDestroy() {
      if (this.socket) {
        this.socket.close();
      }
    },
  };
  </script>
  
  <style scoped>
  canvas {
    border: 1px solid black;
    display: block;
    margin: auto;
  }
  </style>
  