//Orcamento Script

var APP = {
    Init: function() {
        var body = $('body');
        var main = $('main');

        APP.setAttr();
        APP.setSVG();
        // APP.setFlexslider();
        APP.setAccessibility();
        APP.setFancybox();

    },

    setAttr: function() {
        $(".nav").attr("role", "navigation");
        $(".nav li a").attr("role", "menuitem");
        $("#footer").attr("role", "contentinfo");
        $(".alert").attr("role", "alert");
        $("a.btn").attr("role", "button");
        $("#header").attr("role", "banner");
        $(".content").attr("role", "main");
        $(".sidebar").attr("role", "complementary");
        $(".tabs").attr("role", "tablist");
        $(".search-form").attr("role", "search");
        $("form").attr("role", "form");
        $("main").attr("role", "main");
        $(".sidebar").attr("role", "complementary");

    },

    setSVG: function() {
        if (!Modernizr.svg) {
            $('img[src*="svg"]').attr('src', function() {
                return $(this).attr('src').replace('.svg', '.png');
            });
        }
    },
    setFlexslider: function() {
        //Header
        $(".header-slider").flexslider({
            controlNav: false,
            directionNav: false,
            slideshowSpeed: 7000,
            animationSpeed: 600,
        });
    },

    setContrast: function() {
        var self = $('.btn-contrast');
        if (localStorage.getItem("contrast") == "true") {
            self.addClass('active');
            $('body').addClass('contrast');
            $('img').addClass('grayscale');
            $('.title').addClass('contrast-title');

        } else {
            self.removeClass('active');
            $('body').removeClass('contrast');
            $('img').removeClass('grayscale');
            $('.title').removeClass('contrast-title');
        }
    },

    setFont: function() {
        var increase = $('.btn-increase');
        var decrease = $('.btn-decrease');
        var reset = $('.btn-reset');

        if (localStorage.getItem("font") == "increase") {
            increase.addClass('active');
            decrease.removeClass('active');
            reset.removeClass('active');

            $('body').removeClass('font-minus').addClass('font-more');


        } else if (localStorage.getItem("font") == "decrease") {
            decrease.addClass('active');
            increase.removeClass('active');
            reset.removeClass('active');

            $('body').removeClass('font-more').addClass('font-minus');

        } else if (localStorage.getItem("font") == "") {
            decrease.removeClass('active');
            increase.removeClass('active');
            reset.removeClass('active');
            $('body').removeClass('font-minus');
            $('body').removeClass('font-more');

        }
    },



    setAccessibility: function() {

        $('.grayscale').gray();

        APP.setContrast();
        APP.setFont();

        $('.btn-contrast').click(function() {
            $(this).toggleClass('active');

            if($(this).hasClass('active')) {
                window.localStorage.setItem('contrast', "true");
            } else {
                window.localStorage.setItem('contrast', "false");
            }
            APP.setContrast();
        });

        $('.btn-increase, .btn-decrease, .btn-reset').click(function() {
            $(this).toggleClass('active');

            if($(this).hasClass('active') && $(this).hasClass('btn-increase')) {
                window.localStorage.setItem('font', "increase");
            } else if($(this).hasClass('active') && $(this).hasClass('btn-decrease')) {
                window.localStorage.setItem('font', "decrease");
            } else if($(this).hasClass('active') && $(this).hasClass('btn-reset')) {
                window.localStorage.setItem('font', "");
            }
            APP.setFont();
        });

        $('.btn-print').click(function() {
            window.print();
            return false;
        });

        $('#gotocontent').click(function() {
            if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
                var target = $(this.hash);
                target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
                if (target.length) {
                    $('html,body').animate({
                        scrollTop: target.offset().top
                    }, 1000);
                    return false;
                }
            }
        });
    },

    setFancybox: function() {

        $(".item-pdf").fancybox({
            openEffect: 'none',
            closeEffect: 'none',
            autoScale: true,
            autoDimensions: false,
            centerOnScroll: true,
            'closeBtn': false,
            width: '90%',
            iframe: {
                preload: false
            },
            beforeLoad: function() {
                this.title = '<strong>' + $(this.element).attr('title') + '</strong>';
            },

            helpers: {
                title: {
                    type: 'inside'
                },
                buttons: {},
            },
        });

    }

}

jQuery(document).ready(function($) {
    APP.Init();
});
