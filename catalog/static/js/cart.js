var updateButton = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateButton.length; i++){
    updateButton[i].addEventListener('click',function() {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('ProductId: ', productId, 'action: ', action)

        console.log('USER: ',user)
        if (user === 'AnonymousUser') {
            console.log('NotLoggedIn')
        }
        else {
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    console.log('User is logged sending data')
    
    var url = '/catalog/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type' : 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId , 'action': action})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data', data)
        location.reload()
    })
}