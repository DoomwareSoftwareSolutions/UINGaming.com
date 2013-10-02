'use strict';

/* Controllers */

var controllerName = 'EventDetailCtrl';

// $location: http://docs.angularjs.org/api/ng.$location

// $scope: variables que se reflejan en el HTML que este controlador controla.
// {{events}} en el //HTML es $scope.events en este controlador.
angular.module(controllerName, []).controller(controllerName, ['$scope', '$location', '$http', '$routeParams','$q', 'EventService',
'AuthService','PropertyService' , function ($scope, $location, $http, $routeParams, $q,  EventService, AuthService, PropertyService) {

        $scope.$emit("BackgroundChange", "events-background");
        $scope.$emit("ShowSpinner");
		$scope.memberships = [];
        $scope.members = [];
        $scope.pathEventDelete = EventService.pathEventDelete;
		var pk = $routeParams.pk;
        PropertyService.loadPaths($scope);
        EventService.getEvent($q, $scope, pk)
            .then(function (results) {
            	//Invalid event id
            	if (JSON.stringify(results)=="[]"){
            		$location.path($scope.pathEvents);
            		alert("EVENT NOT FOUND");
            		return;
            	}
                $scope.foundEvent = results[0];
                EventService.setEventPk(results[0].pk);

                $scope.$emit("HideSpinner");
            }, errorOnREST);
        //Now we look for memberships

        EventService.getEventMemberships($q, pk)
            .then(function (results) {
                //Sin membresias

                if (JSON.stringify(results)=="[]"){
                    $scope.memberships = [];
                    return;
                }
                $scope.memberships = results;

            }, errorOnREST);


        $scope.deleteEvent = function(pk){
            EventService.deleteEvent($q, pk)
                .then(function (results) {
                    if (results['error-code']!=0){
                        alert("ERROR: "+results['error-description']);
                        return;
                    }
                    $location.path($scope.pathEvents);
                }, errorOnREST);

        }

        function checkSubscription(){
            AuthService.getSessionInfo($q).then(function(results) {
                if (results.loggedIn) {
                    var userPk = results.pk;
                    EventService.getMembershipByUserAndEvent($q, userPk, pk)
                    .then(function (results) {  
                        if (JSON.stringify(results) != "[]"){
                            $scope.subscribed=true;
                            $scope.suscribedTeam = results[0].fields.teamName;
                        }
                        else 
                            $scope.subscribed=false;
                        $scope.$emit("HideSpinner");
                    }, errorOnREST);
                }
            })
        }

        checkSubscription();
    }]);
