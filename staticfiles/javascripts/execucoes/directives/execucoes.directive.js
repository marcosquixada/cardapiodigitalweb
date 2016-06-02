/**
 * execucoes
 * @namespace jaPedi.execucoes.directives
 */
(function () {
  'use strict';

  angular
    .module('jaPedi.execucoes.directives')
    .directive('execucoes', execucoes);

  /**
   * @namespace execucoes
   */
  function execucoes() {
    /**
     * @name directive
     * @desc The directive to be returned
     * @memberOf restauranete.execucoes.directives.execucoes
     */
    var directive = {
      controller: 'ExecucoesController',
      controllerAs: 'vm',
      restrict: 'E',
      scope: {
        execucoes: '='
      },
      templateUrl: '/static/templates/execucoes/execucoes.html'
    };

    return directive;
  }
})();
