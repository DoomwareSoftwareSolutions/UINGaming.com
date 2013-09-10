'use strict';

/* Controllers */

var controllerName = 'EventRegisterCtrl';

angular.module(controllerName, []).
    controller(controllerName, ['$scope', function ($scope) {

        $scope.$emit("BackgroundChange", "event-register-background");

        $scope.teamMembers = [];

        $scope.newMember = '';

        var triggerDigest = function () {
            if (!$scope.$$phase) {
                $scope.$digest();
            }

        }

        $scope.addMember = function () {
            if ($scope.teamMembers.length < 5) {
                $scope.teamMembers.push($scope.newMember);
                $scope.newMember = '';
                triggerDigest();
            }
        }

        $scope.removeMember = function (index) {
            $scope.teamMembers.splice(index, 1);
            triggerDigest();
        }

    }]);