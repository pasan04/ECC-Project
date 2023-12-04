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
                                        v-bind:class="{'form-control': true, 'is-invalid': searchAccountIdError !== ''}"
                                        placeholder="Patient Id"
                                        @input="keywordInputChanged"
                                    />
                                    <div v-if="searchAccountIdError !== ''" class="invalid-feedback">{{ searchAccountIdError }}</div>
                                </div>
                                <div class="col-xl-3">
                                    <label> Age</label>
                                    <input
                                        v-model="age"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchAccountIdError !== ''}"
                                        placeholder="Age"
                                        v-on:blur="searchAccountIdBlurred = true"
                                        @input="keywordInputChanged"
                                    />
                                    <div v-if="searchAccountIdError !== ''" class="invalid-feedback">{{ searchAccountIdError }}</div>
                                </div>
                                <div class="col-xl-3">
                                    <label> Gender</label>
                                    <input
                                        v-model="gender"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchAccountIdError !== ''}"
                                        placeholder="Gender"
                                        v-on:blur="searchAccountIdBlurred = true"
                                        @input="keywordInputChanged"
                                    />
                                    <div v-if="searchAccountIdError !== ''" class="invalid-feedback">{{ searchAccountIdError }}</div>
                                </div>
                            </div>
                            <div class="row" >
                                <div class="col-xl-3">
                                    <label> Air Pollution</label>
                                    <input
                                        v-model="partientId"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchAccountIdError !== ''}"
                                        placeholder="Patient Id"
                                        v-on:blur="searchAccountIdBlurred = true"
                                        @input="keywordInputChanged"
                                    />
                                    <div v-if="searchAccountIdError !== ''" class="invalid-feedback">{{ searchAccountIdError }}</div>
                                </div>
                                <div class="col-xl-3">
                                    <label> Alcohol use</label>
                                    <input
                                        v-model="sds"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchAccountIdError !== ''}"
                                        placeholder="Account Id"
                                        v-on:blur="searchAccountIdBlurred = true"
                                        @input="keywordInputChanged"
                                    />
                                    <div v-if="searchAccountIdError !== ''" class="invalid-feedback">{{ searchAccountIdError }}</div>
                                </div>
                                <div class="col-xl-3">
                                    <label> Dust Allergy</label>
                                    <input
                                        v-model="sds"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchAccountIdError !== ''}"
                                        placeholder="Account Id"
                                        v-on:blur="searchAccountIdBlurred = true"
                                        @input="keywordInputChanged"
                                    />
                                    <div v-if="searchAccountIdError !== ''" class="invalid-feedback">{{ searchAccountIdError }}</div>
                                </div>
                            </div>
                            <div class="row" >
                                <div class="col-xl-3">
                                    <label> OccuPational Hazards</label>
                                    <input
                                        v-model="partientId"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchAccountIdError !== ''}"
                                        placeholder="Patient Id"
                                        v-on:blur="searchAccountIdBlurred = true"
                                        @input="keywordInputChanged"
                                    />
                                    <div v-if="searchAccountIdError !== ''" class="invalid-feedback">{{ searchAccountIdError }}</div>
                                </div>
                                <div class="col-xl-3">
                                    <label> Genetic Risk</label>
                                    <input
                                        v-model="sds"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchAccountIdError !== ''}"
                                        placeholder="Account Id"
                                        v-on:blur="searchAccountIdBlurred = true"
                                        @input="keywordInputChanged"
                                    />
                                    <div v-if="searchAccountIdError !== ''" class="invalid-feedback">{{ searchAccountIdError }}</div>
                                </div>
                                <div class="col-xl-3">
                                    <label> chronic Lung Disease</label>
                                    <input
                                        v-model="sds"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchAccountIdError !== ''}"
                                        placeholder="Account Id"
                                        v-on:blur="searchAccountIdBlurred = true"
                                        @input="keywordInputChanged"
                                    />
                                    <div v-if="searchAccountIdError !== ''" class="invalid-feedback">{{ searchAccountIdError }}</div>
                                </div>
                            </div>
                            <div class="row" >
                                <div class="col-xl-3">
                                    <label> Balanced Diet</label>
                                    <input
                                        v-model="partientId"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchAccountIdError !== ''}"
                                        placeholder="Patient Id"
                                        v-on:blur="searchAccountIdBlurred = true"
                                        @input="keywordInputChanged"
                                    />
                                    <div v-if="searchAccountIdError !== ''" class="invalid-feedback">{{ searchAccountIdError }}</div>
                                </div>
                                <div class="col-xl-3">
                                    <label> Obesity</label>
                                    <input
                                        v-model="sds"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchAccountIdError !== ''}"
                                        placeholder="Account Id"
                                        v-on:blur="searchAccountIdBlurred = true"
                                        @input="keywordInputChanged"
                                    />
                                    <div v-if="searchAccountIdError !== ''" class="invalid-feedback">{{ searchAccountIdError }}</div>
                                </div>
                                <div class="col-xl-3">
                                    <label> Smoking</label>
                                    <input
                                        v-model="sds"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchAccountIdError !== ''}"
                                        placeholder="Account Id"
                                        v-on:blur="searchAccountIdBlurred = true"
                                        @input="keywordInputChanged"
                                    />
                                    <div v-if="searchAccountIdError !== ''" class="invalid-feedback">{{ searchAccountIdError }}</div>
                                </div>
                            </div>
                            <div class="row" >
                                <div class="col-xl-3">
                                    <label> Passive Smoker</label>
                                    <input
                                        v-model="partientId"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchAccountIdError !== ''}"
                                        placeholder="Patient Id"
                                        v-on:blur="searchAccountIdBlurred = true"
                                        @input="keywordInputChanged"
                                    />
                                    <div v-if="searchAccountIdError !== ''" class="invalid-feedback">{{ searchAccountIdError }}</div>
                                </div>
                                <div class="col-xl-3">
                                    <label> Coughing of Blood</label>
                                    <input
                                        v-model="sds"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchAccountIdError !== ''}"
                                        placeholder="Account Id"
                                        v-on:blur="searchAccountIdBlurred = true"
                                        @input="keywordInputChanged"
                                    />
                                    <div v-if="searchAccountIdError !== ''" class="invalid-feedback">{{ searchAccountIdError }}</div>
                                </div>
                                <div class="col-xl-3">
                                    <label> Data</label>
                                    <input
                                        v-model="sds"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchAccountIdError !== ''}"
                                        placeholder="Account Id"
                                        v-on:blur="searchAccountIdBlurred = true"
                                        @input="keywordInputChanged"
                                    />
                                    <div v-if="searchAccountIdError !== ''" class="invalid-feedback">{{ searchAccountIdError }}</div>
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
            <div class="alert alert-warning" v-if="statusesArray.length === 0 && this.searched">
                <fa icon="exclamation-triangle" /> No data available.
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
import VueMultiselect from "vue-multiselect";

