/**
 * execucoes
 * @namespace jaPedi.execucoes.directives
 */
(function () {
  'use strict';

  angular
    .module('jaPedi.layout.directives')
    .directive('sidebar', sidebar);

  /**
   * @namespace execucoes
   */
  function sidebar() {
    /**
     * @name directive
     * @desc The directive to be returned
     * @memberOf restauranete.execucoes.directives.execucoes
     */
    var directive = {
      controller: 'IndexController',
      controllerAs: 'vm',
      restrict: 'E',
      scope: {
        categorias: '='
      },
      templateUrl: '/templates/sidebar.html'
    };

    return directive;
  }
})();
