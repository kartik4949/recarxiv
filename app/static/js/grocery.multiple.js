/**
 * Created by Malal91 and Haziel
 * Select multiple email by jquery.email_multiple
 * **/

(function($){

    $.fn.email_multiple = function(options) {

        let defaults = {
            reset: false,
            fill: false,
            data: null
        };

        let settings = $.extend(defaults, options);
        let email = "";

        return this.each(function()
        {
            $(this).after("<span class=\"to-input\">Press enter after each category:</span>\n" +
                "<div class=\"all-mail\"></div>\n" +
                "<input type=\"text\" name=\"email\" class=\"enter-mail-id\" placeholder=\"Enter sub category ...\" />");
            let $orig = $(this);
            let $element = $('.enter-mail-id');
            $element.keydown(function (e) {
                $element.css('border', '');
                if (e.keyCode === 13) {
                    let getValue = $element.val();
                    $('.all-mail').append('<span class="email-ids">' + getValue + '<span class="cancel-email">x</span></span>');
                    $element.val('');

                    email += getValue + ';'
                }
                $orig.val(email.slice(0, -1))
            });

            $(document).on('click','.cancel-email',function(){
                var curr_email = $(this).parent().text().slice(0, -1) + ';';
                email = email.replace(curr_email,'');
                $orig.val(email.slice(0, -1));
                $(this).parent().remove();
            });

            if(settings.data){
                $.each(settings.data, function (x, y) {
                    $('.all-mail').append('<span class="email-ids">' + y + '<span class="cancel-email">x</span></span>');
                    $element.val('');

                    email += y + ';'
                })

                $orig.val(email.slice(0, -1))
            }

            if(settings.reset){
                $('.email-ids').remove()
            }

            return $orig.hide()
        });
    };

})(jQuery);
