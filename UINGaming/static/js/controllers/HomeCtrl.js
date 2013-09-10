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

        $scope.slides = HomeService.getSlides($q, $scope);
        $scope.features = HomeService.getFeatures($q, $scope);

    }]);