<template>
    <div>
        <div id="layoutSidenav">
            <div id="layoutSidenav_nav">
                <nav class="sb-sidenav accordion sb-sidenav-dark" id="sidenavAccordion">
                    <div class="sb-sidenav-menu">
                        <div class="nav">
                            <div class="sb-sidenav-menu-heading">INSTANCES</div>
                            <router-link class="nav-item nav-link" :to="{name: 'SearchResults'}" exact-active-class="active-link" >
                                <div class="sb-nav-link-icon"><i class="fas fa-list-alt"></i></div>Mastodon Instances
                            </router-link>
                            <a class="nav-link collapsed" href="#" data-bs-toggle="collapse" data-bs-target="#collapsePages" aria-expanded="false" aria-controls="collapsePages">
                                <div class="sb-nav-link-icon"><i class="fas fa-book-open"></i></div>
                                Get Accounts
                                <div class="sb-sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
                            </a>
                        </div>
                    </div>
                </nav>
            </div>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';

export default {
    data() {
        return {
            is_expanded: ref(localStorage.getItem('is_expanded') === 'true'),
        };
    },
    methods: {
    },
};
</script>


<style scoped>

.active-link {
    border-right: 8px solid #0096FF;
    color:#0073cf;
    .sb-nav-link-icon{
        color: #0073cf;
    }
    background: linear-gradient(to right, #151C62, #0073cf);
}

.active-link:hover {
    border-right: 8px solid #0096FF;
    color:#0073cf;
    .sb-nav-link-icon{
        color: #0073cf;
    }
    .nav{
        color: #0073cf;
    }
    background: linear-gradient(to right, #151C62, #0073cf);
}

</style>
