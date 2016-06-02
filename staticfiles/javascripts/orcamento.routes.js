(function () {
  'use strict';

  angular
    .module('jaPedi.routes')
    .config(config);

  config.$inject = ['$routeProvider'];

  /**
   * @name config
   * @desc Define valid application routes
   */
  function config($routeProvider) {
    $routeProvider.when('/', {
      controller: 'IndexController',
      templateUrl: '/static/templates/layout/index.html',
      activetab: 'Home'
    });

    $routeProvider.when('/sobre', {
      controller: 'SobreController',
      templateUrl: '/static/templates/layout/sobre.html',
      activetab: 'Sobre'
    });

    $routeProvider.when('/sophia', {
      controller: 'SophiaController',
      templateUrl: '/static/templates/layout/sophia.html',
      activetab: 'Sophia'
    });

    $routeProvider.when('/informativos', {
      controller: 'InformativosController',
      templateUrl: '/static/templates/informativos/index.html',
      activetab: 'Informativos'
    });

    $routeProvider.when('/informativo', {
      controller: 'InformativosController',
      templateUrl: '/static/templates/informativos/informativo.html',
      activetab: 'Informativos'
    });

    $routeProvider.when('/ajuda', {
      controller: 'AjudaController',
      templateUrl: '/static/templates/layout/ajuda.html',
      activetab: 'Ajuda'
    });

    $routeProvider.when('/contato', {
      controller: 'ContatoController',
      templateUrl: '/static/templates/layout/contato.html',
      activetab: 'Contato'
    });

    $routeProvider.when('/legislacao', {
      controller: 'LegislacaoController',
      templateUrl: '/static/templates/layout/legislacao.html',
      activetab: 'Legislação'
    });

    $routeProvider.when('/publicacao/loa', {
      controller: 'PublicacoesController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/publicacoes/loa.html'
    });

    $routeProvider.when('/publicacao/ldo', {
      controller: 'PublicacoesController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/publicacoes/ldo.html'
    });

  }
})();
