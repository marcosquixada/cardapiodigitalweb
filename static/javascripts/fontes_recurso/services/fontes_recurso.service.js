/**
 * Items
 * @namespace jaPedi.fontes_recurso.services
 */
(function () {
  'use strict';

  angular
    .module('jaPedi.fontes_recurso.services')
    .factory('FontesRecurso', FontesRecurso);

  FontesRecurso.$inject = ['$http'];

  /**
   * @namespace Items
   * @returns {Factory}
   */
  function FontesRecurso($http) {
    var FontesRecurso = {
      all: all
    };

    return FontesRecurso;

    /**
     * @name get
     * @desc Get the Items of a given user
     * @param {string} username The username to get Items for
     * @returns {Promise}
     * @memberOf jaPedi.fontes_recurso.services.execucoes
     */
    function all() {
      var params = "";
      return $http.get('/api/v1/fontes_recurso/');
    }
  }
})();
