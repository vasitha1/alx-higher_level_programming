$(document).ready(function() {
    function translateHello() {
      let languageCode = $('#language_code').val();
      $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function(data) {
        $('#hello').text(data.hello);
      }).fail(function() {
        $('#hello').text('Error fetching translation.');
      });
    }
  
    $('#btn_translate').click(translateHello);
  
    $('#language_code').keypress(function(event) {
      if (event.which === 13) { // Enter key
        translateHello();
      }
    });
  });
  