'use strict';

/* Controllers */

var controllerName = 'SignInCtrl';

angular.module(controllerName, []).
    controller(controllerName, ['$scope', function ($scope) {

        $scope.$emit("BackgroundChange", "signin-background");

    }]);
