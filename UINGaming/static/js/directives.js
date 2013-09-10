'use strict';

/* Directives */

// Las directivas se llaman desde el HTML pasando del camelCase a camel-case.
// Esta, por ejemplo se invoca haciendo <div nav-bar></div> o cualquier elemento que
// se quiera ( <p nav-bar></p> etc...). Lo que hace la directiva es inyectar el HTML
// que se referencia con templateUrl dentro del elemento en el que se invoca la directiva (el div o el p).
angular.module('myApp.directives', []).
    directive('navBar', function () {
        return {templateUrl: 'partials/NavBarView', controller: 'NavCtrl'};
    });
