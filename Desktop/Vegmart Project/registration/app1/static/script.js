function increaseQuantity(itemId) {
    const quantityElement = document.getElementById('quantity-' + itemId);
    let quantity = parseInt(quantityElement.innerText);
    quantityElement.innerText = quantity + 1;
}
 
function decreaseQuantity(itemId) {
    const quantityElement = document.getElementById('quantity-' + itemId);
    let quantity = parseInt(quantityElement.innerText);
    if (quantity > 0) {
        quantityElement.innerText = quantity - 1;
    }
}
 
function addItem(itemId) {
    const quantityElement = document.getElementById('quantity-' + itemId);
    const quantity = parseInt(quantityElement.innerText);
    const cartItem = {
        id: itemId,
        name: document.getElementById(itemId).getElementsByTagName('h3')[0].innerText,
        price: getPrice(itemId),
        quantity: quantity
    };
 
    addToCart(cartItem);
 
   
}
 
function getPrice(itemId) {
    switch(itemId) {
        case 'item1':
            return 50;  
        case 'item2':
            return 33;  
        case 'item3':
            return 16;  
        default:
            return 0;
    }
}
 
function addToCart(item) {
    const cartItemsDiv = document.getElementById('cart-items');
    const cartTotalAmount = document.getElementById('cart-total-amount');
 
    const existingCartItem = document.getElementById(`cart-item-${item.id}`);
    if (existingCartItem) {
       
        const existingQuantity = parseInt(existingCartItem.querySelector('.cart-item-quantity').innerText);
        existingCartItem.querySelector('.cart-item-quantity').innerText = existingQuantity + item.quantity;
    } else {
       
        const cartItemElement = document.createElement('div');
        cartItemElement.classList.add('cart-item');
        cartItemElement.setAttribute('id', `cart-item-${item.id}`);
        cartItemElement.innerHTML = `
            <span>${item.name}</span>
            <span class="cart-item-quantity">${item.quantity}</span>
            <span>₹${item.price}</span>
        `;
        cartItemsDiv.appendChild(cartItemElement);
    }
 
 
    let currentTotal = parseInt(cartTotalAmount.innerText);
    currentTotal += item.price * item.quantity;
    cartTotalAmount.innerText = currentTotal;
}
 
function goToCart() {
    const cartItems = document.getElementById('cart-items').innerHTML;
    const cartTotal = document.getElementById('cart-total-amount').innerText;
    localStorage.setItem('cartItems', cartItems);
    localStorage.setItem('cartTotal', cartTotal);
    window.location.href = 'Commercial.html';
}