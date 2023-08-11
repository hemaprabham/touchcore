<template>
  <div>
    <video ref="videoPlayer" class="video-js"></video>
    <div class="subtitles-container">
      <p v-for="subtitle in subtitles" :key="subtitle.timestamp">{{ subtitle.text }}</p>
    </div>
  </div>
</template>

<script>
import videojs from 'video.js';

export default {
  props: ['src', 'subtitles'],
  mounted() {
    // Initialize the Video.js player
    this.player = videojs(this.$refs.videoPlayer, {
      sources: [{ src: this.src, type: 'video/mp4' }]
    });

    // Update subtitles on timeupdate event
    this.player.on('timeupdate', this.handleTimeUpdate);
  },
  methods: {
    handleTimeUpdate() {
      const currentTime = this.player.currentTime();
      // Find the active subtitle based on the current time
      const activeSubtitle = this.subtitles.find(subtitle =>
        subtitle.timestamp <= currentTime
      );

      // Display the active subtitle
      if (activeSubtitle) {
        this.$refs.subtitlesContainer.scrollTop = this.$refs.subtitlesContainer.scrollHeight;
      }
    }
  },
  beforeDestroy() {
    // Dispose of the Video.js player to prevent memory leaks
    if (this.player) {
      this.player.dispose();
    }
  }
};
</script>

<style scoped>
/* Style the subtitles container */
.subtitles-container {
  position: absolute;
  bottom: 10px;
  left: 50%;
  transform: translateX(-50%);
  background-color: rgba(0, 0, 0, 0.7);
  padding: 10px;
  color: white;
}
</style>
