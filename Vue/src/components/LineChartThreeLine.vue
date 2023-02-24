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
  
  ChartJS.register(Title, Tooltip, Legend, LineElement, PointElement, CategoryScale, LinearScale)
  
  export default {
    name: 'LineChart',
    components: { Line },
    props: {
      'xlabel': {type: Object}, 
      'datas': {type: Object},
      'legend': {type: Array},
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
              label: this.legend[0],
              backgroundColor:'#F19823',
              borderColor: '#F19823',
              data: this.datas[0]
            },
            {
              label: this.legend[1],
              backgroundColor:'#FF88AA',
              borderColor: '#FF88AA',
              data: this.datas[1]
            },
            {
              label: this.legend[2],
              backgroundColor:'#5555FF',
              borderColor: '#5555FF',
              data: this.datas[2]
            },
          ]
        },
        chartOptions: {
          responsive: true,
          maintainAspectRatio: false
        }
      }
    }
  }
  </script>