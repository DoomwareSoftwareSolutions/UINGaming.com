'use strict';

/* Controllers */

var controllerName = 'EventAddCtrl';

// $location: http://docs.angularjs.org/api/ng.$location

// $scope: variables que se reflejan en el HTML que este controlador controla.
// {{events}} en el HTML es $scope.events en este controlador.
angular.module(controllerName, []).
    controller(controllerName, ['$scope', '$location', '$http', '$q', 'EventService', function ($scope, $location, $http, $q, EventService) {
		
		$scope.eventData = { 
        "pk": -1,  
        "model": "events.event",
        "fields": {
            "body": "A new event ",
            "head": "asd",
            "image": "asd.png",
            "game": "League of Draven",
            "date": new Date(),
            "inscriptionDeadline": new Date()
			}
		}
        $scope.$emit("BackgroundChange", "events-background");
        $scope.$emit("HideSpinner");
            
        $scope.addEvent = function(){
		    EventService.addEvent($q,$scope.eventData)
		        .then(function (results) {
		            $scope.$emit("HideSpinner");
		        }, errorOnREST);
		}

    }]);
