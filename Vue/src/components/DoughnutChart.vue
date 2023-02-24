<template>
  <Doughnut :data="data" :options="options" />
</template>

<script>
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
import { Doughnut } from 'vue-chartjs'

ChartJS.register(ArcElement, Tooltip, Legend)

export default {
  name: 'DoughnutChart',
  components: {
    Doughnut
  },
  data() {
    return {
      data: {
        labels: ['No', 'Yes'],
        datasets: [
          {
            backgroundColor: ['rgb(235, 235, 235)','#9ac486'],
            data: [6, 6]
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: false
          }
        }
      }
    }
  }
}
</script>
