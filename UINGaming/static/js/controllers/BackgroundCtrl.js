'use strict';

/* Controllers */

var controllerName = 'BackgroundCtrl';

angular.module(controllerName, []).
    controller(controllerName, function ($scope) {

        $scope.bgClass = '';

        $scope.$on("BackgroundChange", function (event, data) {
            $scope.bgClass = data;
            triggerDigest();
        });

        $scope.$on("ShowSpinner", function () {
            $scope.activeSpinner = true;
            triggerDigest();
        });

        $scope.$on("HideSpinner", function () {
            $scope.activeSpinner = false;
            triggerDigest();
        });

        var triggerDigest = function () {
            if (!$scope.$$phase) {
                $scope.$digest();
            }
        }

    });
