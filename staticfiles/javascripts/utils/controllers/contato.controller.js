/**
 * ContatoController
 * @namespace jaPedi.utils.controllers
 */
(function () {
  'use strict';

  angular
    .module('jaPedi.utils.controllers')
    .controller('ContatoController', ContatoController);

  ContatoController.$inject = ['$scope', 'Snackbar'];

  /**
   * @namespace ContatoController
   */
  function ContatoController($scope, Snackbar) {
    $scope.contato =  {'address': 'R. Cincinato Pinto, 503 - Centro, Maceió - AL',
                        'lat': '-9.660086',
                        'lng': '-35.740821',
                        'email': 'contato@jaPedi.al.gov.br',
                        'phone': '(82) 3315-1723',
                         'icon': 'static/assets/images/marker.png'}
  }
})();
