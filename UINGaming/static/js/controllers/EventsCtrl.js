'use strict';

/* Controllers */

var controllerName = 'EventsCtrl';

// $location: http://docs.angularjs.org/api/ng.$location

// $scope: variables que se reflejan en el HTML que este controlador controla.
// {{events}} en el HTML es $scope.events en este controlador.
angular.module(controllerName, []).
    controller(controllerName, ['$scope', '$location', '$http', '$q', 'EventService', function ($scope, $location, $http, $q, EventService) {
		
		$scope.eventData = {
					"pk": -1,
					"model": "events.eventmembership",
					"fields": {
						"paid": false,
						"teamMembers": "asd",
						"teamTag": "",
						"event": -1,
						"teamName": "",
						"user": -1
					}
		}
        $scope.$emit("BackgroundChange", "events-background");
        $scope.$emit("ShowSpinner");

        EventService.getEvents($q, $scope)
            .then(function (results) {
                $scope.events = results;
                $scope.$emit("HideSpinner");
            }, errorOnREST);
            
        $scope.addEvent = function(){
		    EventService.addEvents($q,$scope.eventData)
		        .then(function (results) {
		            $scope.$emit("HideSpinner");
		        }, errorOnREST);
		}

    }]);
