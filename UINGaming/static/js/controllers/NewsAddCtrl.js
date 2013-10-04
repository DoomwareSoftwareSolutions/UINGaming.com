'use strict';

/* Controllers */

var controllerName = 'NewsAddCtrl';

// $location: http://docs.angularjs.org/api/ng.$location

// $scope: variables que se reflejan en el HTML que este controlador controla.
// {{events}} en el HTML es $scope.events en este controlador.
angular.module(controllerName, []).
    controller(controllerName, ['$scope', '$location', '$http', '$q', 'NewsService','PropertyService', function ($scope, $location, $http, $q, NewsService, PropertyService) {
		

	$scope.$emit("BackgroundChange", "events-background");
	$scope.$emit("HideSpinner");
	$scope.edit = false
	
	PropertyService.loadPaths($scope);
	PropertyService.loadFields('news', 'en', $scope);
		
    $scope.addNew = function(){
	    $scope.$emit("ShowSpinner");
	    NewsService.addNew($q,$scope.nnew)
		.then(function (results) {
		    $scope.$emit("HideSpinner");
		    $location.url($scope.pathNews)
		}, errorOnREST);
	}

       
    

    }]);
