/**
 * Item
 * @namespace jaPedi.execucoes.directives
 */
(function () {
  'use strict';

  angular
    .module('jaPedi.execucoes.directives')
    .directive('execucao', execucao);

  /**
   * @namespace execucao
   */
  function execucao() {
    /**
     * @name directive
     * @desc The directive to be returned
     * @memberOf jaPedi.execucoes.directives.execucao
     */
    var directive = {
      restrict: 'E',
      scope: {
        execucao: '='
      },
      templateUrl: '/static/templates/execucoes/execucao.html'
    };

    return directive;
  }
})();