export default {
    name: 'timelinestatus',
    components: {
        HollowDotsSpinner,
        Modal,
        VueMultiselect
    },
    data() {
        return {
            instanceId: "",
            clientKey: null,
            clientSecret: null,
            instanceData:[],
            limitNo: "",
            dataType: "",
            statusesArray: [],
            loading: false,
            instanceIdError: "",
            instanceIdBlurred: false,
            limitNoBlurred: false,
            limitNoError: "",
            dataTypeError: "",
            dataTypeBlurred: false,
            modalIsOpen: false,
            osomeURL: "",
            officialURL: "",
            header_text: "",
            searched: false,
            selectedMastodonInstances: [],
        }
    },
    methods: {
        instanceInputChanged(e){
            let valueReceived = e.target.value;
            if(valueReceived){
                this.instanceIdError = ""
                this.instanceIdBlurred = false;
            }
            this.instanceId = e.target.value;
        },
        isValidInput(inputValue) {
            return inputValue.trim() !== '';
        },
        limitNoInputChanged(e){
            let valueReceived = e.target.value;
            if(valueReceived){
                this.limitNoError = "";
                this.limitNoBlurred = false;
            }
            this.limitNo = e.target.value;
        },
        dataTypeInputChanged(e){
            let valueReceived = e.target.value;
            if(valueReceived){
                this.dataTypeError = "";
                this.dataTypeBlurred = false;
            }
            this.dataType = e.target.value;
        },
        fetchAllInstanceData(){
            let dataUrl = constants.url + '/api/get-instance-data-saved'
            axios.get(dataUrl)
                .then(res => {
                    this.instanceData = res.data;
                }).catch(error => {
                console.log(error);
            });
        },
        submitStatusesSearch(){
            if (!this.isValidInput(this.limitNo)) {
                this.limitNoError = "Please enter limit No";
            }
            if (!this.isValidInput(this.dataType)) {
                this.dataTypeError = "Please enter data type";
            }

            if(this.isValidInput(this.limitNo) && this.isValidInput(this.dataType)) {
                this.header_text = "Search Statuses URL"
                this.loading = true;
                this.statusesArray = [];
                let dataUrl = constants.url + '/api/timeline-statuses';
                let requestData = {
                    mastodon_instances: this.selectedMastodonInstances,
                    data_type: this.dataType,
                    limit_no: this.limitNo
                };

                let jsonData = JSON.stringify(requestData);

                this.osomeURL = `curl -X POST -H "Content-Type: application/json" -d '${jsonData}' "https://osome.iu.edu/tools/mastodon/api/timeline-statuses"`;
                this.officialURL = "https://"+this.selectedMastodonInstances[0].name+ "/api/v1/timelines/public?local="+this.dataType+"&limit="+this.limitNo;

                axios.post(dataUrl, requestData)
                    .then(res => {
                        let data_received = res.data;
                        //Assuming res.data is an array containing hashtag data
                        for (let data of data_received) {
                            for (let j = 0; j < data.timeline_status.length; j++) {
                                this.statusesArray.push(data.timeline_status[j]);
                            }
                        }
                        this.loading = false;
                        let message = this.statusesArray.length + " data retrieved";
                        this.successShowToast(message);
                    })
                    .catch(error => {
                        this.errorShowToast();
                        this.loading = false;
                        console.log(error);
                    });
            }
        },
        stringifyJSON(stringobject) {
            return JSON.stringify(stringobject, function (key, value) {
                return value;
            }, 4);
        },
        downloadJSON(){
            // Create a Blob containing the JSON data
            const blob = new Blob([JSON.stringify(this.statusesArray)], { type: 'application/json' });

            // Create a download link
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = 'hastag_data-'+new Date() +'.json';

            // Append the link to the document and trigger the click event
            document.body.appendChild(a);
            a.click();

            // Remove the link from the document
            document.body.removeChild(a);
        },
        clearAllFields(){
            this.note = null,
                this.username = null,
                this.statusCount = null,
                this.followersCount= null,
                this.followingCount = null,
                this.bot = null,
                this.avatarLink = null,
                this.displayName = null
        },
        viewAccountInfo(accountId){
            this.$router.push({
                name: 'AccountsById',
                params: { accountId: accountId, instanceId: this.instanceId},
            });
        },
        extractURLtoGetInstanceName(acct) {
            const parts = acct.split('/');
            return parts[2];
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
        addMastodonInstance (newInstance) {
            const mastodonInstance = {
                name: newInstance
            }
            this.instanceData.push(mastodonInstance)
            this.selectedMastodonInstances.push(mastodonInstance)
        },
    },
    mounted() {
        this.fetchAllInstanceData();
    },
    created() {
        this.accountId = this.$route.params.accountId;
        this.instanceId = this.$route.params.instanceId;
        if(!this.instanceId){
            this.instanceId = ""
        }
        else{
            this.submitAccountSearch();
        }
    },
}
</script>
<style src="vue-multiselect/dist/vue-multiselect.css"></style>