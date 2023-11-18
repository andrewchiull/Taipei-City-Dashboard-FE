<!-- Developed by andrewchiull from ntu777 -->
<!-- [Docs | Taipei City Dashboard](https://tuic.gov.taipei/documentation/front-end/custom-charts) -->

<script setup>
import { ref } from 'vue';
import { useMapStore } from '../../store/mapStore';

// register the four required props
const props = defineProps(['chart_config', 'activeChart', 'series', 'map_config']);
const mapStore = useMapStore();

// Optional.
// a few charts require this to achieve interoperability between chart types.
// const parseSeries = computed(() => {
//     // Parse props.series to compatible format
//     ...
//     return output
// })

// Apexcharts options
const chartOptions = ref({
	chart: {
		stacked: true,
		toolbar: {
			show: false
		},
	},
	colors: props.chart_config.color,
	labels: props.chart_config.categories ? props.chart_config.categories : [],
	plotOptions: {
		boxPlot: {
			colors: {
				upper: '#00E396',
				lower: '#008FFB'
			}
		},
		scatter: {

		}
		
	},
	// [markers – ApexCharts.js](https://apexcharts.com/docs/options/markers/)
	markers: {
		size: 10,
		colors: ["#008FFB", "#00E396"],
		strokeColors: '#fff',
		strokeWidth: 2,
		strokeOpacity: 0.9,
		strokeDashArray: 0,
		fillOpacity: 1,
		discrete: [],
		shape: "circle",
		radius: 2,
		offsetX: 0,
		offsetY: 0,
		onClick: undefined,
		onDblClick: undefined,
		showNullDataPoints: true,
		hover: {
			size: undefined,
			sizeOffset: 3
		}
	},
	xaxis: {
		// type: 'datetime',
		// tooltip: {
		// 	formatter: function (val) {
		// 		return new Date(val).getFullYear()
		// 	}
		// }
	},
	tooltip: {
		shared: false,
		intersect: true
	}


}
)

// Optional
// Required for charts that support map filtering

const selectedIndex = ref(null);

function handleDataSelection(e, chartContext, config) {
	if (!props.chart_config.map_filter) {
		return;
	}
	if (config.dataPointIndex !== selectedIndex.value) {
		mapStore.addLayerFilter(`${props.map_config[0].index}-${props.map_config[0].type}`, props.chart_config.map_filter[0], props.chart_config.map_filter[1][config.dataPointIndex]);
		selectedIndex.value = config.dataPointIndex;
	} else {
		mapStore.clearLayerFilter(`${props.map_config[0].index}-${props.map_config[0].type}`);
		selectedIndex.value = null;
	}
}
</script>

<!-- <apexchart type="boxPlot" height="350" :options="chartOptions" :series="series"></apexchart>
[Vue BoxPlot and Scatter Example – ApexCharts.js](https://apexcharts.com/vue-chart-demos/box-whisker-charts/boxplot-scatter/) -->

<template>
	<div v-if="activeChart === 'BoxPlotChart'">
		<apexchart width="100%" height="270px" type="boxPlot" :options="chartOptions" :series="series"
			@dataPointSelection="handleDataSelection">
		</apexchart>
	</div>
</template>