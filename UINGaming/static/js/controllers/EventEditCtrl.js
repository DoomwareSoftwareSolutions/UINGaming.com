'use strict';

/* Controllers */

var controllerName = 'EventEditCtrl';

// $location: http://docs.angularjs.org/api/ng.$location

// $scope: variables que se reflejan en el HTML que este controlador controla.
// {{events}} en el HTML es $scope.events en este controlador.
angular.module(controllerName, []).
    controller(controllerName, ['$scope', '$location', '$http', '$q', 'EventService', '$routeParams', function ($scope, $location, $http, $q, EventService, $routeParams) {
		
        EventService.getEvent($q, $scope, $routeParams.pk)
            .then(function (results) {
                //Invalid event id
                if (JSON.stringify(results)=="[]"){
                    alert("EVENT NOT FOUND");
                    return;
                }
                $scope.eventData = results[0];
                $scope.$emit("HideSpinner");
            }, errorOnREST);
        $scope.$emit("BackgroundChange", "events-background");
        $scope.$emit("HideSpinner");
            
        $scope.editEvent = function(){
		    EventService.editEvent($q, $scope.eventData)
		        .then(function (results) {
		            $scope.$emit("HideSpinner");
		        }, errorOnREST);
		}

        

    }]);
