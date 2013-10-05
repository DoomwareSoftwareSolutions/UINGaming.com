'use strict';

/* Controllers */

var controllerName = 'NewsEditCtrl';

// $location: http://docs.angularjs.org/api/ng.$location

// $scope: variables que se reflejan en el HTML que este controlador controla.
// {{events}} en el HTML es $scope.events en este controlador.
angular.module(controllerName, []).
    controller(controllerName, ['$scope', '$location', '$http', '$q', '$routeParams', 'NewsService','PropertyService', function ($scope, $location, $http, $q, routeParam, NewsService, PropertyService) {
		

	$scope.$emit("BackgroundChange", "events-background");
	$scope.$emit("ShowSpinner");
	$scope.edit = true
	
	PropertyService.loadPaths($scope);
	PropertyService.loadFields('news', 'en', $scope);
	
	NewsService.getNew($q, $scope,routeParam.pk)
            .then(function (results) {
                $scope.nnew = results;
                $scope.$emit("HideSpinner");
            }, errorOnREST);
		
	$scope.editNew = function(){
		$scope.$emit("ShowSpinner");
		NewsService.editNew($q,routeParam.pk,$scope.nnew)
		.then(function (results) {
			$scope.$emit("HideSpinner");
			$location.url($scope.pathNews)
		}, errorOnREST);
	}

       
    

    }]);
