/**
 * Items
 * @namespace jaPedi.unidades_orcamentarias.services
 */
(function () {
  'use strict';

  angular
    .module('jaPedi.unidades_orcamentarias.services')
    .factory('UnidadesOrcamentarias', UnidadesOrcamentarias);

  UnidadesOrcamentarias.$inject = ['$http'];

  /**
   * @namespace Items
   * @returns {Factory}
   */
  function UnidadesOrcamentarias($http) {
    var UnidadesOrcamentarias = {
      all: all,
      get: get
    };

    return UnidadesOrcamentarias;

    /**
     * @name get
     * @desc Get the Items of a given user
     * @param {string} username The username to get Items for
     * @returns {Promise}
     * @memberOf jaPedi.unidades_orcamentarias.services.execucoes
     */
    function get(id,ano) {
      var params = "";
      return $http.get('/api/v1/unidades_orcamentarias/'+ id+"/?ano="+ano);
    }


    /**
     * @name get
     * @desc Get the Items of a given user
     * @param {string} username The username to get Items for
     * @returns {Promise}
     * @memberOf jaPedi.unidades_orcamentarias.services.execucoes
     */
    function all(ano) {
      var params = "";
      return $http.get('/api/v1/unidades_orcamentarias/?ano='+ano);
    }
  }
})();
