<template>
    <div id="toTopBtn">
        <div class="material-icons" onclick="javascript:window.scrollTo(0,0)">arrow_upward</div>
    </div>
</template>

<script>
</script>

<style scoped>
#toTopBtn {
    width: 42px;
    height: 42px;
    background-color:#9ac486;
    color: #fff;
    border: 2px solid #fff;
    border-radius: 10px;
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    bottom: 30px;
    right: 30px;
    z-index: 9;
    }
</style>