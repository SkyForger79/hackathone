<template>
  <div
    :class="{alert: true, 'alert-danger': isDangerLevel, 'alert-warning': isWarningLevel}"
    style="display:flex;justify-content:space-between;align-items:center"
    data-notify="container"
  >
    <div style="display:flex;align-items:center">
      <i style="display:block" class="material-icons">add_alert</i>
      <div style="padding-left:10px" data-notify="message">{{ item.body }}</div>
    </div>
    <button class="flat-btn" @click="maximize()">
      <i style="color:white" class="material-icons">insert_photo</i>
    </button>
    <picture-modal
      :level="item.level"
      :host="this.host"
      :path="item.img"
      v-if="maximized"
      @minimize="minimize()"
    />
  </div>
</template>

<script>
import PictureMaximizedModal from './PictureMaximizedModal';

export default {
  components: {
    'picture-modal': PictureMaximizedModal,
  },
  props: [ 'item', 'host' ],
  computed: {
    isDangerLevel() {
      return this.item.level == 'danger';
    },
    isWarningLevel() {
      return this.item.level == 'warning';
    }
  },
  mounted() {
    console.log(this.item);
  },
  data() {
    return {
      maximized: false
    }
  },
  methods: {
    maximize() {
      this.maximized = true;
    },
    minimize() {
      this.maximized = false;
    }
  }
}
</script>