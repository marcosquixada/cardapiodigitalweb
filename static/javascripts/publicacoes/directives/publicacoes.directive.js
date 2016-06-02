/**
 * publicacoes
 * @namespace jaPedi.publicacoes.directives
 */
(function () {
  'use strict';

  angular
    .module('jaPedi.publicacoes.directives')
    .directive('publicacoes', publicacoes);

  /**
   * @namespace publicacoes
   */
  function publicacoes() {
    /**
     * @name directive
     * @desc The directive to be returned
     * @memberOf jaPedi.publicacoes.directives.publicacoes
     */
    var directive = {
      controller: 'PublicacoesController',
      controllerAs: 'vm',
      restrict: 'E',
      scope: {
        publicacoes: '='
      },
      templateUrl: '/static/templates/publicacoes/publicacoes.html'
    };

    return directive;
  }
})();
