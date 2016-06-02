(function () {
  'use strict';

  angular
    .module('jaPedi', [
      'jaPedi.config',
      'jaPedi.routes',
      'jaPedi.layout',
      'jaPedi.execucoes',
      'jaPedi.unidades_orcamentarias',
      'jaPedi.fontes_recurso',
      'jaPedi.localizacoes',
      'jaPedi.programas_trabalho',
      'jaPedi.orgaos',
      'jaPedi.publicacoes',
      'jaPedi.utils'
    ]);

  angular
    .module('jaPedi.config', []);

  angular
    .module('jaPedi.routes', ['ngRoute']);

  angular
    .module('jaPedi')
    .run(run);

  run.$inject = ['$http'];

  /**
   * @name run
   * @desc Update xsrf $http headers to align with Django's defaults
   */
  function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }
})();
