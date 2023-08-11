<template>
  <div>
    <canvas ref="chartCanvas"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js';

export default {
  props: ['data'],
  mounted() {
    this.createChart();
  },
  methods: {
    createChart() {
      const ctx = this.$refs.chartCanvas.getContext('2d');
      new Chart(ctx, {
        type: 'line',
        data: {
          labels: this.data.labels,
          datasets: [
            {
              label: 'Sentiment Analysis',
              data: this.data.values,
              borderColor: 'rgba(75, 192, 192, 1)',
              fill: false
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false
        }
      });
    }
  }
};
</script>

<style scoped>
canvas {
  width: 100%;
  height: 300px;
}
</style>
