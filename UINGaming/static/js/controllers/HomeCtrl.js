'use strict';

/* Controllers */

var controllerName = 'HomeCtrl';

angular.module(controllerName, []).
    controller(controllerName, ['$scope', '$http', '$q', 'HomeService', function ($scope, $http, $q, HomeService) {

        $scope.$emit("BackgroundChange", "home-background");
        $scope.$emit("ShowSpinner");

        var setCarouselDimensions = function () {
            $('#homeSlider').height(window.innerHeight);
        }

        $(window).resize(function () {
            setCarouselDimensions();
        });

        $(document).ready(function () {
            setCarouselDimensions();
        });

        if (window.location.href.search('#homeSlider') < 0) {
            window.location.href = window.location.href + '#homeSlider'
        }

        $scope.arrowLink = 'home#homeSlider';

        HomeService.getSlides($q)
            .then(function (results) {
                $scope.slides = results;
                $scope.$emit("HideSpinner");
            }, errorOnREST);

        HomeService.getFeatures($q)
            .then(function (results) {
                $scope.features = results;
                $scope.$emit("HideSpinner");
            }, errorOnREST);

    }]);