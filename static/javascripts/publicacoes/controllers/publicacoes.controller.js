/**
 * PublicacoesController
 * @namespace jaPedi.publicacoes.controllers
 */
(function () {
  'use strict';

  angular
    .module('jaPedi.publicacoes.controllers')
    .controller('PublicacoesController', PublicacoesController);

  PublicacoesController.$inject = ['$scope', 'Publicacoes', 'Snackbar'];

  /**
   * @namespace PublicacoesController
   */
  function PublicacoesController($scope, Publicacoes, Snackbar) {
    var vm = this;

    vm.loa = [];
    vm.ldo = [];

    activate();
    

    function activate() {
      Publicacoes.loa().then(publicacoesLoaSuccessFn, publicacoesErrorFn);
      Publicacoes.ldo().then(publicacoesLdoSuccessFn, publicacoesErrorFn);

      function publicacoesLoaSuccessFn(data, status, headers, config) {
        console.log(data.data.result.results[0]);
        vm.loa = data.data.result.results[0];
      }

      function publicacoesLdoSuccessFn(data, status, headers, config) {
        console.log(data.data.result.results[0]);
        vm.ldo = data.data.result.results[0];
      }

      function publicacoesErrorFn(data, status, headers, config) {
        Snackbar.error(data.error);
      }
    }

  }
})();
