import Vue from 'vue';
import VueRouter from 'vue-router';
import charts from '../views/charts.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    component: charts,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
