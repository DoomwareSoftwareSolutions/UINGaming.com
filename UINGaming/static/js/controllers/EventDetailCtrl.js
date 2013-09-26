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
		
		var pk = $routeParams.pk;
        EventService.getEvent($q, $scope, pk)
            .then(function (results) {
            	//Invalid event id
            	if (JSON.stringify(results)=="[]"){
            		$location.path( "/events" );
            		alert("EVENT NOT FOUND");
            		return;
            	}
                $scope.events = results;
                EventService.setEventPk(results[0].pk);
                $scope.$emit("HideSpinner");
            }, errorOnREST);

    }]);
