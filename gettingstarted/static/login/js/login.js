      $('.validate').on('blur', function(){
        if( $('.validate').hasClass('valid') ){
          $(this).siblings('.prefix').addClass('active')
        }else{
          $(this).siblings('.prefix').removeClass('active')
        }
      });


      $(document).ready(function(){


        $('#registroEmpleador #test5').on('click', function(){
          if( $(this).is(':checked') && $('input').val() != "" ){
            $('.registroBtn').removeClass('disabled');
          }else{
            $('.registroBtn').addClass('disabled');
          }
        });



        $('input').on('blur', function(){
          if( $('#pass').hasClass('valid') ){
            $('.g-recaptcha').removeClass('hide');
          }else{
            $('.g-recaptcha').addClass('hide');
          }
        });




        $('.showPass').click(function () {
          if ($('.cambiaPass').attr('type') == 'password') {
            $('.cambiaPass').attr('type', 'text');
            $(this).text('visibility');
          } else {
            $('.cambiaPass').attr('type', 'password');
            $(this).text('visibility_off');
          }
        });



      });




      $(document).ready(function(){

        var industrias = new Array();

        var limit = 3;
        $('.seleccionaItem > div').click(function(){
          if( $('.seleccionaItem > div.active').length >= limit ){
            // $(this).toggleClass('active');
            if($(this).hasClass("active")){
              $(this).toggleClass("active");
            }
          }else{
           $(this).toggleClass("active");
          }



          pre_texto = $(this).text().replace(" check_circle", "");
          texto = $.trim(pre_texto);

          //console.log( texto );



          index = industrias.indexOf(texto);

          console.log( "index: " + index);

          if( index != -1){
            industrias.splice(index, 1);
          }else{
            industrias.push(texto);
          }

          console.log(industrias);



        })


      });

