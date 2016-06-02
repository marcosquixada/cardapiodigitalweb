/**
 * Items
 * @namespace jaPedi.execucoes.services
 */
(function () {
  'use strict';

  angular
    .module('jaPedi.execucoes.services')
    .factory('Execucoes', Execucoes);

  Execucoes.$inject = ['$http'];

  /**
   * @namespace Items
   * @returns {Factory}
   */
  function Execucoes($http) {
    var Execucoes = {
      all: all,
      get: get
    };

    return Execucoes;

    ////////////////////
    
    /**
     * @name all
     * @desc Get all Execucoes
     * @returns {Promise}
     * @memberOf jaPedi.execucoes.services.execucoes
     */
    function all(order) {
      var params = "";
      console.log(order);
      if (order != null){
          if(order == "false"){
            params = "?order=asc";
          }else{
            params = "?order=desc";
          }
      }
      return $http.get('/api/v1/execucoes/'+params);
    }


    /**
     * @name get
     * @desc Get the Items of a given user
     * @param {string} username The username to get Items for
     * @returns {Promise}
     * @memberOf jaPedi.execucoes.services.execucoes
     */
    function get(id,order) {
      var params = "";
      if (order != null){
          if(order == "false"){
            params = "?order=asc";
          }else{
            params = "?order=desc";
          }
      }
      return $http.get('/api/v1/execucoes/'+ id +"/"+params);
    }
  }
})();
