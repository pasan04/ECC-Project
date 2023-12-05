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
                                    <select v-model="gender"
                                            label="Choose Data"
                                            class="form-control">
                                        <option disabled value="">Choose Data</option>
                                        <option value="0">Male</option>
                                        <option value="1">Female</option>
                                    </select>
                                </div>
                            </div>
                            <div class="row" >
                                <div class="col-xl-3">
                                    <label> Air Pollution(1-10)</label>
                                    <input
                                        v-model="airpollution"
                                        v-bind:class="{'form-control': true}"
                                        placeholder="Air Pollution"
                                    />
                                </div>
                                <div class="col-xl-3">
                                    <label> Alcohol use(1-10)</label>
                                    <input
                                        v-model="alcoholuse"
                                        v-bind:class="{'form-control': true}"
                                        placeholder="Alcohol use"
                                    />
                                </div>
                                <div class="col-xl-3">
                                    <label> Dust Allergy(1-10)</label>
                                    <input
                                        v-model="dustallergy"
                                        v-bind:class="{'form-control': true}"
                                        placeholder="Dust Allergy"
                                    />
                                </div>
                            </div>
                            <div class="row" >
                                <div class="col-xl-3">
                                    <label> OccuPational Hazards(1-10)</label>
                                    <input
                                        v-model="occupationalhazards"
                                        v-bind:class="{'form-control': true}"
                                        placeholder="OccuPational Hazards"
                                    />
                                </div>
                                <div class="col-xl-3">
                                    <label> Genetic Risk(1-10)</label>
                                    <input
                                        v-model="geneticrisk"
                                        v-bind:class="{'form-control': true}"
                                        placeholder="Genetic Risk"
                                    />
                                </div>
                                <div class="col-xl-3">
                                    <label> chronic Lung Disease(1-10)</label>
                                    <input
                                        v-model="chroniclungdisease"
                                        v-bind:class="{'form-control': true}"
                                        placeholder="chronic Lung Disease"
                                    />
                                </div>
                            </div>
                            <div class="row" >
                                <div class="col-xl-3">
                                    <label> Balanced Diet(1-10)</label>
                                    <input
                                        v-model="balanceddiet"
                                        v-bind:class="{'form-control': true}"
                                        placeholder="Balanced Diet"
                                    />
                                </div>
                                <div class="col-xl-3">
                                    <label> Obesity(1-10)</label>
                                    <input
                                        v-model="obesity"
                                        v-bind:class="{'form-control': true}"
                                        placeholder="Obesity"
                                    />
                                </div>
                                <div class="col-xl-3">
                                    <label> Smoking(1-10)</label>
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
                    <div class="col-12" v-if="submit_data">
                        <div class="alert alert-info" v-if="result_data>0.90">
                            <p>There is high risk of having lung cancer for the patient. Risk is: {{result_data}}</p>
                        </div>
                        <div class="alert alert-info"  v-if="0.80>result_data>0.90">
                            <p>There is a risk of having lung cancer for the patient. Risk is: {{result_data}}</p>
                        </div>
                        <div class="alert alert-info"  v-if="result_data<0.50">
                            <p>There is a lesser risk of having lung cancer. Risk is: {{result_data}}</p>
                        </div>
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
            result_data: "",
            submit_data: false,
        }
    },
    methods: {
        submitData(){
                this.loading = true;
                this.submit_data = false;
                let dataUrl = constants.url + '/api/getdata';
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
                        this.result_data = res.data.result;
                        console.log(this.result_data)
                        this.loading = false;
                        let message = "Successfully retrieved the data!"
                        this.successShowToast(message);
                        this.submit_data = true;
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