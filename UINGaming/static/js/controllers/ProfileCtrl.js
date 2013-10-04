'use strict';

/* Controllers */

var controllerName = 'ProfileCtrl';

// $location: http://docs.angularjs.org/api/ng.$location

// $scope: variables que se reflejan en el HTML que este controlador controla.
// {{events}} en el HTML es $scope.events en este controlador.
angular.module(controllerName, []).
    controller(controllerName, ['$scope', '$location', '$http', '$q', 'EventService', 'PropertyService', 'AuthService', function ($scope, $location, $http, $q, EventService, PropertyService, AuthService) {
		

        $scope.$emit("BackgroundChange", "events-background");
        $scope.$emit("ShowSpinner");
		PropertyService.loadFields('profile', 'en', $scope);
		
		AuthService.getSessionInfo($q).then(function(results) {
			if (results.loggedIn) {
				var userPk = results.pk;
							
				AuthService.getUserProfile($q, userPk)
				.then(function(results) {
					$scope.user = results;	
				})
				
				EventService.getEventsByUser($q, $scope, userPk)
				.then(function (results) {
					$scope.events = results;
					PropertyService.loadPaths($scope);
					$scope.$emit("HideSpinner");
				}, errorOnREST);
			}
		})

    

    }]);
