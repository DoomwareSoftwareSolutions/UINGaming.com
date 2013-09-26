'use strict';

/* Controllers */

var controllerName = 'EventDetailCtrl';

// $location: http://docs.angularjs.org/api/ng.$location

// $scope: variables que se reflejan en el HTML que este controlador controla.
// {{events}} en el //HTML es $scope.events en este controlador.
angular.module(controllerName, []).controller(controllerName, ['$scope', '$location', '$http', '$routeParams','$q', 'EventService',
'AuthService', function ($scope, $location, $http, $routeParams, $q,  EventService, AuthService) {

        $scope.$emit("BackgroundChange", "events-background");
        $scope.$emit("ShowSpinner");
		$scope.memberships = [];
		var pk = $routeParams.pk;
        EventService.getEvent($q, $scope, pk)
            .then(function (results) {
            	//Invalid event id
            	if (JSON.stringify(results)=="[]"){
            		$location.path( "/events" );
            		alert("EVENT NOT FOUND");
            		return;
            	}
                $scope.foundEvent = results[0];
                EventService.setEventPk(results[0].pk);

                $scope.$emit("HideSpinner");
            }, errorOnREST);
        //Now we look for memberships

        EventService.getEventMemberships($q, pk)
            .then(function (results) {
                //Sin membresias

                if (JSON.stringify(results)=="[]"){
                    $scope.memberships = [];
                    return;
                }
                $scope.memberships = results;

            }, errorOnREST);

    }]);
