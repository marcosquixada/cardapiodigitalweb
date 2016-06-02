(function () {
  'use strict';

  angular
    .module('jaPedi.publicacoes', [
      'jaPedi.publicacoes.controllers',
      'jaPedi.publicacoes.directives',
      'jaPedi.publicacoes.services'
    ]);

  angular
    .module('jaPedi.publicacoes.controllers', []);

  angular
    .module('jaPedi.publicacoes.directives', ['ngDialog']);

  angular
    .module('jaPedi.publicacoes.services', []);
})();
