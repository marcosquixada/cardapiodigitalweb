/**
 * Items
 * @namespace jaPedi.orgaos.services
 */
(function () {
  'use strict';

  angular
    .module('jaPedi.orgaos.services')
    .factory('Orgaos', Orgaos);

  Orgaos.$inject = ['$http'];

  /**
   * @namespace Items
   * @returns {Factory}
   */
  function Orgaos($http) {
    var Orgaos = {
      all: all,
      get: get
    };

    return Orgaos;

    /**
     * @name get
     * @desc Get the Items of a given user
     * @param {string} username The username to get Items for
     * @returns {Promise}
     * @memberOf jaPedi.orgaos.services.execucoes
     */
    function all() {
      var params = "";
      return $http.get('/api/v1/orgaos/');
    }

    function get(id_orgao) {
      var params = "";
      return $http.get('/api/v1/orgaos_/'+id_orgao+"/");
    }
  }
})();
