'use strict';

/* Controllers */

var controllerName = 'EventRegisterCtrl';
var minTeamSize = 5;
angular.module(controllerName, []).
    controller(controllerName, ['$scope','PropertyService', 'EventService','$q', 'AuthService', '$location', function ($scope, PropertyService,EventService, $q, AuthService, $location) {

        $scope.$emit("BackgroundChange", "event-register-background");

        $scope.teamMembers = [];

        $scope.newMember = '';

		
        var triggerDigest = function () {
            if (!$scope.$$phase) {
                $scope.$digest();
            }

        }

        $scope.addMember = function () {
            if ($scope.teamMembers.length < minTeamSize) {
                $scope.teamMembers.push($scope.newMember);
                $scope.newMember = '';
                triggerDigest();
            }
        }
        
        
        $scope.removeMember = function (index) {
            $scope.teamMembers.splice(index, 1);
            triggerDigest();
        }
        
        //Respeto el formato json que pide la api
        var loadFields = function () {
            PropertyService.loadFields('eventRegister', 'en', $scope);
            $scope.registerData = 
				{
					"pk": -1,
					"model": "events.eventmembership",
					"fields": {
						"paid": false,
						"teamMembers": "asd",
						"teamTag": "",
						"event": -1,
						"teamName": "",
						"user": -1
					}
				}
        }
        
        //TODO get user and event ID!
        $scope.register = function () {
    		//Paso el array a string separado por comas. TODO: escapar las comas / prohibir las comas del member name.
        	$scope.registerData.fields['teamMembers']=$scope.teamMembers.join(",");
        	$scope.registerData.fields['event']=EventService.getEventPk();
            $scope.registerData.fields['user']=AuthService.getUsername();
        	//API expects a json enclosed between brackets
        	var auxJsonContainer=[$scope.registerData];
            EventService.registerToEvent($q, auxJsonContainer)
                .then(function (results) {
                    // Prueba funcionamiento mostrando el response
                    if (results['error_code'] != 0)
                       $location.path( "/events" );
                    else
                        alert('error_code: '+results['error_code']+'  error_desc: '+results['error_description']);
                    $scope.$emit("HideSpinner");
                }, errorOnREST);
        }
        
		loadFields();
    }]);
