$(document).read(function (){
   let loadForm = function (){
       let btn = $(this);
       $.ajax({
           url: btn.attr("data-url"),
           type: 'get',
           dataType: 'json',
           beforeSend: function (){
               $("#modal-agendamento .modal-content").html("");
               $("#modal-agendamento").modal("show");
           },
           success: function (data){
               $("#modal-agendamento .modal-content").html(data.html_form);
           }
       });
   };
   $(".js-create-agendamento").click(loadForm);
});