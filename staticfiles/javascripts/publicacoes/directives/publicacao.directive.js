/**
 * Item
 * @namespace jaPedi.publicacoes.directives
 */
(function () {
  'use strict';

  angular
    .module('jaPedi.publicacoes.directives')
    .directive('publicacao', publicacao);

  /**
   * @namespace publicacao
   */
  function publicacao() {
    /**
     * @name directive
     * @desc The directive to be returned
     * @memberOf jaPedi.publicacoes.directives.publicacao
     */
    var directive = {
      restrict: 'E',
      scope: {
        publicacao: '='
      },
      templateUrl: '/static/templates/publicacoes/publicacao.html'
    };

    return directive;
  }
})();
