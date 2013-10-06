'use strict';

/* Controllers */

var controllerName = 'HomeCtrl';

angular.module(controllerName, []).
    controller(controllerName, ['$scope', '$http', '$q', 'HomeService' ,'PropertyService', function ($scope, $http, $q, HomeService, PropertyService) {

        $scope.$emit("BackgroundChange", "home-background");
        $scope.$emit("ShowSpinner");

        var aspectRatio = 1920 / 1080;

        var setCarouselDimensions = function () {
            var screenWidth = window.innerWidth;
            var screenHeight = window.innerHeight;
            $('#homeSlider').height(screenWidth / aspectRatio);
            if ($('#homeSlider').height() > screenHeight) {
                $('#homeSlider').height(screenHeight);
            }
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
        PropertyService.loadFields('news', 'en', $scope);
        PropertyService.loadPaths($scope);
        $scope.arrowLink = 'home#homeSlider';

        HomeService.getNews($q)
            .then(function (results) {
                $scope.slides = new Array()
                var length = results.length
                var nnew = null
                for (var i = 0 ; i < length ; i++) {
                    nnew = results[i]
                    var slide = new Object()
                    slide.heading = nnew.header
                    slide.caption = nnew.subheader
                    slide.image = nnew.image
                    slide.linkText = $scope.readPlaceholder
                    slide.linkRef = $scope.pathNewsViewer+'/'+nnew.pk
                    console.log(JSON.stringify(slide))
                    $scope.slides.push(slide)
                }
                $scope.$emit("HideSpinner");
            }, errorOnREST);

    }]);