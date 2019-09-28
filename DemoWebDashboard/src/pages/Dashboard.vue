<template>
  <div class="content">
    <div class="md-layout">
      <div
        class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-50"
      >
        <chart-card
          :chart-data="dailySalesChart.data"
          :chart-options="dailySalesChart.options"
          :chart-type="'Bar'"
          data-background-color="blue"
        >
          <template slot="content">
            <h4 class="title">Усталость нарастает</h4>
            <p class="category">
              <span class="text-danger"
                ><i class="fas fa-long-arrow-alt-down"></i> 69%
              </span>
              Стало хуже
            </p>
          </template>

          <template slot="footer">
            <div class="stats">
              <md-icon>access_time</md-icon>
              обновлено 4 минуты назад
            </div>
          </template>
        </chart-card>
      </div>
      <div
        class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-50"
      >
        <chart-card
          :chart-data="emailsSubscriptionChart.data"
          :chart-options="emailsSubscriptionChart.options"
          :chart-responsive-options="emailsSubscriptionChart.responsiveOptions"
          :chart-type="'Line'"
          data-background-color="red"
        >
          <template slot="content">
            <h4 class="title">Продуктивность сегодня</h4>
            <p class="category">
              Ваше самое продуктивное время: <strong>1am - 3am - типично для айтишника!</strong>
            </p>
          </template>

          <template slot="footer">
            <div class="stats">
              <md-icon>access_time</md-icon>
              обновлено 12 минут назад
            </div>
          </template>
        </chart-card>
      </div>
      <div
        class="md-layout-item md-medium-size-50 md-xsmall-size-100 md-size-33"
      >
        <stats-card data-background-color="green">
          <template slot="header">
            <md-icon>favorite_border</md-icon>
          </template>

          <template slot="content">
            <p class="category">Состояние здоровья</p>
            <h3 class="title"><strong style="color:darkgreen">4.2</strong>/5</h3>
          </template>

          <template slot="footer">
            <div class="stats">
              <md-icon>date_range</md-icon>
              В среднем за 7 дней
            </div>
          </template>
        </stats-card>
      </div>
      <div
        class="md-layout-item md-medium-size-50 md-xsmall-size-100 md-size-33"
      >
        <stats-card data-background-color="orange">
          <template slot="header">
            <md-icon>speed</md-icon>
          </template>

          <template slot="content">
            <p class="category">Продуктивность</p>
            <h3 class="title">
              <strong style="color:darkgreen">88</strong>/100
              <!-- <small>GB</small> -->
            </h3>
          </template>

          <template slot="footer">
            <div class="stats">
              <md-icon>date_range</md-icon>
              В среднем за 7 дней
            </div>
          </template>
        </stats-card>
      </div>
      <div
        class="md-layout-item md-medium-size-50 md-xsmall-size-100 md-size-33"
      >
        <stats-card data-background-color="red">
          <template slot="header">
            <md-icon>warning</md-icon>
          </template>

          <template slot="content">
            <p class="category">Предупреждений</p>
            <h3 class="title">75</h3>
          </template>

          <template slot="footer">
            <div class="stats">
              <md-icon>thumb_down</md-icon>
              Много проблем!
            </div>
          </template>
        </stats-card>
      </div>
      <div
        class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-100"
      >
        <md-card>
          <md-card-header data-background-color="orange">
            <h4 class="title">Рекомендации</h4>
            <p class="category">Стоит прислушаться...</p>
          </md-card-header>
          <md-card-content>
            <ordered-table table-header-color="orange"></ordered-table>
          </md-card-content>
        </md-card>
      </div>
    </div>
  </div>
</template>

<script>
import {
  StatsCard,
  ChartCard,
  NavTabsCard,
  NavTabsTable,
  OrderedTable
} from "@/components";

export default {
  components: {
    StatsCard,
    ChartCard,
    NavTabsCard,
    NavTabsTable,
    OrderedTable
  },
  data() {
    return {
      dailySalesChart: {
        data: {
          labels: ["Пн", "Вт", "Ср", "Чт", "Пт", "Cб", "Вс"],
          series: [[ 10, 9, 18, 20, 25, 5, 6], [ 12, 17, 16, 24, 40, 61, 75]]
        },
        options: {
          lineSmooth: this.$Chartist.Interpolation.cardinal({
            tension: 0
          }),
          low: 0,
          high: 100, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
          chartPadding: {
            top: 0,
            right: 0,
            bottom: 0,
            left: 0
          }
        }
      },
      emailsSubscriptionChart: {
        data: {
          labels: [
            "6am",
            "9am",
            "12am",
            "3pm",
            "6pm",
            "9pm",
            "12pm",
            "3am"
          ],
          series: [[0, 9, 35, 50, 4, 10, 70, 90]]
        },
        options: {
          axisX: {
            showGrid: false
          },
          low: 0,
          high: 120,
          chartPadding: {
            top: 0,
            right: 5,
            bottom: 0,
            left: 0
          }
        },
        responsiveOptions: [
          [
            "screen and (max-width: 640px)",
            {
              seriesBarDistance: 5,
              axisX: {
                labelInterpolationFnc: function(value) {
                  return value[0];
                }
              }
            }
          ]
        ]
      }
    };
  }
};
</script>
