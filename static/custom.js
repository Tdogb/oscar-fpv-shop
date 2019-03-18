// let url = document.URL
// let base_url = url.substring(0, url.indexOf('/'))

// if(base_url.equals(url)) {
    let target = document.querySelector(".carousel-indicators").children
    console.log(target)
    let observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
        console.log(mutation.type);
        });
    });
    let config = { attributes: true, childList: false, characterData: true }
    for(let _target in target) {
        observer.observe(_target, config);
    }

// }

