<template>
  <div>
    <md-table v-model="users" :table-header-color="tableHeaderColor">
      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="№">{{ item.number }}</md-table-cell>
        <md-table-cell md-label="Важность">{{ item.type }}</md-table-cell>
        <md-table-cell md-label="Описание">{{ item.content }}</md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<script>
export default {
  name: "ordered-table",
  props: {
    tableHeaderColor: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      selected: [],
      users: [
        {
          number: 1,
          type: "Критично",
          content: "Вы засыпаете за компьютером. Вам следует делать перерывы по 5-7 минут каждые полчаса, иначе посадите себе глаза."
        },
        {
          number: 2,
          type: "На всякий",
          content: "Ваши глаза слишком близко к монитору. Возможно, это связано с неправильной осанкой, но может быть вы просто сидите слишком близко к экрану. Последите за этим."
        }
      ]
    };
  }
};
</script>
