'use strict';

/* Controllers */

var controllerName = 'SignInCtrl';

angular.module(controllerName, []).
    controller(controllerName, ['$scope', '$http', '$q', 'AuthService',  function ($scope, $http, $q, AuthService) {

        $scope.$emit("BackgroundChange", "signin-background");
	
	/* Eso es solo de prueba. Hay que sacarlo */
	
	var userData = {username: "tomas", password: "1234", remember: true}
	AuthService.loginUser($q, $scope, userData);

    }]);
