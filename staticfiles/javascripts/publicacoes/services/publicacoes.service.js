/**
 * Items
 * @namespace jaPedi.publicacoes.services
 */
(function () {
  'use strict';

  angular
    .module('jaPedi.publicacoes.services')
    .factory('Publicacoes', Publicacoes);

  Publicacoes.$inject = ['$http'];

  /**
   * @namespace Publicacoes
   * @returns {Factory}
   */
  function Publicacoes($http) {
    var Publicacoes = {
      loa: loa,
      ldo: ldo
    };

    return Publicacoes;

    /**
     * @name loa
     * @desc Get the Items of a publication
     * @returns {Promise}
     * @memberOf jaPedi.execucoes.services.execucoes
     */
    function loa() {
      return $http.get('http://dados.al.gov.br/api/3/action/package_search?q=lei-orcamentaria-anual-loa');
    }

    /**
     * @name ldo
     * @desc Get the Items of a publication
     * @returns {Promise}
     * @memberOf jaPedi.execucoes.services.execucoes
     */
    function ldo() {
      return $http.get('http://dados.al.gov.br/api/3/action/package_search?q=lei-de-diretrizes-orcamentarias-ldo');
    }


  }
})();
