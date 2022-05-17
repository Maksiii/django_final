
function confirmDelete(plu_codigo) {
    Swal.fire({
        title: 'Estas seguro?',
        text: 'No podras deshacer la accion',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, eliminar!',
        cancelButtonText: "Cancelar"
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire(
            'elimnado',
            'producto eliminado correctamente',
            'success'
          ).then(function(){
            window.location.href = "/eliminar/"+ plu_codigo +"/";
          })
        }
      })

}


function eliminar (plu_codigo){
    Swal.fire({
        title: 'Estas seguro?',
        text: "No podrás revertir esto!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, eliminar!'
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire(
            'eliminado',
            'producto eliminado correctamente',
            'success'
          ).then(function(){
            window.location.href = "/eliminarProducto/"+ plu_codigo +"/";
          })
        }
      })
}
function eliminarUsu (nombre){
    Swal.fire({
        title: 'Estas seguro?',
        text: "No podrás revertir esto!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, eliminar!'
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire(
            'eliminado',
            'producto eliminado correctamente',
            'success'
          ).then(function(){
            window.location.href = "/eliminarUsuario/"+ nombre +"/";
          })
        }
      })
}


function registrese (){
  Swal.fire({
    title: 'Sweet!',
    text: 'Modal with a custom image.',
    imageUrl: 'https://unsplash.it/400/200',
    imageWidth: 400,
    imageHeight: 200,
    imageAlt: 'Custom image',
  })
}