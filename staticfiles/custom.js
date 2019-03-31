let product_pods = document.getElementsByClassName('product_pod');

for(var i = 0; i < product_pods.length; i++) {
    product_pods[i].addEventListener('onmouseover', function () {
        console.log(event);
        displayDetail(elem);
    });
    console.log("hi");
}

function displayDetail(product) {
    console.log(product);
    product_pods[product].classList.toggle("show");
    console.log("hi2");
}

$('#myDropdown').on('show.bs.dropdown', function () {

})