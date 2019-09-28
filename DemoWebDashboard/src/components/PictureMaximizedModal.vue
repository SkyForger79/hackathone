<template>
  <div :class="{'picture-modal': true, alert: true, 'alert-danger': isDangerLevel, 'alert-warning': isWarningLevel }">
    <img :src="fullpath">
    <button class="flat-btn" @click="minimize()">X</button>
  </div>
</template>

<script>
export default {
  props: ['path', 'level', 'host'],
  computed: {
    isDangerLevel() {
      return this.level == 'danger';
    },
    isWarningLevel() {
      return this.level == 'warning';
    },
    fullpath() {
      return this.host + '/upload/' + this.path;
    }
  },
  methods: {
    minimize() {
      this.$emit('minimize');
    }
  }
}
</script>