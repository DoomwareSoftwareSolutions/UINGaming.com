'use strict';

/* Controllers */

var controllerName = 'NewsViewerCtrl';

// $location: http://docs.angularjs.org/api/ng.$location

// $scope: variables que se reflejan en el HTML que este controlador controla.
// {{events}} en el HTML es $scope.events en este controlador.
angular.module(controllerName, []).
    controller(controllerName, ['$scope', '$location', '$http', '$q','$routeParams', 'NewsService','PropertyService', function ($scope, $location, $http, $q, routeParam, NewsService, PropertyService) {
		

        $scope.$emit("BackgroundChange", "events-background");
        $scope.$emit("ShowSpinner");
		
		var begin = 0;
		var end = 10;
		
        NewsService.getNew($q, $scope,routeParam.pk)
            .then(function (results) {
				PropertyService.loadPaths($scope);
				PropertyService.loadFields('news', 'en', $scope);
                $scope.current_new = results;
                $scope.$emit("HideSpinner");
            }, errorOnREST);

       
    

    }]);
