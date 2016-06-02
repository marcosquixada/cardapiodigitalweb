/**
 * Item
 * @namespace jaPedi.utils.directives
 */
(function () {
  'use strict';

  angular
    .module('jaPedi.utils.directives')
    .directive('breadcrumbs', breadcrumbs)
    .directive('menu', menu)
    .directive('flexslider', flexslider)
    .directive('booklet', booklet);


  /**
   * @namespace breadcrumbs
   */
  function breadcrumbs() {
    /**
     * @name directive
     * @desc The directive to be returned
     * @memberOf jaPedi.utils.directives.breadcrumbs
     */
    var directive = {
      restrict: 'E',
      replace: true,
      scope: {
        secao: '=',
        subsecao: '='
      },
      templateUrl: '/static/templates/utils/breadcrumbs.html'
    };

    return directive;
  }


  /**
   * @namespace menu
   */
  function menu() {
    /**
     * @name directive
     * @desc The directive to be returned
     * @memberOf jaPedi.utils.directives.menu
     */
    var directive = {
      restrict: 'E',
      replace: true,
      scope: true,
      templateUrl: '/static/templates/utils/menu.html'
    };

    return directive;
  }


  /**
   * @namespace flexslider
   */
  function flexslider() {
    /**
     * @name directive
     * @desc The directive to be returned
     * @memberOf jaPedi.utils.directives.flexslider
     */
    return {
      link: function (scope, element, attrs) {

        element.flexslider({
            controlNav: false,
            directionNav: false,
            slideshowSpeed: 7000,
            animationSpeed: 600,
        });
      }
    }
  }

  /**
   * @namespace booklet
   */
  function booklet() {
    /**
     * @name directive
     * @desc The directive to be returned
     * @memberOf jaPedi.utils.directives.booklet
     */
       return {
         link: function (scope, element, attrs) {

           element.booklet({
             width: '100%',
             height: '680',
             manual: true,
             // shadows: true,
             startingPage: 1,
             autoCenter: true,
             pageBorder: 0,
             chapterSelector: true
           });
         }
       }
  }


})();
