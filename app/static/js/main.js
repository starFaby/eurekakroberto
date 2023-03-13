$(document).ready(function () {
    const abg = document.querySelector('.abg');
    const navs = document.querySelector('.navs');
    const abgm = document.querySelector('.abgm');
    const btnsm = document.querySelector('.btnsm');
    /** variables de carrito */
    const cantMas = document.querySelector('.cantMas');
    const cantMenos = document.querySelector('.cantMenos');
   



    count = 1;
  
    if (abg) {
      abg.addEventListener('click', () => {
        numpi = count++;
        if (numpi % 2 != 0) {
          navs.style.display = 'none'
        } else {
          navs.style.display = 'block'
        }
      });
    }
  
    if (btnsm) {
      btnsm.addEventListener('click', () => {
        numpi = count++;
        if (numpi % 2 != 0) {
          abgm.style.display = 'block'
        } else {
          abgm.style.display = 'none'
        }
      });
    }

    const getTitleMessageFromCategory = category => {
        const titles = {
            'success': 'Bien Hecho',
            'warning': 'Atencion',
            'info': 'Atencion',
            'error': 'Oops...!',

        }
        return titles[category]
    }

    function showMessageAlert(category, message) {
        const Toast = Swal.mixin({
            toast: true,
            position: 'top-end',
            showConfirmButton: false,
            timer: 3000,
            timerProgressBar: true,
            didOpen: (toast) => {
                toast.addEventListener('mouseenter', Swal.stopTimer)
                toast.addEventListener('mouseleave', Swal.resumeTimer)
            }
        })

        Toast.fire({
            icon: category,
            title: getTitleMessageFromCategory(category),
            text: message
        })
    }

    /** Carrito */
    let cont = 1;
    if (cantMas) {
      cantMas.addEventListener('click', () => {
        cont++;
        cantstok = document.getElementById("stok").value;
        cantProd = document.getElementById("cant").value;
        precioProd = document.getElementById("precio").value;
        aux = cont;
        if(aux == cantstok){
          document.getElementById("cant").value = 1;
          cont = 1
          precioFinal = 1 * precioProd;
          document.getElementById("precioFinal").value=precioFinal;
        }else{
          document.getElementById("cant").value = aux;
          precioFinal = aux * precioProd;
          document.getElementById("precioFinal").value=precioFinal;
        }
        


      });
    }
    if (cantMenos) {
      cantMenos.addEventListener('click', () => {
        cont--;
        cantProd = document.getElementById("cant").value;
        precioProd = document.getElementById("precio").value;
        aux = cont;
        document.getElementById("cant").value = aux;
        if(aux <= 0){
          document.getElementById("cant").value = 1;
          cont=1
          console.log("===> "+ aux)
        }
        
      });
    }

});