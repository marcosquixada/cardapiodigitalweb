(function () {
  'use strict';

  angular
    .module('jaPedi.utils', [
      'jaPedi.utils.services',
      'jaPedi.utils.directives',
      'jaPedi.utils.controllers',
      'jaPedi.utils.filters'
    ]);

  angular
    .module('jaPedi.utils.directives', []);

    angular
    .module('jaPedi.utils.controllers', []);

  angular
    .module('jaPedi.utils.services', []);

    angular
      .module('jaPedi.utils.filters', []);
})();
