(function () {
  'use strict';

  angular
    .module('jaPedi.execucoes', [
      'jaPedi.execucoes.controllers',
      'jaPedi.execucoes.directives',
      'jaPedi.execucoes.services'
    ]);

  angular
    .module('jaPedi.execucoes.controllers', []);

  angular
    .module('jaPedi.execucoes.directives', ['ngDialog']);

  angular
    .module('jaPedi.execucoes.services', []);
})();
