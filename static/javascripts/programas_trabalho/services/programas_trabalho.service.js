/**
 * Items
 * @namespace jaPedi.programas_trabalho.services
 */
(function () {
  'use strict';

  angular
    .module('jaPedi.programas_trabalho.services')
    .factory('ProgramasTrabalho', ProgramasTrabalho);

  ProgramasTrabalho.$inject = ['$http'];

  /**
   * @namespace Items
   * @returns {Factory}
   */
  function ProgramasTrabalho($http) {
    var ProgramasTrabalho = {
      get: get
    };

    return ProgramasTrabalho;

    /**
     * @name get
     * @desc Get the Items of a given user
     * @param {string} username The username to get Items for
     * @returns {Promise}
     * @memberOf jaPedi.programas_trabalho.services.execucoes
     */

    function get(id_localizacao) {
      var params = "";
      return $http.get('/api/v1/programas/'+id_localizacao+"/");
    }
  }
})();
