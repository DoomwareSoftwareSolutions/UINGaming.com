'use strict';

/* Controllers */

var controllerName = 'ProfileEditCtrl';

// $location: http://docs.angularjs.org/api/ng.$location

// $scope: variables que se reflejan en el HTML que este controlador controla.
// {{events}} en el HTML es $scope.events en este controlador.
angular.module(controllerName, []).
    controller(controllerName, ['$scope', '$location', '$http', '$routeParams', '$q', 'EventService', 'PropertyService', 'AuthService', function ($scope, $location, $http, $routeParams,$q, EventService, PropertyService, AuthService) {
		

        $scope.$emit("BackgroundChange", "events-background");
        $scope.$emit("ShowSpinner");
		PropertyService.loadFields('profile', 'en', $scope);
		
		var userPk = $routeParams.pk;
		
		AuthService.getUserProfile($q, userPk)
		.then(function(results) {
			$scope.user = results;
			$scope.$emit("HideSpinner");
		});
		
		
		$scope.editUserProfile = function(){
		    AuthService.editUserProfile($q, $scope.user)
		   .then(function (results) {
			  $scope.$emit("HideSpinner");
			   $location.path( "/profile/" + $scope.user.username );
			}, errorOnREST);
		}
				
    }]);
