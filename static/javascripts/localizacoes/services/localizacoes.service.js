/**
 * Items
 * @namespace jaPedi.localizacoes.services
 */
(function () {
  'use strict';

  angular
    .module('jaPedi.localizacoes.services')
    .factory('Localizacoes', Localizacoes);

  Localizacoes.$inject = ['$http'];

  /**
   * @namespace Items
   * @returns {Factory}
   */
  function Localizacoes($http) {
    var Localizacoes = {
      all: all,
      get: get
    };

    return Localizacoes;

    /**
     * @name get
     * @desc Get the Items of a given user
     * @param {string} username The username to get Items for
     * @returns {Promise}
     * @memberOf jaPedi.localizacoes.services.execucoes
     */
    function all() {
      var params = "";
      return $http.get('/api/v1/localizacoes/');
    }
    function get(id_localizacao) {
      var params = "";
      return $http.get('/api/v1/localizacoes_/'+id_localizacao+'/');
    }
  }
})();
