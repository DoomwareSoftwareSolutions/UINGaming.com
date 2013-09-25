'use strict';

/* Controllers */

var controllerName = 'NavCtrl';

angular.module(controllerName, []).
    controller(controllerName, [ '$q', '$scope', '$location', 'PropertyService', 'AuthService', '$cookieStore',
    							function ($q, $scope, $location, PropertyService, AuthService, $cookieStore) {
		
		var greeting = "Bienvenido, ";
        $scope.login = false;
        
        var triggerDigest = function () {
            if (!$scope.$$phase) {
                $scope.$digest();
            }
        }
        
        $scope.$on('UserChange', setUsername);
        
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
			if (user == undefined) {
				$scope.helloUser = "";
                $scope.login = false;
            } else {
                $scope.username = user.split(":")[0]
				$scope.helloUser = greeting+$scope.username
                $scope.login = true;
            }
                
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
                    $scope.$emit("UserChange");
                    $scope.$emit("HideSpinner");
                }, errorOnREST);
        }
        
        
	
    }]);
