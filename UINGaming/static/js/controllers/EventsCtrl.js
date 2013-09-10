'use strict';

/* Controllers */

var controllerName = 'EventsCtrl';

// $location: http://docs.angularjs.org/api/ng.$location

// $scope: variables que se reflejan en el HTML que este controlador controla.
// {{events}} en el HTML es $scope.events en este controlador.
angular.module(controllerName, []).
    controller(controllerName, ['$scope', '$location', '$http', '$q', 'EventService', function ($scope, $location, $http, $q, EventService) {

        $scope.$emit("BackgroundChange", "events-background");
        $scope.$emit("ShowSpinner");

        $scope.events = EventService.getEvents($q, $scope);

    }]);
