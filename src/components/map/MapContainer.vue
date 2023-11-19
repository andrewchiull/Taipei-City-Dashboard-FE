<!-- Developed by Taipei Urban Intelligence Center 2023 -->

<script setup>
import { onMounted, ref } from "vue";
import { useMapStore } from "../../store/mapStore";
import { useDialogStore } from "../../store/dialogStore";
import { useContentStore } from "../../store/contentStore";

import MobileLayers from "../dialogs/MobileLayers.vue";

const mapStore = useMapStore();
const dialogStore = useDialogStore();
const contentStore = useContentStore();

const newSavedLocation = ref("");

function handleSubmitNewLocation() {
	mapStore.addNewSavedLocation(newSavedLocation.value);
	newSavedLocation.value = "";
}

onMounted(() => {
	mapStore.initializeMapBox();
});

const categories = ref([
	{ name: "Category A", selected: false },
	{ name: "Category B", selected: false },
	// 添加更多的虚构类别数据
]);
</script>

<template>
	<div class="mapcontainer">
		<div id="mapboxBox">
			<div
				class="mapcontainer-loading"
				v-if="mapStore.loadingLayers.length > 0"
			>
				<div></div>
			</div>
			<button
				class="mapcontainer-layers show-if-mobile"
				@click="dialogStore.showDialog('mobileLayers')"
			>
				<span>layers</span>
			</button>
			<!-- The key prop informs vue that the component should be updated when switching dashboards -->
			<MobileLayers :key="contentStore.currentDashboard.index" />
		</div>
		<div id="map-control-panel" class="map-control-panel"></div>
		<div class="mapcontainer-controls hide-if-mobile">
			<button
				@click="
					mapStore.easeToLocation([
						[121.536609, 25.044808],
						12.5,
						0,
						0,
					])
				"
			>
				返回預設
			</button>
			<div
				v-for="(item, index) in mapStore.savedLocations"
				:key="`${item[4]}-${index}`"
			>
				<button @click="mapStore.easeToLocation(item)">
					{{ item[4] }}
				</button>
				<div
					class="mapcontainer-controls-delete"
					@click="mapStore.removeSavedLocation(index)"
				>
					<span>delete</span>
				</div>
			</div>
			<input
				v-if="mapStore.savedLocations.length < 10"
				type="text"
				placeholder="新增後按Enter"
				v-model="newSavedLocation"
				maxlength="6"
				@focusout="newSavedLocation = ''"
				@keypress.enter="handleSubmitNewLocation"
			/>
		</div>
	</div>
</template>

<style scoped lang="scss">
.mapcontainer {
	position: relative;
	width: 100%;
	height: calc(100%);
	flex: 1;

	&-loading {
		position: absolute;
		top: 110px;
		right: 10px;
		display: flex;
		align-items: center;
		justify-content: center;
		z-index: 20;

		@media (max-width: 1000px) {
			top: 145px;
		}

		div {
			width: 1.3rem;
			height: 1.3rem;
			border-radius: 50%;
			border: solid 4px var(--color-border);
			border-top: solid 4px var(--color-highlight);
			animation: spin 0.7s ease-in-out infinite;
		}
	}

	&-controls {
		display: flex;
		margin-top: 8px;
		overflow: visible;

		button {
			height: 1.5rem;
			width: fit-content;
			margin-right: 6px;
			padding: 4px;
			border-radius: 5px;
			background-color: var(--color-component-background);
			color: var(--color-complement-text);

			&:focus {
				animation-name: colorfade;
				animation-duration: 4s;
			}
		}

		div {
			position: relative;
			overflow: visible;

			div {
				width: 1.2rem;
				height: 1.2rem;
				position: absolute;
				display: flex;
				align-items: center;
				justify-content: center;
				top: -0.5rem;
				right: -0.3rem;
				border-radius: 50%;
				opacity: 0;
				background-color: var(--color-border);
				box-shadow: 0 0 3px black;
				transition: opacity 0.2s;
				z-index: 10;
				pointer-events: none;
				cursor: pointer;

				span {
					color: rgb(185, 185, 185);
					font-family: var(--font-icon);
					font-size: 0.8rem;
					transition: color 0.2s;
				}

				&:hover span {
					color: rgb(255, 65, 44);
				}
			}

			&:hover div {
				opacity: 1;
				pointer-events: all;
			}
		}

		input {
			height: calc(1.5rem - 4px);
			width: 1.7rem;
			margin-right: 6px;
			padding: 2px 4px;
			border-radius: 5px;
			border: none;
			background-color: rgb(30, 30, 30);
			color: var(--color-complement-text);
			font-size: 0.82rem;

			&:focus {
				width: 5.4rem;
			}
		}
	}

	&-layers {
		width: 1.75rem;
		height: 1.75rem;
		display: flex;
		align-items: center;
		justify-content: center;
		position: absolute;
		right: 10px;
		top: 108px;
		border-radius: 50%;
		background-color: white;
		z-index: 1;

		span {
			color: var(--color-component-background);
			font-size: 1.2rem;
			font-family: var(--font-icon);
		}
	}
}

#mapboxBox {
	width: 100%;
	height: calc(100% - 32px);
	border-radius: 5px;

	@media (max-width: 1000px) {
		height: 100%;
	}
}

@keyframes colorfade {
	0% {
		color: var(--color-highlight);
	}

	75% {
		color: var(--color-highlight);
	}

	100% {
		color: var(--color-complement-text);
	}
}

@keyframes spin {
	to {
		transform: rotate(360deg);
	}
}

.map-control-panel {
	font: 12px/20px "Helvetica Neue", Arial, Helvetica, sans-serif;
	background-color: #fff; /* 将背景颜色更改为白色 */
	font-weight: 600;
	position: absolute;
	top: 10px;
	left: 10px;
	z-index: 9999;
	border-radius: 3px;
	color: #000; /* 设置文本颜色为黑色 */
}

// .filter-group input[type="checkbox"]:first-child + label {
// 	border-radius: 3px 3px 0 0;
// }

// .filter-group label:last-child {
// 	border-radius: 0 0 3px 3px;
// 	border: none;
// }

// .filter-group input[type="checkbox"] {
// 	display: none;
// }

// .filter-group input[type="checkbox"] + label {
// 	background-color: #3386c0;
// 	display: block;
// 	cursor: pointer;
// 	padding: 10px;
// 	border-bottom: 1px solid rgba(0, 0, 0, 0.25);
// }

// .filter-group input[type="checkbox"] + label {
// 	background-color: #3386c0;
// 	text-transform: capitalize;
// }

// .filter-group input[type="checkbox"] + label:hover,
// .filter-group input[type="checkbox"]:checked + label {
// 	background-color: #4ea0da;
// }

// .filter-group input[type="checkbox"]:checked + label:before {
// 	content: "✔";
// 	margin-right: 5px;
// }
</style>
