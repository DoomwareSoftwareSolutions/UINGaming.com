'use strict';

/* Controllers */

var controllerName = 'NavCtrl';

angular.module(controllerName, []).
    controller(controllerName, function ($scope, $location) {

        $scope.activeLink = '/home';

        $scope.activeClass = function (linkName) {
            return $scope.activeLink == linkName;
        }

        $scope.clickLink = function (linkName) {
            $scope.activeLink = linkName;
            return linkName;
        }

    });
