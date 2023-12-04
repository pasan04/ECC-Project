<template>
    <main>
        <Modal :isOpen="modalIsOpen" @cancel="closeModal" :osomeURL="this.osomeURL" :officialURL="this.officialURL" :header="this.header_text"/>
        <div class="container-fluid px-4">
            <h1 class="page-title">Lung Cancer <span class="subtitle">- Prediction</span></h1>
            <div class="col-12">
                <div class="alert alert-info">
                    <p>Lung cancer is the leading cause of cancer death worldwide, accounting for 1.59 million deaths in 2018. The majority of lung cancer cases are attributed to smoking, but exposure to air pollution is also a risk factor. Here is a prediction to find the probability of having a lung cancer based on the specific criteria.</p>
                </div>
            </div>
            <div class="row">
                <div class="col-xl-12">
                    <div class="card mb-4">
                        <div class="card-body">
                            <div class="row" >
                                <div class="col-xl-3">
                                    <label> Patient Id</label>
                                    <input
                                        v-model="partientId"
                                        v-bind:class="{'form-control': true}"
                                        placeholder="Patient Id"
                                    />
                                </div>
                                <div class="col-xl-3">
                                    <label> Age</label>
                                    <input
                                        v-model="age"
                                        v-bind:class="{'form-control': true}"
                                        placeholder="Age"
                                    />
                                </div>
                                <div class="col-xl-3">
                                    <label> Gender</label>
                                    <input
                                        v-model="gender"
                                        v-bind:class="{'form-control': true}"
                                        placeholder="Gender"
                                    />
                                </div>
                            </div>
                            <div class="row" >
                                <div class="col-xl-3">
                                    <label> Air Pollution</label>
                                    <input
                                        v-model="airpollution"
                                        v-bind:class="{'form-control': true}"
                                        placeholder="Patient Id"
                                    />
                                </div>
                                <div class="col-xl-3">
                                    <label> Alcohol use</label>
                                    <input
                                        v-model="alcoholuse"
                                        v-bind:class="{'form-control': true}"
                                        placeholder="Account Id"
                                    />
                                </div>
                                <div class="col-xl-3">
                                    <label> Dust Allergy</label>
                                    <input
                                        v-model="dustallergy"
                                        v-bind:class="{'form-control': true}"
                                        placeholder="Account Id"
                                    />
                                </div>
                            </div>
                            <div class="row" >
                                <div class="col-xl-3">
                                    <label> OccuPational Hazards</label>
                                    <input
                                        v-model="occupationalhazards"
                                        v-bind:class="{'form-control': true}"
                                        placeholder="Patient Id"
                                    />
                                </div>
                                <div class="col-xl-3">
                                    <label> Genetic Risk</label>
                                    <input
                                        v-model="geneticrisk"
                                        v-bind:class="{'form-control': true}"
                                        placeholder="Account Id"
                                    />
                                </div>
                                <div class="col-xl-3">
                                    <label> chronic Lung Disease</label>
                                    <input
                                        v-model="chroniclungdisease"
                                        v-bind:class="{'form-control': true}"
                                        placeholder="Account Id"
                                    />
                                </div>
                            </div>
                            <div class="row" >
                                <div class="col-xl-3">
                                    <label> Balanced Diet</label>
                                    <input
                                        v-model="balanceddiet"
                                        v-bind:class="{'form-control': true}"
                                        placeholder="Balanced Diet"
                                    />
                                </div>
                                <div class="col-xl-3">
                                    <label> Obesity</label>
                                    <input
                                        v-model="obesity"
                                        v-bind:class="{'form-control': true}"
                                        placeholder="Obesity"
                                    />
                                </div>
                                <div class="col-xl-3">
                                    <label> Smoking</label>
                                    <input
                                        v-model="smoking"
                                        v-bind:class="{'form-control': true}"
                                        placeholder="Smoking"
                                    />
                                </div>
                            </div>
                            <div class="row" style="margin-top: 23px;">
                                <div class="col-md-12 text-right">
                                    <button type="button" class="btn btn-primary" @click="submitData" style="margin-right: 20px">Get Result</button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div style="display: flex; justify-content: center; align-items: center; margin-top: 100px" v-if="loading">
                        <hollow-dots-spinner
                            :animation-duration="1000"
                            :dot-size="15"
                            :dots-num="3"
                            color="#ff1d5e"
                        />
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import axios from "axios";
import * as constants from "@/shared/Constants";
import { HollowDotsSpinner } from 'epic-spinners'
import {toast} from "vue3-toastify";
import Modal from "@/components/Modal.vue";

export default {
    name: 'timelinestatus',
    components: {
        HollowDotsSpinner,
        Modal
    },
    data() {
        return {
            partientId: "",
            age: "",
            gender: "",
            airpollution:"",
            alcoholuse: "",
            dustallergy: "",
            occupationalhazards: "",
            geneticrisk: "",
            chroniclungdisease: "",
            balanceddiet: "",
            obesity: "",
            smoking: "",
            loading: false,
        }
    },
    methods: {
        submitData(){
                this.loading = true;
                this.statusesArray = [];
                let dataUrl = constants.url + '/api/submitcancerresult';
                let requestData = {
                    partientId: this.partientId,
                    age: this.age,
                    gender: this.gender,
                    airpollution: this.airpollution,
                    alcoholuse: this.alcoholuse,
                    dustallergy: this.dustallergy,
                    occupationalhazards: this.occupationalhazards,
                    geneticrisk: this.geneticrisk,
                    chroniclungdisease: this.chroniclungdisease,
                    balanceddiet: this.balanceddiet,
                    obesity: this.obesity,
                    smoking: this.smoking,
                };

                axios.post(dataUrl, requestData)
                    .then(res => {
                        let data_received = res.data;
                    })
                    .catch(error => {
                        this.errorShowToast();
                        this.loading = false;
                        console.log(error);
                    });
        },
        errorShowToast(){
            toast.error('Error in retrieving data!', {
                autoClose: 3000,
            })
        },
        successShowToast(message){
            toast.success(message, {
                autoClose: 3000,
            })
        },
        closeModal() {
            this.modalIsOpen = false;
        },
        showModal() {
            this.modalIsOpen = true;
        },
    },
}
</script>
<style src="vue-multiselect/dist/vue-multiselect.css"></style>