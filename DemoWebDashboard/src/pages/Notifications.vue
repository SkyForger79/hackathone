<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item">
        <md-card>
          <md-card-header data-background-color="green">
            <h4 class="title">Уведомления</h4>
            <!-- <p class="category">
              Handcrafted by us with <i class="fa fa-heart heart"></i>
            </p> -->
          </md-card-header>
          <md-card-content>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100">
                <notification-item v-for="item in items" :key="item.id" :item="item"></notification-item>
              </div>
            </div>
          </md-card-content>
        </md-card>
      </div>
    </div>
  </div>
</template>

<script>

import NotificationItem from '../components/NotificationItem';

export default {
  components: {
    'notification-item': NotificationItem
  },
  data() {
    return {
      type: ["", "info", "success", "warning", "danger"],
      notifications: {
        topCenter: false
      },
      host: 'http://10.70.0.243:9999/v1/',
      items: [
        {
          id: 0,
          level: 'danger',
          body: 'Lorem ipsum',
          head: 'Hello',
          img: 'http://10.70.0.243:9999/v1/uploads/2019.09.28-17.54.54.jpeg'
        },
        {
          id: 1,
          level: 'warning',
          body: 'Lorem ipsum #2',
          head: 'Hello',
          img: 'http://10.70.0.243:9999/v1/uploads/2019.09.28-17.54.54.jpeg'
        },
      ]
    };
  },
  mounted() {
    this.update();
  },
  methods: {
    update() {
      fetch(this.host + 'get_msg')
        .then(response => {
          return response.json();
        })
        .then(items => {
          console.log(items);
          this.items = items;
        })
        .catch(err => console.log(err));
    }
  }
};
</script>
