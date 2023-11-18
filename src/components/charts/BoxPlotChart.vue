<!-- Developed by andrewchiull from ntu777 -->

<script setup>
import { ref } from 'vue';
import { useMapStore } from '../../store/mapStore';

const props = defineProps(['chart_config', 'activeChart', 'series', 'map_config']);
const mapStore = useMapStore();

const chartOptions = ref({
})

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
			@dataPointSelection="handleDataSelection">
		</apexchart>
	</div>
</template>