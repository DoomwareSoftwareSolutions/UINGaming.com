'use strict';

var name = 'AuthService';

// $http: http://docs.angularjs.org/api/ng.$http
angular.module(name, []).factory(name,['$http', '$cookieStore', function ($http, $cookieStore) {

    var AuthService = {};
	var username = "";


	AuthService.getUserIDfromCookie = function (){
		var aux = $cookieStore.get('user_id');
		if (aux == undefined)
			return undefined;
		return aux.split(":")[0];
	}

	AuthService.getSessionInfo = function ($q) {
		var deferred = $q.defer();
        $http.get('http://localhost:8000/api/user-session')
            .success(function (jsonData) {
                deferred.resolve(jsonData);
                //if (jsonData['error-code']!= 0)error check  			
            });
    	 return deferred.promise;
	}
    AuthService.registerUser = function ($q, userData) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        $http.post('http://localhost:8000/api/signup', userData)
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
        return deferred.promise;
    }

    AuthService.loginUser = function ($q, userData) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        $http.post('http://localhost:8000/api/signin', userData)
            .success(function (jsonData) {
                deferred.resolve(jsonData);
                username = AuthService.getUserIDfromCookie();
            });
    	 return deferred.promise;
    }

	
	AuthService.logOutUser = function ($q) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        $http.get('http://localhost:8000/api/logout')
            .success(function (jsonData) {
                deferred.resolve(jsonData);
                //if (jsonData['error-code']!= 0)error check  			
            });
    	 return deferred.promise;
    }	
	
	
	AuthService.getUserProfile = function ($q, pk) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        $http.get('http://localhost:8000/api/users/' + pk)
            .success(function (jsonData) {
                deferred.resolve(jsonData);
                //if (jsonData['error-code']!= 0)error check  			
            });
    	 return deferred.promise;
    }	
	
    return AuthService;

}]);
