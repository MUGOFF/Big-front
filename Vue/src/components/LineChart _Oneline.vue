<template>
    <Line
      id="my-chart-id"
      :options="chartOptions"
      :data="chartData"
      :width="null"
      :height="null"
    />
  </template>
  
  <script>
  import { Line } from 'vue-chartjs'
  import { Chart as ChartJS, Title, Tooltip, Legend, PointElement, LineElement, CategoryScale, LinearScale } from 'chart.js'
import { hide } from '@popperjs/core'
  
  ChartJS.register(Title, Tooltip, Legend, LineElement, PointElement, CategoryScale, LinearScale)
  
  export default {
    name: 'LineChart',
    components: { Line },
    props: {
      'xlabel': {type: Object}, 
      'datas': {type: Object},
      'legend': {type: String},
    },
    // mounted () {
    //   this.renderChart(this.chartData, this.chartOptions)
    // },
    data() {
      return {
        chartData: {
          labels: this.xlabel,
          datasets: [
            {
              label: this.legend,
              backgroundColor:'#F19823',
              borderColor: '#F19823',
              tension: 0.3,
              data: this.datas
            },
          ]
        },
        chartOptions: {
          responsive: true,
          maintainAspectRatio: false,
          pointRadius: 3,
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