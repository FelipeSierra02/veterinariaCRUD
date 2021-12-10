(function(){
    const btnEliminar = document.querySelectorAll('.btnEliminar');

    btnEliminar.forEach(btn=>{
        btn.addEventListener('click', (e) =>{
            const confirmar = confirm('¿Eliminar Servicio?');
            if(!confirmar){
                e.preventDefault();
            }
        });
    });
})();