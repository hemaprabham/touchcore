<template>
  <div>
    <input type="file" @change="handleFileUpload">
    <v-btn @click="uploadVideo">Upload</v-btn>
  </div>
</template>

<script>
export default {
  data() {
    return {
      videoFile: null
    };
  },
  methods: {
    handleFileUpload(event) {
      this.videoFile = event.target.files[0];
    },
    async uploadVideo() {
      const formData = new FormData();
      formData.append("video", this.videoFile);
      
      try {
        // Make a POST request to the backend API to upload the video
        const response = await this.$axios.post("/api/upload", formData);
        console.log("Video uploaded:", response.data);
      } catch (error) {
        console.error("Error uploading video:", error);
      }
    }
  }
};
</script>
