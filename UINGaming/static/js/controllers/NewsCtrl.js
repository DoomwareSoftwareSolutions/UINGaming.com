'use strict';

/* Controllers */

var controllerName = 'NewsCtrl';

// $location: http://docs.angularjs.org/api/ng.$location

// $scope: variables que se reflejan en el HTML que este controlador controla.
// {{events}} en el HTML es $scope.events en este controlador.
angular.module(controllerName, []).
    controller(controllerName, ['$scope', '$location', '$http', '$q', 'NewsService','PropertyService', function ($scope, $location, $http, $q, NewsService, PropertyService) {
		

        $scope.$emit("BackgroundChange", "events-background");
        $scope.$emit("ShowSpinner");
		PropertyService.loadFields('newsView', 'en', $scope);
		
		var begin = 0;
		var end = 10;
		
        NewsService.getNews($q, $scope,begin, end)
            .then(function (results) {
				PropertyService.loadPaths($scope);
				PropertyService.loadFields('news', 'en', $scope);
                $scope.news = results;
                $scope.$emit("HideSpinner");
            }, errorOnREST);

       
    

    }]);
