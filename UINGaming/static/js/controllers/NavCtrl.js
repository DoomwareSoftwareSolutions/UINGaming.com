'use strict';

/* Controllers */

var controllerName = 'NavCtrl';

angular.module(controllerName, []).
    controller(controllerName, [ '$q', '$scope', '$location', 'PropertyService', 'AuthService', '$cookieStore',
    							function ($q, $scope, $location, PropertyService, AuthService, $cookieStore) {
		
		var greeting = "Bienvenido, ";
		
        var loadFields = function () {
            PropertyService.loadPaths($scope);
            PropertyService.loadFields('navBar', 'en', $scope);
        }

        loadFields();
        $scope.activeClass = function (linkName) {
            return $scope.activeLink == linkName;
        }
        
        function setUsername(){
        	var user=$cookieStore.get('user_id');
			if (user == undefined)
				$scope.helloUser = "";
			else
				$scope.helloUser = greeting+user.split(":")[0]
		}
		setUsername();
        $scope.clickLink = function (linkName) {
            $scope.activeLink = linkName;
            return linkName;
        }
        
        $scope.signOut = function () {
            $scope.$emit("ShowSpinner");
            AuthService.logOutUser($q)
                .then(function (results) {
                    // Prueba funcionamiento mostrando el response
                    alert(JSON.stringify(results));
                    $scope.$emit("HideSpinner");
                }, errorOnREST);
                $location.path('/home');
        }
        
        
	
    }]);
