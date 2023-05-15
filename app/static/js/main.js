$(document).ready(function () {
  const abg = document.querySelector('.abg');
  const navs = document.querySelector('.navs');
  const abgm = document.querySelector('.abgm');
  const btnsm = document.querySelector('.btnsm');
  /** variables de carrito */
  const btnCantMenos = document.querySelector('#btnCantMenos');
  const btnCantMas = document.querySelector('#btnCantMas');

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

  let cont = 1;
  const aux = 0;
  /** Carrito 
  
  if (cantMas) {
    cantMas.addEventListener('click', () => {
      cont++;
      if (cont < 1) {
        cont = 0;
      } else {
        cantstok = document.getElementById("stok").value;
        cantProd = document.getElementById("cant").value;
        precioProd = document.getElementById("precio").value;
        aux = cont;
        if (aux == cantstok) {
          document.getElementById("cant").value = cantstok;
          precioFinal = cantstok * precioProd;
          document.getElementById("precioFinal").value = precioFinal;
          cont = 0
        } else {
          document.getElementById("cant").value = aux;
          precioFinal = aux * precioProd;
          document.getElementById("precioFinal").value = precioFinal;
        }
      }

    });
  }
  if (cantMenos) {
    cantMenos.addEventListener('click', () => {
      cont--;
      cantstok = document.getElementById("stok").value;
      cantProd = document.getElementById("cant").value;
      precioProd = document.getElementById("precio").value;
      aux = cont;
      if (aux <= 1) {
        document.getElementById("cant").value = 1;
        precioFinal = 1 * precioProd;
        document.getElementById("precioFinal").value = precioFinal;
        aux = 1
      } else {
        document.getElementById("cant").value = aux;
        precioFinal = aux * precioProd;
        document.getElementById("precioFinal").value = precioFinal;
      }

    });
  }
*/
  if (btnCantMas) {
    btnCantMas.addEventListener('click', () => {
      cont++;
      if (cont < 1) {
        cont = 0;
      } else {
        txtStock = document.getElementById("txtStock").value;
        txtCantidad = document.getElementById("txtCantidad").value;
        txtPrecio = document.getElementById("txtPrecio").value;
        cont;
        if (cont == txtStock) {
          document.getElementById("txtCantidad").value = txtStock;
          precioFinal = txtStock * txtPrecio;
          document.getElementById("txtPrecioFinal").value = precioFinal;
          cont = 0
        } else {
          document.getElementById("txtCantidad").value = cont;
          precioFinal = cont * txtPrecio;
          document.getElementById("txtPrecioFinal").value = precioFinal;
        }
      }
    });
  }
  if (btnCantMenos) {
    btnCantMenos.addEventListener('click', () => {
      cont--;
      txtStock = document.getElementById("txtStock").value;
      txtCantidad = document.getElementById("txtCantidad").value;
      txtPrecio = document.getElementById("txtPrecio").value;
      cont;
      if (cont <= 1) {
        document.getElementById("txtCantidad").value = 1;
        precioFinal = 1 * txtPrecio;
        document.getElementById("txtPrecioFinal").value = precioFinal;
        cont = 1
      } else {
        document.getElementById("txtCantidad").value = cont;
        precioFinal = cont * txtPrecio;
        document.getElementById("txtPrecioFinal").value = precioFinal;
      }
    });
  }
});