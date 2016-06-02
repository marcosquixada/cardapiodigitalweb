/**
 * ExecucoesController
 * @namespace jaPedi.execucoes.controllers
 */
(function () {
  'use strict';

  angular
    .module('jaPedi.execucoes.controllers')
    .controller('ExecucoesController', ExecucoesController);

  ExecucoesController.$inject = ['$scope'];

  /**
   * @namespace ExecucoesController
   */
  function ExecucoesController($scope) {
    var vm = this;

    vm.columns = [];

    activate();
    /**
     * @name activate
     * @desc Actions to be performed when this controller is instantiated
     * @memberOf jaPedi.execucoes.controllers.execucoesController
     */
    function activate() {

      $scope.$watchCollection(function () { return $scope.execucoes; }, render);
      $scope.$watch(function () { return $(window).width(); }, render);
    }

    /**
     * @name calculateNumberOfColumns
     * @desc Calculate number of columns based on screen width
     * @returns {Number} The number of columns containing Items
     * @memberOf jaPedi.execucoes.controllers.execucoesController
     */
    function calculateNumberOfColumns() {
      var width = $(window).width();

      if (width >= 1200) {
        return 4;
      } else if (width >= 992) {
        return 3;
      } else if (width >= 768) {
        return 2;
      } else {
        return 1;
      }
    }

    function render(current, original) {
        if(current instanceof Array){
          vm.columns = [];

          for (var i = 0; i < current.length; ++i) {
              vm.columns.push(current[i]);
          }
          
        }
      }
  }
})();
