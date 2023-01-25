$(document).ready(function () {
    const abg = document.querySelector('.abg');
    const navs = document.querySelector('.navs');
    const abgm = document.querySelector('.abgm');
    const btnsm = document.querySelector('.btnsm');
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

});