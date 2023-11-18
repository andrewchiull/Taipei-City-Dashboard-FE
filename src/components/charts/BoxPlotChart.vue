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

	dataLabels: {
		// enabled: props.chart_config.categories ? false : true,
	},
	legend: {
		show: true
	},
	markers: {
		size: 4,
	},
	stroke: {
		show: true,
		// curve: 'smooth',
		// lineCap: 'butt',
		colors: ["#FFFFFF"],
		width: 1,
		// dashArray: 0,
	},
	plotOptions: {
		boxPlot: {
			// colors: {
			// 	// upper: '#2dcfa1',
			// 	// lower: '#1155a8'
			// }
		},
		scatter: {

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
	},
	yaxis: {
		// show: true,
		// showAlways: true,
		// showForNullSeries: true,
		// seriesName: undefined,
		// opposite: false,
		// reversed: false,
		// logarithmic: false,
		// logBase: 10,
		tickAmount: 5,
		min: 0,
		max: 100,
		// forceNiceScale: false,
		// floating: false,
		// decimalsInFloat: undefined,
		// labels: {
		// 	show: true,
		// 	align: 'right',
		// 	minWidth: 0,
		// 	maxWidth: 160,
		// 	style: {
		// 		colors: [],
		// 		fontSize: '12px',
		// 		fontFamily: 'Helvetica, Arial, sans-serif',
		// 		fontWeight: 400,
		// 		cssClass: 'apexcharts-yaxis-label',
		// 	},
		// 	offsetX: 0,
		// 	offsetY: 0,
		// 	rotate: 0,
		// 	// formatter: (value) => { return val },
		// },
		// axisBorder: {
		// 	show: true,
		// 	color: '#78909C',
		// 	offsetX: 0,
		// 	offsetY: 0
		// },
		// axisTicks: {
		// 	show: true,
		// 	borderType: 'solid',
		// 	color: '#78909C',
		// 	width: 6,
		// 	offsetX: 0,
		// 	offsetY: 0
		// },
		// title: {
		// 	text: undefined,
		// 	rotate: -90,
		// 	offsetX: 0,
		// 	offsetY: 0,
		// 	style: {
		// 		color: undefined,
		// 		fontSize: '12px',
		// 		fontFamily: 'Helvetica, Arial, sans-serif',
		// 		fontWeight: 600,
		// 		cssClass: 'apexcharts-yaxis-title',
		// 	},
		// },
		// crosshairs: {
		// 	show: true,
		// 	position: 'back',
		// 	stroke: {
		// 		color: '#b6b6b6',
		// 		width: 1,
		// 		dashArray: 0,
		// 	},
		// },
		// tooltip: {
		// 	enabled: true,
		// 	offsetX: 0,
		// },

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