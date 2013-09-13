'use strict';

/* Controllers */

var controllerName = 'NavCtrl';

angular.module(controllerName, []).
    controller(controllerName, [ '$scope', '$location', 'PropertyService', function ($scope, $location, PropertyService) {

        var loadFields = function () {
            PropertyService.loadPaths($scope);
            PropertyService.loadFields('navBar', 'en', $scope);
        }

        loadFields();

        $scope.activeClass = function (linkName) {
            return $scope.activeLink == linkName;
        }

        $scope.clickLink = function (linkName) {
            $scope.activeLink = linkName;
            return linkName;
        }

    }]);
