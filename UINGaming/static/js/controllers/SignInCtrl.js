'use strict';

/* Controllers */

var controllerName = 'SignInCtrl';

angular.module(controllerName, []).
    controller(controllerName, ['$scope', '$http', '$q', 'AuthService',  function ($scope, $http, $q, AuthService) {

        $scope.$emit("BackgroundChange", "signin-background");

    }]);
