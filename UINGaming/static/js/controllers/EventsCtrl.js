'use strict';

/* Controllers */

var controllerName = 'EventsCtrl';

// $location: http://docs.angularjs.org/api/ng.$location

// $scope: variables que se reflejan en el HTML que este controlador controla.
// {{events}} en el HTML es $scope.events en este controlador.
angular.module(controllerName, []).
    controller(controllerName, ['$scope', '$location', '$http', '$q', 'EventService','PropertyService', function ($scope, $location, $http, $q, EventService, PropertyService) {
		

        $scope.$emit("BackgroundChange", "events-background");
        $scope.$emit("ShowSpinner");
		PropertyService.loadFields('eventsView', 'en', $scope);
		
        EventService.getEvents($q, $scope)
            .then(function (results) {
                $scope.events = results;
                PropertyService.loadPaths($scope);
                $scope.$emit("HideSpinner");
            }, errorOnREST);

       
    

    }]);
