<template>
  <div>
    <input type="text" v-model="subtitleText" placeholder="Enter subtitle text">
    <input type="number" v-model="timestamp" placeholder="Timestamp (seconds)">
    <v-btn @click="addSubtitle">Add Subtitle</v-btn>
  </div>
</template>

<script>
export default {
  data() {
    return {
      subtitleText: "",
      timestamp: 0
    };
  },
  methods: {
    addSubtitle() {
      const newSubtitle = {
        text: this.subtitleText,
        timestamp: this.timestamp
      };

      // Emit an event to parent component to handle subtitle addition
      this.$emit("subtitleAdded", newSubtitle);

      // Clear input fields
      this.subtitleText = "";
      this.timestamp = 0;
    }
  }
};
</script>
