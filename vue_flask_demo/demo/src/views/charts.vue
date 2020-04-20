<template>

  <div class="charts">
    <div class="myEcharts" ref="myEcharts" ></div>
  </div>
</template>

<script>
// 导入echarts
import echarts from 'echarts';
import axios from 'axios';

export default {
  mounted() {
    // 基于准备好的dom，初始化echarts实例
    const myChart = echarts.init(this.$refs.myEcharts);
    // ajax 请求
    axios({
      method: 'get',
      url: 'http://127.0.0.1:5000/index',
      data: {},
    }).then((res) => {
      window.console.log(res.data.data);
      // 指定图表的配置项和数据
      // const { data } = res.data.data;
      const keys = [];
      const values = [];
      // console.log(data);
      const { data } = res.data;
      data.forEach((item, index) => {
        console.log(item, index);
        keys.push(item.key);
        values.push(item.value);
      });
      const option = {
        title: {
          text: 'ECharts Demo',
        },
        tooltip: {},
        legend: {
          data: ['销量'],
        },
        xAxis: {
          data: keys,
        },
        yAxis: {},
        series: [{
          name: '销量',
          type: 'bar',
          data: values,
        }],
      };
      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option);
    });
  },
};
</script>
<style lang="less" scoped>
  .myEcharts {
    width: 600px;
    height: 400px;
  }
</style>
