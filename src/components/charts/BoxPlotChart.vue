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
	// colors: props.chart_config.color,

	legend: {
		show: true
	},

	stroke: {
		// of boxPlot
		show: true,
		colors: ["#FFFFFF"],
		width: 2,
	},

	plotOptions: {
		boxPlot: {
			colors: {
				upper: '#2dcfa1',
				lower: '#1155a8'
			}
		}
	},





	// Outliers
	markers: {
		colors: ["#888787"],
		size: 5,
		strokeColors: '#FFFFFF',
		strokeWidth: 2,
	},


	xaxis: {
		labels: {
			// show: false
		},
		tooltip: {
			enabled: false
		},
	},
	yaxis: {
		tickAmount: 5,
		min: 0,
		max: 100,
	},

	// Customized tooltip by tuic
	tooltip: {
		theme: "dark"

		// // The class "chart-tooltip" could be edited in /assets/styles/chartStyles.css
		// custom: function ({ series, seriesIndex, dataPointIndex, w }) {
		// 	return '<div class="chart-tooltip">' +
		// 		'<h6>' + w.globals.labels[dataPointIndex] + `${props.chart_config.categories ? '-' + w.globals.seriesNames[seriesIndex] : ''}` + '</h6>' +
		// 		'<span>' + series[seriesIndex][dataPointIndex] + ` ${props.chart_config.unit}` + '</span>' +
		// 		'</div>';
		// },
	},

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
	<apexchart
		width="100%"
		height="270px"
		type="boxPlot" 
		:options="chartOptions" 
		:series="series"
		@dataPointSelection="handleDataSelection"
		>
	</apexchart>
	</div>
</template>