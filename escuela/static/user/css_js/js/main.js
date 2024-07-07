const openVentanas = document.querySelectorAll('.edit');
const ventana = document.querySelector('.ventana');
const closeVentana = document.querySelector('.ventana_close');


openVentanas.forEach((openVentana)=>
openVentana.addEventListener('click', (e) =>{
    e.preventDefault();
    ventana.classList.add('ventana--show');
})

)


closeVentana.addEventListener('click', (e) =>{
    e.preventDefault();
    ventana.classList.remove('ventana--show');
});

