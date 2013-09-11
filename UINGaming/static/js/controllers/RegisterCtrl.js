'use strict';

/* Controllers */

var controllerName = 'RegisterCtrl';

angular.module(controllerName, []).
    controller(controllerName, ['$scope', '$http', '$q', 'AuthService', function ($scope, $http, $q, AuthService) {

        $scope.$emit("BackgroundChange", "signin-background");
	
	/* Eso es solo de prueba. Hay que sacarlo */
	
	var userData = {username: "tomas", email: "tomas@tomas.com", password: "1234", vpassword: "1234"}
	AuthService.registerUser($q, $scope, userData);

    }]);
