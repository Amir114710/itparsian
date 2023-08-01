//doc ready
$(function(){
  //call owl carousel
  $('.owl-carousel').owlCarousel();
});
//owl
$('.owl-carousel').owlCarousel({
  margin:50,
  dots:false,
  center:true,
  nav:true,
  loop:true,
  autoWidth:true,
  autoHeight:true,

  navText : ['<i class="d-none d-md-block bi bi-arrow-left-circle-fill fs-1 text-warning" aria-hidden="true"></i>','<i class="d-none d-md-block bi bi-arrow-right-circle-fill fs-1 text-warning" aria-hidden="true"></i>'],
  item:4,
  
})
var owl = $('.owl-carousel');
owl.owlCarousel({
    loop:true,
    nav:true,
    margin:10,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },            
        960:{
            items:5
        },
        1200:{
            items:6
        }
    }
});
owl.on('mousewheel', '.owl-stage', function (e) {
  if (e.deltaY>0) {
      owl.trigger('next.owl');
  } else {
      owl.trigger('prev.owl');
  }
  e.preventDefault();
});
// bootstrap tooltips enable code in all document

var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

//slider two
document.addEventListener('click',function(e){
  if(e.target.classList.contains("img-slider-small")){
    const src = e.target.getAttribute("src");
    document.querySelector("#img-slider-big").src = src;
  }
})

const btn = document.getElementById('send');
const div = document.getElementById('seccess-send');


btn.addEventListener('click', show);

function show(){
    div.style.display = 'block';
    // setTimeout(() => {
    //     // 👇️ removes element from DOM
    //     div.style.display = 'none';
    //
    //     // 👇️ hides element (still takes up space on page)
    //     // box.style.visibility = 'hidden';
    //   }, 3000)

}