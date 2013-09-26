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
            AuthService.getSessionInfo($q).then(function(results) {
            if (!results.loggedIn) {
                $scope.helloUser = "";
                $scope.username = "";
                $scope.login = false;
                $scope.admin = false
            } else {
                $scope.username = results.username;
				$scope.helloUser = greeting+$scope.username
                $scope.login = true;
                $scope.admin = false;
                if (results.permission == "AD"){
                    $scope.admin = true;
                }
            }
            })
                
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
